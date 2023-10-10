from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from dotenv import load_dotenv

from keybords import kb, kb1, ikb_main, ikb_first, ikb_second, ikb_three, ikb_four

import os
from os.path import join, dirname


def get_from_env(key):
    dotenv_path = join(dirname(__file__), 'token.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)


token = get_from_env('TG_BOT_TOKEN')

bot = Bot(token)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>запуск бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/mainMenu</b> - <em>запуск главного меню</em>
"""


async def on_startup(_):
    print('Я включился')


@dp.message_handler(Text(equals='MainMenu'))
async def open_kb_main(message: types.Message):
    await message.answer(text='<i>Добро пожаловать в главное меню</i>',
                         parse_mode='HTML',
                         reply_markup=ikb_main)

    await message.answer(text='<i>Обновили палитру команд</i>',
                         parse_mode='HTML',
                         reply_markup=kb1)
    await message.delete()


@dp.message_handler(Text(equals='Выход'))  # Закрытие reply-keyboard
async def open_kb_open(message: types.Message):
    await message.answer(text='<i>Закрытие кнопок подсказки</i>',
                         parse_mode='HTML',
                         reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(commands=['mainMenu'])
async def open_kb_main(message: types.Message):
    await message.answer(text='<i>Добро пожаловать в главное меню</i>',
                         parse_mode='HTML',
                         reply_markup=ikb_main)

    await message.answer(text='<i>Обновили палитру команд</i>',
                         parse_mode='HTML',
                         reply_markup=kb1)
    await message.delete()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text=f'<i>Добро пожаловать, <b>{message.from_user.first_name}</b> ,'
                              f'в наш Информационный Бот </i>', parse_mode='HTML',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['description'])
async def cmd_description(message: types.Message):
    await message.answer(text='Наш бот предназначен для '
                              'облегчения серфинга сайта ЗелБиблио',
                         parse_mode='HTML')
    await message.delete()


@dp.callback_query_handler()
async def callback_measure(callback: types.CallbackQuery):
    if callback.data == 'time_action':
        await callback.message.answer(text='<i>Расписание мероприятий</i>',
                                      parse_mode='HTML',
                                      reply_markup=ikb_first)
    elif callback.data == 'clubs and studios':
        await callback.message.answer(text='<i>Кружки и студии</i>',
                                      parse_mode='HTML',
                                      reply_markup=ikb_three)
    elif callback.data == 'age':
        await callback.message.answer(text='<i>По возрасту</i>',
                                      parse_mode='HTML',
                                      reply_markup=ikb_second)
    elif callback.data == 'services':
        await callback.message.answer(text='<i>Услуги</i>',
                                      parse_mode='HTML',
                                      reply_markup=ikb_four)

    elif callback.data == 'return_main-menu':
        await callback.message.answer(text='<i>Возврат назад</i>',
                                      parse_mode='HTML',
                                      reply_markup=ikb_main)
    await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)

    # func=lambda callback: True
