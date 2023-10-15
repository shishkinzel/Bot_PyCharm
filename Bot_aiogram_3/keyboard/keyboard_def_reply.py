from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def keyboard_reply() -> ReplyKeyboardMarkup:
    key_button: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='/help'),
                KeyboardButton(text='/start'),
            ],
            [
                KeyboardButton(text='/description'),
                KeyboardButton(text='/mainMenu'),
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действия из меню"
    )
    return key_button


def keyboard_inline_main() -> InlineKeyboardButton:
    pass
