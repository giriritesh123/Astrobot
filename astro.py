def calculate_moolank(day):
    while day > 9:
        day = sum(map(int, str(day)))
    return day

def calculate_bhagyank(day, month, year):
    total = day + month + year
    while total > 9 and total not in (11, 22):
        total = sum(map(int, str(total)))
    return total

def calculate_sun_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"

def suggest_direction(moolank):
    directions = {
        1: "East",
        2: "North-West",
        3: "North-East",
        4: "South",
        5: "North",
        6: "South-East",
        7: "West",
        8: "South-West",
        9: "Any direction (if disciplined)"
    }
    return directions.get(moolank, "Direction not defined.")

def features_of_person(moolank):
    features = {
        1: "Leader, ambitious, independent",
        2: "Diplomatic, peace-loving, friendly",
        3: "Creative, social, optimistic",
        4: "Hardworking, practical, disciplined",
        5: "Adventurous, smart, quick thinker",
        6: "Responsible, caring, artistic",
        7: "Spiritual, thinker, introverted",
        8: "Powerful, ambitious, goal-oriented",
        9: "Compassionate, brave, selfless"
    }
    return features.get(moolank, "Traits not defined.")

def suitable_field(moolank):
    fields = {
        1: "Leadership, Politics, Business",
        2: "Teaching, Mediation, Psychology",
        3: "Arts, Entertainment, Writing",
        4: "Engineering, Admin, Logistics",
        5: "Marketing, Sales, Travel",
        6: "Care, Art, Beauty, Home-related fields",
        7: "Research, Spiritual Work, Healing",
        8: "Law, Finance, Management",
        9: "Defense, NGO, Service-oriented roles"
    }
    return fields.get(moolank, "Explore based on interest")
