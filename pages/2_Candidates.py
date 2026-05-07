import streamlit as st
import pandas as pd
import os

from utils.database import (
    fetch_all,
    get_connection
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
# DATABASE CONNECTION
# ============================================

conn = get_connection()

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
# PAGE TITLE
# ============================================

st.title("👥 Candidate Management")

st.write(
    "Manage candidate profiles and recruitment pipeline"
)

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
            "Final Round"
        ])
    ]
)

rejected_count = len(
    df[df["Status"] == "Rejected"]
)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Candidates", total_candidates)

with m2:
    st.metric("Interview", interview_count)

with m3:
    st.metric("Hired", hired_count)

with m4:
    st.metric("Rejected", rejected_count)

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
    "Hired",
    "Rejected"
]

status_colors = {

    "Applied": "🟡",
    "HR Interview": "🔵",
    "Technical Round": "🟣",
    "Final Round": "🟠",
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

        st.markdown("""
        <div style="
            background:white;
            padding:24px;
            border-radius:18px;
            border:1px solid #e5e7eb;
            margin-bottom:18px;
            box-shadow:0px 2px 10px rgba(0,0,0,0.05);
        ">
        """, unsafe_allow_html=True)

        top1, top2 = st.columns([4,1])

        # ====================================
        # LEFT
        # ====================================

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
                st.write(
                    f"🎓 {row['Qualification']}"
                )

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

            st.write(
                f"{icon} Current Status: {current_status}"
            )

            # ====================================
            # RESUME
            # ====================================

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

            else:

                st.caption(
                    "No resume uploaded"
                )

        # ====================================
        # RIGHT
        # ====================================

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

            st.markdown("<br>", unsafe_allow_html=True)

            if new_status != row["Status"]:

                update_status(
                    row["ID"],
                    new_status
                )

                st.success("Updated")

                st.rerun()

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )