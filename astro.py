import streamlit as st
from datetime import datetime

# Mulank and Bhagyank meanings (basic examples)
mulank_meanings = {
    1: "Leader, Independent, Strong",
    2: "Cooperative, Diplomatic, Sensitive",
    3: "Creative, Expressive, Cheerful",
    4: "Practical, Hardworking, Reliable",
    5: "Adventurous, Dynamic, Free-spirited",
    6: "Caring, Responsible, Nurturing",
    7: "Spiritual, Analytical, Deep Thinker",
    8: "Ambitious, Efficient, Business-minded",
    9: "Compassionate, Humanitarian, Wise"
}

bhagyank_meanings = {
    1: "Leadership qualities will bring success.",
    2: "Collaboration and partnerships bring growth.",
    3: "Creative expression leads to fortune.",
    4: "Hard work and structure shape destiny.",
    5: "Flexibility and change open new paths.",
    6: "Family, harmony and service define your journey.",
    7: "Spirituality and wisdom are your strengths.",
    8: "Business, power and authority await you.",
    9: "Charity and compassion will reward you."
}

# Streamlit Page Config
st.set_page_config(page_title="Astrology & Numerology Bot", page_icon="🔮", layout="centered")

# Title
st.title("🔮 AstroBot - DOB Based Numerology Insights")

# Sidebar for Input
st.sidebar.header("Enter your Birth Details")
dob = st.sidebar.date_input("Enter your Date of Birth:")

# Calculate Mulank
def calculate_mulank(dob):
    day = dob.day
    while day > 9:
        day = sum(map(int, str(day)))
    return day

# Calculate Bhagyank (Sum of DDMMYYYY digits)
def calculate_bhagyank(dob):
    digits = f"{dob.day:02d}{dob.month:02d}{dob.year}"
    total = sum(map(int, digits))
    while total > 9:
        total = sum(map(int, str(total)))
    return total

# Calculate Life Path Number (similar to Bhagyank)
def calculate_life_path(dob):
    total = sum(map(int, dob.strftime("%Y%m%d")))
    while total > 9 and total not in [11, 22]:
        total = sum(map(int, str(total)))
    return total

# Button to Process
if st.sidebar.button("Show My Astro Details"):
    mulank = calculate_mulank(dob)
    bhagyank = calculate_bhagyank(dob)
    life_path = calculate_life_path(dob)

    st.markdown("---")
    st.subheader("🌟 Your Numerology Insights:")

    st.success(f"🔢 **Mulank (Moolank): {mulank}** - {mulank_meanings.get(mulank, 'Special Personality')}")
    st.success(f"🔮 **Bhagyank (Destiny Number): {bhagyank}** - {bhagyank_meanings.get(bhagyank, 'Special Destiny Path')}")
    st.success(f"🌈 **Life Path Number: {life_path}** - Reflects your spiritual journey.")

    st.markdown("---")
    st.info("✨ _'Your date of birth hides powerful secrets. Embrace your unique journey.'_")

# Footer
st.markdown(
    "<h6 style='text-align: center; color: gray;'>Made with ❤️ by Ritesh Giri</h6>",
    unsafe_allow_html=True
)
