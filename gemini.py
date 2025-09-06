import streamlit as st
import pandas as pd
import numpy as np

# --- Page Configuration ---
st.set_page_config(page_title="agriIntel", layout="wide", initial_sidebar_state="collapsed")

# --- State Management ---
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- Styling ---
st.markdown("""
<style>
    /* --- Font Import & Base Reset --- */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&display=swap');
    
    html { scroll-behavior: smooth; }
    
    .stApp { padding: 0 !important; margin: 0 !important; }
    header[data-testid="stHeader"], footer[data-testid="stFooter"] { display: none !important; }

    body, .stApp {
        font-family: 'Inter', sans-serif;
        background-color: #000000;
        color: #E6E6E6;
    }

    /* --- Fixed Header --- */
    .fixed-header {
        position: fixed;
        top: 0.8rem;
        left: 50%;
        transform: translateX(-50%);
        width: auto;
        min-width: 300px;
        max-width: 90%;
        background-color: rgba(30, 30, 30, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        z-index: 1000;
        padding: 0.6rem 2rem;
        border-radius: 50px;
        box-shadow: 0 4px 25px rgba(0,0,0,0.2);
        border: 1px solid #333;
        display: flex;
        justify-content: space-between;
        align-items: center;
        white-space: nowrap;
        flex-wrap: nowrap;
    }
    
    .main .block-container {
        padding-top: 5.2rem !important;
    }

    .header-logo { 
        font-size: 1.9rem; 
        font-weight: 700; 
        margin-right: 1.5rem;
    }
    .nav-links a {
        color: #A3A3A3;
        text-decoration: none;
        margin: 0 1rem;
        font-weight: 500;
        transition: color 0.3s;
    }
    .nav-links a:hover { color: #FFFFFF; }

    /* Hero */
    .hero-section {
        text-align: center;
        padding: 3.5rem 0;
        position: relative;
    }
    .hero-section::before {
        content: '';
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        width: 800px; height: 800px;
        background: radial-gradient(circle, rgba(94, 4, 219, 0.2), transparent 70%);
        filter: blur(80px);
        z-index: 0;
    }
    .hero-content { position: relative; z-index: 1; }
    .brand-name {
        font-size: 5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        line-height: 1;
        color: #FFFFFF;
        letter-spacing: -2px;
        text-align: center;
        background: linear-gradient(90deg, #FF9C46, #FF408C, #9F5EFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1.5rem !important;
    }
    .title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        line-height: 1.1;
        color: #FFFFFF;
        letter-spacing: -1px;
        text-align: center;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #A3A3A3;
        margin-bottom: 2.5rem;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
    }

    .stButton>button {
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
        background: linear-gradient(90deg, #FF9C46, #FF408C, #9F5EFF);
        color: #FFFFFF;
        border: none;
        font-size: 1rem;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        background: linear-gradient(90deg, #FFA95A, #FF5599, #AB70FF);
        box-shadow: 0 0 15px rgba(159, 94, 255, 0.4);
    }

    /* About */
    .about-section { padding: 5rem 0; text-align: center; }
    .about-title { font-size: 3rem; font-weight: 700; margin-bottom: 2rem; color: #FFFFFF; }
    .about-body {
        font-size: 1.1rem; color: #A3A3A3; line-height: 1.8;
    }

    /* Dashboard */
    .dashboard-container { animation: fadeIn 0.5s ease-in-out; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }
    .dashboard-title { font-size: 3rem; font-weight: 700; color: #FFFFFF; }
    .kpi-card {
        background: #111;
        border: 1px solid #333;
        padding: 1.5rem;
        border-radius: 12px;
        height: 100%;
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }
    .kpi-card:hover { background-color: #1A1A1A; border-color: #555; }
    .kpi-title { font-size: 1rem; color: #A3A3A3; font-weight: 500; }
    .kpi-value { font-size: 2.2rem; font-weight: 700; color: #FFFFFF; }
    .kpi-delta { font-size: 0.9rem; font-weight: 600; color: #9F5EFF; }
    h3 {
        color: #FFFFFF;
        border-bottom: 1px solid #333;
        padding-bottom: 0.5rem;
        margin-top: 2rem !important;
    }
    hr { border-top: 1px solid #333; }
</style>
""", unsafe_allow_html=True)

# --- Page Switching Functions ---
def go_to_dashboard():
    st.session_state.page = "Dashboard"

def go_to_home():
    st.session_state.page = "Home"

# --- Header ---
st.markdown(
    """
    <div class="fixed-header">
        <div class="header-logo">agriIntel</div>
        <div class="nav-links">
            <a href="#" onclick="window.parent.postMessage({type: 'streamlit:setSessionState', state: {page: 'Home'}}, '*'); return false;">Home</a>
            <a href="#about-us">About Us</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Main App Logic ---
_, main_content_col, _ = st.columns([1, 8, 1])

with main_content_col:
    if st.session_state.page == "Home":
        st.markdown('<div id="home"></div>', unsafe_allow_html=True)

        st.markdown('<div class="hero-section">', unsafe_allow_html=True)
        st.markdown('<div class="hero-content">', unsafe_allow_html=True)

        # Added the agriIntel brand name with gradient styling
        st.markdown('<div class="brand-name">agriIntel</div>', unsafe_allow_html=True)
        st.markdown('<div class="title">AI-driven intelligence for modern agriculture</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">AgriIntel combines advanced analytics with agronomy to help you make sharper, greener decisions.</div>', unsafe_allow_html=True)
        
        _, btn_col_inner, _ = st.columns([1, 1, 1])
        with btn_col_inner:
            st.button("Explore the Dashboard", on_click=go_to_dashboard, key="home_dashboard_button", use_container_width=True)

        st.markdown('</div></div>', unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)

        st.markdown('<div id="about-us"></div>', unsafe_allow_html=True)
        st.markdown('<div class="about-section">', unsafe_allow_html=True)
        st.markdown('<div class="about-title">Our Mission</div>', unsafe_allow_html=True)
        st.markdown('<div class="about-body">Our goal is to make data-driven farming accessible to everyone. By providing clear, actionable intelligence, we help you make confident decisions that improve yields, reduce environmental impact, and secure a more profitable future for your farm.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.markdown('<div class="dashboard-container">', unsafe_allow_html=True)
        st.markdown('<div class="dashboard-title"> Prediction Dashboard</div>', unsafe_allow_html=True)

        st.button("← Back to Home", on_click=go_to_home)

        st.markdown("<hr>", unsafe_allow_html=True)

        st.markdown("### Key Metrics")
        kpi1, kpi2, kpi3 = st.columns(3)
        with kpi1:
            st.markdown('<div class="kpi-card"><div class="kpi-title">Predicted Yield</div><div class="kpi-value">8.2 T/Ha</div><div class="kpi-delta">+5.2% vs last season</div></div>', unsafe_allow_html=True)
        with kpi2:
            st.markdown('<div class="kpi-card"><div class="kpi-title">Optimal Harvest Window</div><div class="kpi-value">12 Days</div><div class="kpi-delta">Starts: Sept 18th</div></div>', unsafe_allow_html=True)
        with kpi3:
            st.markdown('<div class="kpi-card"><div class="kpi-title">Water Savings Potential</div><div class="kpi-value">25%</div><div class="kpi-delta">≈1.2M Gallons</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("### Yield Prediction Analysis")
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Nitrogen", "Phosphorus", "Potassium"])
        st.area_chart(chart_data)

        st.markdown('</div>', unsafe_allow_html=True)