# -*- coding: utf-8 -*-
"""Manish Maltare Portfolio — FIXED Raw URL Version"""

import streamlit as st
import docx
import re
import requests
from io import BytesIO
from html import escape

# -------------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------------
st.set_page_config(page_title="Manish Maltare - Digital Portfolio", layout="wide")

# -------------------------------------------------------------
# LOAD DOCX FROM GITHUB RAW URL
# -------------------------------------------------------------
def load_docx_from_github(raw_url):
    """Download DOCX from GitHub raw URL and return python-docx Document."""
    try:
        response = requests.get(raw_url)
        response.raise_for_status()
        return docx.Document(BytesIO(response.content))
    except Exception as e:
        st.error(f"❌ Error loading DOCX from {raw_url}: {e}")
        return None


# -------------------------------------------------------------
# CONVERT DOCX → HTML (Preserve ONLY Bold)
# -------------------------------------------------------------
def docx_to_html_preserve_bold(doc):
    if doc is None:
        return "<p>Project description not available.</p>"

    paragraphs_html = []
    for para in doc.paragraphs:
        html_parts = []
        for run in para.runs:
            text = escape(run.text or "")
            if run.bold:
                html_parts.append(f"<strong>{text}</strong>")
            else:
                html_parts.append(text)

        paragraphs_html.append(
            f"<p style='margin:6px 0;'>{''.join(html_parts)}</p>"
        )
    return "\n".join(paragraphs_html)


# -------------------------------------------------------------
# EXTRACT LINKS FROM DOCX RAW TEXT
# -------------------------------------------------------------
def extract_links(doc):
    if doc is None:
        return {}

    mapping = {}
    for para in doc.paragraphs:
        line = para.text.strip()
        url_match = re.search(r"(https?://\S+)", line)
        if not url_match:
            continue

        url = url_match.group(1).rstrip(").,")
        low = line.lower()

        if "youtube" in low or "youtu" in low:
            mapping["youtube"] = url
        elif "app" in low and "streamlit" in low:
            mapping["app"] = url
        elif "deploy" in low or "deployment" in low:
            mapping["deploy"] = url
        elif "script" in low or ".ipynb" in low:
            mapping["script"] = url
        else:
            if "script" not in mapping:
                mapping["script"] = url

    return mapping


# -------------------------------------------------------------
# YOUR RAW URLs — REPLACE THESE WITH YOUR REAL RAW LINKS
# -------------------------------------------------------------
RAW_ABOUT = "PASTE RAW URL HERE"
RAW_NLP = "PASTE RAW URL HERE"
RAW_LR = "PASTE RAW URL HERE"
RAW_SOLAR = "PASTE RAW URL HERE"
RAW_GDP = "PASTE RAW URL HERE"


PROJECT_FILES = {
    "NLP - Sentiment Analysis": RAW_NLP,
    "Logistic Regression - Titanic Survival Prediction": RAW_LR,
    "Solar Panel Regression": RAW_SOLAR,
    "Machine Learning Insights into GDP Drivers": RAW_GDP
}

# -------------------------------------------------------------
# PRELOAD PROJECT CONTENT
# -------------------------------------------------------------
PROJECT_CONTENT_HTML = {}
PROJECT_LINKS = {}

for proj, url in PROJECT_FILES.items():
    doc = load_docx_from_github(url)
    PROJECT_CONTENT_HTML[proj] = docx_to_html_preserve_bold(doc)
    PROJECT_LINKS[proj] = extract_links(doc)


