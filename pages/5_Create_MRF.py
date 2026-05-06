import streamlit as st
import sqlite3
import os
from datetime import datetime

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Create MRF",
    page_icon="📄",
    layout="wide"
)

# ============================================
# DATABASE
# ============================================

conn = sqlite3.connect(
    "candidates.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ============================================
# CREATE MRF TABLE
# ============================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS mrf_requests (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    position TEXT,

    department TEXT,

    branch TEXT,

    candidate_type TEXT,

    vacancies INTEGER,

    reason TEXT,

    experience TEXT,

    jd_file TEXT,

    description TEXT,

    status TEXT,

    created_date TEXT
)
""")

conn.commit()

# ============================================
# CREATE JD FOLDER
# ============================================

if not os.path.exists("jd_files"):

    os.makedirs("jd_files")

# ============================================
# STYLING
# ============================================

st.markdown("""
<style>

/* ============================================
BACKGROUND
============================================ */

.stApp {
    background-color: #f4f7fb;
}

/* ============================================
SPACING
============================================ */

.block-container {

    padding-top: 1rem !important;

    padding-left: 2rem !important;

    padding-right: 2rem !important;

    padding-bottom: 2rem !important;
}

/* ============================================
FORM AREA
============================================ */

.form-container {

    background: white;

    padding: 30px;

    border-radius: 20px;

    border: 1px solid #dbe4ee;

    box-shadow:
        0px 4px 18px rgba(0,0,0,0.05);

    margin-top: 20px;
}

/* ============================================
INPUTS
============================================ */

.stTextInput input,
.stNumberInput input {

    border-radius: 10px !important;

    border: 1px solid #d6dfeb !important;

    height: 50px !important;
}

.stTextArea textarea {

    border-radius: 10px !important;

    border: 1px solid #d6dfeb !important;
}

.stSelectbox div[data-baseweb="select"] {

    border-radius: 10px !important;

    border: 1px solid #d6dfeb !important;

    min-height: 50px !important;
}

/* ============================================
UPLOAD
============================================ */

[data-testid="stFileUploader"] {

    background: white;

    border: 1px solid #d6dfeb;

    border-radius: 12px;

    padding: 12px;
}

/* ============================================
BUTTON
============================================ */

.stButton button {

    background:
        linear-gradient(
            135deg,
            #4a90e2,
            #6ea8f1
        );

    color: white;

    border: none;

    border-radius: 12px;

    height: 52px;

    width: 100%;

    font-size: 16px;

    font-weight: 700;
}

.stButton button:hover {

    transform: translateY(-1px);

    box-shadow:
        0px 8px 18px rgba(74,144,226,0.20);
}

</style>
""", unsafe_allow_html=True)

# ============================================
# PAGE HEADER
# ============================================

st.title("📄 MRF Management")

st.caption(
    "Create and manage manpower requisition forms"
)

# ============================================
# TOP METRICS
# ============================================

cursor.execute(
    "SELECT COUNT(*) FROM mrf_requests"
)

total_mrf = cursor.fetchone()[0]

cursor.execute(
    "SELECT COUNT(*) FROM mrf_requests WHERE status='Open'"
)

open_mrf = cursor.fetchone()[0]

cursor.execute(
    "SELECT COUNT(*) FROM mrf_requests WHERE status='Closed'"
)

closed_mrf = cursor.fetchone()[0]

m1, m2, m3 = st.columns(3)

with m1:

    st.metric(
        "Total MRF",
        total_mrf
    )

with m2:

    st.metric(
        "Open Positions",
        open_mrf
    )

with m3:

    st.metric(
        "Closed Positions",
        closed_mrf
    )

# ============================================
# FORM CONTAINER
# ============================================

st.markdown(
    '<div class="form-container">',
    unsafe_allow_html=True
)

st.subheader("➕ Create New MRF")

# ============================================
# ROW 1
# ============================================

col1, col2 = st.columns(2)

with col1:

    position = st.text_input(
        "Position Title",
        placeholder="Software Engineer"
    )

with col2:

    department = st.selectbox(
        "Department",
        [
            "Engineering",
            "HR",
            "Finance",
            "Operations",
            "Marketing",
            "Sales"
        ]
    )

# ============================================
# ROW 2
# ============================================

col3, col4 = st.columns(2)

with col3:

    branch = st.selectbox(
        "Branch",
        [
            "Bhubaneswar",
            "Berhampur",
            "Balasore"
        ]
    )

with col4:

    candidate_type = st.selectbox(
        "Candidate Type",
        [
            "Fresher",
            "Experienced"
        ]
    )

# ============================================
# ROW 3
# ============================================

col5, col6 = st.columns(2)

with col5:

    vacancies = st.number_input(
        "No. of Vacancies",
        min_value=1,
        step=1
    )

with col6:

    reason = st.selectbox(
        "Reason for Recruitment",
        [
            "New Position",
            "Replacement",
            "Project Requirement",
            "Expansion Hiring"
        ]
    )

# ============================================
# ROW 4
# ============================================

col7, col8 = st.columns(2)

with col7:

    jd_file = st.file_uploader(
        "Upload JD File",
        type=["pdf", "docx"]
    )

with col8:

    experience = st.text_input(
        "Minimum Experience",
        placeholder="Example: 3 Years"
    )

# ============================================
# DESCRIPTION
# ============================================

description = st.text_area(
    "Job Description",
    placeholder="Enter detailed job description..."
)

# ============================================
# SAVE JD FILE
# ============================================

jd_path = ""

if jd_file is not None:

    jd_path = f"jd_files/{jd_file.name}"

    with open(jd_path, "wb") as f:

        f.write(
            jd_file.getbuffer()
        )

# ============================================
# BUTTON
# ============================================

create = st.button(
    "🚀 Create MRF"
)

# ============================================
# SAVE MRF
# ============================================

if create:

    if position == "":

        st.warning(
            "Please enter position title."
        )

    else:

        cursor.execute("""
        INSERT INTO mrf_requests (

            position,
            department,
            branch,
            candidate_type,
            vacancies,
            reason,
            experience,
            jd_file,
            description,
            status,
            created_date

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

        """, (

            position,
            department,
            branch,
            candidate_type,
            vacancies,
            reason,
            experience,
            jd_path,
            description,
            "Open",
            datetime.now().strftime("%Y-%m-%d")

        ))

        conn.commit()

        st.success(
            "✅ MRF Created Successfully!"
        )

        st.balloons()

st.markdown(
    '</div>',
    unsafe_allow_html=True
)