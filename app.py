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
# SESSION STATE REAL DATA
# =========================================================

if "candidate_data" not in st.session_state:

    st.session_state.candidate_data = pd.DataFrame({

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
            "2 Years",
            "3 Years",
            "1 Year",
            "4 Years",
            "2 Years"
        ],

        # REAL LOCATIONS FROM ADD CANDIDATE PAGE

        "Location": [
            "Bhubaneswar",
            "Berhampur",
            "Balasore",
            "Noida",
            "Remote"
        ]
    })

candidate_df = st.session_state.candidate_data

# =========================================================
# REAL MRF DATA
# =========================================================

if "mrf_data" not in st.session_state:

    st.session_state.mrf_data = pd.DataFrame({

        "Role": [
            "Business Analyst",
            "Data Analyst",
            "HR Executive",
            "Python Developer"
        ],

        "Branch": [
            "Bhubaneswar",
            "Berhampur",
            "Balasore",
            "Noida"
        ],

        "Status": [
            "Open",
            "Open",
            "Closed",
            "Open"
        ],

        "Vacancies": [
            2,
            1,
            1,
            3
        ]
    })

mrf_df = st.session_state.mrf_data

# =========================================================
# DASHBOARD COUNTS
# =========================================================

total_roles = len(mrf_df)

total_candidates = len(candidate_df)

applied_count = len(
    candidate_df[
        candidate_df["Status"] == "Applied"
    ]
)

interview_count = len(
    candidate_df[
        candidate_df["Status"].isin([
            "HR Interview",
            "Technical Round",
            "Final Round"
        ])
    ]
)

hired_count = len(
    candidate_df[
        candidate_df["Status"] == "Hired"
    ]
)

rejected_count = len(
    candidate_df[
        candidate_df["Status"] == "Rejected"
    ]
)

# =========================================================
# PREMIUM CSS
# =========================================================

