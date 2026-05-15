import streamlit as st
import streamlit_notify as stn
import streamlit.components.v1 as components
import pandas as pd
from engine import run_diagnosis_engine
from engine import symptoms

st.set_page_config(layout="wide")


if "disclaimer_accepted" not in st.session_state:
    st.session_state.disclaimer_accepted = False

def show_blocking_modal():
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body { margin:0; }

        .overlay {
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.65);
            display:flex;
            align-items:center;
            justify-content:center;
            z-index:999999;
        }

        .modal {
            background: white;
            padding: 2rem;
            border-radius: 16px;
            width: 600px;
            max-width: 90%;
            text-align:center;
            box-shadow: 0 0 40px rgba(0,0,0,0.4);
            font-family: sans-serif;
        }

        h2 { color:#ff4b4b; }

        .btn {
            display:inline-block;
            margin-top:20px;
            padding:14px 28px;
            font-size:18px;
            border-radius:10px;
            background:#ff4b4b;
            color:white;
            text-decoration:none;
        }
    </style>
    </head>

    <body>
        <div class="overlay">
            <div class="modal">
                <h2>⚠️ Medical Disclaimer</h2>
                <p>
                This app is for <b>educational purposes only</b> and does NOT
                provide medical advice or diagnosis.<br><br>
                Always consult a qualified healthcare professional.
                </p>

                <a class="btn" href="?accepted=true" target="_top"> I Understand and Agree </a>
            </div>
        </div>
    </body>
    </html>
    """, height=0, width=0)


params = st.query_params

if not st.session_state.disclaimer_accepted:
    show_blocking_modal()

    if params.get("accepted") == "true":
        st.session_state.disclaimer_accepted = True
        st.query_params.clear()  # remove ?accepted from URL
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