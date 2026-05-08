import streamlit as st
import pandas as pd
import os

from utils.database import (
    fetch_all,
    get_connection,
    create_tables
)

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Candidates",
    page_icon="👥",
    layout="wide"
)

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
REMOVE STREAMLIT SPACE
============================================ */

header {

    background: transparent !important;
}

div[data-testid="stDecoration"] {

    display: none !important;
}

/* ============================================
MAIN CONTAINER
============================================ */

.block-container {

    max-width: 1500px;

    padding-top: 1rem !important;

    padding-left: 2.5rem !important;

    padding-right: 2.5rem !important;

    padding-bottom: 3rem !important;
}

/* ============================================
REMOVE EMPTY BLOCKS
============================================ */

div[data-testid="stVerticalBlock"] > div:empty {

    display: none !important;
}

/* ============================================
HERO
============================================ */

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

    line-height: 1.7;
}

/* ============================================
PREMIUM BADGE
============================================ */

.premium-badge {

    display: inline-block;

    padding: 8px 16px;

    background: rgba(255,255,255,0.16);

    border-radius: 999px;

    font-size: 13px;

    font-weight: 700;

    margin-top: 14px;
}

/* ============================================
METRIC CARDS
============================================ */

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

/* ============================================
SEARCH + FILTERS
============================================ */

.stTextInput input,
.stSelectbox div[data-baseweb="select"] {

    background:
        rgba(255,255,255,0.92) !important;

    border:
        1px solid #dbe4ee !important;

    border-radius:
        14px !important;

    min-height:
        52px !important;

    padding-left:
        16px !important;

    font-size:
        15px !important;

    box-shadow:
        none !important;
}

.stSelectbox div {

    background: transparent !important;
}

/* ============================================
DROPDOWN
============================================ */

div[data-baseweb="popover"] {

    border-radius: 16px !important;

    overflow: hidden !important;

    border: 1px solid #e5e7eb !important;

    background: white !important;

    box-shadow:
        0px 14px 30px rgba(0,0,0,0.10) !important;
}

/* ============================================
OPTIONS
============================================ */

li {

    padding: 13px !important;

    font-size: 14px !important;
}

li:hover {

    background: #f3f0ff !important;

    color: #6d28d9 !important;
}

/* ============================================
TEXT AREA
============================================ */

.stTextArea textarea {

    background:
        rgba(255,255,255,0.92) !important;

    border:
        1px solid #dbe4ee !important;

    border-radius:
        16px !important;

    padding:
        18px !important;

    font-size:
        15px !important;

    line-height:
        1.7 !important;
}

/* ============================================
SLIDER
============================================ */

.stSlider {

    padding-top: 10px;
}

/* ============================================
BUTTON
============================================ */

.stButton button {

    border-radius: 14px !important;

    border: none !important;

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed
        ) !important;

    color: white !important;

    font-weight: 700 !important;

    transition: 0.3s;

    box-shadow:
        0px 10px 24px rgba(79,70,229,0.25);
}

.stButton button:hover {

    transform: translateY(-2px);

    box-shadow:
        0px 18px 34px rgba(79,70,229,0.32);
}

/* ============================================
DELETE BUTTON
============================================ */

div[data-testid="stButton"] button[kind="secondary"] {

    background:
        linear-gradient(
            135deg,
            #ef4444,
            #dc2626
        ) !important;

    color: white !important;

    box-shadow:
        0px 10px 24px rgba(239,68,68,0.25);
}

/* ============================================
CANDIDATE CARD
============================================ */

.candidate-card {

    background:
        rgba(255,255,255,0.76);

    backdrop-filter:
        blur(14px);

    padding:
        28px;

    border-radius:
        24px;

    border:
        1px solid rgba(255,255,255,0.45);

    margin-bottom:
        24px;

    box-shadow:
        0px 12px 28px rgba(0,0,0,0.05);

    transition:
        0.3s;
}

.candidate-card:hover {

    transform:
        translateY(-4px);

    box-shadow:
        0px 20px 36px rgba(0,0,0,0.08);
}

/* ============================================
STATUS PILLS
============================================ */

.status-pill {

    display: inline-block;

    padding: 7px 14px;

    border-radius: 999px;

    font-size: 12px;

    font-weight: 700;

    margin-top: 6px;
}

