def calculate_sun_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries (Mesh - मेष)"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus (Vrishabh - वृषभ)"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini (Mithun - मिथुन)"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer (Karka - कर्क)"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo (Singh - सिंह)"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo (Kanya - कन्या)"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra (Tula - तुला)"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio (Vrishchik - वृश्चिक)"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius (Dhanu - धनु)"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn (Makar - मकर)"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius (Kumbh - कुम्भ)"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces (Meen - मीन)"
