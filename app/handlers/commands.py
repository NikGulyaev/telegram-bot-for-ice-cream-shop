from app.core.orders.constants import OrderStatusEnum
from app.core.orders.exceptions import ActiveOrderExists
from app.core.orders.services import OrderService, ProductService
from app.core.users.services import UserService
#from app.handlers.
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_chat and update.effective_user:
        await context.application.user_service.register_visitor(update.effective_user.id) #type: ignore[attr-defined]
        keyboard = [
            [InlineKeyboardButton("Сделать заказ", callback_data=("order_create",))]
        ]
        markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Добро пожаловать",
            reply_markup=markup
        )