from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("👨‍💻 Developer 👨‍💻", url="https://t.me/Amani_m_h_d")],
        [InlineKeyboardButton(
            "💢 Other Bots 💢", url="https://t.me/My_Test_botz")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}\nI am Youtube Downloader Bot🤓</b> \n\n<code>I Will Convert Youtube Link to Video/File & Mp3</code> \n\n<code>For more details Press /help</code>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
