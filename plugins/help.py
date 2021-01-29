from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"\n➠ Send Me Your Youtube Link And Select Desired Option To Be Uploaded To Telegram \n➠ Currently Only Supports Youtube Single  (No playlist) Just Send Any Youtube Link \n\n<b>📜Quote : </b><code>കിടന്ന് അടി വയ്ക്കരുത് എല്ലാർക്കും ഉപയോഗിക്കാൻ പറ്റും😌</code>"
    await message.reply_text(helptxt)
