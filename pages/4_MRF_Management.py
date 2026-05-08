import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="MRF Management",
    page_icon="📄",
    layout="wide"
)

# =========================================================
# SAMPLE DATA
# =========================================================

sample_mrfs = [

    {
        "position": "Data Analyst",
        "department": "Analytics",
        "branch": "Bhubaneswar",
        "type": "Experienced",
        "vacancies": 4,
        "reason": "New Position",
        "status": "Open",
        "priority": "High"
    },

    {
        "position": "Python Developer",
        "department": "Technology",
        "branch": "Berhampur",
        "type": "Fresher",
        "vacancies": 2,
        "reason": "Replacement",
        "status": "Closed",
        "priority": "Medium"
    },

    {
        "position": "UI/UX Designer",
        "department": "Design",
        "branch": "Balasore",
        "type": "Experienced",
        "vacancies": 1,
        "reason": "Expansion",
        "status": "Open",
        "priority": "Low"
    }
]

# =========================================================
# PREMIUM CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
GLOBAL
========================================================= */

.stApp {

    background:
        linear-gradient(
            135deg,
            #eef3f9,
            #f8fbff
        );

    font-family: 'Segoe UI', sans-serif;
}

/* =========================================================
CONTAINER
========================================================= */

.block-container {

    padding-top: 1rem !important;

    padding-left: 2.5rem !important;

    padding-right: 2.5rem !important;

    padding-bottom: 2rem !important;

    max-width: 1500px;
}

/* =========================================================
REMOVE STREAMLIT SPACE
========================================================= */

header {

    background: transparent !important;
}

div[data-testid="stDecoration"] {

    display: none !important;
}

/* =========================================================
REMOVE EMPTY WHITE BLOCKS
========================================================= */

div[data-testid="stVerticalBlock"] > div:empty {

    display: none !important;
}

/* =========================================================
HERO SECTION
========================================================= */

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

    margin-bottom: 28px;

    position: relative;

    overflow: hidden;

    box-shadow:
        0px 18px 40px rgba(79,70,229,0.24);
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

    bottom: -40px;

    left: -40px;

    width: 180px;

    height: 180px;

    background: rgba(255,255,255,0.05);

    border-radius: 50%;
}

.hero-title {

    font-size: 46px;

    font-weight: 800;

    margin-bottom: 12px;

    position: relative;

    z-index: 2;
}

.hero-sub {

    font-size: 17px;

    opacity: 0.96;

    line-height: 1.8;

    position: relative;

    z-index: 2;
}

/* =========================================================
PREMIUM BADGE
========================================================= */

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

/* =========================================================
METRIC CARDS
========================================================= */

[data-testid="metric-container"] {

    background:
        rgba(255,255,255,0.74);

    backdrop-filter:
        blur(14px);

    border-radius:
        24px;

    padding:
        26px;

    border:
        1px solid rgba(255,255,255,0.5);

    box-shadow:
        0px 10px 28px rgba(0,0,0,0.05);

    transition:
        0.3s;
}

[data-testid="metric-container"]:hover {

    transform:
        translateY(-5px);

    box-shadow:
        0px 20px 36px rgba(0,0,0,0.08);
}

/* =========================================================
SECTION TITLE
========================================================= */

.section-title {

    font-size: 34px;

    font-weight: 800;

    color: #111827;

    margin-top: 20px;

    margin-bottom: 20px;
}

/* =========================================================
SEARCH INPUT
========================================================= */

.stTextInput input {

    background:
        rgba(255,255,255,0.92) !important;

    border:
        1px solid #dbe4ee !important;

    border-radius:
        16px !important;

    height:
        56px !important;

    padding-left:
        18px !important;

    font-size:
        15px !important;

    box-shadow:
        none !important;
}

/* =========================================================
SELECTBOX
========================================================= */

.stSelectbox div[data-baseweb="select"] {

    background:
        rgba(255,255,255,0.92) !important;

    border:
        1px solid #dbe4ee !important;

    border-radius:
        16px !important;

    min-height:
        56px !important;

    box-shadow:
        none !important;
}

.stSelectbox div {

    background:
        transparent !important;
}

/* =========================================================
DROPDOWN
========================================================= */

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

/* =========================================================
OPTIONS
========================================================= */

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

/* =========================================================
CARDS
========================================================= */

.mrf-card {

    background:
        rgba(255,255,255,0.76);

    backdrop-filter:
        blur(14px);

    border-radius:
        26px;

    padding:
        32px;

    border:
        1px solid rgba(255,255,255,0.5);

    margin-bottom:
        26px;

    box-shadow:
        0px 12px 30px rgba(0,0,0,0.05);

    transition:
        0.3s;
}

.mrf-card:hover {

    transform:
        translateY(-6px);

    box-shadow:
        0px 22px 40px rgba(0,0,0,0.08);
}

/* =========================================================
STATUS BADGES
========================================================= */

.open-badge {

    background:
        linear-gradient(
            135deg,
            #dcfce7,
            #bbf7d0
        );

    color:
        #166534;

    padding:
        12px 20px;

    border-radius:
        14px;

    font-weight:
        700;

    text-align:
        center;

    box-shadow:
        0px 4px 12px rgba(34,197,94,0.18);
}

.closed-badge {

    background:
        linear-gradient(
            135deg,
            #fee2e2,
            #fecaca
        );

    color:
        #991b1b;

    padding:
        12px 20px;

    border-radius:
        14px;

    font-weight:
        700;

    text-align:
        center;

    box-shadow:
        0px 4px 12px rgba(239,68,68,0.18);
}

