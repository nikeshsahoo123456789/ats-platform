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
# PREMIUM UI
# ============================================

st.markdown("""
<style>

/* ============================================
GLOBAL
============================================ */

.stApp {

    background:
        linear-gradient(
            135deg,
            #eef3f9,
            #f8fbff
        );

    font-family: 'Segoe UI', sans-serif;
}

/* ============================================
REMOVE TOP SPACE
============================================ */

.block-container {

    padding-top: 1rem !important;

    padding-bottom: 2rem !important;

    padding-left: 2.5rem !important;

    padding-right: 2.5rem !important;

    max-width: 1500px;
}

/* ============================================
REMOVE EMPTY WHITE BLOCKS
============================================ */

div[data-testid="stVerticalBlock"] > div:empty {

    display: none !important;
}

/* ============================================
REMOVE STREAMLIT SPACE
============================================ */

header {

    background: transparent !important;
}

div[data-testid="stDecoration"] {

    display: none !important;
}

/* ============================================
HERO SECTION
============================================ */

.hero {

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed
        );

    padding: 42px;

    border-radius: 30px;

    color: white;

    margin-bottom: 30px;

    box-shadow:
        0px 18px 40px rgba(79,70,229,0.24);

    position: relative;

    overflow: hidden;
}

.hero::before {

    content: "";

    position: absolute;

    top: -60px;

    right: -60px;

    width: 240px;

    height: 240px;

    background: rgba(255,255,255,0.08);

    border-radius: 50%;
}

.hero::after {

    content: "";

    position: absolute;

    bottom: -50px;

    left: -50px;

    width: 180px;

    height: 180px;

    background: rgba(255,255,255,0.05);

    border-radius: 50%;
}

.hero-title {

    font-size: 44px;

    font-weight: 800;

    margin-bottom: 12px;

    position: relative;

    z-index: 2;
}

.hero-sub {

    font-size: 16px;

    opacity: 0.96;

    line-height: 1.8;

    position: relative;

    z-index: 2;
}

/* ============================================
PREMIUM BADGE
============================================ */

.premium-badge {

    display: inline-block;

    margin-top: 18px;

    padding: 10px 18px;

    background: rgba(255,255,255,0.14);

    border: 1px solid rgba(255,255,255,0.18);

    backdrop-filter: blur(10px);

    border-radius: 999px;

    font-size: 13px;

    font-weight: 700;

    position: relative;

    z-index: 2;
}

/* ============================================
FORM CONTAINER
============================================ */

.form-container {

    background:
        rgba(255,255,255,0.76);

    backdrop-filter:
        blur(16px);

    padding:
        38px;

    border-radius:
        28px;

    border:
        1px solid rgba(255,255,255,0.45);

    box-shadow:
        0px 12px 32px rgba(0,0,0,0.05);

    margin-top:
        10px;
}

/* ============================================
SECTION TITLE
============================================ */

.section-title {

    font-size: 32px;

    font-weight: 800;

    color: #111827;

    margin-bottom: 28px;
}

/* ============================================
LABELS
============================================ */

label {

    color: #374151 !important;

    font-size: 14px !important;

    font-weight: 700 !important;
}

/* ============================================
INPUTS
============================================ */

.stTextInput input,
.stNumberInput input {

    background:
        rgba(255,255,255,0.92) !important;

    border:
        1px solid #dbe4ee !important;

    border-radius:
        14px !important;

    height:
        54px !important;

    padding-left:
        16px !important;

    font-size:
        15px !important;

    box-shadow:
        none !important;
}

/* ============================================
SELECTBOX
============================================ */

.stSelectbox div[data-baseweb="select"] {

    background:
        rgba(255,255,255,0.92) !important;

    border-radius:
        14px !important;

    border:
        1px solid #dbe4ee !important;

    min-height:
        54px !important;

    box-shadow:
        none !important;
}

.stSelectbox div {

    background:
        transparent !important;
}

/* ============================================
DROPDOWN
============================================ */

div[data-baseweb="popover"] {

    border-radius:
        18px !important;

    overflow:
        hidden !important;

    border:
        1px solid #e5e7eb !important;

    background:
        white !important;

    box-shadow:
        0px 16px 34px rgba(0,0,0,0.10) !important;
}

/* ============================================
OPTIONS
============================================ */

li {

    padding:
        14px !important;

    font-size:
        14px !important;
}

li:hover {

    background:
        #f3f0ff !important;

    color:
        #6d28d9 !important;
}

/* ============================================
TEXT AREA
============================================ */

.stTextArea textarea {

    background:
        rgba(255,255,255,0.92) !important;

    border-radius:
        16px !important;

    border:
        1px solid #dbe4ee !important;

    padding:
        18px !important;

    line-height:
        1.8 !important;

    font-size:
        14px !important;
}

/* ============================================
UPLOAD BOX
============================================ */

[data-testid="stFileUploader"] {

    border-radius:
        18px;

    border:
        2px dashed #dbe4ee;

    background:
        rgba(255,255,255,0.74);

    padding:
        18px;
}

/* ============================================
INFO BOX
============================================ */

[data-testid="stAlert"] {

    border-radius:
        16px;

    background:
        #eef2ff;

    border:
        none;
}

/* ============================================
BUTTON
============================================ */

.stButton button {

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed
        );

    color:
        white;

    border:
        none;

    border-radius:
        16px;

    height:
        56px;

    width:
        100%;

    font-size:
        16px;

    font-weight:
        700;

    transition:
        0.3s;

    box-shadow:
        0px 12px 28px rgba(79,70,229,0.26);
}

.stButton button:hover {

    transform:
        translateY(-3px);

    box-shadow:
        0px 20px 38px rgba(79,70,229,0.32);
}

/* ============================================
COLUMN SPACING
============================================ */

div[data-testid="column"] {

    padding-left: 8px;

    padding-right: 8px;
}

/* ============================================
REMOVE EXTRA GAPS
============================================ */

.element-container {

    margin-bottom: 0.5rem !important;
}

/* ============================================
REMOVE HORIZONTAL LINE SPACE
============================================ */

hr {

    display: none;
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
and premium recruitment workflow experience
</div>

<div class="premium-badge">
✨ Enterprise Hiring Workflow
</div>

</div>

""", unsafe_allow_html=True)

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
# FIRST ROW
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
# AI SKILLS
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
            "Noida"
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

    budget = st.text_input(
        "Salary Budget",
        placeholder="Example: 6 LPA - 9 LPA"
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

    priority = st.selectbox(

        "Hiring Priority",

        [
            "High",
            "Medium",
            "Low"
        ]
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

    joining_time = st.selectbox(

        "Expected Joining Timeline",

        [
            "Immediate",
            "15 Days",
            "30 Days",
            "60 Days"
        ]
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