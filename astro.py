

# Initialize colorama
init(autoreset=True)

def calculate_moolank(day):
    while day > 9:
        day = sum(map(int, str(day)))
    return day

def calculate_bhagyank(day, month, year):
    total = day + month + year
    while total > 9 and total != 11 and total != 22:
        total = sum(map(int, str(total)))
    return total

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

def suggest_direction(moolank):
    directions = {
        1: "🧭 East direction is lucky.",
        2: "🧭 North-West direction suits you.",
        3: "🧭 North-East direction will benefit you.",
        4: "🧭 South direction brings success.",
        5: "🧭 North direction is favorable.",
        6: "🧭 South-East direction suits your growth.",
        7: "🧭 West direction is lucky for you.",
        8: "🧭 South-West direction gives stability.",
        9: "🧭 Every direction is favorable if you maintain discipline."
    }
    return directions.get(moolank, "🧭 Direction not defined.")

def features_of_person(moolank):
    features = {
        1: "🔥 Leader, ambitious, independent.",
        2: "🌸 Diplomatic, peace-loving, friendly.",
        3: "🎨 Creative, social, optimistic.",
        4: "🏗️ Hardworking, practical, disciplined.",
        5: "🌟 Adventurous, smart, quick thinker.",
        6: "🎶 Responsible, caring, artistic.",
        7: "🔮 Spiritual, thinker, introverted.",
        8: "🏆 Powerful, ambitious, goal-oriented.",
        9: "❤️ Compassionate, brave, selfless."
    }
    return features.get(moolank, "✨ Personality traits not defined.")

def main():
    print(Fore.CYAN + Style.BRIGHT + "\n🔮 Welcome to Astro Numerology Bot 🔮\n")
    
    dob_input = input(Fore.YELLOW + "📅 Enter your Date of Birth (DD-MM-YYYY): ")
    time_input = input(Fore.YELLOW + "⏰ Enter your Time of Birth (HH:MM AM/PM): ")
    location_input = input(Fore.YELLOW + "📍 Enter your Birth Location: ")
    
    try:
        day, month, year = map(int, dob_input.strip().split('-'))
    except:
        print(Fore.RED + "❌ Invalid date format. Please enter in DD-MM-YYYY format.")
        return
    
    moolank = calculate_moolank(day)
    bhagyank = calculate_bhagyank(day, month, year)
    sun_sign = calculate_sun_sign(month, day)
    direction = suggest_direction(moolank)
    features = features_of_person(moolank)
    
    print(Fore.GREEN + "\n✨ Your Astro-Numerology Report ✨\n")
    print(Fore.BLUE + f"📅 Date of Birth: {dob_input}")
    print(Fore.BLUE + f"⏰ Birth Time: {time_input}")
    print(Fore.BLUE + f"📍 Birth Location: {location_input}\n")
    
    print(Fore.MAGENTA + f"🔢 Your Moolank (मूलांक): {moolank}")
    print(Fore.MAGENTA + f"🎯 Your Bhagyank (भाग्यांक): {bhagyank}")
    print(Fore.MAGENTA + f"♈ Your Sun Sign: {sun_sign}\n")
    
    print(Fore.CYAN + f"{direction}")
    print(Fore.CYAN + f"{features}")
    
    print(Fore.LIGHTYELLOW_EX + "\n🌟 Thank you for using Astro Numerology Bot! 🌟\n")

if __name__ == "__main__":
    main()
