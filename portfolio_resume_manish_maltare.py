# -*- coding: utf-8 -*-
"""Portfolio Resume - Manish Maltare | Animated Green Theme"""

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

@import url('https://fonts.cdnfonts.com/css/copperplate-gothic');

/* GLOBAL FONT */
* {
    font-family: 'Copperplate Gothic', sans-serif !important;
}

/* PAGE BACKGROUND - GREEN (#9DC183) */
body {
    background-color: #9DC183 !important;
}

/* CONTAINER WIDTH (NARROW CENTERED LOOK) */
.block-container {
    padding-left: 180px !important;
    padding-right: 180px !important;
    animation: fadeSlideZoom 0.7s ease-in-out;
    background-color: #9DC183 !important;
}

/* MAIN CONTENT AREA - GREEN BACKGROUND */
.main {
    background-color: #9DC183 !important;
}

[data-testid="stAppViewContainer"] {
    background-color: #9DC183 !important;
}

/* MIXED ANIMATION */
@keyframes fadeSlideZoom {
    0% { opacity: 0; transform: translateY(25px) scale(0.96); }
    100% { opacity: 1; transform: translateY(0px) scale(1); }
}

/* ---------------------- SIDEBAR - LIGHT GREY BACKGROUND ---------------------- */
section[data-testid="stSidebar"] {
    background-color: #D3D3D3 !important;  /* light grey */
    padding: 20px 15px;
    width: 220px !important; /* reduce width */
}

/* SIDEBAR TITLE - BLACK TEXT */
.sidebar-title {
    font-size: 28px;
    font-weight: 800;
    color: #000000 !important;
    text-align: left;
    line-height: 1.1;
    margin-bottom: 40px;
}

/* NAV ITEMS - BLACK TEXT */
div[data-testid="stSidebar"] label,
div[data-testid="stSidebar"] span {
    color: #000000 !important;
    font-weight: 600 !important;
}

/* RADIO BUTTON OPTIONS (Navigation Items) */
div[data-testid="stSidebar"] .st-radio > label > div {
    color: #000000 !important;
}

/* RADIO BUTTON TEXT */
div[data-testid="stSidebar"] .st-radio label span {
    color: #000000 !important;
    font-size: 16px !important;
}

/* ALL TEXT IN SIDEBAR */
div[data-testid="stSidebar"] * {
    color: #000000 !important;
}

/* RADIO BUTTON HOVER */
div[data-testid="stSidebar"] .st-radio:hover {
    background-color: rgba(0, 0, 0, 0.1) !important;
}

/* SELECTED RADIO BUTTON */
div[data-testid="stSidebar"] .st-radio [role="radio"][aria-checked="true"] {
    color: #000000 !important;
}

/* ---------------------- TITLES - BLACK TEXT ON GREEN ---------------------- */

.main-title {
    font-size: 55px;
    font-weight: 900;
    color: #000000;
    text-align: center;
    margin-top: 10px;
    margin-bottom: -10px;
}

.sub-title-tagline {
    font-size: 28px;
    font-weight: 600;
    color: #333333;
    text-align: center;
    margin-bottom: 45px;
}

.section-title {
    font-size: 32px;
    font-weight: 700;
    color: #000000;
    margin-top: 40px;
    margin-bottom: 20px;
}

/* PROJECT CATEGORY TITLE */
.project-category {
    font-size: 24px;
    font-weight: 700;
    color: #000000;
    margin-bottom: 15px;
}

/* PROJECT BUTTON CONTAINER */
.project-button {
    margin-bottom: 30px;
}

/* Reduce font size of project buttons */
.project-button button {
    font-size: 14px !important;
    padding: 8px 12px !important;
    border-radius: 8px !important;
    width: 100% !important;
    text-align: center !important;
    margin-bottom: 10px !important;
}

/* CONTENT CARD WITH HOVER EFFECT */
.hover-card {
    padding: 18px;
    border-radius: 10px;
    background-color: #E6E6E6;
    border: 1px solid #999999;
    color: #000000;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.hover-card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.15);
    background-color: #CCCCCC;
}

/* BUTTON LINKS */
.link-btn a {
    padding: 8px 15px;
    margin-right: 10px;
    background-color: #000000;
    color: white !important;
    border-radius: 6px;
    text-decoration: none;
    font-size: 15px;
    border: 1px solid #000000;
    transition: 0.3s;
}
.link-btn a:hover {
    background-color: white;
    color: black !important;
    border-color: black;
}

/* TEXT COLOR - BLACK ON GREEN */
.stMarkdown, .stWrite, .stText {
    color: #000000 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------- LOAD TEXT FILES ----------------------------
def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

about_text = read_docx("About Me2.docx")
projects_text = read_docx("Projects2.docx")

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
def extract_project_section(project_name):
    pattern = rf"{project_name}(.*?)(?=[A-Z ]{{3,}}|$)"
    match = re.search(pattern, projects_text, re.S)
    return match.group(1).strip() if match else ""

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
        match = re.findall(rf"{project_name}.*?:\s*(https?://\\S+)", block)
        if match:
            result[label] = match[0]
    return result

def render_project(project_name):
    st.markdown(f"<div class='project-category'>{project_name}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='hover-card'>{extract_project_section(project_name)}</div>", unsafe_allow_html=True)
    proj_links = get_project_links(project_name)
    if proj_links:
        st.markdown("<div class='link-btn'>", unsafe_allow_html=True)
        for title, url in proj_links.items():
            st.markdown(f"<a href='{url}' target='_blank'>{title}</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------- SIDEBAR ----------------------------
st.sidebar.markdown(
    "<div class='sidebar-title'>Manish Maltare<br>Portfolio</div>",
    unsafe_allow_html=True
)

menu = st.sidebar.radio(
    "Navigation",
    ["About Me", "Projects", "Resume Download", "Contact Me"]
)

# ---------------------------- PAGE ROUTING ----------------------------

# ABOUT ME PAGE
if menu == "About Me":

    st.markdown("<div class='main-title'>Manish Maltare</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title-tagline'>Digital Portfolio</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)

    st.write(about_text)

# PROJECTS PAGE
elif menu == "Projects":

    st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)

    # Create two columns for Classification and Regression
    col1, col2 = st.columns(2)

    selected_project = None

    with col1:
        st.markdown("<div class='project-category'>Classification</div>", unsafe_allow_html=True)
        st.markdown("<div class='project-button'>", unsafe_allow_html=True)
        if st.button("NLP - Sentiment Analysis"):
            selected_project = "NLP - Sentiment Analysis"
        if st.button("Logistic Regression - Titanic Survival Prediction"):
            selected_project = "Logistic Regression - Titanic Survival Prediction"
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='project-category'>Regression</div>", unsafe_allow_html=True)
        st.markdown("<div class='project-button'>", unsafe_allow_html=True)
        if st.button("Solar Panel Regression"):
            selected_project = "Solar Panel Regression"
        if st.button("Machine Learning Insights into GDP Drivers"):
            selected_project = "Machine Learning Insights into GDP Drivers"
        st.markdown("</div>", unsafe_allow_html=True)

    # Show project details below buttons if a project is selected
    if selected_project:
        st.markdown(f"<div class='section-title'>About the Project: {selected_project}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='hover-card'>{extract_project_section(selected_project)}</div>", unsafe_allow_html=True)
        proj_links = get_project_links(selected_project)
        if proj_links:
            st.markdown("<div class='link-btn'>", unsafe_allow_html=True)
            for title, url in proj_links.items():
                st.markdown(f"<a href='{url}' target='_blank'>{title}</a>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# RESUME PAGE
elif menu == "Resume Download":
    st.markdown("<div class='section-title'>Download Resume</div>", unsafe_allow_html=True)
    with open("Resume - Manish Maltare - final.pdf", "rb") as f:
        st.download_button(
            label="📄 Download Resume (PDF)",
            data=f,
            file_name="Manish_Maltare_Resume.pdf",
            mime="application/pdf"
        )

# CONTACT PAGE
elif menu == "Contact Me":
    st.markdown("<div class='section-title'>Contact Me</div>", unsafe_allow_html=True)

    st.write("📧 **Email:** manishmaltare@gmail.com")
    st.write("📞 **Phone:** +91 9589945630")
    st.write("📍 **Address:** Keshavnagar, Pune")
