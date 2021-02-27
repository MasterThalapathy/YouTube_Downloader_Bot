elif query.data == "help_data":
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("BACK", callback_data="start_data"),
                    InlineKeyboardButton("ABOUT", callback_data="about_data"),
                ],
            ]
        )
        await query.message.edit_text(
            script.HELP_MSG, reply_markup=keyboard, disable_web_page_preview=True
        )
elif query.data == "about_data":
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("BACK", callback_data="help_data"),    
                ],
            ]
        )
        await query.message.edit_text(
            script.ABOUT_MSG, reply_markup=keyboard, disable_web_page_preview=True
        )
