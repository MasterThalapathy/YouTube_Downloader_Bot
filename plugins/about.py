By #masterThalapathy
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from script import script  

@Client.on_message(filters.command(["about"]) & filters.private)
 async def about(client, message):

    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Developer', url='https://t.me/Amani_m_h_d'),
                    ],
                
                ]
            ),
            quote=True
    )
