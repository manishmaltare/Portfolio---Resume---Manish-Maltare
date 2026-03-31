import streamlit as st
import docx
import os

# ---------------------------- PAGE CONFIG ----------------------------
st.set_page_config(
    page_title="Manish Maltare | Data Science Portfolio",
    layout="wide"
)

# ---------------------------- CSS ----------------------------
st.markdown("""
<style>

/* BACKGROUND */
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/manishmaltare/Portfolio---Resume---Manish-Maltare/main/5072609.jpg");
    background-size: cover;
    background-attachment: fixed;
}

/* BUTTON FIX */
.stButton>button, div[data-testid="stDownloadButton"] button {
    background-color: rgba(0,0,0,0.6) !important;
    color: white !important;
    border-radius: 6px;
}

/* FOOTER FIXED */
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    text-align: center;
    background: rgba(0,0,0,0.7);
    color: white;
    padding: 10px;
    font-weight: 600;
}

/* CARD */
.hover-card {
    padding: 15px;
    border-radius: 10px;
    background: rgba(0,0,0,0.6);
    margin-top: 20px;
    color: white;
}

/* LINK BUTTONS */
.circle-container {
    display: flex;
    gap: 20px;
    margin-top: 20px;
    flex-wrap: wrap;
}

.circle-icon {
    width: 120px;
    height: 120px;
    background: rgba(0,0,0,0.7);
    border-radius: 50%;
    display:flex;
    align-items:center;
    justify-content:center;
    color:white;
    font-weight:bold;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------- DOCX ----------------------------
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

# ---------------------------- LINKS ----------------------------
def render_links(name):

    links = {

        "Machine Learning Insights into GDP Drivers": {
            "Presentation": "https://drive.google.com/file/d/1Z0z1QTypvr6lqDpTgLb05LM_R5775P1T/view?usp=sharing",
            "GitHub Script": "https://github.com/manishmaltare/Project---Machine-Learning-Insights-into-GDP-Drivers",
            "GitHub Deployment": "https://github.com/manishmaltare/Project---Machine-Learning-Insights-into-GDP-Drivers",
            "YouTube": "https://youtu.be/y6vTDqyEPdw?si=9x0Zb8B-2KPosX0R"
        },

        "Solar Panel Regression": {
            "Presentation": "https://drive.google.com/file/d/1unMOirI9oFjn2lKJH97sVE4985Gp0mea/view?usp=sharing",
            "GitHub Script": "https://github.com/manishmaltare/Solar-Panel-Regression-1",
            "GitHub Deployment": "https://github.com/manishmaltare/Solar-Panel-Regression-1",
            "App": "https://solar-panel-regression-1-q3nwvmajqzqloi5aevksgq.streamlit.app/"
        },

        "NLP - Sentiment Analysis": {
            "Presentation": "https://drive.google.com/file/d/1x81_6kRZkUQtznd0JxplF-7pSEt0dZrs/view?usp=sharing",
            "GitHub Script": "https://github.com/manishmaltare/NLP---Sentiment-Analysis",
            "GitHub Deployment": "https://github.com/manishmaltare/Manish-Maltare/blob/main/SVC%20App%20Deployment%20-%20Sentiment%20Analysis%20-%20Group%201.py",
            "App": "https://manish-maltare-kfkyft36opaoieycyadutr.streamlit.app/"
        },

        "Online Course Recommendation System": {
            "Presentation": "https://drive.google.com/file/d/1j8fGEzcJEIPPGAcSLznOcoRYOj2cWVPS/view?usp=drive_link",
            "GitHub Script": "https://github.com/manishmaltare/Online-Class-Recommendations/blob/main/online_course_recommendation_file.ipynb"
        }
    }

    html = '<div class="circle-container">'
    for k,v in links[name].items():
        html += f'<a href="{v}" target="_blank"><div class="circle-icon">{k}</div></a>'
    html += '</div>'

    st.markdown(html, unsafe_allow_html=True)

# ---------------------------- PROJECT DISPLAY ----------------------------
def show_project(name, text):

    st.markdown(f"<div class='hover-card'><h3>{name}</h3></div>", unsafe_allow_html=True)

    st.markdown(
        f"<div class='hover-card'>{text.replace(chr(10),'<br>')}</div>",
        unsafe_allow_html=True
    )

    render_links(name)

# ---------------------------- SIDEBAR ----------------------------
menu = st.sidebar.radio("Navigation",
    ["About Me","Projects","Resume","Contact Me"]
)

# ---------------------------- ABOUT ----------------------------
if menu == "About Me":
    st.title("Manish Maltare")
    st.markdown(about.replace("\n","<br>"), unsafe_allow_html=True)

# ---------------------------- PROJECTS ----------------------------
elif menu == "Projects":

    col1,col2,col3 = st.columns(3)

    with col1:
        st.subheader("Classification")
        if st.button("NLP - Sentiment Analysis"):
            st.session_state["p"]="NLP - Sentiment Analysis"

    with col2:
        st.subheader("Regression")
        if st.button("Solar Panel Regression"):
            st.session_state["p"]="Solar Panel Regression"
        if st.button("Machine Learning Insights into GDP Drivers"):
            st.session_state["p"]="Machine Learning Insights into GDP Drivers"

    with col3:
        st.subheader("Recommendation System")
        if st.button("Online Course Recommendation System"):
            st.session_state["p"]="Online Course Recommendation System"

    if "p" in st.session_state:
        if st.session_state["p"]=="NLP - Sentiment Analysis":
            show_project("NLP - Sentiment Analysis", nlp)

        elif st.session_state["p"]=="Solar Panel Regression":
            show_project("Solar Panel Regression", solar)

        elif st.session_state["p"]=="Machine Learning Insights into GDP Drivers":
            show_project("Machine Learning Insights into GDP Drivers", gdp)

        elif st.session_state["p"]=="Online Course Recommendation System":
            show_project("Online Course Recommendation System", rec)

# ---------------------------- RESUME ----------------------------
elif menu == "Resume":
    st.subheader("Download Resume")
    with open("Resume - Manish Maltare - final.pdf","rb") as f:
        st.download_button("Download Resume",f)

# ---------------------------- CONTACT ----------------------------
elif menu == "Contact Me":
    st.subheader("Contact Details")
    st.write("📧 manishmaltare@gmail.com")
    st.write("📞 +91 9589945630")
    st.write("📍 Pune")

# ---------------------------- FOOTER ----------------------------
st.markdown('<div class="footer">Created by Manish Maltare</div>', unsafe_allow_html=True)
