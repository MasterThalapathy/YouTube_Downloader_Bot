from script import script

@Client.on_message(filters.command(["about"]))
def about(bot, update):

    bot.send_message(
        chat_id=update.chat.id, 
        text=script.ABOUT_TEXT,
        parse_mode="html", 
        reply_to_message_id=update.message_id, 
        disable_web_page_preview=True 
    ) 
