import streamlit as st

# ============================================
# TOP NAVIGATION
# ============================================

def show_navigation():

    st.markdown("""
    <style>

    .navigation-wrapper {
        margin-top: 10px;
        margin-bottom: 25px;
    }

    .stPageLink {
        width: 100% !important;
    }

    .stPageLink a {

        display: flex !important;

        align-items: center !important;

        justify-content: center !important;

        width: 100% !important;

        min-height: 60px !important;

        background: white !important;

        border-radius: 14px !important;

        border: 1px solid #dbe4ee !important;

        text-decoration: none !important;

        color: #1e293b !important;

        font-size: 18px !important;

        font-weight: 600 !important;

        box-shadow:
            0px 2px 6px rgba(0,0,0,0.04);

        transition: all 0.25s ease-in-out !important;

        cursor: pointer !important;
    }

    .stPageLink a p {
        margin: 0 !important;
        padding: 0 !important;
        text-decoration: none !important;
    }

    .stPageLink a:hover {

        transform: translateY(-2px);

        border: 1px solid #4a90e2 !important;

        color: #4a90e2 !important;

        box-shadow:
            0px 8px 18px rgba(74,144,226,0.15);
    }

    .stPageLink a:active {
        transform: scale(0.98);
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="navigation-wrapper">',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    # ============================================
    # DASHBOARD
    # ============================================

    with col1:

        st.page_link(
            "app.py",
            label="📊 Dashboard",
            use_container_width=True
        )

    # ============================================
    # CANDIDATES
    # ============================================

    with col2:

        st.page_link(
            "pages/2_Candidates.py",
            label="👥 Candidates",
            use_container_width=True
        )

    # ============================================
    # ADD CANDIDATE
    # ============================================

    with col3:

        st.page_link(
            "pages/3_Add_Candidate.py",
            label="➕ Add Candidate",
            use_container_width=True
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )