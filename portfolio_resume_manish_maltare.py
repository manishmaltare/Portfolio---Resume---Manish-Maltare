import streamlit as st
import docx
import os

# ---------------------------- PAGE CONFIG ----------------------------
st.set_page_config(
    page_title="Manish Maltare | Data Science & Analytics Portfolio",
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
ml_insights_text = read_docx_safe("Machine learning insights.docx")

# ✅ NEW PROJECT DOCX (YOUR FILES)
recommendation_text = read_docx_safe("Online Course Recommendations.docx")

# ---------------------------- PROJECT LINKS ----------------------------
def render_circle_links_fixed(project_name):
    links_map = {

        "NLP - Sentiment Analysis": {
            "GitHub - Script": "https://github.com/manishmaltare/NLP---Sentiment-Analysis",
            "App Link": "https://manish-maltare-kfkyft36opaoieycyadutr.streamlit.app/",
        },

        "Solar Panel Regression": {
            "GitHub - Script": "https://github.com/manishmaltare/Solar-Panel-Regression-1",
            "App Link": "https://solar-panel-regression-1-q3nwvmajqzqloi5aevksgq.streamlit.app/",
        },

        "Machine Learning Insights into GDP Drivers": {
            "GitHub - Script": "https://github.com/manishmaltare/Project---Machine-Learning-Insights-into-GDP-Drivers",
        },

        # ✅ NEW PROJECT
        "Online Course Recommendation System": {
            "GitHub - Script": "https://github.com/manishmaltare",  # update if needed
            "App Link": "#"
        }
    }

    proj_links = links_map.get(project_name, {})
    if not proj_links:
        return

    html = '<div class="circle-container">'
    for label, url in proj_links.items():
        html += f'<a href="{url}" target="_blank"><div class="circle-icon">{label}</div></a>'
    html += '</div>'

    st.markdown(html, unsafe_allow_html=True)

# ---------------------------- PROJECT DISPLAY ----------------------------
def render_docx_block(title, body_html, project_name=None):
    st.markdown(f"<div class='hover-card'><h3>{title}</h3></div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='hover-card'>{body_html}</div>",
        unsafe_allow_html=True
    )
    if project_name:
        render_circle_links_fixed(project_name)

def render_project_details(project_name):

    if project_name == "NLP - Sentiment Analysis":
        render_docx_block(
            project_name,
            nlp_text.replace("\n", "<br>"),
            project_name
        )

    elif project_name == "Solar Panel Regression":
        render_docx_block(
            project_name,
            solar_text.replace("\n", "<br>"),
            project_name
        )

    elif project_name == "Machine Learning Insights into GDP Drivers":
        render_docx_block(
            project_name,
            ml_insights_text.replace("\n", "<br>"),
            project_name
        )

    # ✅ NEW PROJECT
    elif project_name == "Online Course Recommendation System":
        render_docx_block(
            project_name,
            recommendation_text.replace("\n", "<br>"),
            project_name
        )

# ---------------------------- SIDEBAR ----------------------------
st.sidebar.markdown("### Digital Portfolio\nManish Maltare")

menu = st.sidebar.radio(
    "Navigation",
    ["About Me", "Projects", "Resume", "Contact Me"]
)

# ---------------------------- ABOUT ----------------------------
if menu == "About Me":
    st.title("Manish Maltare")
    st.subheader("Digital Portfolio")

    st.markdown(about_text.replace("\n", "<br>"), unsafe_allow_html=True)

# ---------------------------- PROJECTS ----------------------------
elif menu == "Projects":

    st.header("Projects")

    col1, col2, col3 = st.columns(3)

    # ✅ CLASSIFICATION
    with col1:
        st.subheader("Classification")
        if st.button("NLP - Sentiment Analysis"):
            st.session_state["selected_project"] = "NLP - Sentiment Analysis"

    # ✅ REGRESSION
    with col2:
        st.subheader("Regression")
        if st.button("Solar Panel Regression"):
            st.session_state["selected_project"] = "Solar Panel Regression"

        if st.button("Machine Learning Insights into GDP Drivers"):
            st.session_state["selected_project"] = "Machine Learning Insights into GDP Drivers"

    # ✅ NEW SECTION
    with col3:
        st.subheader("Recommendation System")
        if st.button("Online Course Recommendation System"):
            st.session_state["selected_project"] = "Online Course Recommendation System"

    if st.session_state.get("selected_project"):
        render_project_details(st.session_state["selected_project"])

# ---------------------------- RESUME ----------------------------
elif menu == "Resume":
    st.header("Download Resume")
    with open("Resume - Manish Maltare - final.pdf", "rb") as f:
        st.download_button(
            label="Download Resume",
            data=f,
            file_name="Manish_Maltare_Resume.pdf",
            mime="application/pdf"
        )

# ---------------------------- CONTACT ----------------------------
elif menu == "Contact Me":
    st.header("Contact Me")
    st.write("📧 manishmaltare@gmail.com")
    st.write("📞 +91 9589945630")
    st.write("📍 Pune")

# ---------------------------- FOOTER ----------------------------
st.markdown("Website created by Manish Maltare")
