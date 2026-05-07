import streamlit as st
import sqlite3
from utils.database import get_connection
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
# CREATE TABLE
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

    work_mode TEXT,

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
# SMART ROLE TEMPLATES
# ============================================

job_templates = {

    "Data Analyst": {

        "skills":
        "SQL • Excel • Power BI • Python • Data Visualization",

        "mode":
        "Hybrid",

        "experience":
        "2-4 Years",

        "department":
        "Engineering",

        "jd":
        """
Analyze business data, create interactive dashboards,
generate reports, and provide insights using SQL,
Excel and Power BI.
"""
    },

    "Python Developer": {

        "skills":
        "Python • Django • APIs • SQL • Git",

        "mode":
        "Remote",

        "experience":
        "1-3 Years",

        "department":
        "Engineering",

        "jd":
        """
Develop scalable backend applications using Python,
integrate APIs, optimize databases and maintain
high-performance systems.
"""
    },

    "UI/UX Designer": {

        "skills":
        "Figma • Adobe XD • Wireframing • Prototyping",

        "mode":
        "Hybrid",

        "experience":
        "2-5 Years",

        "department":
        "Design",

        "jd":
        """
Design modern interfaces, improve user experience,
create wireframes and collaborate with development teams.
"""
    },

    "HR Executive": {

        "skills":
        "Recruitment • ATS • Screening • Communication",

        "mode":
        "Onsite",

        "experience":
        "1-3 Years",

        "department":
        "HR",

        "jd":
        """
Manage recruitment workflows, coordinate interviews,
maintain employee records and support HR operations.
"""
    }
}

# ============================================
# MODERN PREMIUM UI
# ============================================

st.markdown("""
<style>

/* ============================================
GLOBAL
============================================ */

.stApp {

    background:
        linear-gradient(
            to bottom right,
            #f6f9fc,
            #edf3fa
        );

    font-family: 'Segoe UI', sans-serif;
}

/* ============================================
MAIN CONTAINER
============================================ */

.block-container {

    padding-top: 2rem !important;

    padding-left: 3rem !important;

    padding-right: 3rem !important;

    padding-bottom: 3rem !important;

    max-width: 1550px;
}

/* ============================================
TOP HERO
============================================ */

.hero {

    background:
        linear-gradient(
            135deg,
            #4a90e2,
            #6ea8f1
        );

    padding: 42px;

    border-radius: 28px;

    color: white;

    margin-bottom: 35px;

    box-shadow:
        0px 12px 30px rgba(74,144,226,0.22);
}

.hero-title {

    font-size: 44px;

    font-weight: 800;

    margin-bottom: 10px;
}

.hero-sub {

    font-size: 18px;

    opacity: 0.95;
}

/* ============================================
METRIC CARDS
============================================ */

[data-testid="metric-container"] {

    background: white;

    padding: 28px;

    border-radius: 22px;

    border: 1px solid #e5edf5;

    box-shadow:
        0px 6px 18px rgba(0,0,0,0.04);

    transition: 0.3s;
}

[data-testid="metric-container"]:hover {

    transform: translateY(-4px);
}

/* ============================================
FORM CONTAINER
============================================ */

.form-container {

    background: white;

    padding: 45px;

    border-radius: 30px;

    border: 1px solid #e5edf5;

    box-shadow:
        0px 12px 28px rgba(0,0,0,0.05);

    margin-top: 25px;
}

/* ============================================
SECTION TITLE
============================================ */

.section-title {

    font-size: 30px;

    font-weight: 800;

    color: #1f2937;

    margin-bottom: 35px;
}

/* ============================================
LABELS
============================================ */

label {

    font-size: 15px !important;

    font-weight: 700 !important;

    color: #344054 !important;
}

/* ============================================
INPUTS
============================================ */

.stTextInput input,
.stNumberInput input {

    height: 62px !important;

    border-radius: 16px !important;

    border: 1px solid #d9e2ec !important;

    background: #fbfdff !important;

    padding-left: 18px !important;

    font-size: 15px !important;
}

/* ============================================
SELECTBOX
============================================ */

.stSelectbox div[data-baseweb="select"] {

    min-height: 62px !important;

    border-radius: 16px !important;

    border: 1px solid #d9e2ec !important;

    background: #fbfdff !important;

    font-size: 15px !important;
}

/* ============================================
TEXT AREA
============================================ */

.stTextArea textarea {

    border-radius: 18px !important;

    border: 1px solid #d9e2ec !important;

    background: #fbfdff !important;

    padding: 20px !important;

    font-size: 15px !important;

    line-height: 1.8 !important;
}

/* ============================================
UPLOAD BOX
============================================ */

[data-testid="stFileUploader"] {

    border-radius: 18px;

    border: 2px dashed #c7d7ea;

    background: #f9fbff;

    padding: 25px;
}

/* ============================================
INFO BOX
============================================ */

[data-testid="stAlert"] {

    border-radius: 18px;

    padding: 18px;

    border: none;

    background: #eef5ff;
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

    border-radius: 18px;

    height: 64px;

    width: 100%;

    font-size: 18px;

    font-weight: 700;

    margin-top: 20px;

    box-shadow:
        0px 10px 20px rgba(74,144,226,0.25);

    transition: 0.3s;
}

.stButton button:hover {

    transform: translateY(-3px);

    box-shadow:
        0px 14px 30px rgba(74,144,226,0.35);
}

/* ============================================
SPACING
============================================ */

div[data-testid="column"] {

    padding-left: 12px;

    padding-right: 12px;
}

/* ============================================
DIVIDER
============================================ */

hr {

    margin-top: 35px;

    margin-bottom: 35px;

    border: none;

    border-top: 1px solid #edf2f7;
}

</style>
""", unsafe_allow_html=True)

