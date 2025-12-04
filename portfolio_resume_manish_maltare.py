# -*- coding: utf-8 -*-
"""Manish Maltare - Portfolio with Top Ribbon and Transparent About Me Box"""

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

/* TOP HEADER RIBBON */
.top-header {
    width: 100%;
    background-color: rgba(0,0,0,0.7);
    padding: 20px 0;
    text-align: center;
    font-size: 32px;
    font-weight: 800;
    color: #FFFECB;
    position: fixed;
    top: 0;
    z-index: 101;
}

/* Top navigation ribbon */
.top-nav {
    width: 100%;
    background-color: rgba(0,0,0,0.5);
    padding: 15px 0;
    display: flex;
    justify-content: center;
    gap: 50px;
    position: fixed;
    top: 70px; /* below top-header */
    z-index: 100;
    border-radius: 0 0 10px 10px;
}

/* Top nav links */
.top-nav a {
    color: #FFFECB;
    text-decoration: none;
    font-weight: 700;
    font-size: 22px;
    transition: 0.3s;
}
.top-nav a:hover {
    color: #FFD700;
}

/* Main content container padding */
.block-container {
    padding-top: 160px !important; /* space for top-header + nav */
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

/* About Me box */
.about-box {
    background-color: rgba(0,0,0,0.6);
    padding: 20px;
    border-radius: 10px;
    color: white;
    line-height: 1.6;
}

/* Sidebar footer text */
.sidebar-footer {
    position: absolute;
    bottom: 20px;
    text-align: center;
    width: 100%;
    font-weight: bold;
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
</style>
""", unsafe_allow_html=True)

# ---------------------------- TOP HEADER ----------------------------
st.markdown("""
<div class="top-header">
    Digital Portfolio - Manish Maltare
</div>
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

    # Wrap About Me text in a semi-transparent black box
    st.markdown(
        f"<div class='about-box'>{about_text.replace(chr(10), '<br>')}</div>",
        unsafe_allow_html=True
    )

elif menu == "Projects":
    st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)

elif menu == "Resume Download":
    st.markdown('<a id="resume"></a>', unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Download Resume</div>", unsafe_allow_html=True)

elif menu == "Contact Me":
    st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Contact Me</div>", unsafe_allow_html=True)
