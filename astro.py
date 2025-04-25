import streamlit as st

# Title
st.title("🔮 Astrology & Numerology Bot")

# Ask user to input life path number
life_path = st.number_input("Enter your Life Path Number (1-9, 11, 22)", min_value=1, max_value=22)

# Dummy basic meanings (You will update real ones later!)
meanings = {
    1: "Leader, Independent, Strong-willed",
    2: "Diplomatic, Sensitive, Cooperative",
    3: "Creative, Joyful, Communicator",
    4: "Hardworking, Practical, Disciplined",
    5: "Adventurous, Freedom-loving, Dynamic",
    6: "Responsible, Caring, Teacher",
    7: "Spiritual, Thinker, Philosopher",
    8: "Powerful, Business-minded, Ambitious",
    9: "Humanitarian, Compassionate, Wise",
    11: "Visionary, Intuitive, Dreamer",
    22: "Master Builder, Visionary Leader, Practical Genius"
}

# Display meaning
if life_path in meanings:
    st.success(f"🌟 Your Life Path Number {life_path} Meaning: {meanings[life_path]}")
else:
    st.warning("Please enter a valid number between 1-9, 11, or 22.")
