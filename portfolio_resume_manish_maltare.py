# -*- coding: utf-8 -*-
"""Portfolio Resume - Manish Maltare"""

import streamlit as st
import docx
import re

# ---------------------------- PAGE CONFIG ----------------------------
st.set_page_config(
    page_title="Manish Maltare - Digital Portfolio",
    layout="wide"
)

# ---------------------------- GLOBAL STYLE ----------------------------
st.markdown("""
<style>

@import url('https://fonts.cdnfonts.com/css/copperplate-gothic');

* {
    font-family: 'Copperplate Gothic', sans-serif !important;
}

/* DARK MODE BACKGROUND */
body {
    background-color: #111 !important;
    color: #EEE !important;
}

/* SIDEBAR STYLING */
section[data-testid="stSidebar"] {
    background-color: #0D0D0D;
    padding-top: 30px;
}

.sidebar-title {
    font-size: 26px;
    font-weight: 700;
    color: #F1C40F;
    text-align: center;
    margin-bottom: 20px;
}

/* HEADINGS */
.main-title {
    font-size: 45px;
    font-weight: 700;
    color: #F7DC6F;
    margin-bottom: 10px;
}

.sub-title {
    font-size: 28px;
    font-weight: 600;
    color: #F4D03F;
    margin-top: 20px;
}

.project-title {
    font-size: 22px;
    font-weight: 700;
    color: #F7DC6F;
    margin-top: 30px;
}

/* LINKS */
.link-btn a {
    padding: 8px 15px;
    margin-right: 10px;
    background-color: #F1C40F;
    color: black !important;
    border-radius: 6px;
    text-decoration: none;
    font-size: 15px;
}
.link-btn a:hover {
    background-color: #D4AC0D;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------- FUNCTIONS ----------------------------

def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

about_text = read_docx("About Me2.docx")
projects_text = read_docx("Projects2.docx")

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
        match = re.findall(rf"{project_name}.*?:\s*(https?://\S+)", block)
        if match:
            result[label] = match[0]
    return result

def render_project(project_name):
    st.markdown(f"<div class='project-title'>{project_name}</div>", unsafe_allow_html=True)
    st.write(extract_project_section(project_name))
    proj_links = get_project_links(project_name)
    if proj_links:
        st.markdown("<div class='link-btn'>", unsafe_allow_html=True)
        for title, url in proj_links.items():
            st.markdown(f"<a href='{url}' target='_blank'>{title}</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------- SIDEBAR MENU ----------------------------
st.sidebar.markdown("<div class='sidebar-title'>📘 Portfolio</div>", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Navigation",
    ["Home", "About Me", "Projects", "Contact Me", "Resume Download"],
)

# ---------------------------- PAGE ROUTING ----------------------------

if menu == "Home":
    st.markdown("<div class='main-title'>Manish Maltare - Digital Portfolio</div>", unsafe_allow_html=True)
    st.write("### Welcome! Explore my work through the left navigation panel.")

elif menu == "About Me":
    st.markdown("<div class='sub-title'>About Me</div>", unsafe_allow_html=True)
    st.write(about_text)

elif menu == "Projects":
    st.markdown("<div class='sub-title'>Projects</div>", unsafe_allow_html=True)
    render_project("SOLAR PANEL REGRESSION")
    render_project("NLP  - Sentiment Analysis")
    render_project("Machine Learning Insights into GDP Drivers")
    render_project("Logistic Regression - Titanic Survival Prediction")

elif menu == "Contact Me":
    st.markdown("<div class='sub-title'>Contact Me</div>", unsafe_allow_html=True)
    st.write("📧 **Email:** manishmaltare@gmail.com")
    st.write("📞 **Phone:** +91 9589945630")
    st.write("📍 **Address:** Keshavnagar, Pune")

elif menu == "Resume Download":
    st.markdown("<div class='sub-title'>Download Resume</div>", unsafe_allow_html=True)
    with open("Resume - Manish Maltare - final.pdf", "rb") as f:
        st.download_button(
            label="📄 Download Resume (PDF)",
            data=f,
            file_name="Manish_Maltare_Resume.pdf",
            mime="application/pdf"
        )
