import logging
import uvicorn

from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from src import load_config
from src.handlers.start import start_router
from src.handlers.settings import settings_router
from src.middlewares.config import ConfigMiddleware
from src.logo import consol

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
)

config = load_config(".env")
storage = MemoryStorage()

WEBHOOK_PATH = f"/bot/{config.tg.token}"
WEBHOOK_URL = config.tg.webhook_url + WEBHOOK_PATH

app = FastAPI()
bot = Bot(token=config.tg.token, parse_mode="HTML")
dp = Dispatcher(storage=storage)


@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(url=WEBHOOK_URL)

    logger.info("Бот запущен")

    # Регистрация мидлваре
    dp.update.outer_middleware(ConfigMiddleware(config))

    # Регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(settings_router)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()
    logger.info("Бот остановлен")


if __name__ == "__main__":
    consol.logotip()#вывод логотипа
    uvicorn.run(app, host="0.0.0.0", port=8000)
