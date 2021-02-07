from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]),group=-2)
sync def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Owner", url="https://t.me/Amani_m_h_d")],
        [InlineKeyboardButton(
            "Other Bots", url="https://t.me/My_Test_botz")]
    ])
    helptxt = f"<b>Hai, Follow these Steps..</b> \n\n➠ Send Me Your Youtube Link And Select Desired Option To Be Uploaded To Telegram \n\n➠ Currently Only Supports Youtube Single  (No playlist) Just Send Any Youtube Link \n\n<b>📜Quote : </b><code>കിടന്ന് അടി വയ്ക്കരുത് എല്ലാർക്കും ഉപയോഗിക്കാൻ പറ്റും😌</code>"
    await message.reply_text(helptxt, reply_markup=joinButton)
    raise StopPropagation