st.markdown("""
<style>

.stApp {

    background:
        linear-gradient(
            135deg,
            #eef2ff 0%,
            #f8fbff 45%,
            #f3f4ff 100%
        );

    font-family:
        'Segoe UI', sans-serif;
}

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

.block-container {

    padding-top: 1rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;

    max-width: 1600px;
}

/* HERO */

.hero {

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed,
            #9333ea
        );

    border-radius: 36px;

    padding: 52px;

    color: white;

    position: relative;

    overflow: hidden;

    box-shadow:
        0px 28px 58px rgba(79,70,229,0.28);

    margin-bottom: 26px;
}

.hero::before {

    content: "";

    position: absolute;

    width: 320px;
    height: 320px;

    background:
        rgba(255,255,255,0.08);

    border-radius: 50%;

    top: -120px;
    right: -80px;
}

.hero-title {

    font-size: 56px;
    font-weight: 800;
    z-index: 2;
    position: relative;
}

.hero-sub {

    margin-top: 12px;

    font-size: 18px;

    line-height: 1.8;

    position: relative;

    z-index: 2;
}

.hero-badge {

    display: inline-block;

    margin-top: 24px;

    padding: 12px 24px;

    border-radius: 999px;

    background:
        rgba(255,255,255,0.14);

    border:
        1px solid rgba(255,255,255,0.16);

    backdrop-filter:
        blur(14px);

    font-size: 13px;

    font-weight: 700;
}

/* NAV BUTTONS */

.stButton > button {

    width: 100%;

    height: 72px;

    border-radius: 24px;

    border:
        1px solid rgba(255,255,255,0.48);

    background:
        rgba(255,255,255,0.72);

    backdrop-filter:
        blur(18px);

    font-size: 16px;

    font-weight: 700;

    color: #111827;

    transition: 0.35s ease;

    box-shadow:
        0px 10px 28px rgba(0,0,0,0.06);
}

.stButton > button:hover {

    transform:
        translateY(-5px);

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed
        );

    color: white;

    box-shadow:
        0px 20px 40px rgba(79,70,229,0.26);
}

/* GLASS BOX */

.glass-box {

    background:
        rgba(255,255,255,0.60);

    backdrop-filter:
        blur(18px);

    border:
        1px solid rgba(255,255,255,0.50);

    border-radius: 34px;

    padding: 34px;

    margin-top: 26px;

    box-shadow:
        0px 18px 42px rgba(0,0,0,0.05);
}

/* HEADINGS */

.section-heading {

    font-size: 40px;
    font-weight: 800;
    color: #111827;
}

.section-sub {

    color: #64748b;

    margin-top: 10px;

    margin-bottom: 24px;
}

/* METRIC CARDS */

.metric-card {

    padding: 28px;

    border-radius: 28px;

    color: white;

    box-shadow:
        0px 16px 34px rgba(0,0,0,0.08);
}

.metric-title {

    font-size: 15px;

    font-weight: 700;

    margin-bottom: 14px;
}

.metric-value {

    font-size: 46px;

    font-weight: 800;
}

.roles-card {
    background: linear-gradient(135deg,#2563eb,#60a5fa);
}

.candidate-card {
    background: linear-gradient(135deg,#7c3aed,#a855f7);
}

.applied-card {
    background: linear-gradient(135deg,#f59e0b,#fbbf24);
}

.interview-card {
    background: linear-gradient(135deg,#ec4899,#f472b6);
}

.hired-card {
    background: linear-gradient(135deg,#10b981,#34d399);
}

.rejected-card {
    background: linear-gradient(135deg,#ef4444,#f87171);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🚀 AABSys Talent Management
</div>

<div class="hero-sub">
AI Powered Recruitment, Candidate Tracking and
Workforce Management Platform with premium
enterprise analytics experience
</div>

<div class="hero-badge">
✨ Smart Hiring • AI ATS • Enterprise Dashboard
</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# NAVIGATION
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

# =========================================================
# DASHBOARD HEADER
# =========================================================

st.markdown("""
<div class="glass-box">

<div class="section-heading">
📊 Executive Hiring Dashboard
</div>

<div class="section-sub">
Track recruitment analytics, candidate conversion,
hiring pipeline and workforce growth through an
AI-powered premium ATS experience.
</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# METRICS
# =========================================================

c1, c2, c3, c4, c5, c6 = st.columns(6)

metric_data = [

    ("📋 Total Roles", total_roles, "roles-card"),
    ("👥 Candidates", total_candidates, "candidate-card"),
    ("📝 Applied", applied_count, "applied-card"),
    ("🎯 Interview", interview_count, "interview-card"),
    ("✅ Hired", hired_count, "hired-card"),
    ("❌ Rejected", rejected_count, "rejected-card")
]

for col, data in zip([c1,c2,c3,c4,c5,c6], metric_data):

    title, value, css = data

    with col:

        st.markdown(f"""
        <div class="metric-card {css}">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# PIPELINE DATAFRAME
# =========================================================

pipeline_df = pd.DataFrame({

    "Stage": [
        "📝 Applied",
        "🎯 HR Interview",
        "💻 Technical Round",
        "🏁 Final Round",
        "✅ Hired"
    ],

    "Candidate Count": [
        applied_count,
        len(candidate_df[candidate_df["Status"] == "HR Interview"]),
        len(candidate_df[candidate_df["Status"] == "Technical Round"]),
        len(candidate_df[candidate_df["Status"] == "Final Round"]),
        hired_count
    ],

    "Status": [
        "Waiting",
        "Active",
        "Ongoing",
        "Pending",
        "Completed"
    ]
})

st.markdown("""
<div class="glass-box">

<div class="section-heading">
🚀 Recruitment Pipeline
</div>

<div class="section-sub">
Track hiring stages and monitor candidate progress intelligently.
</div>

</div>
""", unsafe_allow_html=True)

st.dataframe(
    pipeline_df,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# RECENT CANDIDATES
# =========================================================

st.markdown("""
<div class="glass-box">

<div class="section-heading">
🧑‍💼 Recent Candidates
</div>

<div class="section-sub">
Update from Candidate profile
</div>

</div>
""", unsafe_allow_html=True)

display_df = candidate_df.copy()

display_df["Status"] = display_df["Status"].apply(

    lambda x:
    f"🟢 {x}" if x == "Hired"
    else f"🔴 {x}" if x == "Rejected"
    else f"🟣 {x}"
)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    height=320
)

# =========================================================
# FOOTER
# =========================================================

st.caption(
    "© 2026 AABSys Talent Management • AABsys ATS Dashboard"
)