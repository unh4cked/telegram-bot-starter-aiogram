import asyncio
import logging
import os
from typing import Optional

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: Optional[str] = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN not set. Put it in .env (BOT_TOKEN=...) or environment.")

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer("سلام! من یک ربات تلگرامی با Aiogram v3 هستم. /help را امتحان کن ✨")

@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer("دستورات:\n/start — شروع گفتگو\n/help — راهنما\nپیام بده تا برات echo کنم.")

@router.message(F.text)
async def echo_text(message: Message) -> None:
    await message.answer(f"Echo: {message.text}")

async def amain() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    logging.info("Starting bot polling...")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(amain())
