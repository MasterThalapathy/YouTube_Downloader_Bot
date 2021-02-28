from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["about"]),group=-2)
async def help(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⚙ Developer ⚙", url="https://t.me/Amani_m_h_d")],
    ])
    abouttxt = f"<b>Hai, Follow these Steps..</b> \n\n➠ Send Me Your Youtube Link And Select Desired Option To Be Uploaded To Telegram \n\n➠ Currently Only Supports Youtube Single  (No playlist) Just Send Any Youtube Link \n\n<b>📜Quote : </b><code>കിടന്ന് അടി വയ്ക്കരുത് എല്ലാർക്കും ഉപയോഗിക്കാൻ പറ്റും😌</code>"
    await message.reply_text(abouttxt, reply_markup=joinButton)
    raise StopPropagation
