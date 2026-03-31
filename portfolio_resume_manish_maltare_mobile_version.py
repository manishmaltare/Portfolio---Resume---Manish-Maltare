import streamlit as st
import docx
import os

# ---------------------------- PAGE CONFIG ----------------------------
st.set_page_config(
    page_title="Manish Maltare - Digital Portfolio",
    layout="wide"
)

# ---------------------------- LOAD DOCX ----------------------------
def read_docx_safe(path):
    if not os.path.exists(path):
        return ""
    doc = docx.Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

about_text = read_docx_safe("About Me2.docx")
nlp_text = read_docx_safe("NLP.docx")
solar_text = read_docx_safe("solar panel regression.docx")
ml_text = read_docx_safe("Machine learning insights.docx")

# ✅ NEW FILE
reco_text = read_docx_safe("Online Course Recommendations.docx")

# ---------------------------- LINKS ----------------------------
def render_links(project):
    links_map = {
        "NLP - Sentiment Analysis": {
            "GitHub": "https://github.com/manishmaltare/NLP---Sentiment-Analysis",
            "App": "https://manish-maltare-kfkyft36opaoieycyadutr.streamlit.app/",
        },
        "Solar Panel Regression": {
            "GitHub": "https://github.com/manishmaltare/Solar-Panel-Regression-1",
        },
        "Machine Learning Insights into GDP Drivers": {
            "GitHub": "https://github.com/manishmaltare/Project---Machine-Learning-Insights-into-GDP-Drivers",
        },
        "Online Course Recommendation System": {
            "GitHub": "https://github.com/manishmaltare",  # update if needed
        }
    }

    if project not in links_map:
        return

    html = '<div style="display:flex;gap:20px;margin-top:20px;">'
    for label, url in links_map[project].items():
        html += f'<a href="{url}" target="_blank">{label}</a>'
    html += '</div>'

    st.markdown(html, unsafe_allow_html=True)

# ---------------------------- PROJECT RENDER ----------------------------
def render_project(project):
    if project == "NLP - Sentiment Analysis":
        body = nlp_text

    elif project == "Solar Panel Regression":
        body = solar_text

    elif project == "Machine Learning Insights into GDP Drivers":
        body = ml_text

    elif project == "Online Course Recommendation System":
        body = reco_text

    else:
        body = "Project not found"

    st.markdown(f"<div style='margin-top:20px;'>{body.replace('\n','<br>')}</div>", unsafe_allow_html=True)
    render_links(project)

# ---------------------------- SIDEBAR ----------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["About Me", "Projects", "Resume", "Contact"]
)

# ---------------------------- ABOUT ----------------------------
if menu == "About Me":
    st.title("About Me")
    st.markdown(about_text.replace("\n","<br>"), unsafe_allow_html=True)

# ---------------------------- PROJECTS ----------------------------
elif menu == "Projects":
    st.title("Projects")

    # ✅ FIX: NOW 3 COLUMNS (THIS IS MAIN CHANGE)
    col1, col2, col3 = st.columns(3)

    # ---------------- CLASSIFICATION ----------------
    with col1:
        st.subheader("Classification")
        if st.button("NLP - Sentiment Analysis"):
            st.session_state["project"] = "NLP - Sentiment Analysis"

    # ---------------- REGRESSION ----------------
    with col2:
        st.subheader("Regression")
        if st.button("Solar Panel Regression"):
            st.session_state["project"] = "Solar Panel Regression"

        if st.button("Machine Learning Insights into GDP Drivers"):
            st.session_state["project"] = "Machine Learning Insights into GDP Drivers"

    # ---------------- RECOMMENDATION SYSTEM ----------------
    with col3:
        st.subheader("Recommendation System")
        if st.button("Online Course Recommendation System"):
            st.session_state["project"] = "Online Course Recommendation System"

    # ---------------- DISPLAY PROJECT ----------------
    if "project" in st.session_state:
        render_project(st.session_state["project"])

# ---------------------------- RESUME ----------------------------
elif menu == "Resume":
    st.title("Resume")
    try:
        with open("Resume - Manish Maltare - final.pdf", "rb") as f:
            st.download_button(
                label="Download Resume",
                data=f,
                file_name="Manish_Maltare_Resume.pdf"
            )
    except:
        st.warning("Resume file not found")

# ---------------------------- CONTACT ----------------------------
elif menu == "Contact":
    st.title("Contact")
    st.write("Email: manishmaltare@gmail.com")
    st.write("Phone: +91 9589945630")
    st.write("Location: Pune")
