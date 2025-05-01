import streamlit as st
from astro import (
    calculate_moolank,
    calculate_bhagyank,
    calculate_sun_sign,
    suggest_direction,
    features_of_person,
    suitable_field
)
from astro_api import get_zodiac_message  # ✅ use this now instead of API

st.set_page_config(page_title="Astro Numerology Bot", page_icon="🔮")

st.title("🔮 Astro Numerology Bot")
st.write("Enter your birth details to discover your personality, lucky direction, and today's astrological insights.")

with st.form("astro_form"):
    dob_input = st.text_input("📅 Date of Birth (DD-MM-YYYY)")
    time_input = st.text_input("⏰ Time of Birth (HH:MM AM/PM)")
    location_input = st.text_input("📍 Birth Location")
    submitted = st.form_submit_button("Get My Report")

if submitted:
    try:
        day, month, year = map(int, dob_input.strip().split("-"))
        moolank = calculate_moolank(day)
        bhagyank = calculate_bhagyank(day, month, year)
        sun_sign = calculate_sun_sign(month, day)
        zodiac_sign = sun_sign.lower()

        direction = suggest_direction(moolank)
        traits = features_of_person(moolank)
        field = suitable_field(moolank)

        st.subheader("🔢 Numerology Report")
        st.write(f"**Moolank (मूलांक):** {moolank}")
        st.write(f"**Bhagyank (भाग्यांक):** {bhagyank}")
        st.write(f"**Personality Traits:** {traits}")
        st.write(f"**Suggested Direction:** {direction}")
        st.write(f"**Suitable Career Field:** {field}")

        st.subheader("♈ Sun Sign")
        st.write(f"**Zodiac Sign:** {sun_sign}")

        # ✅ Horoscope-style message using predefined text
        message = get_zodiac_message(zodiac_sign)
        st.subheader("🌟 Today's Message")
        st.write(message)

        st.balloons()

    except Exception as e:
        st.error(f"❌ Error: {e}")
