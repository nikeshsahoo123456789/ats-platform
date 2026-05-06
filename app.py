import streamlit as st
import pandas as pd

from database import create_tables
from database import get_connection

# ============================================
# LOAD CSS
# ============================================

def load_css():

    with open("styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="AABsys ATS",
    page_icon="📋",
    layout="wide"
)

# ============================================
# LOAD STYLES
# ============================================

load_css()

# ============================================
# CREATE TABLES
# ============================================

create_tables()

# ============================================
# DATABASE CONNECTION
# ============================================

conn = get_connection()

# ============================================
# LOAD DATA
# ============================================

try:
    df = pd.read_sql_query(
        "SELECT * FROM candidates",
        conn
    )

except:

    df = pd.DataFrame()

# ============================================
# STATUS COUNTS
# ============================================

total_candidates = len(df)

applied_count = 0
interview_count = 0
hired_count = 0
rejected_count = 0

if not df.empty and "Status" in df.columns:

    applied_count = len(
        df[df["Status"] == "Applied"]
    )

    interview_count = len(
        df[
            df["Status"].isin([
                "HR Interview",
                "Technical Round",
                "Final Round"
            ])
        ]
    )

    hired_count = len(
        df[df["Status"] == "Hired"]
    )

    rejected_count = len(
        df[df["Status"] == "Rejected"]
    )

# ============================================
# UNIQUE ROLES COUNT
# ============================================

if not df.empty and "Role" in df.columns:

    total_roles = df["Role"].nunique()

else:

    total_roles = 0

# ============================================
# HEADER
# ============================================

st.markdown("""
<div class="main-header">
    <div class="main-title">
        AABsys Talent Management
    </div>
    <div class="main-subtitle">
        Smart Hiring Dashboard
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# NAVIGATION
# ============================================

st.markdown("""
<style>

.navigation-wrapper {
    margin-top: 10px;
    margin-bottom: 25px;
}

.stPageLink {
    width: 100% !important;
}

.stPageLink a {

    display: flex !important;

    align-items: center !important;

    justify-content: center !important;

    width: 100% !important;

    min-height: 60px !important;

    background: white !important;

    border-radius: 14px !important;

    border: 1px solid #dbe4ee !important;

    text-decoration: none !important;

    color: #1e293b !important;

    font-size: 18px !important;

    font-weight: 600 !important;

    box-shadow:
        0px 2px 6px rgba(0,0,0,0.04);

    transition: all 0.25s ease-in-out !important;

    cursor: pointer !important;
}

.stPageLink a p {
    margin: 0 !important;
    padding: 0 !important;
    text-decoration: none !important;
}

.stPageLink a:hover {

    transform: translateY(-2px);

    border: 1px solid #4a90e2 !important;

    color: #4a90e2 !important;

    box-shadow:
        0px 8px 18px rgba(74,144,226,0.15);
}

.stPageLink a:active {
    transform: scale(0.98);
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="navigation-wrapper">',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

# ============================================
# DASHBOARD BUTTON
# ============================================

with col1:

    st.page_link(
        "app.py",
        label="📊 Dashboard",
        use_container_width=True
    )

# ============================================
# CANDIDATES BUTTON
# ============================================

with col2:

    st.page_link(
        "pages/2_Candidates.py",
        label="👥 Candidates",
        use_container_width=True
    )

# ============================================
# ADD CANDIDATE BUTTON
# ============================================

with col3:

    st.page_link(
        "pages/3_Add_Candidate.py",
        label="➕ Add Candidate",
        use_container_width=True
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

# ============================================
# DASHBOARD TITLE
# ============================================

st.markdown("""
<div class="section-title">
    📊 Dashboard Overview
</div>
""", unsafe_allow_html=True)

# ============================================
# METRIC CARDS
# ============================================

c1, c2, c3, c4, c5, c6 = st.columns(6)

metrics = [
    ("Total Roles", total_roles),
    ("Candidates", total_candidates),
    ("Applied", applied_count),
    ("Interview", interview_count),
    ("Hired", hired_count),
    ("Rejected", rejected_count)
]

columns = [c1, c2, c3, c4, c5, c6]

for col, metric in zip(columns, metrics):

    with col:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{metric[0]}</div>
            <div class="metric-value">{metric[1]}</div>
        </div>
        """, unsafe_allow_html=True)