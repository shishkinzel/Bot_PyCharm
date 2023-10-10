from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardRemove)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text='/help')
btn2 = KeyboardButton(text='/description')
btn3 = KeyboardButton(text='MainMenu')
btn4 = KeyboardButton(text='Выход')

kb.add(btn1, btn2).add(btn3, btn4)
kb1.add(btn1, btn2).add(btn4)


# def get_ikb_main() -> InlineKeyboardMarkup:
#     ikb = InlineKeyboardMarkup([
#         [InlineKeyboardButton(text='Библиотеки и культурные центры', url='https://zelkultura.ru/biblio_cc/')],
#         [InlineKeyboardButton(text='Расписание мероприятий', callback_data='time_action')],
#         [InlineKeyboardButton(text='Кружки и студии', callback_data='clubs and studios')],
#         [InlineKeyboardButton(text='Услуги', callback_data='services')],
#         [InlineKeyboardButton(text='Сувенирная продукция', url='https://zelkultura.ru/souvenir/')],
#     ])
#
#     return ikb

ikb_main = InlineKeyboardMarkup()
ibtn_m1 = InlineKeyboardButton(text='Библиотеки и культурные центры', url='https://zelkultura.ru/biblio_cc/')
ibtn_m2 = InlineKeyboardButton(text='Расписание мероприятий', callback_data='time_action')
ibtn_m3 = InlineKeyboardButton(text='Кружки и студии', callback_data='clubs and studios')
ibtn_m4 = InlineKeyboardButton(text='Услуги', callback_data='services')
ibtn_m5 = InlineKeyboardButton(text='Сувенирная продукция', url='https://zelkultura.ru/souvenir/')

ikb_main.add(ibtn_m1).add(ibtn_m2).add(ibtn_m3).add(ibtn_m4).add(ibtn_m5)


ikb_first = InlineKeyboardMarkup()   # Расписание мероприятий
ibtn_f1 = InlineKeyboardButton(text='Платные', url='https://zelkultura.ru/events?tfc_charact:5137744['
                                                   '475890235]=%D0%9F%D0%BB%D0%B0%D1%82%D0%BD%D0%BE&tfc_div=:::')
ibtn_f2 = InlineKeyboardButton(text='Бесплатные', url='https://zelkultura.ru/events?tfc_charact:5137744['
                                                      '475890235]=%D0%91%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0'
                                                      '%BE&tfc_div=:::')
ibtn_f3 = InlineKeyboardButton(text='По возрасту', callback_data='age')
ibtn_f4 = InlineKeyboardButton(text='Главное меню', callback_data='return_main-menu')

ikb_first.add(ibtn_f1, ibtn_f2).add(ibtn_f3).add(ibtn_f4)

ikb_second = InlineKeyboardMarkup()  # Расписание мероприятий по возрасту
ibtn_s1 = InlineKeyboardButton(text='Для всей семьи', url='https://zelkultura.ru/events?tfc_charact:5137753[475890235]=%D0%94%D0%BB%D1%8F+%D0%B2%D1%81%D0%B5%D0%B9+%D1%81%D0%B5%D0%BC%D1%8C%D0%B8&tfc_div=:::')
ibtn_s2 = InlineKeyboardButton(text='Для взрослых', url='https://zelkultura.ru/events?tfc_charact:5137753[475890235]=%D0%94%D0%BB%D1%8F+%D0%B2%D0%B7%D1%80%D0%BE%D1%81%D0%BB%D1%8B%D1%85&tfc_div=:::')
ibtn_s3 = InlineKeyboardButton(text='Для детей', url='https://zelkultura.ru/events?tfc_charact:5137753[475890235]=%D0%94%D0%BB%D1%8F+%D0%B4%D0%B5%D1%82%D0%B5%D0%B9&tfc_div=:::')
ibtn_s4 = InlineKeyboardButton(text='Для подростков', url='https://zelkultura.ru/events?tfc_charact:5137753[475890235]=%D0%94%D0%BB%D1%8F+%D0%BF%D0%BE%D0%B4%D1%80%D0%BE%D1%81%D1%82%D0%BA%D0%BE%D0%B2&tfc_div=:::')
ibtn_s5 = InlineKeyboardButton(text='Главное меню', callback_data='return_main-menu')

ikb_second.add(ibtn_s1).add(ibtn_s2, ibtn_s3).add(ibtn_s4).add(ibtn_s5)

ikb_three = InlineKeyboardMarkup()   # Кружки и студии
ibtn_th1 = InlineKeyboardButton(text='Вокал', url='https://zelkultura.ru/clubs?tfc_charact:5137768[475890330]=%D0%92%D0%BE%D0%BA%D0%B0%D0%BB&tfc_charact:5137744[475890330]=%D0%9F%D0%BB%D0%B0%D1%82%D0%BD%D0%BE&tfc_div=:::')
ibtn_th2 = InlineKeyboardButton(text='Декоративное творчество', url='https://zelkultura.ru/clubs?tfc_charact:5137744[475890330]=%D0%9F%D0%BB%D0%B0%D1%82%D0%BD%D0%BE&tfc_charact:5137768[475890330]=%D0%94%D0%B5%D0%BA%D0%BE%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5+%D1%82%D0%B2%D0%BE%D1%80%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE&tfc_div=:::')
ibtn_th3 = InlineKeyboardButton(text='Изобразительное искусство', url='https://zelkultura.ru/clubs?tfc_charact:5137744[475890330]=%D0%9F%D0%BB%D0%B0%D1%82%D0%BD%D0%BE&tfc_charact:5137768[475890330]=%D0%98%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5+%D0%B8%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%BE&tfc_div=:::')
ibtn_th4 = InlineKeyboardButton(text='Развитие', url='https://zelkultura.ru/clubs?tfc_charact:5137744[475890330]=%D0%9F%D0%BB%D0%B0%D1%82%D0%BD%D0%BE&tfc_charact:5137768[475890330]=%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5&tfc_div=:::')
ibtn_th5 = InlineKeyboardButton(text='Спорт', url='https://zelkultura.ru/clubs?tfc_charact:5137744[475890330]=%D0%9F%D0%BB%D0%B0%D1%82%D0%BD%D0%BE&tfc_charact:5137768[475890330]=%D0%A1%D0%BF%D0%BE%D1%80%D1%82&tfc_div=:::')
ibtn_th6 = InlineKeyboardButton(text='Танец', url='https://zelkultura.ru/clubs?tfc_charact:5137744[475890330]=%D0%9F%D0%BB%D0%B0%D1%82%D0%BD%D0%BE&tfc_charact:5137768[475890330]=%D0%A2%D0%B0%D0%BD%D0%B5%D1%86&tfc_div=:::')
ibtn_th7 = InlineKeyboardButton(text='Театр', url='https://zelkultura.ru/clubs?tfc_charact:5137744[475890330]=%D0%9F%D0%BB%D0%B0%D1%82%D0%BD%D0%BE&tfc_charact:5137768[475890330]=%D0%A2%D0%B5%D0%B0%D1%82%D1%80&tfc_div=:::')
ibtn_th8 = InlineKeyboardButton(text='МОСКОВСКОЕ ДОЛГОЛЕТИЕ', url='https://zelkultura.ru/clubs?tfc_charact:5137768[475890330]=%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B5+%D0%B4%D0%BE%D0%BB%D0%B3%D0%BE%D0%BB%D0%B5%D1%82%D0%B8%D0%B5&tfc_div=:::')
ibtn_th9 = InlineKeyboardButton(text='ЧАТ С ПЕРСОНАЛЬНЫМ МЕНЕДЖЕРОМ', url='https://api.whatsapp.com/send/?phone=79956552559&text&type=phone_number&app_absent=0')
ibtn_th10 = InlineKeyboardButton(text='Главное меню', callback_data='return_main-menu')

ikb_three.add(ibtn_th2).add(ibtn_th1, ibtn_th6).add(ibtn_th5,ibtn_th4).add(ibtn_th7).add(ibtn_th3).add(ibtn_th8).add(ibtn_th9).add(ibtn_th10)


ikb_four = InlineKeyboardMarkup()   # Услуги
ibtn_four1 = InlineKeyboardButton(text='Аренда помещений', url='https://zelkultura.ru/arenda')
ibtn_four2 = InlineKeyboardButton(text='Организация экскурсий', url='https://zelkultura.ru/organizatsiya-ekskursiy')
ibtn_four3 = InlineKeyboardButton(text='Предложения для школ', url='https://zelkultura.ru/predlozheniya_dlya_shkol')
ibtn_four4 = InlineKeyboardButton(text='Полиграфия', url='https://zelkultura.ru/poligrafiya')
ibtn_four5 = InlineKeyboardButton(text='Бесплатные', url='https://zelkultura.ru/besplatnye-uslugi')
ibtn_four6 = InlineKeyboardButton(text='Главное меню', callback_data='return_main-menu')

ikb_four.add(ibtn_four1).add(ibtn_four2).add(ibtn_four3).add(ibtn_four4).add(ibtn_four5).add(ibtn_four6)

