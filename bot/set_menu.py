from aiogram import Bot
from aiogram.types import BotCommand#, BotCommandScopeAllPrivateChats


async def set_menu_commands(bot: Bot):
    commands_dict={'/start':'Запуск','/help':'Помощь','/about':'tt2'}
    await bot.set_my_commands(commands=[BotCommand(command=k, description=v) for k,v in commands_dict.items()])