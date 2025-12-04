# -*- coding: utf-8 -*-
"""Manish Maltare - Portfolio with Top Navigation and Transparent Buttons
   Updated: full DOCX text included for projects, preserve ONLY bold (as <strong>),
   add 4 circular icon buttons under each project (links hidden in code, opened via buttons).
"""
portfolio_resume_manish_maltare.py
NLP.docx
Logistic Regression.docx
Solar Panel Regression.docx
Machine Learning Insights.docx
About Me2.docx

import streamlit as st
import docx
import re
from html import escape

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
    text-decoration: none;
}
.circle-icon:hover {
    background: rgba(255,255,255,0.35);
    color: black;
    transform: scale(1.08);
    border-color: white;
}

/* Disabled circle look */
.circle-disabled {
    pointer-events: none;
    opacity: 0.5;
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

# ---------------------------- DOCX READ + BOLD PRESERVE ----------------------------
def docx_to_html_preserve_bold(docx_path):
    """
    Convert a .docx to HTML string while preserving only bold formatting.
    Bold runs are wrapped with <strong>..</strong>. Italic/underline/etc are ignored.
    Paragraphs are wrapped with <p>..</p>.
    """
    doc = docx.Document(docx_path)
    paragraphs_html = []
    for para in doc.paragraphs:
        para_html_parts = []
        # If no runs, treat whole paragraph's text as plain
        if not para.runs:
            paragraphs_html.append(f"<p>{escape(para.text)}</p>")
            continue
        for run in para.runs:
            text = escape(run.text or "")
            if text == "":
                continue
            # Only preserve bold
            if run.bold:
                para_html_parts.append(f"<strong>{text}</strong>")
            else:
                para_html_parts.append(text)
        # join runs, keep paragraph as a block
        paragraph_html = "".join(para_html_parts)
        paragraphs_html.append(f"<p style='margin:6px 0;'>{paragraph_html}</p>")
    return "\n".join(paragraphs_html)

def read_docx_raw_text(docx_path):
    """Return raw joined text for easier link extraction (line-separated)."""
    doc = docx.Document(docx_path)
    lines = []
    for para in doc.paragraphs:
        lines.append(para.text)
    return "\n".join(lines)


# ---------------------------- EXTRACT LINKS FROM DOCX TEXT ----------------------------
def extract_links_from_docx_text(text):
    """
    Heuristic extraction: examine each line and map URLs to one of:
    'script', 'deploy', 'app', 'youtube'
    Returns dict with possible keys and URL strings.
    """
    mapping = {}
    for line in text.splitlines():
        if not line or line.strip() == "":
            continue
        url_match = re.search(r'(https?://\S+)', line)
        if not url_match:
            continue
        url = url_match.group(1).rstrip('.,)')
        low = line.lower()
        # heuristics based on presence of keywords near the URL
        if 'youtube' in low or 'youtu' in low:
            mapping['youtube'] = url
        elif 'app link' in low or ('streamlit' in low and 'app' in low) or 'app' in low and 'streamlit' in low:
            mapping['app'] = url
        elif 'github' in low and ('script' in low or 'script file' in low or '.ipynb' in low):
            mapping['script'] = url
        elif 'github' in low and ('deploy' in low or 'deployment' in low or 'pickle' in low or '.py' in low):
            mapping['deploy'] = url
        elif 'github' in low and 'deployment' not in low and 'script' not in low and 'repo' in low:
            # fallback for generic github lines
            if 'script' not in mapping:
                mapping['script'] = url
        else:
            # If none of the above and only one url present, try assigning by absence
            # Do not overwrite if key already present
            if 'script' not in mapping:
                mapping['script'] = url
    return mapping


# ---------------------------- LOAD PROJECTS (DOCX files placed in /mnt/data) ----------------------------
# Update these paths if your files are elsewhere. These correspond to the uploaded files.
PROJECT_FILES = {
    "NLP - Sentiment Analysis": "/mnt/data/NLP.docx",
    "Logistic Regression - Titanic Survival Prediction": "/mnt/data/Logistics Regression .docx",
    "Solar Panel Regression": "/mnt/data/solar panel regression .docx",
    "Machine Learning Insights into GDP Drivers": "/mnt/data/Machine learning insights .docx"
}

# Precompute HTML content and links per project
PROJECT_CONTENT_HTML = {}
PROJECT_LINKS = {}
for proj_name, path in PROJECT_FILES.items():
    try:
        PROJECT_CONTENT_HTML[proj_name] = docx_to_html_preserve_bold(path)
        raw_text = read_docx_raw_text(path)
        PROJECT_LINKS[proj_name] = extract_links_from_docx_text(raw_text)
    except Exception as e:
        # Fallback to empty content if file missing or error
        PROJECT_CONTENT_HTML[proj_name] = "<p><em>Project description not available.</em></p>"
        PROJECT_LINKS[proj_name] = {}


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

# ---------------------------- PROJECT RENDERER ----------------------------
def render_project_details_from_docx(project_name):
    """
    Render project description (full DOCX content) keeping only bold (as <strong>),
    and render four circular link icons (GitHub Script, GitHub Deployment, App Link, YouTube).
    Link addresses are kept hidden in variables and used as hrefs.
    If a particular link is not found, a disabled circle will be shown.
    """
    st.markdown(f"<div class='hover-card'><h3>{escape(project_name)}</h3>", unsafe_allow_html=True)
    # Insert the HTML content converted from DOCX (already has <strong> tags for bold)
    project_html = PROJECT_CONTENT_HTML.get(project_name, "<p>No description available.</p>")
    st.markdown(project_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Prepare links map (hidden inside code)
    links = PROJECT_LINKS.get(project_name, {})

    # For deterministic order and labels requested by you:
    link_items = [
        ("GitHub - Script file", links.get('script')),
        ("GitHub - Deployment file", links.get('deploy')),
        ("App Link", links.get('app')),
        ("YouTube video Link", links.get('youtube'))
    ]

    # Render circular icons in a horizontal row
    icons_html_parts = ["<div class='circle-container'>"]
    for label, url in link_items:
        if url:
            # Normal anchor with hidden URL (not displayed) - opens in new tab
            icons_html_parts.append(
                f"<a class='circle-icon' href='{url}' target='_blank' rel='noreferrer noopener'>{escape(label)}</a>"
            )
        else:
            # Disabled circle (no href)
            icons_html_parts.append(
                f"<div class='circle-icon circle-disabled'>{escape(label)}<br><small style='font-weight:600; font-size:11px; opacity:0.9;'>Not available</small></div>"
            )
    icons_html_parts.append("</div>")
    st.markdown("".join(icons_html_parts), unsafe_allow_html=True)


# ---------------------------- PAGE ROUTING ----------------------------
if menu == "About Me":
    st.markdown('<a id="about"></a>', unsafe_allow_html=True)
    st.markdown("<div class='main-title'>Manish Maltare</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title-tagline'>Digital Portfolio</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)

    # Try reading About Me docx if exists in working dir, otherwise show placeholder
    try:
        about_html = docx_to_html_preserve_bold("/mnt/data/About Me2.docx")
        st.markdown(
            f"""
            <div style="
                background-color: rgba(0,0,0,0.6);
                padding: 20px;
                border-radius: 10px;
                color: white;
                line-height: 1.6;
            ">
                {about_html}
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception:
        st.markdown(
            """
            <div style="
                background-color: rgba(0,0,0,0.6);
                padding: 20px;
                border-radius: 10px;
                color: white;
                line-height: 1.6;
            ">
                <p>About Me content not found. Please ensure <strong>About Me2.docx</strong> is present in the application folder.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

elif menu == "Projects":
    st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # Setup session_state selected_project default
    if "selected_project" not in st.session_state:
        st.session_state["selected_project"] = None

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
        render_project_details_from_docx(st.session_state["selected_project"])

elif menu == "Resume Download":
    st.markdown('<a id="resume"></a>', unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Download Resume</div>", unsafe_allow_html=True)
    try:
        with open("/mnt/data/Resume - Manish Maltare - final.pdf", "rb") as f:
            st.download_button(
                label="📄 Download Resume (PDF)",
                data=f,
                file_name="Manish_Maltare_Resume.pdf",
                mime="application/pdf",
                key="resume_button"
            )
    except FileNotFoundError:
        st.markdown("<p style='color:#FFD700;'>Resume PDF not found in /mnt/data. Please upload the file named 'Resume - Manish Maltare - final.pdf'.</p>", unsafe_allow_html=True)

elif menu == "Contact Me":
    st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Contact Me</div>", unsafe_allow_html=True)
    st.write("📧 **Email:** manishmaltare@gmail.com")
    st.write("📞 **Phone:** +91 9589945630")
    st.write("📍 **Address:** Keshavnagar, Pune")
