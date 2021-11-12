import os
from pyrogram import Client, filters
from pyrogram.types import *


TEXT = """👋 Hey there! My name is [Emma Miller](https://t.me/EmmaMillerBot) ✨ - A powerful group management bot which can help you to manage your groups effectively as possible With   Advanced AI . 
Click `menu` button for more information.
Join my [news channel](https://t.me/BotMaster_mkspali) to get information on all the latest updates.  """

MENU = [
    [
        InlineKeyboardButton(
            text="↪️ Main menu ", callback_data="aboutmanu_back"),
    ],
]

@pbot.on_message(filters.command(["tart"]))
async def tart(pbot, update):
    await update.reply_text(
        text=TEXT,
        reply_markup=MENU,
        disable_web_page_preview=True,
        quote=True
    ) 
    
