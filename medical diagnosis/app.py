import streamlit as st
import pandas as pd
from engine import run_diagnosis_engine
from engine import symptoms

st.title("Medical Diagnosis Assistant 🩺")

age = st.number_input("Enter your age", min_value=0, max_value=99)
gender = st.selectbox("Biological sex", ["male", "female", "other"])
symptom_names = [data["name"] for data in symptoms.values()]

selected_symptom_names = st.multiselect(
    "Search and select your symptoms:",
    symptom_names
)

name_to_id = {data["name"]: sid for sid, data in symptoms.items()}
selected_symptom_ids = [name_to_id[name] for name in selected_symptom_names]

emergency_diseases = ["heart attack", "sepsis", "stroke",
                      "meningitis", "pulmonary embolism",
                      "appendicitis"]

if st.button("Run Diagnosis"):
    result = run_diagnosis_engine(age, gender, selected_symptom_ids)
    if result["message"] != "success" :
        st.warning(result["message"], icon="⚠️")
    else:
        ranking =  result["ranking"]
        ranking_df = pd.DataFrame(ranking, columns=["Disease", "Confidence (%)"])
        ranking_df["Confidence (%)"] *= 100
        ranking_df["Confidence (%)"] = ranking_df["Confidence (%)"].round(1)
        st.subheader("Top Predictions")
        st.dataframe(ranking_df)
        st.subheader("Diagnosis Probability Chart")
        st.bar_chart(ranking_df.set_index("Disease"),color="#FDAA48")
        st.markdown("⚠️ This tool is for educational purposes only and is not a substitute for professional medical advice. Always consult a qualified healthcare provider for diagnosis and treatment.")

        for disease, confidence in ranking:
            if disease in emergency_diseases:
                st.error(f'{disease} is an emergency! please seek immidate action', icon="💀" )
    with st.popover("for more info:"):
        st.markdown(
            "<a href="https://www.fraserhealth.ca/Service-Directory/Locations/Abbotsford/abbotsford-urgent-and-primary-care-centre">click here</a>",
            unsafe_allow_html=True
        )