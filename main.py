
import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Super Mom", layout="wide")

# Load data
affirmations = pd.read_csv("app/data/affirmations.csv")
community = pd.read_csv("app/data/community.csv")
resources = pd.read_csv("app/data/learn_resources.csv")
opportunities = pd.read_csv("app/data/opportunities.csv")

# Sidebar Navigation
st.sidebar.title("Super Mom")
page = st.sidebar.radio("Go to", ["Home", "Community Wall", "Uplift Me", "Mama Learns", "Opportunities", "AI Encourager"])

if page == "Home":
    st.title("💖 Super Mom")
    st.subheader("A safe space for healing, growth & emotional wellness")
    st.write("Welcome to Super Mom! Here, you're never alone.")

elif page == "Community Wall":
    st.title("💬 Community Wall")
    for index, row in community.iterrows():
        st.markdown(f"**{row['author'].capitalize()}** says: _{row['message']}_")

elif page == "Uplift Me":
    st.title("💖 Uplift Me")
    st.success(random.choice(affirmations['quote'].tolist()))

elif page == "Mama Learns":
    st.title("📚 Mama Learns")
    st.dataframe(resources)

elif page == "Opportunities":
    st.title("💼 Opportunities for Super Moms")
    st.dataframe(opportunities)

elif page == "AI Encourager":
    st.title("🤖 AI Encourager")
    user_input = st.text_input("How are you feeling today?")
    if user_input:
        if "tired" in user_input.lower():
            st.info("You're doing well. Rest is strength, not weakness. 🌸")
        elif "alone" in user_input.lower():
            st.info("You are not alone. This space is full of moms like you. 💖")
        elif "sad" in user_input.lower():
            st.info("Sad days come, but so do better days. Hold on, Super Mom. 💪")
        else:
            st.info("You are strong. You are enough. You are a Super Mom.")
