import streamlit as st
import sqlite3
from utils.database import get_connection
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

.stApp {
    background: #f4f7fb;
}

.block-container {

    max-width: 1500px;

    padding-top: 2rem;

    padding-left: 4rem;

    padding-right: 4rem;

    padding-bottom: 4rem;
}

/* HEADER */

.main-title {

    font-size: 42px;

    font-weight: 800;

    color: #0f172a;

    margin-bottom: 8px;
}

.sub-title {

    font-size: 15px;

    color: #64748b;

    margin-bottom: 35px;
}

/* METRICS */

div[data-testid="metric-container"] {

    background: white;

    border-radius: 20px;

    padding: 24px;

    border: 1px solid #e2e8f0;

    box-shadow:
        0 8px 24px rgba(15,23,42,0.04);
}

/* FORM CARD */

.form-card {

    background: white;

    border-radius: 30px;

    padding: 50px;

    border: 1px solid #e2e8f0;

    box-shadow:
        0 18px 40px rgba(15,23,42,0.05);

    margin-top: 35px;
}

/* SECTION TITLE */

.section-title {

    font-size: 32px;

    font-weight: 700;

    color: #0f172a;

    margin-bottom: 40px;
}

/* LABELS */

label {

    font-size: 14px !important;

    font-weight: 700 !important;

    color: #334155 !important;
}

/* COLUMN SPACING */

div[data-testid="column"] {

    padding-left: 12px;

    padding-right: 12px;
}

/* INPUTS */

.stTextInput input,
.stSelectbox div[data-baseweb="select"] > div {

    background: white !important;

    border: 1px solid #dbe4ee !important;

    border-radius: 14px !important;

    height: 54px !important;

    padding-left: 16px !important;

    font-size: 15px !important;

    margin-bottom: 20px !important;
}

/* TEXTAREA */

.stTextArea textarea {

    background: white !important;

    border: 1px solid #dbe4ee !important;

    border-radius: 16px !important;

    min-height: 160px !important;

    padding: 16px !important;

    font-size: 15px !important;

    margin-bottom: 20px !important;
}

/* FOCUS */

.stTextInput input:focus,
.stTextArea textarea:focus {

    border: 1px solid #6366f1 !important;

    box-shadow:
        0 0 0 4px rgba(99,102,241,0.10) !important;
}

/* FILE */

[data-testid="stFileUploader"] {

    background: #f8fafc !important;

    border: 2px dashed #cbd5e1 !important;

    border-radius: 18px !important;

    padding: 25px !important;

    margin-top: 15px;
}

/* BUTTON */

.stButton button {

    width: 100%;

    height: 58px;

    border-radius: 16px;

    border: none !important;

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed
        ) !important;

    color: white !important;

    font-size: 16px !important;

    font-weight: 700 !important;

    margin-top: 15px;
}

</style>

""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""

<div class="main-title">
🚀 AABsys Talent Management
</div>

<div class="sub-title">
Professional ATS Candidate Management Dashboard
</div>

""", unsafe_allow_html=True)

# =====================================================
# METRICS
# =====================================================

cursor.execute("SELECT COUNT(*) FROM candidates")

total_candidates = cursor.fetchone()[0]

m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Total Candidates", total_candidates)

with m2:
    st.metric("Resume Support", "PDF / DOCX")

with m3:
    st.metric("ATS Status", "Active")

# =====================================================
# FORM CARD
# =====================================================

st.markdown('<div class="form-card">', unsafe_allow_html=True)

st.markdown("""

<div class="section-title">
➕ Add New Candidate
</div>

""", unsafe_allow_html=True)

# =====================================================
# FORM
# =====================================================

left, right = st.columns(2, gap="large")

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
            "Bangalore",
            "Hyderabad",
            "Remote"
        ]
    )

    status = st.selectbox(
        "Application Status",
        [
            "Applied",
            "HR Interview",
            "Technical Round",
            "Selected",
            "Rejected"
        ]
    )

# =====================================================
# RESUME UPLOAD
# =====================================================

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

resume_path = ""

if resume is not None:

    resume_path = f"resumes/{resume.name}"

    with open(resume_path, "wb") as f:
        f.write(resume.getbuffer())

# =====================================================
# SAVE BUTTON
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

st.markdown("</div>", unsafe_allow_html=True)