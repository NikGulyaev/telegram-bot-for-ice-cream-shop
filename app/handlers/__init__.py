from telegram.ext import CommandHandler

from app.handlers.commands import start


HANDLERS = (
    CommandHandler("start", start),
    # сюда можно добавить другие команды, например:
    # CommandHandler("menu", menu),
)
