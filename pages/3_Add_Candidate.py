import streamlit as st
import sqlite3
import os

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Add Candidate",
    page_icon="🚀",
    layout="wide"
)

# =====================================================
# CREATE RESUME FOLDER
# =====================================================

if not os.path.exists("resumes"):

    os.makedirs("resumes")

# =====================================================
# DATABASE CONNECTION
# =====================================================

conn = sqlite3.connect(
    "candidates.db",
    check_same_thread=False
)

cursor = conn.cursor()

# =====================================================
# PREMIUM CSS
# =====================================================

st.markdown("""

<style>

/* =====================================================
GLOBAL
===================================================== */

.stApp {

    background:
        linear-gradient(
            135deg,
            #eef3f9,
            #f8fbff
        );

    font-family: 'Segoe UI', sans-serif;
}

.block-container {

    max-width: 1500px;

    padding-top: 1rem !important;

    padding-left: 2.5rem !important;

    padding-right: 2.5rem !important;

    padding-bottom: 3rem !important;
}

/* =====================================================
REMOVE STREAMLIT SPACE
===================================================== */

header {

    background: transparent !important;
}

div[data-testid="stDecoration"] {

    display: none !important;
}

/* =====================================================
REMOVE EMPTY WHITE BLOCKS
===================================================== */

div[data-testid="stVerticalBlock"] > div:empty {

    display: none !important;
}

/* =====================================================
HERO SECTION
===================================================== */

.hero {

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed
        );

    padding: 38px;

    border-radius: 28px;

    color: white;

    margin-bottom: 28px;

    position: relative;

    overflow: hidden;

    box-shadow:
        0px 14px 35px rgba(79,70,229,0.24);
}

.hero::after {

    content: "";

    position: absolute;

    top: -50px;

    right: -50px;

    width: 220px;

    height: 220px;

    background: rgba(255,255,255,0.08);

    border-radius: 50%;
}

.hero-title {

    font-size: 42px;

    font-weight: 800;

    margin-bottom: 10px;
}

.hero-sub {

    font-size: 16px;

    opacity: 0.95;
}

/* =====================================================
METRICS
===================================================== */

div[data-testid="metric-container"] {

    background: rgba(255,255,255,0.72);

    backdrop-filter: blur(14px);

    border-radius: 22px;

    padding: 24px;

    border: 1px solid rgba(255,255,255,0.45);

    box-shadow:
        0px 10px 28px rgba(0,0,0,0.05);

    transition: 0.3s;
}

div[data-testid="metric-container"]:hover {

    transform: translateY(-4px);

    box-shadow:
        0px 18px 34px rgba(0,0,0,0.08);
}

/* =====================================================
FORM CARD
===================================================== */

.form-card {

    background: rgba(255,255,255,0.74);

    backdrop-filter: blur(16px);

    border-radius: 30px;

    padding: 42px;

    border: 1px solid rgba(255,255,255,0.45);

    box-shadow:
        0px 16px 40px rgba(0,0,0,0.05);

    margin-top: 18px;
}

/* =====================================================
SECTION TITLE
===================================================== */

.section-title {

    font-size: 34px;

    font-weight: 800;

    color: #0f172a;

    margin-bottom: 35px;
}

/* =====================================================
LABELS
===================================================== */

label {

    font-size: 14px !important;

    font-weight: 700 !important;

    color: #334155 !important;
}

/* =====================================================
COLUMN SPACING
===================================================== */

div[data-testid="column"] {

    padding-left: 10px;

    padding-right: 10px;
}

/* =====================================================
INPUTS
===================================================== */

.stTextInput input,
.stSelectbox div[data-baseweb="select"] {

    background:
        rgba(255,255,255,0.92) !important;

    border:
        1px solid #dbe4ee !important;

    border-radius:
        14px !important;

    min-height:
        54px !important;

    padding-left:
        16px !important;

    font-size:
        15px !important;

    box-shadow:
        none !important;

    transition:
        0.3s;
}

/* REMOVE INNER WHITE */

.stSelectbox div {

    background: transparent !important;
}

/* =====================================================
TEXT AREA
===================================================== */

.stTextArea textarea {

    background:
        rgba(255,255,255,0.92) !important;

    border:
        1px solid #dbe4ee !important;

    border-radius:
        16px !important;

    min-height:
        180px !important;

    padding:
        18px !important;

    font-size:
        15px !important;

    line-height:
        1.7 !important;

    box-shadow:
        none !important;
}

/* =====================================================
FOCUS EFFECT
===================================================== */

.stTextInput input:focus,
.stTextArea textarea:focus {

    border:
        1px solid #7c3aed !important;

    box-shadow:
        0 0 0 4px rgba(124,58,237,0.10) !important;
}

/* =====================================================
DROPDOWN
===================================================== */

div[data-baseweb="popover"] {

    border-radius: 16px !important;

    overflow: hidden !important;

    border: 1px solid #e5e7eb !important;

    background: white !important;

    box-shadow:
        0px 14px 30px rgba(0,0,0,0.10) !important;
}

/* =====================================================
OPTIONS
===================================================== */

li {

    padding: 13px !important;

    font-size: 14px !important;
}

li:hover {

    background: #f3f0ff !important;

    color: #6d28d9 !important;
}

/* =====================================================
FILE UPLOADER
===================================================== */

[data-testid="stFileUploader"] {

    background:
        rgba(255,255,255,0.74) !important;

    border:
        2px dashed #cbd5e1 !important;

    border-radius:
        20px !important;

    padding:
        25px !important;

    margin-top:
        15px;
}

/* =====================================================
BUTTON
===================================================== */

.stButton button {

    width: 100%;

    height: 60px;

    border-radius: 18px;

    border: none !important;

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed
        ) !important;

    color: white !important;

    font-size: 17px !important;

    font-weight: 700 !important;

    margin-top: 18px;

    transition: 0.3s;

    box-shadow:
        0px 12px 28px rgba(79,70,229,0.25);
}

.stButton button:hover {

    transform: translateY(-3px);

    box-shadow:
        0px 18px 34px rgba(79,70,229,0.32);
}

/* =====================================================
BADGE
===================================================== */

.premium-badge {

    display: inline-block;

    padding: 8px 16px;

    background: rgba(255,255,255,0.16);

    border-radius: 999px;

    font-size: 13px;

    font-weight: 700;

    margin-top: 10px;
}

/* =====================================================
REMOVE HR SPACE
===================================================== */

hr {

    display: none;
}

</style>

""", unsafe_allow_html=True)

