# -*- coding: utf-8 -*-
"""Portfolio_Resume_Manish Maltare.ipynb"""

import streamlit as st
import docx
import re

# ------------------------------------------------
# PAGE CONFIG & FONT IMPORT
# ------------------------------------------------
st.set_page_config(page_title="Manish Maltare - Digital Portfolio", layout="wide")

# Custom UI Styling + Copperplate Gothic Font
st.markdown("""
    <style>
        @import url('https://fonts.cdnfonts.com/css/copperplate-gothic');

        * {
            font-family: 'Copperplate Gothic', sans-serif !important;
        }

        body {
            background-color: #F7F9FC;
        }
        .main-title {
            text-align: center;
            font-size: 45px;
            font-weight: 700;
            padding-bottom: 10px;
