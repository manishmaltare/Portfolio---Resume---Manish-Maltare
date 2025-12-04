# -*- coding: utf-8 -*-
"""Manish Maltare - Portfolio with Top Navigation and Transparent Buttons"""

import streamlit as st
import docx
import re

# ---------------------------- PAGE CONFIG ----------------------------
st.set_page_config(
    page_title="Manish Maltare - Digital Portfolio",
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
    background-attachment: fixed;
    color: white !important;
}

/* Remove default button styling */
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

/* Top navigation ribbon */
.top-nav {
    width:100%;
    background-color: rgba(0,0,0,0.5);
    padding:15px 0px;
    display:flex;
    justify-content:center;
    gap:50px;
    position:fixed;
    top:0;
    z-index:100;
    border-radius:0 0 10px 10px;
}

/* Top nav links */
.top-nav a {
    color: #FFFECB;
    text-decoration: none;
    font-weight:700;
    font-size:22px;
    transition:0.3s;
}
.top-nav a:hover {
    color:#FFD700;
}

/* Sidebar footer text */
.sidebar-footer {
    position: absolute;
    bottom: 20px;
    text-align: center;
    width: 100%;
    font-weight: bold;
}

/* Main content container padding */
.block-container {
    padding-top:90px !important;
    padding-left:150px !important;
    padding-right:150px !important;
    color: white !important;
}

/* Titles */
.main-title {
    font-size: 55px;
    font-weight: 900;
    color: white;
    text-align: center;
    margin-top: 10px;
}

.sub-title-tagline {
    font-size: 28px;
    color: white;
    text-align: center;
    margin-bottom: 40px;
}

.section-title {
    font-size: 32px;
    color: white;
    margin-top: 20px;
    margin-bottom: 20px;
}

/* Project details card */
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

/* Grid layout */
.grid-container {
    display: flex;
    gap: 50px;
}
.grid-column {
    flex: 1;
}

/* Make resume button transparent */
div[data-testid="stDownloadButton"] button {
    background-color: rgba(255,255,255,0.1) !important;
    color: white !important;
    border-radius:6px !important;
    font-weight:600 !important;
}
div[data-testid="stDownloadButton"] button:hover {
    background-color: rgba(255,255,255,0.3) !important;
    color: black !important;
}

/* ------------------ CIRCULAR ICON BUTTONS ------------------ */
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
    background: rgba(255,255,255,0.15);
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
    background: rgba(255,255,255,0.35);
    color: black;
    transform: scale(1.08);
    border-color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------- TOP NAVIGATION ----------------------------
st.markdown("""
<div class="top-nav">
    <a href="#about">About Me</a>
    <a href="#projects">Projects</a>
    <a href="#resume">Resume Download</a>
    <a href="#contact">Contact Me</a>
</div>
""", unsafe_allow_html=True)

import os

# ---------------------------- LOAD TEXT FILES ----------------------------
def read_docx_safe(path, fallback=""):
    if not os.path.exists(path):
        return fallback
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

about_text = read_docx_safe("About Me2.docx", "About content coming soon.")

# individual project write‑ups from separate files
nlp_text = read_docx_safe("NLP.docx", "NLP – Sentiment Analysis write‑up coming soon.")
logreg_text = read_docx_safe("Logistics-Regression.docx", "Logistic Regression project write‑up coming soon.")
solar_text = read_docx_safe("solar-panel-regression.docx", "Solar Panel Regression write‑up coming soon.")
ml_insights_text = read_docx_safe("Machine-learning-insights.docx", "Machine Learning Insights write‑up coming soon.")

# ---------------------------- LOAD LINKS ----------------------------
def load_links():
    data = open("Links.txt", "r").read()
    return {
        "ppt": re.findall(r"PPTs.*?:-(.*?)(?=GitHub Files)", data, re.S),
        "github_files": re.findall(r"GitHub Files.*?:-(.*?)(?=GitHub Deployment)", data, re.S),
        "github_deploy": re.findall(r"GitHub Deployment.*?:-(.*?)(?=App Deployment)", data, re.S),
        "app_links": re.findall(r"App Deployment.*?:-(.*?)(?=YouTube)", data, re.S),
        "youtube": re.findall(r"YouTube.*?:-(.*?)(?=Resume)", data, re.S),
        "resume": re.findall(r"Resume Link.*?:(.*)", data, re.S)
    }

links = load_links()

# ---------------------------- PROJECT FUNCTIONS ----------------------------
def get_project_links(project_name):
    result = {}
    mapping = {
        "ppt": "PPT",
        "github_files": "GitHub Files",
        "github_deploy": "GitHub Deployment Files",
        "app_links": "App Link",
        "youtube": "YouTube Video"
    }
    for key, label in mapping.items():
        block = links.get(key, [""])[0]
        match = re.findall(rf"{project_name}.*?:\s*(https?://\S+)", block)
        if match:
            result[label] = match[0]
    return result

# --- NLP PROJECT WITH CUSTOM LAYOUT + DOCX TEXT ---
def render_nlp_project():
    st.markdown(
        "<div class='hover-card'><h3>NLP - Sentiment Analysis</h3></div>",
        unsafe_allow_html=True
    )

    # body text from NLP.docx inside same style box
    st.markdown(
        f"""
        <div class='hover-card' style="margin-top:10px;">
            {nlp_text.replace('\n','<br>')}
        </div>
        """,
        unsafe_allow_html=True
    )

    # project image (if present)
    st.image("nlp_sentiment_image.png", use_container_width=True)

    # Circular icon links
    st.markdown("""
    <div class="circle-container">

        <a href="https://drive.google.com/file/d/1x81_6kRZkUQtznd0JxplF-7pSEt0dZrs/view?usp=sharing" target="_blank">
            <div class="circle-icon">Presentation</div>
        </a>

        <a href="https://github.com/manishmaltare/NLP---Sentiment-Analysis" target="_blank">
            <div class="circle-icon">GitHub<br>Script</div>
        </a>

        <a href="https://github.com/manishmaltare/Manish-Maltare/blob/main/SVC%20App%20Deployment%20-%20Sentiment%20Analysis%20-%20Group%201.py" target="_blank">
            <div class="circle-icon">Deployment<br>Script</div>
        </a>

        <a href="https://manish-maltare-kfkyft36opaoieycyadutr.streamlit.app/" target="_blank">
            <div class="circle-icon">App Link</div>
        </a>

    </div>
    """, unsafe_allow_html=True)

def render_generic_docx_project(title, body_text, project_name):
    # header + body from given DOCX
    st.markdown(
        f"<div class='hover-card'><h3>{title}</h3></div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class='hover-card' style="margin-top:10px;">
            {body_text.replace('\n','<br>')}
        </div>
        """,
        unsafe_allow_html=True
    )

    proj_links = get_project_links(project_name)
    if proj_links:
        for link_title, url in proj_links.items():
            st.markdown(
                f"<a href='{url}' target='_blank'><button class='stButton'>{link_title}</button></a>",
                unsafe_allow_html=True
            )

def render_project_details(project_name):
    if project_name == "NLP - Sentiment Analysis":
        render_nlp_project()
    elif project_name == "Logistic Regression - Titanic Survival Prediction":
        render_generic_docx_project(
            "Logistic Regression - Titanic Survival Prediction",
            logreg_text,
            project_name
        )
    elif project_name == "Solar Panel Regression":
        render_generic_docx_project(
            "Solar Panel Regression",
            solar_text,
            project_name
        )
    elif project_name == "Machine Learning Insights into GDP Drivers":
        render_generic_docx_project(
            "Machine Learning Insights into GDP Drivers",
            ml_insights_text,
            project_name
        )

# ---------------------------- SIDEBAR ----------------------------
st.sidebar.markdown(
    """
    <div class="sidebar-footer">
        Digital Portfolio<br>
        Manish Maltare
    </div>
    """,
    unsafe_allow_html=True
)

menu = st.sidebar.radio(
    "Navigation",
    ["About Me", "Projects", "Resume Download", "Contact Me"]
)

# ---------------------------- PAGE ROUTING ----------------------------
if menu == "About Me":
    st.markdown('<a id="about"></a>', unsafe_allow_html=True)
    st.markdown("<div class='main-title'>Manish Maltare</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title-tagline'>Digital Portfolio</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style="
            background-color: rgba(0,0,0,0.6);
            padding: 20px;
            border-radius: 10px;
            color: white;
            line-height: 1.6;
        ">
            {about_text.replace('\n','<br>')}
        </div>
        """,
        unsafe_allow_html=True
    )

elif menu == "Projects":
    st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
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
        render_project_details(st.session_state["selected_project"])

elif menu == "Resume Download":
    st.markdown('<a id="resume"></a>', unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Download Resume</div>", unsafe_allow_html=True)
    with open("Resume - Manish Maltare - final.pdf", "rb") as f:
        st.download_button(
            label="📄 Download Resume (PDF)",
            data=f,
            file_name="Manish_Maltare_Resume.pdf",
            mime="application/pdf",
            key="resume_button"
        )

elif menu == "Contact Me":
    st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Contact Me</div>", unsafe_allow_html=True)
    st.write("📧 **Email:** manishmaltare@gmail.com")
    st.write("📞 **Phone:** +91 9589945630")
    st.write("📍 **Address:** Keshavnagar, Pune")
