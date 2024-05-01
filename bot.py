from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram import types
from keyboards import *
from db import Database
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(token="7013945314:AAFFMhgCIe-8ibJd9D1Bk8u8OBAZzqUpp24")
dp = Dispatcher(bot, storage = MemoryStorage())
db = Database(r'db.db')

class Form(StatesGroup):
    waiting_for_message = State()
class Form1(StatesGroup):
    waiting_for_message = State()

async def check_sub_channel(user_id):
    try:
        chat_id = -1002020136505
        chat_member = await bot.get_chat_member(chat_id, user_id)
        is_subscribed = chat_member.status in [types.ChatMemberStatus.MEMBER, types.ChatMemberStatus.ADMINISTRATOR, types.ChatMemberStatus.CREATOR]
        return is_subscribed
    except Exception as e:
        print(e)
        return False

def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
   keyboard = types.InlineKeyboardMarkup(row_width=1) #создаем клавиатуру
   one_butt_and = types.InlineKeyboardMarkup(text="Для Android/Windows 🖥", web_app=types.WebAppInfo(url = "https://hcof.github.io/site/"))
   one_butt_apple = types.InlineKeyboardMarkup(text="Для Apple 📱", web_app=types.WebAppInfo(url = "https://superfirsthero.github.io/site/"))
   keyboard.add(one_butt_and).add(one_butt_apple)

   return keyboard


@dp.message_handler()
async def start(message: types.Message):
    var = await check_sub_channel(message.from_user.id)
    print(var)
    if var== True:
        if db.user_exists(message.from_user.id):
            await message.reply("<b>Добро пожаловать в 🔸 Hack mines V3.0🔸!</b>\n<i>💣Mines - это гэмблинг игра в букмекерской конторе 1win, которая основывается на классическом “Сапёре”</i>. Ваша цель - открывать безопасные ячейки и не попадаться в ловушки.\nНаш бот основан на нейросети от OpenAI.\nОн может предугадать расположение звёзд с вероятностью 80-90%.", reply_markup=get_sygnal_markup, parse_mode=types.ParseMode.HTML)

        else:
            await message.reply("Выберите функцию:", reply_markup = register_acc_markup)
    else:
        await message.reply(f"<b>Здраствуйте, <i>{message.from_user.full_name}</i>\nДля использования бота подпишитесь на наш канал:</b>", parse_mode=types.ParseMode.HTML, reply_markup = subscribeCheck_markup)





@dp.callback_query_handler(lambda c: c.data.startswith('subscribe_button_check'))
async def col1(call: types.CallbackQuery):
    bool_res = await check_sub_channel(user_id = call.from_user.id)
    if bool_res == True:
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f'<b>✅Вы успешно подписались на наш канал,</b>\n🕹Теперь вы можете использовать бота.',
            parse_mode=types.ParseMode.HTML,
            reply_markup=register_acc_markup
        )
    else:
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f'<b>❌Вы не подписаны на наш канал,</b>\nПопробуйте еще раз.',
            reply_markup=subscribeCheck_markup,
            parse_mode=types.ParseMode.HTML
        )

@dp.callback_query_handler(lambda c: c.data.startswith('acc_reg'))
async def col1(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "💠 1. Для начала зарегистрируйтесь по ссылке <b>на сайте 1WIN по ссылке ниже</b>\n💠 2. После успешной регистрации cкопируйте <b>ваш айди на сайте</b> (Вкладка 'пополнение' и в правом верхнем углу будет ваш ID).\n💠 3. И отправьте его <b>сообщением боту</b>!", parse_mode=types.ParseMode.HTML, reply_markup=keyboard_link)
    await Form.waiting_for_message.set()

@dp.callback_query_handler(lambda c: c.data.startswith('get_sygnal'))
async def col1(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "Выберите опцю:", reply_markup=webAppKeyboard())

@dp.message_handler(state=Form.waiting_for_message)
async def process_action(message: types.Message, state: FSMContext):
    try:
        if int(message.text) >1 and len(message.text) >=5 and len(message.text) <= 10:
            await message.reply("<b>Добро пожаловать в 🔸 Hack mines V3.0 🔸!</b>\n<i>💣Mines - это гэмблинг игра в букмекерской конторе 1win, которая основывается на классическом “Сапёре”</i>. Ваша цель - открывать безопасные ячейки и не попадаться в ловушки.\nНаш бот основан на нейросети от OpenAI.\nОн может предугадать расположение звёзд с вероятностью 80-90%.", reply_markup=get_sygnal_markup, parse_mode=types.ParseMode.HTML)
        else:
            await message.reply("Вы ввели неправильный айди. Попробуйте еще раз", reply_markup = register_acc_markup)
        await state.finish()
    except Exception:
        await message.reply("Вы ввели неправильный айди. Попробуйте еще раз", reply_markup = register_acc_markup)


@dp.callback_query_handler(lambda c: c.data.startswith('get_sigg'))
async def col1(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "💠 Для запуска приложения введите ваш айди на сайте 1WIN", parse_mode=types.ParseMode.HTML, reply_markup=keyboard_link)
    await Form1.waiting_for_message.set()

@dp.message_handler(state=Form1.waiting_for_message)
async def process_action(message: types.Message, state: FSMContext):
    try:
        if int(message.text) >1 and len(message.text) >=5 and len(message.text) <= 10:
            await message.reply("<b>Выберите опцию</b>.", reply_markup=webAppKeyboard(), parse_mode=types.ParseMode.HTML)
        await state.finish()
    except Exception:
        await message.reply("Вы ввели неправильный айди. Попробуйте еще раз")

if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    
    except Exception:
        pass