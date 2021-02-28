from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["about"]),group=-2)
async def about(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⚙ Developer ⚙", url="https://t.me/Amani_m_h_d")],
    ])
    abouttxt = f"➠<b>My Name :</b> <code>Youtube Downloader🤓</code>
➠<b>Dev :</b> <a href='https://t.me/Amani_m_h_d'>Amani Muhammed</a>
➠<b>Credits :</b> <code>Everyone in this journey</code>
➠<b>Language :</b> <code>Python3</code>
➠<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 
➠<b>Server :</b> <a href='https://herokuapp.com/'>Heroku</a>
➠<b>Source Code :</b> 👉 <a href='http://t.me/nokkiirunnoippokittum'>Click Here</a> 
       <b>📜Quote :</b> <code>ആരും പേടിക്കണ്ട എല്ലാവർക്കും കിട്ടും™️</code>"
    await message.reply_text(abouttxt, reply_markup=joinButton)
    raise StopPropagation
