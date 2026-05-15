import streamlit as st
import streamlit_notify as stn
import pandas as pd
from engine import run_diagnosis_engine
from engine import symptoms

if "disclaimer_accepted" not in st.session_state:
    st.session_state.disclaimer_accepted = False

def show_blocking_modal():
    st.markdown("""
    <style>
    /* Fullscreen overlay */
    .overlay {
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,0.65);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 999999;
    }

    /* Modal adapts to Streamlit theme */
    .modal {
        background: var(--background-color);
        color: var(--text-color);
        padding: 2rem;
        border-radius: 16px;
        width: 650px;
        max-width: 90%;
        text-align: center;
        box-shadow: 0 0 40px rgba(0,0,0,0.4);
        border: 1px solid rgba(150,150,150,0.2);
        font-family: sans-serif;
    }

    .modal h2 {
        margin-top: 0;
        color: #ff4b4b;
    }

    .big-btn {
        margin-top: 20px;
        padding: 12px 28px;
        font-size: 18px;
        border-radius: 10px;
        border: none;
        background: #ff4b4b;
        color: white;
        cursor: pointer;
    }
    </style>

    <div class="overlay">
        <div class="modal">
            <h2>⚠️ Medical Disclaimer</h2>
            <p>
            This app is for <b>educational purposes only</b> and does NOT provide
            medical advice, diagnosis, or treatment.<br><br>
            Always consult a qualified healthcare professional.
            </p>

            <form action="" method="post">
                <button class="big-btn" name="accept" type="submit">
                    I Understand and Agree
                </button>
            </form>
        </div>
    </div>
    """, unsafe_allow_html=True)


# show modal until accepted
if not st.session_state.disclaimer_accepted:
    show_blocking_modal()

    # Detect form submit
    if st.query_params.get("accept") is not None:
        st.session_state.disclaimer_accepted = True
        st.rerun()

    st.stop()

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