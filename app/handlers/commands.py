from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_user:
        return

    user_id = update.effective_user.id
    user_service = context.application.user_service  # type: ignore[attr-defined]

    # Сначала регистрируем пользователя, если его ещё нет
    await user_service.register_visitor(user_id)

    # Проверяем роль
    is_waiter = await user_service.is_waiter(user_id)

    if is_waiter:
        text = "Добро пожаловать на смену, официант! Что нужно сделать?"
    else:
        text = "Добро пожаловать! Выберите действие из меню."

    await update.effective_message.reply_text(text)
