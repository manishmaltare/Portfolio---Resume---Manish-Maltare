# -*- coding: utf-8 -*-
"""Manish Maltare - Portfolio with Background Image and Project Grid"""

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

/* PAGE BACKGROUND IMAGE */
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/manishmaltare/Portfolio---Resume---Manish-Maltare/main/5072609.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white !important;
}

/* SIDEBAR - semi-transparent black */
section[data-testid="stSidebar"] {
    background-color: rgba(0,0,0,0.6);
    padding: 20px;
    color: white;
}

/* Sidebar title */
.sidebar-title {
    font-size: 28px;
    font-weight: 800;
    color: white;
    margin-bottom: 30px;
}

/* Sidebar menu options */
div[data-testid="stSidebar"] label, 
div[data-testid="stSidebar"] span {
    color: white !important;
    font-weight: 600 !important;
    font-size: 16px;
}

/* MAIN CONTENT AREA */
.block-container {
    padding-left: 150px !important;
    padding-right: 150px !important;
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

/* Project buttons */
.project-btn {
    padding: 10px 15px;
    font-size: 16px;
    font-weight: 600;
    border-radius: 8px;
    background-color: rgba(0,0,0,0.5);
    color: white;
    margin-bottom: 15px;
    width: 100%;
    text-align: left;
    transition: 0.3s;
}
.project-btn:hover {
    background-color: rgba(255,255,255,0.3);
    color: black;
    cursor: pointer;
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

def render_project_details(project_name):
    st.markdown(f"<div class='hover-card'><h3>{project_name}</h3><p>{extract_project_section(project_name)}</p></div>", unsafe_allow_html=True)
    proj_links = get_project_links(project_name)
    if proj_links:
        st.markdown("<div class='link-btn'>", unsafe_allow_html=True)
        for title, url in proj_links.items():
            st.markdown(f"<a href='{url}' target='_blank' class='project-btn'>{title}</a>", unsafe_allow_html=True)
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

if menu == "About Me":
    st.markdown("<div class='main-title'>Manish Maltare</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title-tagline'>Digital Portfolio</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)
    st.write(about_text)

elif menu == "Projects":
    st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)

    # Create two columns: Classification and Regression
    st.markdown("<div class='grid-container'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3>Classification</h3>", unsafe_allow_html=True)
        if st.button("NLP - Sentiment Analysis"): selected_project = "NLP - Sentiment Analysis"
        elif st.button("Logistic Regression - Titanic Survival Prediction"): selected_project = "Logistic Regression - Titanic Survival Prediction"
        else: selected_project = None

    with col2:
        st.markdown("<h3>Regression</h3>", unsafe_allow_html=True)
        if st.button("Solar Panel Regression"): selected_project = "Solar Panel Regression"
        elif st.button("Machine Learning Insights into GDP Drivers"): selected_project = "Machine Learning Insights into GDP Drivers"
        else: selected_project = selected_project if 'selected_project' in locals() else None

    st.markdown("</div>", unsafe_allow_html=True)

    # Show project details below the grid
    if selected_project:
        render_project_details(selected_project)

elif menu == "Resume Download":
    st.markdown("<div class='section-title'>Download Resume</div>", unsafe_allow_html=True)
    with open("Resume - Manish Maltare - final.pdf", "rb") as f:
        st.download_button(
            label="📄 Download Resume (PDF)",
            data=f,
            file_name="Manish_Maltare_Resume.pdf",
            mime="application/pdf"
        )

elif menu == "Contact Me":
    st.markdown("<div class='section-title'>Contact Me</div>", unsafe_allow_html=True)
    st.write("📧 **Email:** manishmaltare@gmail.com")
    st.write("📞 **Phone:** +91 9589945630")
    st.write("📍 **Address:** Keshavnagar, Pune")