/* =========================================================
PRIORITY TAGS
========================================================= */

.high {

    background:
        linear-gradient(
            135deg,
            #fee2e2,
            #fecaca
        );

    color:
        #991b1b;

    padding:
        8px 16px;

    border-radius:
        12px;

    font-size:
        13px;

    font-weight:
        700;
}

.medium {

    background:
        linear-gradient(
            135deg,
            #fef3c7,
            #fde68a
        );

    color:
        #92400e;

    padding:
        8px 16px;

    border-radius:
        12px;

    font-size:
        13px;

    font-weight:
        700;
}

.low {

    background:
        linear-gradient(
            135deg,
            #dcfce7,
            #bbf7d0
        );

    color:
        #166534;

    padding:
        8px 16px;

    border-radius:
        12px;

    font-size:
        13px;

    font-weight:
        700;
}

/* =========================================================
BUTTON
========================================================= */

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
        54px;

    font-weight:
        700;

    transition:
        0.3s;

    box-shadow:
        0px 12px 26px rgba(79,70,229,0.24);
}

.stButton button:hover {

    transform:
        translateY(-3px);

    box-shadow:
        0px 20px 36px rgba(79,70,229,0.30);
}

/* =========================================================
REMOVE HR SPACE
========================================================= */

hr {

    display: none;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO
# =========================================================

st.markdown("""

<div class="hero">

<div class="hero-title">
📄 MRF Management
</div>

<div class="hero-sub">
Manage manpower requisition workflows with
smart recruitment tracking, hiring analytics
and premium ATS management experience
</div>

<div class="premium-badge">
✨ Enterprise Recruitment Dashboard
</div>

</div>

""", unsafe_allow_html=True)

# =========================================================
# METRICS
# =========================================================

total_mrf = len(sample_mrfs)

open_count = len(
    [
        x for x in sample_mrfs
        if x["status"] == "Open"
    ]
)

closed_count = len(
    [
        x for x in sample_mrfs
        if x["status"] == "Closed"
    ]
)

experienced_count = len(
    [
        x for x in sample_mrfs
        if x["type"] == "Experienced"
    ]
)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("📋 Total MRF", total_mrf)

with m2:
    st.metric("🟢 Open", open_count)

with m3:
    st.metric("🔴 Closed", closed_count)

with m4:
    st.metric("⭐ Experienced", experienced_count)

# =========================================================
# FILTERS
# =========================================================

st.markdown(
    '<div class="section-title">🔎 Filter MRF Records</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:

    type_filter = st.selectbox(
        "Candidate Type",
        [
            "All",
            "Fresher",
            "Experienced"
        ]
    )

with c2:

    status_filter = st.selectbox(
        "Status",
        [
            "All",
            "Open",
            "Closed"
        ]
    )

with c3:

    branch_filter = st.selectbox(
        "Branch",
        [
            "All",
            "Bhubaneswar",
            "Berhampur",
            "Balasore",
            "Noida"
        ]
    )

with c4:

    st.page_link(
        "pages/5_Create_MRF.py",
        label="➕ Create MRF",
        use_container_width=True
    )

# =========================================================
# SEARCH
# =========================================================

search = st.text_input(
    "🔍 Search Position"
)

# =========================================================
# FILTER
# =========================================================

filtered_mrfs = []

for mrf in sample_mrfs:

    if search.lower() not in mrf["position"].lower():
        continue

    if (
        type_filter != "All"
        and mrf["type"] != type_filter
    ):
        continue

    if (
        status_filter != "All"
        and mrf["status"] != status_filter
    ):
        continue

    if (
        branch_filter != "All"
        and mrf["branch"] != branch_filter
    ):
        continue

    filtered_mrfs.append(mrf)

# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="section-title">📋 MRF Records</div>',
    unsafe_allow_html=True
)

# =========================================================
# EMPTY
# =========================================================

if len(filtered_mrfs) == 0:

    st.info(
        "No MRF records found."
    )

# =========================================================
# CARDS
# =========================================================

for mrf in filtered_mrfs:

    st.markdown(
        '<div class="mrf-card">',
        unsafe_allow_html=True
    )

    top1, top2 = st.columns([4,1])

    with top1:

        st.markdown(
            f"## {mrf['position']}"
        )

        st.caption(
            f"{mrf['department']} • {mrf['branch']}"
        )

    with top2:

        if mrf["status"] == "Open":

            st.markdown(
                '<div class="open-badge">Open</div>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                '<div class="closed-badge">Closed</div>',
                unsafe_allow_html=True
            )

    st.write("")

    g1, g2, g3, g4, g5 = st.columns(5)

    with g1:

        st.write("Candidate Type")

        st.markdown(
            f"**{mrf['type']}**"
        )

    with g2:

        st.write("Vacancies")

        st.markdown(
            f"**{mrf['vacancies']}**"
        )

    with g3:

        st.write("Recruitment Reason")

        st.markdown(
            f"**{mrf['reason']}**"
        )

    with g4:

        st.write("Current Status")

        st.markdown(
            f"**{mrf['status']}**"
        )

    with g5:

        st.write("Priority")

        priority_class = mrf["priority"].lower()

        st.markdown(
            f'<span class="{priority_class}">{mrf["priority"]}</span>',
            unsafe_allow_html=True
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )