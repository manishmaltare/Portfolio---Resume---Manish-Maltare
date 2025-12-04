# -*- coding: utf-8 -*-
"""Portfolio Resume - Manish Maltare | Projects Grid Layout with details below"""

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
* { font-family: 'Copperplate Gothic', sans-serif !important; }

/* MAIN BACKGROUND */
body, .block-container, [data-testid="stAppViewContainer"] { background-color: #000000 !important; }

/* MAIN CONTENT WIDTH */
.block-container { padding-left: 150px !important; padding-right: 150px !important; animation: fadeSlideZoom 0.7s ease-in-out; }

/* ANIMATION */
@keyframes fadeSlideZoom {
    0% { opacity: 0; transform: translateY(25px) scale(0.96); }
    100% { opacity: 1; transform: translateY(0px) scale(1); }
}

/* SIDEBAR - LIGHT GREY */
section[data-testid="stSidebar"] { background-color: #D3D3D3 !important; padding: 20px 15px; }

/* SIDEBAR TITLE */
.sidebar-title { font-size: 28px; font-weight: 800; color: #000000 !important; text-align: left; line-height: 1.1; margin-bottom: 30px; }

/* NAV ITEMS */
div[data-testid="stSidebar"] label,
div[data-testid="stSidebar"] span,
div[data-testid="stSidebar"] .stRadio > label > div {
    color: #000000 !important; font-weight: 600 !important;
}

/* MAIN TITLES */
.main-title { font-size: 55px; font-weight: 900; color: #FFFFFF; text-align: center; margin-top: 10px; margin-bottom: -10px; }
.sub-title-tagline { font-size: 28px; font-weight: 600; color: #CCCCCC; text-align: center; margin-bottom: 45px; }
.section-title { font-size: 32px; font-weight: 700; color: #FFFFFF; margin-top: 40px; margin-bottom: 20px; }

/* PROJECT CATEGORY TITLE */
.project-category { font-size: 28px; font-weight: 700; color: #FFFFFF; margin-bottom: 15px; }

/* PROJECT CARD */
.project-card {
    padding: 15px; border-radius: 10px; background-color: #1A1A1A; border: 1px solid #333333;
    color: #E8E8E8; text-align: center; cursor: pointer; transition: transform 0.25s ease, box-shadow 0.25s ease;
    margin-bottom: 15px;
}
.project-card:hover {
    transform: translateY(-4px); box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.2); background-color: #252525;
}

/* PROJECT DETAILS BELOW GRID */
.project-detail {
    padding: 18px; border-radius: 10px; background-color: #252525; border: 1px solid #555555;
    color: #E8E8E8; margin-top: 30px;
}

/* BUTTON LINKS */
.link-btn a {
    padding: 8px 15px; margin-right: 10px; background-color: white; color: black !important;
    border-radius: 6px; text-decoration: none; font-size: 15px; border: 1px solid white; transition: 0.3s;
}
.link-btn a:hover { background-color: #000000; color: white !important; border-color: white; }

/* TEXT COLOR - WHITE */
.stMarkdown, .stWrite, .stText { color: #E8E8E8 !important; }

</style>
""", unsafe_allow_html=True)

# ---------------------------- LOAD DOCX ----------------------------
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

# ---------------------------- SIDEBAR ----------------------------
st.sidebar.markdown("<div class='sidebar-title'>Manish Maltare<br>Portfolio</div>", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Navigation",
    ["About Me", "Projects", "Resume Download", "Contact Me"]
)

# ---------------------------- PAGE ROUTING ----------------------------
if menu == "About Me":
    st.markdown("<div class='main-title'>Manish Maltare</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title-tagline'>Digital Portfolio</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)
    st.write(about_text)

# ---------------------------- PROJECTS PAGE ----------------------------
elif menu == "Projects":
    st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # Store selected project
    selected_project = None

    with col1:
        st.markdown("<div class='project-category'>Classification</div>", unsafe_allow_html=True)
        if st.button("NLP - Sentiment Analysis"):
            selected_project = "NLP - Sentiment Analysis"
        if st.button("Logistic Regression - Titanic Survival Prediction"):
            selected_project = "Logistic Regression - Titanic Survival Prediction"

    with col2:
        st.markdown("<div class='project-category'>Regression</div>", unsafe_allow_html=True)
        if st.button("Solar Panel Regression"):
            selected_project = "Solar Panel Regression"
        if st.button("Machine Learning Insights into GDP Drivers"):
            selected_project = "Machine Learning Insights into GDP Drivers"

    # Show project details below all cards
    if selected_project:
        st.markdown(f"<div class='project-detail'>", unsafe_allow_html=True)
        st.markdown(f"### {selected_project}", unsafe_allow_html=True)
        st.markdown(extract_project_section(selected_project))
        proj_links = get_project_links(selected_project)
        if proj_links:
            st.markdown("<div class='link-btn'>", unsafe_allow_html=True)
            for title, url in proj_links.items():
                st.markdown(f"<a href='{url}' target='_blank'>{title}</a>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------- RESUME PAGE ----------------------------
elif menu == "Resume Download":
    st.markdown("<div class='section-title'>Download Resume</div>", unsafe_allow_html=True)
    with open("Resume - Manish Maltare - final.pdf", "rb") as f:
        st.download_button(
            label="📄 Download Resume (PDF)",
            data=f,
            file_name="Manish_Maltare_Resume.pdf",
            mime="application/pdf"
        )

# ---------------------------- CONTACT PAGE ----------------------------
elif menu == "Contact Me":
    st.markdown("<div class='section-title'>Contact Me</div>", unsafe_allow_html=True)
    st.write("📧 **Email:** manishmaltare@gmail.com")
    st.write("📞 **Phone:** +91 9589945630")
    st.write("📍 **Address:** Keshavnagar, Pune")
