import streamlit as st
import sqlite3
import os

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Add Candidate",
    page_icon="➕",
    layout="wide"
)

# ============================================
# CREATE RESUME FOLDER
# ============================================

if not os.path.exists("resumes"):

    os.makedirs("resumes")

# ============================================
# DATABASE CONNECTION
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
CREATE TABLE IF NOT EXISTS candidates (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    Name TEXT,

    Phone TEXT,

    Email TEXT,

    Role TEXT,

    Experience TEXT,

    Skills TEXT,

    PreviousCompany TEXT,

    CurrentSalary TEXT,

    ExpectedSalary TEXT,

    ReferredBy TEXT,

    EmployeeID TEXT,

    Qualification TEXT,

    Location TEXT,

    Status TEXT,

    Resume TEXT
)
""")

conn.commit()

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
REMOVE TOP SPACE
============================================ */

header {
    background: transparent !important;
}

div[data-testid="stDecoration"] {
    display: none !important;
}

.block-container {

    padding-top: 1rem !important;

    padding-left: 2rem !important;

    padding-right: 2rem !important;

    padding-bottom: 2rem !important;
}

/* ============================================
FORM CONTAINER
============================================ */

.form-container {

    background: white;

    padding: 30px;

    border-radius: 20px;

    border: 1px solid #d9e3ef;

    box-shadow:
        0 4px 18px rgba(0,0,0,0.05);

    margin-top: 20px;

    margin-bottom: 25px;
}

/* ============================================
LABELS
============================================ */

label {

    font-weight: 700 !important;

    color: #1e293b !important;

    font-size: 14px !important;
}

/* ============================================
TEXT INPUTS
============================================ */

.stTextInput input {

    background: white !important;

    border: 1px solid #d6dfeb !important;

    border-radius: 10px !important;

    height: 52px !important;

    padding-left: 15px !important;

    font-size: 15px !important;

    color: #0f172a !important;
}

/* ============================================
TEXT AREA
============================================ */

.stTextArea textarea {

    background: white !important;

    border: 1px solid #d6dfeb !important;

    border-radius: 10px !important;

    font-size: 15px !important;

    padding: 15px !important;

    color: #0f172a !important;
}

/* ============================================
SELECT BOX
============================================ */

.stSelectbox div[data-baseweb="select"] {

    background: white !important;

    border: 1px solid #d6dfeb !important;

    border-radius: 10px !important;

    min-height: 52px !important;
}

/* ============================================
FILE UPLOADER
============================================ */

[data-testid="stFileUploader"] {

    background: white;

    border: 1px solid #d6dfeb;

    border-radius: 14px;

    padding: 14px;
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

    height: 54px;

    width: 100%;

    font-size: 17px;

    font-weight: 700;

    transition: 0.3s;
}

.stButton button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 8px 18px rgba(74,144,226,0.25);
}

</style>
""", unsafe_allow_html=True)

# ============================================
# HEADER
# ============================================

st.title("🚀 AABsys Talent Management")

st.caption("Smart Hiring Dashboard")

# ============================================
# TOTAL CANDIDATES
# ============================================

cursor.execute(
    "SELECT COUNT(*) FROM candidates"
)

total_candidates = cursor.fetchone()[0]

# ============================================
# TOP METRICS
# ============================================

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Total Candidates",
        total_candidates
    )

with c2:

    st.metric(
        "Resume Support",
        "PDF / DOCX"
    )

with c3:

    st.metric(
        "ATS Status",
        "Active"
    )

# ============================================
# PAGE TITLE
# ============================================

st.subheader("➕ Add New Candidate")

# ============================================
# FORM CONTAINER
# ============================================

st.markdown(
    '<div class="form-container">',
    unsafe_allow_html=True
)

# ============================================
# FORM LAYOUT
# ============================================

col1, col2 = st.columns(2)

# ============================================
# LEFT COLUMN
# ============================================

with col1:

    candidate_name = st.text_input(
        "Candidate Full Name",
        placeholder="Enter candidate full name"
    )

    phone = st.text_input(
        "Phone Number",
        placeholder="Enter mobile number"
    )

    applied_role = st.text_input(
        "Applied Job Role",
        placeholder="Example: Data Analyst"
    )

    skills = st.text_area(
        "Skills / Technologies",
        placeholder="Python, SQL, Power BI, Excel...",
        height=100
    )

    current_salary = st.text_input(
        "Current Salary",
        placeholder="₹ Current salary"
    )

    referred_by = st.text_input(
        "Referred By",
        placeholder="Employee / Consultant Name"
    )

    qualification = st.text_input(
        "Highest Qualification",
        placeholder="MBA / B.Tech / MCA"
    )

# ============================================
# RIGHT COLUMN
# ============================================

with col2:

    email = st.text_input(
        "Email Address",
        placeholder="Enter email address"
    )

    experience = st.text_input(
        "Experience (Years)",
        placeholder="Example: 4 Years"
    )

    previous_company = st.text_input(
        "Previous Company",
        placeholder="Enter previous company"
    )

    expected_salary = st.text_input(
        "Expected Salary",
        placeholder="₹ Expected salary"
    )

    employee_id = st.text_input(
        "Employee ID",
        placeholder="Internal employee ID"
    )

    location = st.selectbox(
        "Preferred Work Location",
        [
            "Bhubaneswar",
            "Berhampur",
            "Balasore"
        ]
    )

# ============================================
# STATUS
# ============================================

status = st.selectbox(
    "Application Status",
    [
        "Applied",
        "HR Interview",
        "Technical Round",
        "Final Round",
        "Hired",
        "Rejected"
    ]
)

# ============================================
# RESUME UPLOAD
# ============================================

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

# ============================================
# SAVE BUTTON
# ============================================

if st.button("🚀 Save Candidate"):

    if candidate_name == "" or email == "":

        st.warning(
            "Please fill mandatory fields."
        )

    else:

        cursor.execute("""
        INSERT INTO candidates (

            Name,
            Phone,
            Email,
            Role,
            Experience,
            Skills,
            PreviousCompany,
            CurrentSalary,
            ExpectedSalary,
            ReferredBy,
            EmployeeID,
            Qualification,
            Location,
            Status,
            Resume

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (

            candidate_name,
            phone,
            email,
            applied_role,
            experience,
            skills,
            previous_company,
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
    '</div>',
    unsafe_allow_html=True
)