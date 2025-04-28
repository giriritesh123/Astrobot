import streamlit as st
from astro import calculate_moolank, calculate_bhagyank, calculate_sun_sign, suggest_direction, features_of_person

st.set_page_config(page_title="Astro Numerology Bot 🔮", page_icon="🔮")

st.title("🔮 Astro Numerology Bot")
st.write("Welcome! Get your personalized astro-numerology report based on your birth details.")

with st.form("astro_form"):
    dob_input = st.text_input("📅 Enter your Date of Birth (DD-MM-YYYY)")
    time_input = st.text_input("⏰ Enter your Time of Birth (HH:MM AM/PM)")
    location_input = st.text_input("📍 Enter your Birth Location")
    submit_button = st.form_submit_button(label="Get My Report")

if submit_button:
    try:
        day, month, year = map(int, dob_input.strip().split('-'))
        
        moolank = calculate_moolank(day)
        bhagyank = calculate_bhagyank(day, month, year)
        sun_sign = calculate_sun_sign(month, day)
        direction = suggest_direction(moolank)
        features = features_of_person(moolank)
        
        st.success("✨ Your Astro-Numerology Report ✨")
        st.write(f"**📅 Date of Birth:** {dob_input}")
        st.write(f"**⏰ Birth Time:** {time_input}")
        st.write(f"**📍 Birth Location:** {location_input}")
        st.write(f"**🔢 Your Moolank (मूलांक):** {moolank}")
        st.write(f"**🎯 Your Bhagyank (भाग्यांक):** {bhagyank}")
        st.write(f"**♈ Your Sun Sign:** {sun_sign}")
        st.write(f"**🧭 Suggested Direction:** {direction}")
        st.write(f"**🌟 Personality Traits:** {features}")
        
        st.balloons()

    except:
        st.error("❌ Please enter Date of Birth correctly in DD-MM-YYYY format.")
