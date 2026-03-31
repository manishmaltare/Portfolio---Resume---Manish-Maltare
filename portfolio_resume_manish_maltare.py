import streamlit as st
import docx
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Portfolio", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>

/* BACKGROUND */
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/manishmaltare/Portfolio---Resume---Manish-Maltare/main/5072609.jpg");
    background-size: cover;
    background-attachment: fixed;
    color: white !important;
}

/* FORCE TEXT WHITE */
html, body, [class*="css"]  {
    color: white !important;
}

/* HEADINGS */
h1, h2, h3 {
    font-weight: 800 !important;
    color: white !important;
}

/* -------- BUTTON FIX (IMPORTANT) -------- */
.stButton>button,
div[data-testid="stDownloadButton"] button {
    background: transparent !important;
    color: white !important;
    border: 1px solid white !important;
    border-radius: 6px;
    font-weight: bold;
}
.stButton>button:hover,
div[data-testid="stDownloadButton"] button:hover {
    background: rgba(255,255,255,0.2) !important;
}

/* CARD */
.card {
    background: rgba(0,0,0,0.6);
    padding: 20px;
    border-radius: 10px;
}

/* RIGHT PANEL */
.link-box {
    background: rgba(0,0,0,0.7);
    padding: 20px;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* -------- CIRCULAR WHITE BUTTONS -------- */
.circle-link {
    width: 110px;
    height: 110px;
    background: white;
    color: black;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    margin-bottom: 15px;
    font-weight: bold;
    text-decoration: none;
}
.circle-link:hover {
    transform: scale(1.05);
}

/* FOOTER */
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    background: rgba(0,0,0,0.7);
    text-align: center;
    padding: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- DOCX ----------------
def read_docx(path):
    if not os.path.exists(path):
        return ""
    doc = docx.Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

about = read_docx("About Me2.docx")
nlp = read_docx("NLP.docx")
solar = read_docx("solar panel regression.docx")
gdp = read_docx("Machine learning insights.docx")
rec = read_docx("Online Course Recommendations.docx")

# ---------------- LINKS ----------------
def get_links(name):
    return {
        "Machine Learning Insights into GDP Drivers": {
            "Presentation": "https://drive.google.com/file/d/1Z0z1QTypvr6lqDpTgLb05LM_R5775P1T/view?usp=sharing",
            "GitHub": "https://github.com/manishmaltare/Project---Machine-Learning-Insights-into-GDP-Drivers",
            "YouTube": "https://youtu.be/y6vTDqyEPdw"
        },
        "Solar Panel Regression": {
            "Presentation": "https://drive.google.com/file/d/1unMOirI9oFjn2lKJH97sVE4985Gp0mea/view",
            "GitHub": "https://github.com/manishmaltare/Solar-Panel-Regression-1",
            "App": "https://solar-panel-regression-1-q3nwvmajqzqloi5aevksgq.streamlit.app/"
        },
        "NLP - Sentiment Analysis": {
            "Presentation": "https://drive.google.com/file/d/1x81_6kRZkUQtznd0JxplF-7pSEt0dZrs/view",
            "GitHub": "https://github.com/manishmaltare/NLP---Sentiment-Analysis",
            "App": "https://manish-maltare-kfkyft36opaoieycyadutr.streamlit.app/"
        },
        "Online Course Recommendation System": {
            "Presentation": "https://drive.google.com/file/d/1j8fGEzcJEIPPGAcSLznOcoRYOj2cWVPS/view",
            "GitHub": "https://github.com/manishmaltare/Online-Class-Recommendations/blob/main/online_course_recommendation_file.ipynb"
        }
    }[name]

# ---------------- PROJECT DISPLAY ----------------
def show_project(name, text):

    col1, col2 = st.columns([3,1])

    # LEFT
    with col1:
        st.markdown(f"<div class='card'><h3>{name}</h3><br>{text.replace(chr(10),'<br>')}</div>", unsafe_allow_html=True)

    # RIGHT
    with col2:
        st.markdown("<div class='link-box'>", unsafe_allow_html=True)
        for k, v in get_links(name).items():
            st.markdown(f"<a href='{v}' target='_blank' class='circle-link'>{k}</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio("Navigation", ["About Me","Projects","Resume","Contact Me"])

# ---------------- ABOUT ----------------
if menu == "About Me":
    st.markdown("## **About Me**")
    st.markdown(f"<div class='card'>{about.replace(chr(10),'<br>')}</div>", unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif menu == "Projects":

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown("### **Classification**")
        if st.button("NLP - Sentiment Analysis"):
            st.session_state["p"]="NLP - Sentiment Analysis"

    with col2:
        st.markdown("### **Regression**")
        if st.button("Solar Panel Regression"):
            st.session_state["p"]="Solar Panel Regression"
        if st.button("Machine Learning Insights into GDP Drivers"):
            st.session_state["p"]="Machine Learning Insights into GDP Drivers"

    with col3:
        st.markdown("### **Recommendation System**")
        if st.button("Online Course Recommendation System"):
            st.session_state["p"]="Online Course Recommendation System"

    if "p" in st.session_state:
        mapping = {
            "NLP - Sentiment Analysis": nlp,
            "Solar Panel Regression": solar,
            "Machine Learning Insights into GDP Drivers": gdp,
            "Online Course Recommendation System": rec
        }
        show_project(st.session_state["p"], mapping[st.session_state["p"]])

# ---------------- RESUME ----------------
elif menu == "Resume":
    st.markdown("## **Resume**")
    with open("Resume - Manish Maltare - final.pdf","rb") as f:
        st.download_button("Download Resume",f)

# ---------------- CONTACT ----------------
elif menu == "Contact Me":
    st.markdown("## **Contact Details**")
    st.markdown("""
    📧 manishmaltare@gmail.com  
    📞 +91 9589945630  
    📍 Pune
    """)

# ---------------- FOOTER ----------------
st.markdown("<div class='footer'>Created by Manish Maltare</div>", unsafe_allow_html=True)
