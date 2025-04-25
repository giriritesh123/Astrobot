import streamlit as st

# Life Path Meanings Dictionary
life_path_meanings = {
    1: "Leader, Independent, Strong-willed",
    2: "Diplomatic, Sensitive, Cooperative",
    3: "Creative, Expressive, Cheerful",
    4: "Practical, Hardworking, Reliable",
    5: "Adventurous, Freedom-loving, Energetic",
    6: "Nurturing, Responsible, Protective",
    7: "Analytical, Introspective, Spiritual",
    8: "Ambitious, Efficient, Materially-successful",
    9: "Compassionate, Humanitarian, Generous",
    11: "Visionary, Inspirational, Enlightened",
    22: "Master Builder, Practical Visionary, Powerful Achiever"
}

# Streamlit Page Config
st.set_page_config(page_title="Astrology & Numerology Bot", page_icon="🔮", layout="wide")

# Sidebar for Input
st.sidebar.header("🔢 Enter your Details")
life_path_number = st.sidebar.number_input("Enter your Life Path Number (1-9, 11, 22)", min_value=1, max_value=22, step=1)

# Main Title
st.title("🔮 Astrology & Numerology Bot")
st.markdown("## Discover Your Life Path Meaning 🌟")

# Button to Generate Meaning
if st.sidebar.button("Show Meaning"):
    if life_path_number in life_path_meanings:
        meaning = life_path_meanings[life_path_number]
        st.success(f"✨ **Your Life Path Number {life_path_number} Meaning:** {meaning}")
    else:
        st.error("❌ Please enter a valid Life Path Number (1-9, 11, or 22).")

# Fun Message
st.markdown("---")
st.info("🌱 _'Your journey is written in the stars. Believe in yourself and shine bright!'_")

# Footer
st.markdown(
    "<h6 style='text-align: center; color: gray;'>Made with ❤️ by Ritesh Giri</h6>",
    unsafe_allow_html=True
)
