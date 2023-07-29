import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
#from aiogram.fsm.storage.redis import RedisStorage
from get_config import config

from set_menu import set_menu_commands


async def echo_handler(message) -> None:
    """
    Handler will forward received message back to the sender

    By default, message handler will handle all message types (like text, photo, sticker and etc.)
    """
    try:
        # Send copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


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

    dp.message.register(echo_handler)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())    