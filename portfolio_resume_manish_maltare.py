# -*- coding: utf-8 -*-
"""Portfolio Resume - Manish Maltare | Animated Black & White Theme"""

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

/* MAIN BACKGROUND */
body {
    background-color: #FFFFFF !important;
}

/* FADE + SLIDE + ZOOM MIXED ANIMATION */
@keyframes fadeSlideZoom {
    0% { opacity: 0; transform: translateY(20px) scale(0.97); }
    100% { opacity: 1; transform: translateY(0px) scale(1); }
}
.block-container {
    animation: fadeSlideZoom 0.7s ease-in-out;
}

/* ---------------------- SIDEBAR ---------------------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #000000 0%, #111111 50%, #1A1A1A 100%);
    padding: 25px;
}

.sidebar-title {
    font-size: 30px;
    font-weight: 700;
    color: #FFFFFF;
    text-align: center;
    margin-bottom: 25px;
}

div[data-testid="stSidebar"] * {
    color: white !important;
}

.stRadio > label {
    color: white !important;
}

/* RADIO BUTTON FIX */
section[data-testid="stSidebar"] .st-emotion-cache-17eq0hr {
    color: white !important;
}
.st-emotion-cache-1v0mbdj {
    background-color: transparent !important;
}
.st-emotion-cache-1v0mbdj:hover {
    background-color: #292929 !important;
}

/* ---------------------- TITLES ---------------------- */
.main-title {
    font-size: 50px;
    font-weight: 800;
    color: #000000;
    margin-bottom: 20px;
}

.sub-title {
    font-size: 32px;
    font-weight: 700;
    color: #1A1A1A;
    margin-top: 25px;
}

/* PROJECT TITLES */
.project-title {
    font-size: 22px;
    font-weight: 700;
    color: #000000;
    margin-top: 30px;
}

/* ---------------------- LINKS ---------------------- */
.link-btn a {
    padding: 8px 15px;
    margin-right: 10px;
    background-color: black;
    color: white !important;
    border-radius: 6px;
    text-decoration: none;
    font-size: 15px;
    border: 1px solid white;
    transition: 0.3s;
}
.link-btn a:hover {
    background-color: white;
    color: black !important;
    border-color: black;
}

/* ---------------------- HOVER CARDS ---------------------- */
.hover-card {
    padding: 18px;
    border-radius: 10px;
    background-color: #F8F8F8;
    border: 1px solid #E0E0E0;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.hover-card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------- LOAD TEXT FILES ----------------------------
def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

about_text = read_docx("About Me2.docx")
projects_text = read_docx("Projects2.docx")


# ---------------------------- PARSE LINKS ----------------------------
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
        match = re.findall(rf"{project_name}.*?:\s*(https?://\S+)", block)
        if match:
            result[label] = match[0]
    return result


def render_project(project_name):
    st.markdown(f"<div class='project-title'>{project_name}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='hover-card'>{extract_project_section(project_name)}</div>", unsafe_allow_html=True)

    proj_links = get_project_links(project_name)
    if proj_links:
        st.markdown("<div class='link-btn'>", unsafe_allow_html=True)
        for name, url in proj_links.items():
            st.markdown(f"<a href='{url}' target='_blank'>{name}</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------- SIDEBAR ----------------------------
st.sidebar.markdown("<div class='sidebar-title'>📘 Portfolio</div>", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Navigation",
    ["Home", "About Me", "Projects", "Resume Download", "Contact Me"],
)

# ---------------------------- PAGE ROUTING ----------------------------
if menu == "Home":
    st.markdown("<div class='main-title'>Manish Maltare - Digital Portfolio</div>", unsafe_allow_html=True)
    st.write("### Explore my work using the left navigation panel.")

elif menu == "About Me":
    st.markdown("<div class='sub-title'>About Me</div>", unsafe_allow_html=True)
    st.write(about_text)

elif menu == "Projects":
    st.markdown("<div class='sub-title'>Projects</div>", unsafe_allow_html=True)
    render_project("SOLAR PANEL REGRESSION")
    render_project("NLP  - Sentiment Analysis")
    render_project("Machine Learning Insights into GDP Drivers")
    render_project("Logistic Regression - Titanic Survival Prediction")

elif menu == "Resume Download":
    st.markdown("<div class='sub-title'>Download Resume</div>", unsafe_allow_html=True)
    with open("Resume - Manish Maltare - final.pdf", "rb") as f:
        st.download_button(
            label="📄 Download Resume (PDF)",
            data=f,
            file_name="Manish_Maltare_Resume.pdf",
            mime="application/pdf"
        )

elif menu == "Contact Me":
    st.markdown("<div class='sub-title'>Contact Me</div>", unsafe_allow_html=True)
    st.write("📧 **Email:** manishmaltare@gmail.com")
    st.write("📞 **Phone:** +91 9589945630")
    st.write("📍 **Address:** Keshavnagar, Pune")