# -------------------------------------------------------------
# CSS (UNCHANGED)
# -------------------------------------------------------------
st.markdown("""
<style>
/* your entire CSS remains unchanged */
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# TOP NAV BAR
# -------------------------------------------------------------
st.markdown("""
<div class="top-nav">
    <a href="#about">About Me</a>
    <a href="#projects">Projects</a>
    <a href="#resume">Resume Download</a>
    <a href="#contact">Contact Me</a>
</div>
""", unsafe_allow_html=True)


# -------------------------------------------------------------
# ABOUT ME SECTION
# -------------------------------------------------------------
if "menu" not in st.session_state:
    st.session_state["menu"] = "About Me"

menu = st.sidebar.radio(
    "Navigation",
    ["About Me", "Projects", "Resume Download", "Contact Me"]
)

if menu == "About Me":
    st.markdown("<a id='about'></a>", unsafe_allow_html=True)
    st.markdown("<h1>Manish Maltare</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Digital Portfolio</h3>", unsafe_allow_html=True)

    about_doc = load_docx_from_github(RAW_ABOUT)
    about_html = docx_to_html_preserve_bold(about_doc)

    st.markdown(
        f"<div style='background:rgba(0,0,0,0.6); padding:20px; border-radius:10px;'>{about_html}</div>",
        unsafe_allow_html=True
    )


# -------------------------------------------------------------
# RENDER PROJECT DETAILS
# -------------------------------------------------------------
def render_project(project_name):
    st.markdown(f"<div class='hover-card'><h3>{project_name}</h3>", unsafe_allow_html=True)

    content = PROJECT_CONTENT_HTML.get(project_name, "<p>Project description not available.</p>")
    st.markdown(content, unsafe_allow_html=True)

    links = PROJECT_LINKS.get(project_name, {})

    items = [
        ("GitHub - Script file", links.get("script")),
        ("GitHub - Deployment file", links.get("deploy")),
        ("App Link", links.get("app")),
        ("YouTube video Link", links.get("youtube")),
    ]

    html = ["<div class='circle-container'>"]
    for label, url in items:
        if url:
            html.append(
                f"<a class='circle-icon' href='{url}' target='_blank'>{label}</a>"
            )
        else:
            html.append(
                f"<div class='circle-icon circle-disabled'>{label}<br><small>Not available</small></div>"
            )
    html.append("</div>")

    st.markdown("".join(html), unsafe_allow_html=True)


# -------------------------------------------------------------
# PROJECTS SECTION
# -------------------------------------------------------------
if menu == "Projects":
    st.markdown("<a id='projects'></a>", unsafe_allow_html=True)
    st.markdown("<h2>Projects</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Classification")
        if st.button("NLP - Sentiment Analysis"):
            st.session_state["project"] = "NLP - Sentiment Analysis"
        if st.button("Logistic Regression - Titanic Survival Prediction"):
            st.session_state["project"] = "Logistic Regression - Titanic Survival Prediction"

    with col2:
        st.subheader("Regression")
        if st.button("Solar Panel Regression"):
            st.session_state["project"] = "Solar Panel Regression"
        if st.button("Machine Learning Insights into GDP Drivers"):
            st.session_state["project"] = "Machine Learning Insights into GDP Drivers"

    if st.session_state.get("project"):
        render_project(st.session_state["project"])


# -------------------------------------------------------------
# RESUME DOWNLOAD
# -------------------------------------------------------------
if menu == "Resume Download":
    st.markdown("<a id='resume'></a>", unsafe_allow_html=True)
    st.markdown("<h2>Download Resume</h2>", unsafe_allow_html=True)

    try:
        with open("Resume - Manish Maltare - final.pdf", "rb") as f:
            st.download_button(
                "📄 Download Resume",
                data=f,
                file_name="Manish_Maltare_Resume.pdf",
                mime="application/pdf"
            )
    except:
        st.error("Resume file missing. Upload it to the repo.")


# -------------------------------------------------------------
# CONTACT SECTION
# -------------------------------------------------------------
if menu == "Contact Me":
    st.markdown("<a id='contact'></a>", unsafe_allow_html=True)
    st.markdown("<h2>Contact Me</h2>", unsafe_allow_html=True)

    st.write("📧 **Email:** manishmaltare@gmail.com")
    st.write("📞 **Phone:** +91 9589945630")
    st.write("📍 **Address:** Keshavnagar, Pune")
