import streamlit as st
import docx
import re
import os

# ---------------------------- PAGE CONFIG ----------------------------
st.set_page_config(
    page_title="Manish Maltare | Data Science & Analytics Portfolio",
    layout="wide" # Keeps the wide layout for desktop views
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

/* --- REMOVED TOP NAVIGATION RIBBON CSS (Using Streamlit sidebar only) --- */

/* Sidebar Header Text (MODIFIED: Color Black, Size Default) */
.sidebar-header-new {
    text-align: center;
    width: 100%;
    font-weight: bold;
    color: #000000; /* Set to black */
    margin-bottom: 20px;
    font-size: 16px; /* Kept at default size */
    padding-top: 20px;
    background-color: rgba(255, 255, 255, 0.9); /* Added for better contrast */
    border-radius: 5px;
}

/* Increase font size for sidebar radio options (Navigation) */
div[data-testid="stSidebar"] div[role="radiogroup"] label {
    font-size: 20px !important;
    font-weight: 700 !important;
    padding: 5px 0;
}

/* Main content container padding for DESKTOP */
.block-container {
    padding-top:90px !important;
    padding-left:150px !important;
    padding-right:150px !important;
    color: white !important;
}

/* Titles - DESKTOP SIZES */
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
    font-size: 45px;
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

/* Semi-transparent black background for circle buttons */
.circle-icon {
    width: 120px;
    height: 120px;
    background: rgba(0,0,0,0.7); /* Applied Semi-transparent black background */
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
}
.circle-icon:hover {
    background: rgba(0,0,0,0.85); /* Darker semi-transparent black on hover */
    color: white; /* Kept text white for contrast */
    transform: scale(1.08);
    border-color: white;
}

/* ======================================================= */
/* MOBILE OPTIMIZATION (Media Query)           */
/* ======================================================= */

@media (max-width: 768px) {
    /* Adjust Main content container padding for MOBILE */
    .block-container {
        padding-left: 15px !important;
        padding-right: 15px !important;
        padding-top: 20px !important; /* Reduce top padding */
    }

    /* Titles - MOBILE SIZES */
    .main-title {
        font-size: 38px;
    }

    .sub-title-tagline {
        font-size: 22px;
    }

    .section-title {
        font-size: 32px;
    }

    /* Smaller circular buttons for less screen clutter */
    .circle-container {
        gap: 15px;
    }

    .circle-icon {
        width: 100px;
        height: 100px;
        font-size: 13px;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------------------- TOP NAVIGATION ----------------------------
# The top navigation HTML is removed as it is redundant with the Streamlit sidebar
# and takes up valuable space on mobile. The sidebar provides a better mobile experience.

# ---------------------------- LOAD TEXT FILES ----------------------------
def read_docx_safe(path):
    if not os.path.exists(path):
        return ""
    doc = docx.Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

about_text = read_docx_safe("About Me2.docx")

# keep DOCX files text-only (no HTML inside them)
nlp_text = read_docx_safe("NLP.docx")
logreg_text = read_docx_safe("Logistics Regression.docx")
solar_text = read_docx_safe("solar panel regression.docx")
ml_insights_text = read_docx_safe("Machine learning insights.docx")

# ---------------------------- PROJECT FUNCTIONS ----------------------------

def render_circle_links_fixed(project_name):
    links_map = {
        "NLP - Sentiment Analysis": {
            "Presentation": "https://drive.google.com/file/d/1x81_6kRZkUQtznd0JxplF-7pSEt0dZrs/view?usp=sharing",
            "GitHub - Script": "https://github.com/manishmaltare/NLP---Sentiment-Analysis",
            "GitHub - Deployment": "https://github.com/manishmaltare/Manish-Maltare/blob/main/SVC%20App%20Deployment%20-%20Sentiment%20Analysis%20-%20Group%201.py",
            "App Link": "https://manish-maltare-kfkyft36opaoieycyadutr.streamlit.app/",
        },
        "Logistic Regression - Titanic Survival Prediction": {
            # "Presentation" link removed as requested
            "GitHub - Script": "https://github.com/manishmaltare/Manish-Maltare/blob/main/RESUME_Logistic_Regression_Assignment.ipynb",
            "GitHub - Deployment": "https://github.com/manishmaltare/Manish-Maltare/blob/main/final_pickle_of_assignment_logisticregression_deployment_final.py",
            "App Link": "https://manish-maltare-8pw78deodbfyqewds8uere.streamlit.app/",
        },
        "Solar Panel Regression": {
            "Presentation": "https://drive.google.com/file/d/1unMOirI9oFjn2lKJH97sVE4985Gp0mea/view?usp=sharing",
            "GitHub - Script": "https://github.com/manishmaltare/Solar-Panel-Regression-1",
            "GitHub - Deployment": "https://github.com/manishmaltare/Solar-Panel-Regression-1/blob/main/resume_solar_panel_regression.py",
            "App Link": "https://solar-panel-regression-1-q3nwvmajqzqloi5aevksgq.streamlit.app/",
        },
        "Machine Learning Insights into GDP Drivers": {
            "Report": "https://drive.google.com/file/d/1Z0z1QTypvr6lqDpTgLb05LM_R5775P1T/view?usp=sharing",
            "GitHub - Script": "https://github.com/manishmaltare/Project---Machine-Learning-Insights-into-GDP-Drivers",
            # "GitHub - Deployment" link removed as requested
            "YouTube Video": "https://youtu.be/y6vTDqyEPdw?si=9x0Zb8B-2KPosX0R",
        },
    }

    proj_links = links_map.get(project_name, {})
    if not proj_links:
        return

    # GENERATE HTML LINKS WITHOUT EXTRA NEWLINES/INDENTATION
    link_html_list = []
    for label, url in proj_links.items():
        # Create a single line of HTML for each link to prevent Markdown code block interpretation
        link_html = (
            f'<a href="{url}" target="_blank">'
            f'<div class="circle-icon">{label}</div>'
            f'</a>'
        )
        link_html_list.append(link_html)

    # Join all links and wrap in the container
    html = f'<div class="circle-container">{" ".join(link_html_list)}</div>'

    st.markdown(html, unsafe_allow_html=True)


def render_docx_block(title, body_html, project_name=None):
    st.markdown(
        f"<div class='hover-card'><h3>{title}</h3></div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class='hover-card' style="margin-top:10px;">
            {body_html}
        </div>
        """,
        unsafe_allow_html=True
    )
    if project_name:
        render_circle_links_fixed(project_name)

def render_project_details(project_name):
    if project_name == "NLP - Sentiment Analysis":
        body_html = nlp_text.replace("\n", "<br>") if nlp_text else "NLP DOCX not found."
        render_docx_block(
            "NLP - Sentiment Analysis",
            body_html,
            project_name
        )

    elif project_name == "Logistic Regression - Titanic Survival Prediction":
        body_html = logreg_text.replace("\n", "<br>") if logreg_text else "Logistic Regression DOCX not found."
        render_docx_block(
            "Logistic Regression - Titanic Survival Prediction",
            body_html,
            project_name
        )

    elif project_name == "Solar Panel Regression":
        body_html = solar_text.replace("\n", "<br>") if solar_text else "Solar Panel Regression DOCX not found."
        render_docx_block(
            "Solar Panel Regression",
            body_html,
            project_name
        )

    elif project_name == "Machine Learning Insights into GDP Drivers":
        body_html = ml_insights_text.replace("\n", "<br>") if ml_insights_text else "Machine Learning Insights DOCX not found."
        render_docx_block(
            "Machine Learning Insights into GDP Drivers",
            body_html,
            project_name
        )

# ---------------------------- SIDEBAR ----------------------------

# 1. Sidebar Title/Header (AT THE TOP)
st.sidebar.markdown(
    """
    <div class="sidebar-header-new">
        Digital Portfolio<br>
        Manish Maltare
    </div>
    """,
    unsafe_allow_html=True
)

# 2. Navigation element
menu = st.sidebar.radio(
    "Navigation",
    ["About Me", "Projects", "Resume", "Contact Me"]
)

# ---------------------------- PAGE ROUTING ----------------------------
if menu == "About Me":
    st.markdown('<a id="about"></a>', unsafe_allow_html=True)

    st.markdown("<div class='main-title'>Manish Maltare</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title-tagline'>Digital Portfolio</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style="
            background-color: rgba(0,0,0,0.6);
            padding: 20px;
            border-radius: 10px;
            color: white;
            line-height: 1.6;
        ">
            {about_text.replace('\n','<br>') if about_text else "About content not found."}
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # ADDED: LinkedIn Profile Button
    st.markdown(
        """
        <div class='circle-container'>
            <a href="https://www.linkedin.com/in/manishmaltare/" target="_blank">
                <div class="circle-icon">LinkedIn Profile</div>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )


elif menu == "Projects":
    st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)

    # st.columns handles stacking on mobile by default, which is perfect.
    col1, col2 = st.columns(2)

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
        render_project_details(st.session_state["selected_project"])

elif menu == "Resume":
    st.markdown('<a id="resume"></a>', unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Download Resume</div>", unsafe_allow_html=True)
    with open("Resume - Manish Maltare - final.pdf", "rb") as f:
        st.download_button(
            label="📄 Download Resume (PDF)",
            data=f,
            file_name="Manish_Maltare_Resume.pdf",
            mime="application/pdf",
            key="resume_button"
        )

elif menu == "Contact Me":
    st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Contact Me</div>", unsafe_allow_html=True)
    st.write("📧 **Email:** manishmaltare@gmail.com")
    st.write("📞 **Phone:** +91 9589945630")
    st.write("📍 **Address:** Keshavnagar, Pune")

# ---------------------------- GLOBAL FOOTER ----------------------------
st.markdown(
    "<div style='text-align:center; margin-top: 50px; padding: 20px; background-color: rgba(0,0,0,0.5); border-radius: 10px;'>Website created by Manish Maltare</div>",
    unsafe_allow_html=True
)
