import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/predict"


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Salary Predictor",
    page_icon="🤖",
    layout="centered"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #ddd;
    margin-top: 20px;
}

.result-card {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    border: 2px solid #4CAF50;
    margin-top: 25px;
}

.salary {
    font-size: 35px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🤖 Salary Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Enter your information and get an estimated salary.</div>',
    unsafe_allow_html=True
)


# ---------------- INPUT SECTION ----------------

st.subheader("👤 Enter Your Information")


age = st.slider(
    "Enter your age:",
    min_value=18,
    max_value=100,
    step=1
)


gender = st.selectbox(
    "Select your gender:",
    ["Male", "Female"]
)


education_level = st.selectbox(
    "Select your Education Level:",
    ["Bachelor's", "Master's", "PhD"]
)


job_title = st.text_input(
    "Enter your Job Title (capitalize the first letter of each word):",
    placeholder="e.g. Software Engineer",
    max_chars=50
)

years_of_experience = st.slider(
    "Enter your Years of Experience:",
    min_value=0,
    max_value=60,
    step=1
)


# ---------------- USER SELECTION ----------------

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.subheader("📋 Your Selection")

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Education:** {education_level}")

with col2:
    st.write(f"**Job Title:** {job_title if job_title else 'Not entered'}")
    st.write(f"**Experience:** {years_of_experience} years")

st.markdown("</div>", unsafe_allow_html=True)


# ---------------- PREDICTION ----------------

st.write("")


if st.button("🚀 Predict Salary", use_container_width=True):

    if not job_title.strip():
        st.warning("Please enter your job title first.")

    else:

        data = {
            "Age": age,
            "Gender": gender,
            "EducationLevel": education_level,
            "JobTitle": job_title,
            "YearsofExperience": years_of_experience
        }

        try:

            response = requests.post(
                url=API_URL,
                json=data,
                timeout=20
            )

            if response.status_code == 200:

                result = response.json()

                prediction = result["Salary"]

                st.markdown(
                    f"""
                    <div class="result-card">
                        <h3>💰 Estimated Salary</h3>
                        <div class="salary">
                            {prediction:,.0f} TK
                        </div>
                        <p>Based on the information you provided.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            elif response.status_code == 422:

                st.error(
                    "Invalid input. Please check the information you entered."
                )

            elif response.status_code == 500:

                st.error(
                    "The server encountered an internal error. Please try again."
                )

            else:

                st.error(
                    f"API Error: {response.status_code}"
                )


        except requests.exceptions.ConnectionError:

            st.error(
                "🔌 Could not connect to the prediction API. "
                "Make sure your FastAPI server is running."
            )

        except requests.exceptions.Timeout:

            st.error(
                "⏳ The prediction API took too long to respond."
            )

        except requests.exceptions.RequestException as e:

            st.error(
                f"Request failed: {e}"
            )
