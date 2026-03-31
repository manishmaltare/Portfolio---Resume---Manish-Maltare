import streamlit as st
import docx
import os

# ---------------------------- PAGE CONFIG ----------------------------
st.set_page_config(
    page_title="Manish Maltare - Digital Portfolio",
    layout="wide"
)

# ---------------------------- CUSTOM CSS ----------------------------
st.markdown("""
<style>
body {color:white;}
.block-container {
    padding-top:80px !important;
    padding-left:120px !important;
    padding-right:120px !important;
}
.section-title {
    font-size: 40px;
    margin-bottom: 20px;
}
.hover-card {
    padding: 15px;
    border-radius: 10px;
    background-color: rgba(0,0,0,0.6);
    margin-top: 20px;
}
.circle-container {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
}
.circle-icon {
    width: 110px;
    height: 110px;
    border-radius: 50%;
    background: rgba(0,0,0,0.7);
    display:flex;
    align-items:center;
    justify-content:center;
    text-align:center;
    font-size:14px;
    font-weight:600;
    border:1px solid white;
}
.circle-icon:hover {
    background: rgba(255,255,255,0.3);
    color:black;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------- READ DOCX ----------------------------
def read_docx_safe(path):
    if not os.path.exists(path):
        return ""
    doc = docx.Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

about_text = read_docx_safe("About Me2.docx")
nlp_text = read_docx_safe("NLP.docx")
solar_text = read_docx_safe("solar panel regression.docx")
ml_text = read_docx_safe("Machine learning insights.docx")

# NEW PROJECT FILES
reco_text = read_docx_safe("Online Course Recommendations.docx")
reco_links_text = read_docx_safe("Online Course Recommendations-links.docx")

# ---------------------------- LINKS ----------------------------
def render_links(project):
    links = {
        "NLP - Sentiment Analysis": {
            "GitHub": "https://github.com/manishmaltare/NLP---Sentiment-Analysis",
            "App": "https://manish-maltare-kfkyft36opaoieycyadutr.streamlit.app/"
        },
        "Solar Panel Regression": {
            "GitHub": "https://github.com/manishmaltare/Solar-Panel-Regression-1"
        },
        "Machine Learning Insights into GDP Drivers": {
            "GitHub": "https://github.com/manishmaltare/Project---Machine-Learning-Insights-into-GDP-Drivers"
        },
        "Online Course Recommendation System": {
            "GitHub": "https://github.com/manishmaltare",  # update if needed
        }
    }

    if project not in links:
        return

    html = '<div class="circle-container">'
    for name, url in links[project].items():
        html += f'<a href="{url}" target="_blank"><div class="circle-icon">{name}</div></a>'
    html += '</div>'

    st.markdown(html, unsafe_allow_html=True)

# ---------------------------- PROJECT DISPLAY ----------------------------
def render_project(project):
    if project == "NLP - Sentiment Analysis":
        body = nlp_text

    elif project == "Solar Panel Regression":
        body = solar_text

    elif project == "Machine Learning Insights into GDP Drivers":
        body = ml_text

    elif project == "Online Course Recommendation System":
        body = reco_text + "\n\n" + reco_links_text

    else:
        body = "Project not found"

    st.markdown(f"<div class='hover-card'>{body.replace('\n','<br>')}</div>", unsafe_allow_html=True)
    render_links(project)

# ---------------------------- SIDEBAR ----------------------------
menu = st.sidebar.radio("Navigation", ["About Me", "Projects", "Resume", "Contact"])

# ---------------------------- ABOUT ----------------------------
if menu == "About Me":
    st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='hover-card'>{about_text.replace('\n','<br>')}</div>", unsafe_allow_html=True)

# ---------------------------- PROJECTS ----------------------------
elif menu == "Projects":
    st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # Classification
    with col1:
        st.markdown("### Classification")
        if st.button("NLP - Sentiment Analysis"):
            st.session_state["proj"] = "NLP - Sentiment Analysis"

    # Regression
    with col2:
        st.markdown("### Regression")
        if st.button("Solar Panel Regression"):
            st.session_state["proj"] = "Solar Panel Regression"
        if st.button("Machine Learning Insights into GDP Drivers"):
            st.session_state["proj"] = "Machine Learning Insights into GDP Drivers"

    # Recommendation System
    with col3:
        st.markdown("### Recommendation System")
        if st.button("Online Course Recommendation System"):
            st.session_state["proj"] = "Online Course Recommendation System"

    if "proj" in st.session_state:
        render_project(st.session_state["proj"])

# ---------------------------- RESUME ----------------------------
elif menu == "Resume":
    st.markdown("<div class='section-title'>Resume</div>", unsafe_allow_html=True)
    try:
        with open("Resume - Manish Maltare - final.pdf", "rb") as f:
            st.download_button("Download Resume", f, "Manish_Maltare_Resume.pdf")
    except:
        st.warning("Resume file not found")

# ---------------------------- CONTACT ----------------------------
elif menu == "Contact":
    st.markdown("<div class='section-title'>Contact</div>", unsafe_allow_html=True)
    st.write("Email: manishmaltare@gmail.com")
    st.write("Phone: +91 9589945630")
    st.write("Location: Pune")

# ---------------------------- FOOTER ----------------------------
st.markdown("<div style='text-align:center;margin-top:40px;'>Created by Manish Maltare</div>", unsafe_allow_html=True)
