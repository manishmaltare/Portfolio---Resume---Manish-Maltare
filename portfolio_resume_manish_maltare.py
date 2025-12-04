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
    padding-top:90px !important; /* to avoid overlapping nav */
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

/* Semi-transparent black box for text sections */
.text-card {
    background-color: rgba(0, 0, 0, 0.55);
    padding: 20px 24px;
    border-radius: 12px;
    margin-top: 10px;
}

/* Style all primary buttons like project buttons (light transparent) */
button[kind="primary"] {
    background-color: rgba(255,255,255,0.1) !important;
    color: white !important;
    border-radius:6px !important;
    font-weight:600 !important;
    border: none !important;
}
button[kind="primary"]:hover {
    background-color: rgba(255,255,255,0.3) !important;
    color: black !important;
}

/* Make the resume download button box completely transparent */
div[data-testid="stDownloadButton"] {
    background-color: transparent !important;
    border: none !important;
}

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
    # Match text after project_name until next all‑caps heading (3+ chars) or end of string
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
