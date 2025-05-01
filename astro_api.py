def get_zodiac_message(sign):
    messages = {
        "aries": "You're bold and ambitious. Take charge today!",
        "taurus": "Your calm energy attracts success. Be steady.",
        "gemini": "Talk, connect, and learn — it's your day to shine!",
        "cancer": "Nurture your dreams. Your softness is your strength.",
        "leo": "Shine like the sun. You're meant to be seen.",
        "virgo": "Your detail-oriented nature makes you unbeatable today.",
        "libra": "Balance, charm, and harmony will guide your way.",
        "scorpio": "You're magnetic today. Trust your deep instincts.",
        "sagittarius": "Expand your mind. Travel mentally or physically.",
        "capricorn": "Discipline + determination = big results today.",
        "aquarius": "Think differently. Your ideas can spark change.",
        "pisces": "Dream and create. Your intuition is strong today."
    }
    return messages.get(sign.lower(), "You're amazing! Trust yourself.")
