if menu == "About Me":
    st.markdown('<a id="about"></a>', unsafe_allow_html=True)
    st.markdown("<div class='main-title'>Manish Maltare</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title-tagline'>Digital Portfolio</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)
    
    # Wrap About Me text in a semi-transparent black box
    st.markdown(
        f"""
        <div style="
            background-color: rgba(0,0,0,0.6);
            padding: 20px;
            border-radius: 10px;
            color: white;
            line-height: 1.6;
        ">
            {about_text.replace('\n','<br>')}
        </div>
        """,
        unsafe_allow_html=True
    )
