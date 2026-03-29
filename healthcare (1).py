import streamlit as st

# Title
st.title("Health Assistant 🏥")

# Name input
name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name} 👋 Stay healthy!")

# ------------------------------
# Medicine Reminder
# ------------------------------
st.header("Medicine Reminder 💊")

medicine = st.text_input("Enter medicine name")
time = st.time_input("Select time")

if st.button("Set Reminder"):
    st.success(f"Reminder set for {medicine} at {time}")

# ------------------------------
# Health Data
# ------------------------------
st.header("Health Data 🏃")

steps = st.number_input("Enter steps")
calories = st.number_input("Enter calories")

if st.button("Show Data"):
    st.write("Steps:", steps)
    st.write("Calories:", calories)

# ------------------------------
# Chatbot Mode Selection
# ------------------------------
st.header("Health Chatbot 🤖")

mode = st.selectbox(
    "Choose what you want to know",
    ["Full Info", "Causes", "Symptoms", "Precautions"]
)

query = st.text_input("Ask about disease (fever, cold, cough, etc.)")

# ------------------------------
# Disease Data
# ------------------------------
diseases = {
    "fever": {
        "causes": "Viral infection, bacterial infection, flu",
        "symptoms": "High temperature, sweating, weakness",
        "precautions": "Drink fluids, take rest, use paracetamol"
    },
    "cold": {
        "causes": "Virus, weather changes",
        "symptoms": "Runny nose, sneezing, sore throat",
        "precautions": "Warm fluids, rest, avoid cold food"
    },
    "cough": {
        "causes": "Infection, dust, allergy",
        "symptoms": "Dry/wet cough, throat irritation",
        "precautions": "Warm water, honey, avoid cold drinks"
    },
    "headache": {
        "causes": "Stress, lack of sleep, dehydration",
        "symptoms": "Head pain, sensitivity to light",
        "precautions": "Rest, drink water, reduce stress"
    },
    "diabetes": {
        "causes": "Insulin problem",
        "symptoms": "Frequent urination, thirst",
        "precautions": "Healthy diet, regular checkups"
    },
    "bp": {
        "causes": "Stress, salt intake",
        "symptoms": "Headache, dizziness",
        "precautions": "Exercise, low salt diet"
    },
    "covid": {
        "causes": "Virus infection",
        "symptoms": "Fever, cough, breathing issues",
        "precautions": "Mask, sanitizer, vaccination"
    }
}

# ------------------------------
# Chatbot Logic
# ------------------------------
if query:
    q = query.lower()

    found = False

    for disease in diseases:
        if disease in q:
            found = True
            st.subheader(f"🩺 {disease.capitalize()} Information")

            if mode == "Full Info":
                st.write("**Causes:**", diseases[disease]["causes"])
                st.write("**Symptoms:**", diseases[disease]["symptoms"])
                st.write("**Precautions:**", diseases[disease]["precautions"])

            elif mode == "Causes":
                st.write("**Causes:**", diseases[disease]["causes"])

            elif mode == "Symptoms":
                st.write("**Symptoms:**", diseases[disease]["symptoms"])

            elif mode == "Precautions":
                st.write("**Precautions:**", diseases[disease]["precautions"])

    if not found:
        st.warning("❌ Disease not found. Try fever, cold, cough, diabetes, BP, etc.")

# ------------------------------
# Extra Feature
# ------------------------------
st.header("💡 Daily Health Tip")

tips = [
    "Drink at least 2-3 liters of water 💧",
    "Exercise daily 🏃",
    "Sleep 7-8 hours 😴",
    "Eat healthy food 🥗"
]

if st.button("Get Tip"):
    import random
    st.success(random.choice(tips))