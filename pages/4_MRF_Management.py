import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="MRF Management",
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
        "status": "Open"
    },

    {
        "position": "Python Developer",
        "department": "Technology",
        "branch": "Berhampur",
        "type": "Fresher",
        "vacancies": 2,
        "reason": "Replacement",
        "status": "Closed"
    },

    {
        "position": "UI/UX Designer",
        "department": "Design",
        "branch": "Balasore",
        "type": "Experienced",
        "vacancies": 1,
        "reason": "Expansion",
        "status": "Open"
    }
]

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
GLOBAL
========================================================= */

.stApp {
    background-color: #f4f7fb;
}

.block-container {

    padding-top: 1rem;

    padding-left: 2rem;

    padding-right: 2rem;

    padding-bottom: 2rem;
}

/* =========================================================
REMOVE STREAMLIT TOP SPACE
========================================================= */

header {
    background: transparent !important;
}

div[data-testid="stDecoration"] {
    display: none !important;
}

/* =========================================================
SEARCH BAR
========================================================= */

.stTextInput input {

    background: white !important;

    border: 1px solid #dbe4ee !important;

    border-radius: 14px !important;

    height: 52px !important;

    padding-left: 15px !important;

    font-size: 15px !important;
}

/* =========================================================
BUTTONS
========================================================= */

.stButton button {

    background: white;

    border: 1px solid #dbe4ee;

    border-radius: 12px;

    height: 50px;

    font-weight: 700;

    transition: 0.3s;
}

.stButton button:hover {

    border: 1px solid #4a90e2;

    color: #4a90e2;
}

/* =========================================================
METRIC CARDS
========================================================= */

[data-testid="metric-container"] {

    background: white;

    border: 1px solid #dbe4ee;

    padding: 15px;

    border-radius: 16px;

    box-shadow:
        0px 3px 10px rgba(0,0,0,0.04);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# PAGE TITLE
# =========================================================

st.title("📄 MRF Management")

st.caption(
    "Manage manpower requisition requests"
)

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

    st.metric(
        "Total MRF",
        total_mrf
    )

with m2:

    st.metric(
        "Open",
        open_count
    )

with m3:

    st.metric(
        "Closed",
        closed_count
    )

with m4:

    st.metric(
        "Experienced",
        experienced_count
    )

st.divider()

# =========================================================
# FILTER BUTTONS
# =========================================================

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
            "Balasore"
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
# FILTER DATA
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
# SECTION TITLE
# =========================================================

st.subheader("📋 MRF Records")

# =========================================================
# EMPTY STATE
# =========================================================

if len(filtered_mrfs) == 0:

    st.info(
        "No MRF records found."
    )

# =========================================================
# SHOW MRF CARDS
# =========================================================

for mrf in filtered_mrfs:

    with st.container():

        st.markdown("""
        <div style="
            background:white;
            padding:24px;
            border-radius:18px;
            border:1px solid #dbe4ee;
            margin-bottom:18px;
            box-shadow:0px 3px 10px rgba(0,0,0,0.04);
        ">
        """, unsafe_allow_html=True)

        top1, top2 = st.columns([4,1])

        # =================================================
        # LEFT
        # =================================================

        with top1:

            st.markdown(
                f"### {mrf['position']}"
            )

            st.caption(
                f"{mrf['department']} • {mrf['branch']}"
            )

        # =================================================
        # RIGHT
        # =================================================

        with top2:

            if mrf["status"] == "Open":

                st.success("Open")

            else:

                st.error("Closed")

        st.write("")

        g1, g2, g3, g4 = st.columns(4)

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

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )