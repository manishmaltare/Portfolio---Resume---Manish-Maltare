import streamlit as st
import docx
import re
import os

# ---------------------------- PAGE CONFIG ----------------------------
st.set_page_config(
    page_title="Manish Maltare | Data Science & Analytics Portfolio",
    layout="wide"
)

# ---------------------------- CUSTOM CSS ----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&display=swap');

/* GLOBAL FONT */
* {
    font-family: 'Open Sans', sans-serif !important;
}

/* PAGE BACKGROUND IMAGE */
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/manishmaltare/Portfolio---Resume---Manish-Maltare/main/5072609.jpg");
    background-size: cover;
    background-position: center;
    color: white !important;
}

/* BUTTON STYLING */
.stButton>button {
    background-color: rgba(255,255,255,0.1) !important;
    color: white !important;
    border: none !important;
    padding: 8px 12px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    border-radius: 6px;
    cursor: pointer;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: rgba(255,255,255,0.3) !important;
    color: #000 !important;
}

/* SIDEBAR HEADER */
.sidebar-header-new {
    text-align: center;
    width: 100%;
    font-weight: bold;
    color: #000000;
    margin-bottom: 20px;
    font-size: 16px;
    padding-top: 20px;
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 5px;
}

/* SIDEBAR NAVIGATION FONT */
div[data-testid="stSidebar"] div[role="radiogroup"] label {
    font-size: 20px !important;
    font-weight: 700 !important;
    padding: 5px 0;
}

/* MAIN CONTENT CONTAINER FOR DESKTOP */
.block-container {
    padding-top: 90px !important;
    padding-left: 150px !important;
    padding-right: 150px !important;
    color: white !important;
}

/* TITLES (DESKTOP) */
.main-title {
    font-size: 55px;
    font-weight: 900;
    color: white;
    text-align: center;
    margin-top: 10px;
    white-space: nowrap;
    overflow: hidden;
}

.sub-title-tagline {
    font-size: 28px;
    color: white;
    text-align: center;
    margin-bottom: 40px;
}

.section-title {
    font-size: 45px;
    color: white;
    margin-top: 20px;
    margin-bottom: 20px;
}

/* PROJECT CARD */
.hover-card {
    padding: 15px;
    border-radius: 10px;
    background-color: rgba(0,0,0,0.6);
    color: white;
    margin-top: 20px;
}
.hover-card h3 {
    margin-top: 0;
}

/* CIRCLE LINK BUTTONS */
.circle-container {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-top: 25px;
    flex-wrap: wrap;
}

.circle-icon {
    width: 120px;
    height: 120px;
    background: rgba(0,0,0,0.7);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-size: 15px;
    font-weight: 700;
    color: white;
    transition: 0.3s;
    border: 2px solid rgba(255,255,255,0.4);
    padding: 10px;
}
.circle-icon:hover {
    background: rgba(0,0,0,0.85);
    transform: scale(1.08);
    border-color: white;
}

/* MOBILE FIXES */
@media (max-width: 768px) {
    
    .block-container {
        padding-left: 10px !important;
        padding-right: 10px !important;
        padding-top: 40px !important;
    }

    .main-title {
        font-size: 30px !important;
        white-space: normal !important;
        text-align: center !important;
        line-height: 1.2;
    }

    .sub-title-tagline {
        font-size: 18px !important;
        line-height: 1.2;
    }

    .section-title {
        font-size: 26px !important;
        text-align: center !important;
    }

    .circle-container {
        justify-content: center !important;
        gap: 10px !important;
    }

    .circle-icon {
        width: 85px !important;
        height: 85px !important;
        font-size: 11px !important;
        padding: 5px !important;
    }

    div[data-testid="stColumn"] button {
        width: 100% !important;
        margin-top: 8px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------------------- LOAD TEXT FILES ----------------------------
def read_docx_safe(path):
    if path == "About Me2.docx":
        return "I am a dedicated Data Science and Analytics professional with a passion for transforming complex data into actionable insights. My expertise lies in Python, Machine Learning, NLP, and deploying models using Streamlit. I thrive on challenges and aim to deliver data-driven solutions that significantly impact business outcomes."
    if path == "NLP.docx":
        return "Project: NLP - Sentiment Analysis.\nUsed Natural Language Processing (NLP) techniques, including TF-IDF and Logistic Regression, to classify text reviews."
    if path == "Logistics Regression.docx":
        return "Project: Logistic Regression - Titanic Survival Prediction.\nApplied Logistic Regression to predict survival using feature engineering and data cleaning."
    if path == "solar panel regression.docx":
        return "Project: Solar Panel Regression.\nMultivariate linear regression predicting solar output using weather variables."
    if path == "Machine learning insights.docx":
        return "Project: Machine Learning Insights into GDP Drivers.\nUsed ML models to analyze key macroeconomic indicators driving GDP."
    return ""

about_text = read_docx_safe("About Me2.docx")
nlp_text = read_docx_safe("NLP.docx")
logreg_text = read_docx_safe("Logistics Regression.docx")
solar_text = read_docx_safe("solar panel regression.docx")
ml_insights_text = read_docx_safe("Machine learning insights.docx")

# ---------------------------- PROJECT LINK RENDER ----------------------------
def render_circle_links_fixed(project_name):
    links_map = {
        "NLP - Sentiment Analysis": {
            "Presentation": "https://drive.google.com/file/d/1x81_6kRZkUQtznd0JxplF-7pSEt0dZrs/view?usp=sharing",
            "GitHub - Script": "https://github.com/manishmaltare/NLP---Sentiment-Analysis",
            "Deployment": "https://github.com/manishmaltare/Manish-Maltare/blob/main/SVC%20App%20Deployment%20-%20Sentiment%20Analysis%20-%20Group%201.py",
            "App Link": "https://manish-maltare-kfkyft36opaoieycyadutr.streamlit.app/"
        },
        "Logistic Regression - Titanic Survival Prediction": {
            "GitHub - Script": "https://github.com/manishmaltare/Manish-Maltare/blob/main/RESUME_Logistic_Regression_Assignment.ipynb",
            "Deployment": "https://github.com/manishmaltare/Manish-Maltare/blob/main/final_pickle_of_assignment_logisticregression_deployment_final.py",
            "App Link": "https://manish-maltare-8pw78deodbfyqewds8uere.streamlit.app/"
        },
        "Solar Panel Regression": {
            "Presentation": "https://drive.google.com/file/d/1unMOirI9oFjn2lKJH97sVE4985Gp0mea/view?usp=sharing",
            "GitHub - Script": "https://github.com/manishmaltare/Solar-Panel-Regression-1",
            "Deployment": "https://github.com/manishmaltare/Solar-Panel-Regression-1/blob/main/resume_solar_panel_regression.py",
            "App Link": "https://solar-panel-regression-1-q3nwvmajqzqloi5aevksgq.streamlit.app/"
        },
        "Machine Learning Insights into GDP Drivers": {
            "Report": "https://drive.google.com/file/d/1Z0z1QTypvr6lqDpTgLb05LM_R5775P1T/view?usp=sharing",
            "GitHub - Script": "https://github.com/manishmaltare/Project---Machine-Learning-Insights-into-GDP-Drivers",
            "YouTube": "https://youtu.be/y6vTDqyEPdw"
        },
    }

    proj_links = links_map.get(project_name, {})
    if not proj_links:
        return

    html_links = []
    for label, url in proj_links.items():
        html_links.append(
            f'<a href="{url}" target="_blank"><div class="circle-icon">{label}</div></a>'
        )
    html = f'<div class="circle-container">{" ".join(html_links)}</div>'
    st.markdown(html, unsafe_allow_html=True)

# ---------------------------- PROJECT BLOCK RENDER ----------------------------
def render_docx_block(title, body_html, project_name=None):
    st.markdown(
        f"<div class='hover-card'><h3>{title}</h3></div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div class='hover-card' style='margin-top:10px;'>{body_html}</div>",
        unsafe_allow_html=True
    )
    if project_name:
        render_circle_links_fixed(project_name)

# ---------------------------- SIDEBAR ----------------------------
st.sidebar.markdown(
    """
    <div class="sidebar-header-new">
        Digital Portfolio<br>
        Manish Maltare
    </div>
    """,
    unsafe_allow_html=True
)

menu = st.sidebar.radio(
    "Navigation",
    ["About Me", "Projects", "Resume", "Contact Me"]
)

# ---------------------------- ABOUT ME PAGE ----------------------------
if menu == "About Me":
    st.markdown("<div class='main-title'>Manish Maltare</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title-tagline'>Digital Portfolio</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px; border-radius: 10px;">
            {about_text.replace("\n", "<br>")}
        </div>
        """,
        unsafe_allow_html=True
    )

    # FIXED LINKEDIN CIRCLE BUTTON
    linkedin_url = "https://www.linkedin.com/in/manishmaltare"
    linkedin_html = f"""
        <div class="circle-container" style="margin-top: 25px; justify-content: center !important;">
            <a href="{linkedin_url}" target="_blank">
                <div class="circle-icon">LinkedIn</div>
            </a>
        </div>
    """
    st.markdown(linkedin_html, unsafe_allow_html=True)

# ---------------------------- PROJECT PAGE ----------------------------
elif menu == "Projects":
    st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3>Classification</h3>", unsafe_allow_html=True)
        if st.button("NLP - Sentiment Analysis"):
            st.session_state["selected_project"] = "NLP - Sentiment Analysis"
        if st.button("Logistic Regression - Titanic Survival Prediction"):
            st.session_state["selected_project"] = "Logistic Regression - Titanic Survival Prediction"

    with col2:
        st.markdown("<h3>Regression</h3>", unsafe_allow_html=True)
        if st.button("Solar Panel Regression"):
            st.session_state["selected_project"] = "Solar Panel Regression"
        if st.button("Machine Learning Insights into GDP Drivers"):
            st.session_state["selected_project"] = "Machine Learning Insights into GDP Drivers"

    if st.session_state.get("selected_project"):
        selected = st.session_state["selected_project"]

        if selected == "NLP - Sentiment Analysis":
            body_html = nlp_text.replace("\n", "<br>")
        elif selected == "Logistic Regression - Titanic Survival Prediction":
            body_html = logreg_text.replace("\n", "<br>")
        elif selected == "Solar Panel Regression":
            body_html = solar_text.replace("\n", "<br>")
        else:
            body_html = ml_insights_text.replace("\n", "<br>")

        render_docx_block(selected, body_html, selected)

# ---------------------------- RESUME PAGE ----------------------------
elif menu == "Resume":
    st.markdown("<div class='section-title'>Download Resume</div>", unsafe_allow_html=True)

    try:
        with open("Resume - Manish Maltare - final.pdf", "rb") as f:
            st.download_button(
                label="📄 Download Resume (PDF)",
                data=f,
                file_name="Manish_Maltare_Resume.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error("Resume file not found in the application directory.")

# ---------------------------- CONTACT PAGE ----------------------------
elif menu == "Contact Me":
    st.markdown("<div class='section-title'>Contact Me</div>", unsafe_allow_html=True)
    st.write("📧 **Email:** manishmaltare@gmail.com")
    st.write("📞 **Phone:** +91 9589945630")
    st.write("📍 **Address:** Keshavnagar, Pune")

# ---------------------------- FOOTER ----------------------------
st.markdown(
    "<div style='text-align:center; margin-top: 50px; padding: 20px; background-color: rgba(0,0,0,0.5); border-radius: 10px;'>Website created by Manish Maltare</div>",
    unsafe_allow_html=True
)
