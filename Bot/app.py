from aiogram import executor
from rich.console import Console
console = Console()
from datetime import datetime
import middlewars
from loader import dp
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_command import set_default_commands


async def on_startup(dispatcher):

    await set_default_commands(dispatcher)

    await on_startup_notify(dispatcher)

data = datetime.now()



if __name__ == '__main__':
    console.print(f"[bold red]|INFO|- BOT LAUNCHED [/bold red]\n{data}", justify="center")
    executor.start_polling(dp, on_startup=on_startup)