
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from commons.test_f import f

router = Router()


@router.message(Command("start"))  
async def echo_handler(message: Message) -> None:
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

@router.message(Command("help"))  
async def echo_handler(message: Message) -> None:
        await message.answer(f())       