# =====================================================
# HERO HEADER
# =====================================================

st.markdown("""

<div class="hero">

<div class="hero-title">
🚀 Add New Candidate
</div>

<div class="hero-sub">
Create and manage candidate profiles with
premium ATS recruitment workflow
</div>

<div class="premium-badge">
✨ Smart Candidate Onboarding
</div>

</div>

""", unsafe_allow_html=True)

# =====================================================
# METRICS
# =====================================================

cursor.execute(
    "SELECT COUNT(*) FROM candidates"
)

total_candidates = cursor.fetchone()[0]

m1, m2, m3 = st.columns(3)

with m1:

    st.metric(
        "👥 Total Candidates",
        total_candidates
    )

with m2:

    st.metric(
        "📄 Resume Support",
        "PDF / DOCX"
    )

with m3:

    st.metric(
        "🟢 ATS Status",
        "Active"
    )

# =====================================================
# FORM CARD
# =====================================================

st.markdown(
    '<div class="form-card">',
    unsafe_allow_html=True
)

st.markdown("""

<div class="section-title">
➕ Add New Candidate
</div>

""", unsafe_allow_html=True)

# =====================================================
# FORM
# =====================================================

left, right = st.columns(
    2,
    gap="large"
)

# =====================================================
# LEFT SIDE
# =====================================================

with left:

    candidate_name = st.text_input(
        "Candidate Full Name"
    )

    applied_role = st.text_input(
        "Applied Job Role"
    )

    skills = st.text_area(
        "Skills / Technologies"
    )

    current_salary = st.text_input(
        "Current Salary"
    )

    referred_by = st.text_input(
        "Referred By"
    )

    qualification = st.text_input(
        "Highest Qualification"
    )

# =====================================================
# RIGHT SIDE
# =====================================================

with right:

    email = st.text_input(
        "Email Address"
    )

    experience = st.text_input(
        "Experience (Years)"
    )

    expected_salary = st.text_input(
        "Expected Salary"
    )

    employee_id = st.text_input(
        "Employee ID"
    )

    location = st.selectbox(
        "Preferred Work Location",
        [
            "Bhubaneswar",
            "Berhampur",
            "Balasore",
            "Noida",
            "Remote"
        ]
    )

    status = st.selectbox(
        "Application Status",
        [
            "Applied",
            "HR Interview",
            "Technical Round",
            "Final Round",
            "Hold",
            "Selected",
            "Rejected"
        ]
    )

# =====================================================
# EXTRA PREMIUM FEATURES
# =====================================================

extra1, extra2 = st.columns(2)

with extra1:

    priority = st.selectbox(

        "Candidate Priority",

        [
            "High",
            "Medium",
            "Low"
        ]
    )

with extra2:

    source = st.selectbox(

        "Candidate Source",

        [
            "LinkedIn",
            "Naukri",
            "Referral",
            "Walk-In",
            "Company Website"
        ]
    )

# =====================================================
# RESUME
# =====================================================

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

resume_path = ""

if resume is not None:

    resume_path = f"resumes/{resume.name}"

    with open(resume_path, "wb") as f:

        f.write(
            resume.getbuffer()
        )

# =====================================================
# SAVE
# =====================================================

if st.button("💾 Save Candidate"):

    if candidate_name == "" or email == "":

        st.warning(
            "Please fill mandatory fields."
        )

    else:

        cursor.execute("""

        INSERT INTO candidates (

            Name,
            Email,
            Role,
            Experience,
            Skills,
            CurrentSalary,
            ExpectedSalary,
            ReferredBy,
            EmployeeID,
            Qualification,
            Location,
            Status,
            Resume

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

        """, (

            candidate_name,
            email,
            applied_role,
            experience,
            skills,
            current_salary,
            expected_salary,
            referred_by,
            employee_id,
            qualification,
            location,
            status,
            resume_path

        ))

        conn.commit()

        st.success(
            "✅ Candidate added successfully!"
        )

        st.balloons()

st.markdown(
    "</div>",
    unsafe_allow_html=True
)