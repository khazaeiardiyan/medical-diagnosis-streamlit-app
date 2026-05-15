import streamlit as st
import streamlit_notify as stn
import pandas as pd
from engine import run_diagnosis_engine
from engine import symptoms

if "disclaimer_accepted" not in st.session_state:
    st.session_state.disclaimer_accepted = False

def show_disclaimer():
    modal_html = """
    <style>
    .overlay {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        background-color: rgba(0,0,0,0.6);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
    }
    .modal {
        background: white;
        padding: 30px;
        border-radius: 12px;
        width: 600px;
        max-width: 90%;
        text-align: center;
        box-shadow: 0 0 30px rgba(0,0,0,0.3);
        font-family: sans-serif;
    }
    .modal h2 { color: #cc0000; }
    </style>

    <div class="overlay">
        <div class="modal">
            <h2>⚠️ Medical Disclaimer</h2>
            <p>
            This tool is for <b>educational purposes only</b>.
            It does NOT provide medical advice, diagnosis, or treatment.
            Always consult a qualified healthcare professional.
            </p>
        </div>
    </div>
    """
    st.markdown(modal_html, unsafe_allow_html=True)


if not st.session_state.disclaimer_accepted:
    show_disclaimer()

    st.markdown("### Please confirm to continue")
    if st.button("I Understand and Agree"):
        st.session_state.disclaimer_accepted = True
        st.rerun()

    st.stop() # to help me freez the app


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
        stn.notify()
        st.toast("This tool is for educational purposes only and is not a substitute for professional medical advice. Always consult a qualified healthcare provider for diagnosis and treatment.", icon="⚠️")
        st.divider()
        st.subheader("Top Predictions")
        st.dataframe(ranking_df)
        st.subheader("Diagnosis Probability Chart")
        st.bar_chart(ranking_df.set_index("Disease"),color="#FDAA48")

        for disease, confidence in ranking:
            if disease in emergency_diseases:
                st.error(f'{disease} is an emergency! please seek immidate action', icon="💀" )
    with st.popover("need medical help?"):
        st.markdown(
            f'''<a href="https://www.fraserhealth.ca/Service-Directory/Locations/Abbotsford/abbotsford-urgent-and-primary-care-centre">fraser health care center</a>''',
            unsafe_allow_html=True
        )