from aiogram import Dispatcher
from aiogram.utils.executor import Executor

from app.misc import dp

runner = Executor(dp)


async def on_startup_polling(dispatcher: Dispatcher):
    await dispatcher.start_polling()


def setup():
    runner.on_startup(on_startup_polling, webhook=False, polling=True)
    runner.start_polling()
