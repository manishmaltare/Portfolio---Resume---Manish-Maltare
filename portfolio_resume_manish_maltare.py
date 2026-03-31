import streamlit as st
import docx
import os

# ---------------------------- PAGE CONFIG ----------------------------
st.set_page_config(
    page_title="Manish Maltare | Data Science & Analytics Portfolio",
    layout="wide"
)

# ---------------------------- CUSTOM CSS (BACKGROUND FIXED) ----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&display=swap');

* {
    font-family: 'Open Sans', sans-serif !important;
}

/* ✅ BACKGROUND IMAGE RESTORED */
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/manishmaltare/Portfolio---Resume---Manish-Maltare/main/5072609.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white !important;
}

/* BUTTON */
.stButton>button {
    background-color: rgba(255,255,255,0.1) !important;
    color: white !important;
    border: none !important;
    padding: 8px 12px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    border-radius: 6px;
}

/* NAV BAR */
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
}

/* SECTION TITLE */
.section-title {
    font-size: 45px;
    color: white;
    margin-bottom: 20px;
}

/* CARD */
.hover-card {
    padding: 15px;
    border-radius: 10px;
    background-color: rgba(0,0,0,0.6);
    color: white;
    margin-top: 20px;
}

/* CIRCLE BUTTONS */
.circle-container {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-top: 25px;
}

.circle-icon {
    width: 120px;
    height: 120px;
    background: rgba(0,0,0,0.7);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------- DOCX LOADER ----------------------------
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
recommendation_text = read_docx_safe("Online Course Recommendations.docx")

# ---------------------------- LINKS ----------------------------
def render_links(project):

    links = {
        "NLP - Sentiment Analysis": {
            "GitHub": "https://github.com/manishmaltare/NLP---Sentiment-Analysis",
            "App": "https://manish-maltare-kfkyft36opaoieycyadutr.streamlit.app/"
        },

        "Solar Panel Regression": {
            "GitHub": "https://github.com/manishmaltare/Solar-Panel-Regression-1",
            "App": "https://solar-panel-regression-1-q3nwvmajqzqloi5aevksgq.streamlit.app/"
        },

        "Machine Learning Insights into GDP Drivers": {
            "GitHub": "https://github.com/manishmaltare/Project---Machine-Learning-Insights-into-GDP-Drivers"
        },

        # ✅ NEW PROJECT LINKS (YOUR LINKS)
        "Online Course Recommendation System": {
            "Presentation": "https://drive.google.com/file/d/1j8fGEzcJEIPPGAcSLznOcoRYOj2cWVPS/view?usp=drive_link",
            "GitHub": "https://github.com/manishmaltare/Online-Class-Recommendations/blob/main/online_course_recommendation_file.ipynb"
        }
    }

    proj_links = links.get(project, {})

    html = '<div class="circle-container">'
    for k, v in proj_links.items():
        html += f'<a href="{v}" target="_blank"><div class="circle-icon">{k}</div></a>'
    html += '</div>'

    st.markdown(html, unsafe_allow_html=True)

# ---------------------------- PROJECT DISPLAY ----------------------------
def show_project(name):

    if name == "NLP - Sentiment Analysis":
        body = nlp_text

    elif name == "Solar Panel Regression":
        body = solar_text

    elif name == "Machine Learning Insights into GDP Drivers":
        body = ml_text

    elif name == "Online Course Recommendation System":
        body = recommendation_text

    else:
        body = ""

    st.markdown(f"<div class='hover-card'><h3>{name}</h3></div>", unsafe_allow_html=True)

    st.markdown(
        f"<div class='hover-card'>{body.replace(chr(10),'<br>')}</div>",
        unsafe_allow_html=True
    )

    render_links(name)

# ---------------------------- SIDEBAR ----------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["About Me", "Projects", "Resume", "Contact Me"]
)

# ---------------------------- ABOUT ----------------------------
if menu == "About Me":
    st.title("Manish Maltare")
    st.subheader("Digital Portfolio")
    st.markdown(about_text.replace("\n","<br>"), unsafe_allow_html=True)

# ---------------------------- PROJECTS ----------------------------
elif menu == "Projects":

    st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # CLASSIFICATION
    with col1:
        st.subheader("Classification")
        if st.button("NLP - Sentiment Analysis"):
            st.session_state["p"] = "NLP - Sentiment Analysis"

    # REGRESSION
    with col2:
        st.subheader("Regression")
        if st.button("Solar Panel Regression"):
            st.session_state["p"] = "Solar Panel Regression"

        if st.button("Machine Learning Insights into GDP Drivers"):
            st.session_state["p"] = "Machine Learning Insights into GDP Drivers"

    # ✅ NEW SECTION
    with col3:
        st.subheader("Recommendation System")
        if st.button("Online Course Recommendation System"):
            st.session_state["p"] = "Online Course Recommendation System"

    if "p" in st.session_state:
        show_project(st.session_state["p"])

# ---------------------------- RESUME ----------------------------
elif menu == "Resume":
    with open("Resume - Manish Maltare - final.pdf", "rb") as f:
        st.download_button("Download Resume", f)

# ---------------------------- CONTACT ----------------------------
elif menu == "Contact Me":
    st.write("📧 manishmaltare@gmail.com")
    st.write("📞 +91 9589945630")
    st.write("📍 Pune")

# ---------------------------- FOOTER ----------------------------
st.markdown("Website created by Manish Maltare")
