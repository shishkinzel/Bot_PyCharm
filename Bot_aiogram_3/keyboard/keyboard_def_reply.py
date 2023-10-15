from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


def keyboard_reply() -> ReplyKeyboardMarkup:
    key_button: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Помощь'),
                KeyboardButton(text='Старт'),
            ],
            [
                KeyboardButton(text='Описание'),
                KeyboardButton(text='Главное меню'),
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действия из меню"
    )
    return key_button