.status-hired {

    background: #dcfce7;
    color: #166534;
}

.status-hold {

    background: #fef3c7;
    color: #92400e;
}

.status-rejected {

    background: #fee2e2;
    color: #991b1b;
}

.status-progress {

    background: #ede9fe;
    color: #5b21b6;
}

hr {

    display: none;
}

</style>

""", unsafe_allow_html=True)

# ============================================
# DATABASE CONNECTION
# ============================================

conn = get_connection()

create_tables()

# ============================================
# UPDATE STATUS FUNCTION
# ============================================

def update_status(candidate_id, new_status):

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE candidates
        SET Status = ?
        WHERE id = ?
        """,
        (new_status, candidate_id)
    )

    conn.commit()

# ============================================
# REMOVE CANDIDATE FUNCTION
# ============================================

def remove_candidate(candidate_id):

    cursor = conn.cursor()

    # ========================================
    # GET CANDIDATE DATA
    # ========================================

    cursor.execute(

        """
        SELECT *
        FROM candidates
        WHERE id = ?
        """,

        (candidate_id,)
    )

    candidate = cursor.fetchone()

    # ========================================
    # SAVE TO DELETED CANDIDATES
    # ========================================

    if candidate:

        cursor.execute(

            """
            INSERT INTO deleted_candidates (

                original_id,
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

            VALUES (

                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?

            )
            """,

            (

                candidate[0],
                candidate[1],
                candidate[2],
                candidate[3],
                candidate[4],
                candidate[5],
                candidate[6],
                candidate[7],
                candidate[8],
                candidate[9],
                candidate[10],
                candidate[11],
                candidate[12],
                candidate[13]

            )
        )

    # ========================================
    # DELETE FROM MAIN TABLE
    # ========================================

    cursor.execute(

        """
        DELETE FROM candidates
        WHERE id = ?
        """,

        (candidate_id,)
    )

    conn.commit()

# ============================================
# HERO
# ============================================

st.markdown("""

<div class="hero">

<div class="hero-title">
👥 Candidate Management
</div>

<div class="hero-sub">
Manage candidate profiles, interview pipelines,
hiring stages and recruiter collaboration
with premium ATS workflow experience
</div>

<div class="premium-badge">
✨ Smart Recruitment Dashboard
</div>

</div>

""", unsafe_allow_html=True)

# ============================================
# LOAD DATA
# ============================================

data = fetch_all()

columns = [
    "ID",
    "Name",
    "Email",
    "Role",
    "Experience",
    "Skills",
    "CurrentSalary",
    "ExpectedSalary",
    "ReferredBy",
    "EmployeeID",
    "Qualification",
    "Location",
    "Status",
    "Resume"
]

df = pd.DataFrame(
    data,
    columns=columns
)

# ============================================
# EMPTY STATE
# ============================================

if df.empty:

    st.info("No candidates available.")

    st.stop()

# ============================================
# METRICS
# ============================================

total_candidates = len(df)

hired_count = len(
    df[df["Status"] == "Hired"]
)

interview_count = len(
    df[
        df["Status"].isin([
            "HR Interview",
            "Technical Round",
            "Final Round",
            "Hold"
        ])
    ]
)

rejected_count = len(
    df[df["Status"] == "Rejected"]
)

hold_count = len(
    df[df["Status"] == "Hold"]
)

final_round_count = len(
    df[df["Status"] == "Final Round"]
)

m1, m2, m3, m4, m5, m6 = st.columns(6)

with m1:
    st.metric("👥 Candidates", total_candidates)

with m2:
    st.metric("🎯 Interviews", interview_count)

with m3:
    st.metric("⏸ On Hold", hold_count)

with m4:
    st.metric("🏁 Final Round", final_round_count)

with m5:
    st.metric("✅ Hired", hired_count)

with m6:
    st.metric("❌ Rejected", rejected_count)

st.divider()

# ============================================
# FILTERS
# ============================================

c1, c2, c3 = st.columns(3)

with c1:

    search = st.text_input(
        "🔍 Search Candidate"
    )

with c2:

    role_filter = st.selectbox(
        "💼 Filter Role",
        ["All"] + sorted(
            df["Role"]
            .dropna()
            .unique()
            .tolist()
        )
    )

