import streamlit as st
import pandas as pd

from utils.database import (
    fetch_deleted_candidates,
    restore_candidate,
    permanently_delete_candidate
)

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Deleted Candidates",
    page_icon="🗑",
    layout="wide"
)

# ============================================
# PREMIUM UI
# ============================================

st.markdown("""

<style>

.stApp {

    background:
        linear-gradient(
            135deg,
            #f5f7fb,
            #eef2ff
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

    position: relative;

    overflow: hidden;

    box-shadow:
        0px 14px 35px rgba(79,70,229,0.24);
}

.hero::after {

    content: "";

    position: absolute;

    top: -60px;

    right: -60px;

    width: 240px;

    height: 240px;

    background:
        rgba(255,255,255,0.08);

    border-radius: 50%;
}

.hero-title {

    font-size: 52px;

    font-weight: 800;

    margin-bottom: 12px;

    position: relative;

    z-index: 2;
}

.hero-sub {

    font-size: 18px;

    color: rgba(255,255,255,0.92);

    margin-bottom: 26px;

    max-width: 900px;

    line-height: 1.7;

    position: relative;

    z-index: 2;
}

.hero-badge {

    display: inline-block;

    padding: 12px 24px;

    border-radius: 18px;

    background:
        rgba(255,255,255,0.14);

    border:
        1px solid rgba(255,255,255,0.18);

    font-weight: 600;

    color: white;

    backdrop-filter:
        blur(10px);

    position: relative;

    z-index: 2;
}

/* ============================================
SEARCH
============================================ */

.stTextInput input {

    border-radius: 14px !important;

    border: 1px solid #dbe4ff !important;

    padding: 12px !important;
}

/* ============================================
CARDS
============================================ */

.card {

    background:
        rgba(255,255,255,0.80);

    backdrop-filter:
        blur(14px);

    padding:
        30px;

    border-radius:
        26px;

    margin-bottom:
        24px;

    border:
        1px solid rgba(255,255,255,0.50);

    box-shadow:
        0px 12px 28px rgba(0,0,0,0.05);
}

/* ============================================
BUTTONS
============================================ */

.stButton button {

    border-radius: 14px !important;

    border: none !important;

    font-weight: 700 !important;

    height: 44px !important;
}

</style>

""", unsafe_allow_html=True)

# ============================================
# HERO SECTION
# ============================================

st.markdown("""

<div class="hero">

<div class="hero-title">
🗑 Deleted Candidates
</div>

<div class="hero-sub">
Restore deleted candidate profiles,
review previous hiring records,
or permanently remove outdated resources
with enterprise ATS control.
</div>

<div class="hero-badge">
✨ ATS Recovery & Archive Dashboard
</div>

</div>

""", unsafe_allow_html=True)

# ============================================
# LOAD DATA
# ============================================

data = fetch_deleted_candidates()

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

    st.warning(
        "No deleted candidates found."
    )

    st.stop()

# ============================================
# SEARCH BAR
# ============================================

search = st.text_input(
    "🔍 Search Deleted Candidates"
)

if search:

    df = df[
        df["Name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# ============================================
# METRIC
# ============================================

st.metric(
    "🗑 Deleted Candidates",
    len(df)
)

st.divider()

# ============================================
# CANDIDATE CARDS
# ============================================

for _, row in df.iterrows():

    left, right = st.columns([4,1])

    # ========================================
    # LEFT SECTION
    # ========================================

    with left:

        st.subheader(
            row["Name"]
        )

        st.caption(
            row["Email"]
        )

        c1, c2, c3 = st.columns(3)

        with c1:

            st.write(
                f"💼 {row['Role']}"
            )

        with c2:

            st.write(
                f"📍 {row['Location']}"
            )

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

        st.info(
            f"Last Status: {row['Status']}"
        )

    # ========================================
    # RIGHT SECTION
    # ========================================

    with right:

        restore_btn = st.button(

            "♻ Restore",

            key=f"restore_{row['ID']}",

            use_container_width=True
        )

        if restore_btn:

            restore_candidate(
                row["ID"]
            )

            st.success(
                f"{row['Name']} restored successfully"
            )

            st.rerun()

        st.write("")

        delete_btn = st.button(

            "❌ Delete Permanently",

            key=f"permanent_{row['ID']}",

            use_container_width=True
        )

        if delete_btn:

            permanently_delete_candidate(
                row["ID"]
            )

            st.success(
                f"{row['Name']} permanently deleted"
            )

            st.rerun()

    st.divider()