# ============================================
# HERO SECTION
# ============================================

st.markdown("""

<div class="hero">

<div class="hero-title">
📄 Smart MRF Management
</div>

<div class="hero-sub">
Create intelligent manpower requisition forms
with AI-powered hiring assistance
</div>

</div>

""", unsafe_allow_html=True)

# ============================================
# METRICS
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
        "📋 Total MRF",
        total_mrf
    )

with m2:

    st.metric(
        "🟢 Open Positions",
        open_mrf
    )

with m3:

    st.metric(
        "🔴 Closed Positions",
        closed_mrf
    )

# ============================================
# FORM CONTAINER
# ============================================

st.markdown(
    '<div class="form-container">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">➕ Create Smart MRF</div>',
    unsafe_allow_html=True
)

# ============================================
# ROLE SELECTION
# ============================================

col1, col2 = st.columns(2)

with col1:

    position = st.selectbox(

        "Position Title",

        list(job_templates.keys())
    )

    selected_template = job_templates[position]

with col2:

    department = st.selectbox(

        "Department",

        [
            "Engineering",
            "HR",
            "Finance",
            "Operations",
            "Marketing",
            "Sales",
            "Design"
        ],

        index=[
            "Engineering",
            "HR",
            "Finance",
            "Operations",
            "Marketing",
            "Sales",
            "Design"
        ].index(
            selected_template["department"]
        )
    )

# ============================================
# AI SKILL SUGGESTION
# ============================================

st.info(
    f"💡 Suggested Skills: "
    f"{selected_template['skills']}"
)

# ============================================
# SECOND ROW
# ============================================

col3, col4 = st.columns(2)

with col3:

    branch = st.selectbox(
        "Branch",
        [
            "Bhubaneswar",
            "Berhampur",
            "Balasore",
            "Bangalore",
            "Hyderabad",
            "Pune"
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
# THIRD ROW
# ============================================

col5, col6 = st.columns(2)

with col5:

    vacancies = st.number_input(
        "No. of Vacancies",
        min_value=1,
        step=1
    )

with col6:

    work_mode = st.selectbox(

        "Work Mode",

        [
            "Remote",
            "Hybrid",
            "Onsite"
        ],

        index=[
            "Remote",
            "Hybrid",
            "Onsite"
        ].index(
            selected_template["mode"]
        )
    )

# ============================================
# FOURTH ROW
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

        value=selected_template["experience"]
    )

# ============================================
# REASON
# ============================================

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
# DESCRIPTION
# ============================================

description = st.text_area(

    "Job Description",

    value=selected_template["jd"],

    height=220
)

# ============================================
# FILE SAVE
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
    "🚀 Create Smart MRF"
)

# ============================================
# SAVE TO DATABASE
# ============================================

if create:

    cursor.execute("""
    INSERT INTO mrf_requests (

        position,
        department,
        branch,
        candidate_type,
        vacancies,
        reason,
        experience,
        work_mode,
        jd_file,
        description,
        status,
        created_date

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        position,
        department,
        branch,
        candidate_type,
        vacancies,
        reason,
        experience,
        work_mode,
        jd_path,
        description,
        "Open",
        datetime.now().strftime("%Y-%m-%d")

    ))

    conn.commit()

    st.success(
        "✅ Smart MRF Created Successfully!"
    )

    st.balloons()

st.markdown(
    '</div>',
    unsafe_allow_html=True
)