with c3:

    status_filter = st.selectbox(
        "📌 Filter Status",
        ["All"] + sorted(
            df["Status"]
            .dropna()
            .unique()
            .tolist()
        )
    )

# ============================================
# APPLY FILTERS
# ============================================

if search:

    df = df[
        df["Name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

if role_filter != "All":

    df = df[
        df["Role"] == role_filter
    ]

if status_filter != "All":

    df = df[
        df["Status"] == status_filter
    ]

# ============================================
# STATUS OPTIONS
# ============================================

status_options = [

    "Applied",
    "HR Interview",
    "Technical Round",
    "Final Round",
    "Hold",
    "Hired",
    "Rejected"
]

status_colors = {

    "Applied": "🟡",
    "HR Interview": "🔵",
    "Technical Round": "🟣",
    "Final Round": "🟠",
    "Hold": "🟤",
    "Hired": "🟢",
    "Rejected": "🔴"
}

# ============================================
# NO RESULTS
# ============================================

if df.empty:

    st.warning("No matching candidates found.")

# ============================================
# CANDIDATE CARDS
# ============================================

else:

    for _, row in df.iterrows():

        st.markdown(
            '<div class="candidate-card">',
            unsafe_allow_html=True
        )

        top1, top2 = st.columns([4,1])

        with top1:

            st.markdown(
                f"### {row['Name']}"
            )

            st.caption(
                f"Candidate ID: {row['ID']}"
            )

            st.caption(
                row["Email"]
            )

            c1, c2, c3 = st.columns(3)

            with c1:
                st.write(f"💼 {row['Role']}")

            with c2:
                st.write(f"📍 {row['Location']}")

            with c3:
                st.write(f"🎓 {row['Qualification']}")

            st.write(
                f"🛠 Skills: {row['Skills']}"
            )

            st.write(
                f"📈 Experience: {row['Experience']} yrs"
            )

            current_status = row["Status"]

            icon = status_colors.get(
                current_status,
                "⚪"
            )

            status_class = "status-progress"

            if current_status == "Hired":

                status_class = "status-hired"

            elif current_status == "Rejected":

                status_class = "status-rejected"

            elif current_status == "Hold":

                status_class = "status-hold"

            st.markdown(

                f"""
                <div class="status-pill {status_class}">
                {icon} {current_status}
                </div>
                """,

                unsafe_allow_html=True
            )

            st.markdown("---")

            st.markdown("### 📝 Reviewer Notes")

            review = st.text_area(

                "Add feedback about candidate",

                key=f"review_{row['ID']}",

                height=120
            )

            rating = st.slider(

                "⭐ Candidate Rating",

                1,
                5,
                3,

                key=f"rating_{row['ID']}"
            )

            if rating <= 2:

                st.error(
                    f"🔴 Low Recommendation ({rating}/5)"
                )

            elif rating == 3:

                st.warning(
                    f"🟡 Average Candidate ({rating}/5)"
                )

            else:

                st.success(
                    f"🟢 Strong Candidate ({rating}/5)"
                )

            st.markdown("---")

            resume_path = row["Resume"]

            if (
                isinstance(resume_path, str)
                and resume_path != ""
                and os.path.exists(resume_path)
            ):

                with open(resume_path, "rb") as file:

                    st.download_button(

                        label="📄 Download Resume",

                        data=file,

                        file_name=os.path.basename(
                            resume_path
                        ),

                        mime="application/octet-stream",

                        key=f"d{row['ID']}"
                    )

        with top2:

            current = row["Status"]

            if current not in status_options:

                current = "Applied"

            new_status = st.selectbox(

                "Status",

                status_options,

                index=status_options.index(current),

                key=f"s{row['ID']}"
            )

            st.write("")

            if new_status != row["Status"]:

                update_status(
                    row["ID"],
                    new_status
                )

                st.success("Updated")

                st.rerun()

            st.write("")
            st.write("")

            delete_candidate = st.button(

                "🗑 Delete Candidate",

                key=f"delete_{row['ID']}",

                use_container_width=True
            )

            if delete_candidate:

                remove_candidate(
                    row["ID"]
                )

                st.success(
                    f"{row['Name']} deleted successfully"
                )

                st.rerun()

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )