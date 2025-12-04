# -*- coding: utf-8 -*-
"""Portfolio_Resume_Manish Maltare.ipynb"""

import streamlit as st
import docx
import re

# ------------------------------------------------
# PAGE CONFIG & FONT IMPORT
# ------------------------------------------------
st.set_page_config(page_title="Manish Maltare - Digital Portfolio", layout="wide")

# Custom UI Styling + Copperplate Gothic Font
st.markdown("""
    <style>
        @import url('https://fonts.cdnfonts.com/css/copperplate-gothic');

        * {
            font-family: 'Copperplate Gothic', sans-serif !important;
        }

        body {
            background-color: #F7F9FC;
        }
        .main-title {
            text-align: center;
            font-size: 45px;
            font-weight: 700;
            padding-bottom: 10px;
            color: #2E4053;
        }
        .sub-title {
            font-size: 28px;
            font-weight: 600;
            padding-top: 10px;
            color: #1A5276;
        }
        .project-title {
            font-size: 22px;
            font-weight: 700;
            color: #154360;
            margin-top: 25px;
        }
        .link-btn a {
            padding: 8px 15px;
            margin-right: 10px;
            background-color: #1A5276;
            color: white !important;
            border-radius: 6px;
            text-decoration: none;
            font-size: 15px;
        }
        .link-btn a:hover {
            background-color: #154360;
        }
        .home-buttons button {
            padding: 18px 40px;
            font-size: 20px;
            font-weight: 600;
            border-radius: 10px;
            margin: 8px;
            background-color: #1A5276;
            color: white;
        }
        .home-buttons button:hover {
            background-color: #154360;
        }

        /* TOP RIGHT HOME BUTTON */
        .home-return {
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: #1A5276;
            color: white !important;
            padding: 10px 18px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 16px;
            font-weight: 600;
            z-index: 999;
        }
        .home-return:hover {
            background-color: #154360;
        }

    </style>
""", unsafe_allow_html=True)


# ------------------------------------------------
# HELPER: Add Home Button to Every Page
# ------------------------------------------------
def home_button():
    st.markdown("<a class='home-return' href='/?page=home'>🏠 Home</a>", unsafe_allow_html=True)


# ------------------------------------------------
# LOAD DOCX
# ------------------------------------------------
def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])


about_text = read_docx("About Me2.docx")
projects_text = read_docx("Projects2.docx")


# ------------------------------------------------
# LOAD LINKS FILE
# ------------------------------------------------
def load_links():
    data = open("Links.txt", "r").read()

    sections = {
        "ppt": re.findall(r"PPTs.*?:-(.*?)(?=GitHub Files)", data, re.S),
        "github_files": re.findall(r"GitHub Files.*?:-(.*?)(?=GitHub Deployment)", data, re.S),
        "github_deploy": re.findall(r"GitHub Deployment.*?:-(.*?)(?=App Deployment)", data, re.S),
        "app_links": re.findall(r"App Deployment.*?:-(.*?)(?=YouTube)", data, re.S),
        "youtube": re.findall(r"YouTube.*?:-(.*?)(?=Resume)", data, re.S),
        "resume": re.findall(r"Resume Link.*?:(.*)", data, re.S)
    }
    return sections

links = load_links()


# ------------------------------------------------
# FUNCTIONS TO DISPLAY PROJECTS
# ------------------------------------------------
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

    intro = extract_project_section(project_name)
    st.write(intro)

    proj_links = get_project_links(project_name)

    if proj_links:
        st.markdown("<div class='link-btn'>", unsafe_allow_html=True)
        for name, url in proj_links.items():
            st.markdown(f"<a href='{url}' target='_blank'>{name}</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


# ------------------------------------------------
# PAGES
# ------------------------------------------------
def home():
    st.markdown("<div class='main-title'>Manish Maltare - Digital Portfolio</div>", unsafe_allow_html=True)
    st.markdown("### Explore my work, skills, and experience")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("About Me", use_container_width=True): st.session_state.page = "about"
    with col2:
        if st.button("Projects", use_container_width=True): st.session_state.page = "projects"
    with col3:
        if st.button("Contact Me", use_container_width=True): st.session_state.page = "contact"
    with col4:
        if st.button("Download Resume", use_container_width=True): st.session_state.page = "resume"


def about():
    home_button()
    st.markdown("<div class='sub-title'>About Me</div>", unsafe_allow_html=True)
    st.write(about_text)


def projects():
    home_button()
    st.markdown("<div class='sub-title'>Projects</div>", unsafe_allow_html=True)

    render_project("SOLAR PANEL REGRESSION")
    render_project("NLP  - Sentiment Analysis")
    render_project("Machine Learning Insights into GDP Drivers")
    render_project("Logistic Regression - Titanic Survival Prediction")


def contact():
    home_button()
    st.markdown("<div class='sub-title'>Contact Me</div>", unsafe_allow_html=True)

    st.write("**Email:** manishmaltare@gmail.com")
    st.write("**Phone:** +91 9589945630")
    st.write("**Address:** Keshavnagar, Pune")


def resume():
    home_button()
    st.markdown("<div class='sub-title'>Download Resume</div>", unsafe_allow_html=True)

    with open("Resume - Manish Maltare - final.pdf", "rb") as f:
        st.download_button(
            label="Download My Resume (PDF)",
            data=f,
            file_name="Manish_Maltare_Resume.pdf",
            mime="application/pdf"
        )


# ------------------------------------------------
# MAIN NAVIGATION
# ------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    home()
elif st.session_state.page == "about":
    about()
elif st.session_state.page == "projects":
    projects()
elif st.session_state.page == "contact":
    contact()
elif st.session_state.page == "resume":
    resume()
