from aiogram import types

subscribe_button_telegram = types.InlineKeyboardButton(text = "Telegram канал 🤳", url = "https://t.me/mines_okey")
subscribe_button_check = types.InlineKeyboardButton(text = "Проверить подписку 💠", callback_data="subscribe_button_check")
subscribeCheck_markup = types.InlineKeyboardMarkup(row_width=1).add(subscribe_button_telegram).add(subscribe_button_check)

register_acc = types.InlineKeyboardButton(text = "Зарегестрировать аккаунт ⚙️", callback_data="acc_reg")
register_acc_markup = types.InlineKeyboardMarkup(row_width=1).add(register_acc)

keyboard_link = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text = "Ссылка на сайт 📲", url = "https://1wytvn.life/casino/list?open=register#d28d"))

get_sygnal_markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text = "Получить сигнал 🛠", callback_data = "get_sigg"))