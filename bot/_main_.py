import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
#from aiogram.fsm.storage.redis import RedisStorage
from get_config import config

from set_menu import set_menu_commands
from handlers import default_handlers

async def main():

    logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                        level=config.log_level,
                        filename=f"{config.app_logs}/app.log",filemode="a")
    bot = Bot(config.tg_secret.get_secret_value(), parse_mode="HTML")
    """
    # Выбираем нужный сторадж
    if config.fsm_mode == "redis":
        storage = RedisStorage.from_url(
            url=config.redis,
            connection_kwargs={"decode_responses": True}
        )
    else:
        storage = MemoryStorage()
    """
    storage = MemoryStorage()
    # Создание диспетчера
    dp = Dispatcher(storage=storage)
    # Принудительно настраиваем фильтр на работу только в чатах один-на-один с ботом
    #dp.message.filter(F.chat.type == "private")

    # Регистрация роутеров с хэндлерами
    #dp.include_router(default_commands.router)
    #dp.include_router(spin.router)

    # Регистрация мидлвари для троттлинга
    #dp.message.middleware(ThrottlingMiddleware())

    # Установка команд в интерфейсе
    await set_menu_commands(bot)
    dp.include_router(default_handlers.router)
    #dp.message.register(echo_handler)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())    