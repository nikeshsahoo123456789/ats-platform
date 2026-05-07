import streamlit as st
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AABSys Talent Management",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# PREMIUM UI STYLING
# =========================================================

st.markdown("""
<style>

/* =====================================================
MAIN APP
===================================================== */

.stApp {
    background-color: #f8fafc;
}

/* =====================================================
HIDE STREAMLIT SIDEBAR
===================================================== */

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

/* =====================================================
HEADINGS
===================================================== */

h1, h2, h3 {
    color: #0f172a;
    font-weight: 800;
}

/* =====================================================
PREMIUM NAVIGATION BUTTONS
===================================================== */

.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #ffffff 0%, #f8fbff 100%);
    border: 1px solid #dbeafe;
    border-radius: 14px;
    color: #0f172a;
    font-weight: 700;
    height: 52px;
    font-size: 15px;
    transition: all 0.25s ease;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    margin-top: 2px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
    border: 1px solid #60a5fa;
    color: #2563eb;
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(37, 99, 235, 0.12);
}

/* =====================================================
METRIC CARDS
===================================================== */

[data-testid="stMetric"] {
    background: white;
    border: 1px solid #dbeafe;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}

/* =====================================================
DATAFRAMES
===================================================== */

[data-testid="stDataFrame"] {
    background: white;
    border-radius: 18px;
    border: 1px solid #dbeafe;
    overflow: hidden;
}

/* =====================================================
DIVIDERS
===================================================== */

hr {
    border-color: #dbeafe;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# MODERN PREMIUM HEADER
# =========================================================

st.markdown("""
<div style='
padding:40px;
border-radius:24px;
background: linear-gradient(135deg, #dbeafe 0%, #eff6ff 100%);
border:1px solid #cbd5e1;
margin-bottom:20px;
box-shadow:0 4px 18px rgba(0,0,0,0.04);
'>

<h1 style='
margin:0;
font-size:48px;
color:#0f172a;
font-weight:800;
'>
🚀 AABSys Talent Management
</h1>

<p style='
font-size:20px;
color:#334155;
margin-top:12px;
font-weight:500;
'>
AI Powered Recruitment, Candidate Tracking and Workforce Management Platform
</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# PREMIUM TOP NAVIGATION
# =========================================================

nav1, nav2, nav3, nav4, nav5 = st.columns(5)

with nav1:
    if st.button("📊 Dashboard", use_container_width=True):
        st.switch_page("app.py")

with nav2:
    if st.button("👥 Candidates", use_container_width=True):
        st.switch_page("pages/2_Candidates.py")

with nav3:
    if st.button("➕ Add Candidate", use_container_width=True):
        st.switch_page("pages/3_Add_Candidate.py")

with nav4:
    if st.button("📋 MRF Management", use_container_width=True):
        st.switch_page("pages/4_MRF_Management.py")

with nav5:
    if st.button("📝 Create MRF", use_container_width=True):
        st.switch_page("pages/5_Create_MRF.py")

st.write("")
st.divider()

# =========================================================
# DASHBOARD OVERVIEW
# =========================================================

st.header("📊 Dashboard Overview")

st.write(
    "Monitor hiring performance, recruitment pipeline and workforce activities."
)

st.write("")

# =========================================================
# METRICS SECTION
# =========================================================

m1, m2, m3, m4, m5, m6 = st.columns(6)

with m1:
    st.metric("Total Roles", 4)

with m2:
    st.metric("Candidates", 5)

with m3:
    st.metric("Applied", 0)

with m4:
    st.metric("Interview", 3)

with m5:
    st.metric("Hired", 1)

with m6:
    st.metric("Rejected", 1)

st.write("")
st.divider()

# =========================================================
# RECRUITMENT PIPELINE
# =========================================================

st.subheader("🚀 Recruitment Pipeline")

pipeline_df = pd.DataFrame({
    "Stage": ["Applied", "Interview", "Hired"],
    "Count": [0, 3, 1]
})

st.dataframe(
    pipeline_df,
    use_container_width=True,
    hide_index=True
)

st.write("")
st.divider()

# =========================================================
# RECENT CANDIDATES
# =========================================================

st.subheader("👨‍💼 Recent Candidates")

candidate_df = pd.DataFrame({

    "Name": [
        "Nikesh",
        "Niramehs",
        "Ghaghsa",
        "Nijniji",
        "Mjyuthi"
    ],

    "Role": [
        "Business Analyst",
        "Data Analyst",
        "HR Executive",
        "Python Developer",
        "UI UX Designer"
    ],

    "Status": [
        "Hired",
        "HR Interview",
        "Rejected",
        "Final Round",
        "Technical Round"
    ],

    "Experience": [
        2,
        3,
        1,
        4,
        2
    ],

    "Location": [
        "Bhubaneswar",
        "Hyderabad",
        "Chennai",
        "Bangalore",
        "Pune"
    ]
})

st.dataframe(
    candidate_df,
    use_container_width=True,
    hide_index=True
)

st.write("")
st.divider()

# =========================================================
# FOOTER
# =========================================================

st.caption("© 2025 AABSys Talent Management")