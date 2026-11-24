
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cosmic Explorer | Mission Control",
    page_icon="🚀",
    layout="wide"
)

# =========================
# CUSTOM GALAXY CSS
# =========================

st.markdown("""
<style>

/* Main background */
.stApp {
    background:
        radial-gradient(ellipse at 20% 20%, #25145c 0%, transparent 45%),
        radial-gradient(ellipse at 80% 70%, #102b58 0%, transparent 45%),
        linear-gradient(135deg, #030712, #090d24, #11102d);
    color: white;
}

/* Hide Streamlit default elements */
#MainMenu, footer, header {
    visibility: hidden;
}

/* Animated stars */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    background-image:
        radial-gradient(2px 2px at 20% 30%, white, transparent),
        radial-gradient(2px 2px at 80% 20%, #8be9fd, transparent),
        radial-gradient(2px 2px at 50% 80%, white, transparent),
        radial-gradient(1px 1px at 70% 60%, white, transparent),
        radial-gradient(2px 2px at 10% 90%, #c4b5fd, transparent);
    background-size: 350px 350px;
    animation: stars 20s linear infinite;
}

@keyframes stars {
    from { transform: translateY(0); }
    to { transform: translateY(-350px); }
}

/* Main title */
.hero {
    text-align: center;
    padding: 55px 20px 25px;
    position: relative;
}

.hero h1 {
    font-size: 55px;
    font-weight: 900;
    letter-spacing: 5px;
    background: linear-gradient(90deg, #67e8f9, #a78bfa, #f0abfc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 35px rgba(103,232,249,0.2);
}

.hero p {
    color: #a5b4fc;
    font-size: 16px;
    letter-spacing: 4px;
}

/* Glass cards */
.glass {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(147,197,253,0.25);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(15px);
    box-shadow: 0 0 30px rgba(59,130,246,0.12);
    transition: 0.4s;
}

.glass:hover {
    border-color: #67e8f9;
    box-shadow: 0 0 35px rgba(103,232,249,0.3);
    transform: translateY(-5px);
}

/* Planet */
.planet {
    width: 130px;
    height: 130px;
    margin: 20px auto;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%,
        #c4b5fd, #7c3aed 40%, #1e1b4b 80%);
    box-shadow: 0 0 45px #8b5cf6,
                inset -15px -10px 30px #090b24;
    animation: float 5s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-18px); }
}

/* Glowing buttons */
.stButton > button {
    width: 100%;
    border: 1px solid #67e8f9;
    border-radius: 12px;
    background: linear-gradient(90deg, #312e81, #6d28d9);
    color: white;
    font-weight: bold;
    padding: 15px;
    transition: 0.3s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #0891b2, #7c3aed);
    box-shadow: 0 0 25px #67e8f9;
    border-color: white;
    transform: scale(1.03);
    color: white;
}

/* Other text */
h2, h3 {
    color: #c4b5fd !important;
}

</style>
""", unsafe_allow_html=True)


# =========================
# HERO SECTION
# =========================

st.markdown("""
<div class="hero">
    <div style="font-size:55px;">🚀</div>
    <h1>COSMIC EXPLORER</h1>
    <p>BEYOND THE LIMITS • INTO THE UNKNOWN</p>
</div>
""", unsafe_allow_html=True)


# =========================
# PLANET SECTION
# =========================

st.markdown("""
<div class="planet"></div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; color:#94a3b8;
            letter-spacing:3px; font-size:12px;">
    SYSTEM STATUS: ALL SYSTEMS OPERATIONAL
</div>
""", unsafe_allow_html=True)

st.write("")


# =========================
# MISSION DASHBOARD
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="glass">
        <h3>🌍 LOCATION</h3>
        <h2>EARTH ORBIT</h2>
        <p style="color:#94a3b8;">Mission starting point</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass">
        <h3>🛰️ MISSION</h3>
        <h2>EXPLORATION</h2>
        <p style="color:#94a3b8;">Discover the unknown</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="glass">
        <h3>⚡ STATUS</h3>
        <h2 style="color:#4ade80;">READY</h2>
        <p style="color:#94a3b8;">Awaiting command</p>
    </div>
    """, unsafe_allow_html=True)


st.write("")
st.write("")


# =========================
# INTERACTIVE SECTION
# =========================

st.markdown("""
<div style="text-align:center;">
    <h2>🧑‍🚀 MISSION COMMAND CENTER</h2>
    <p style="color:#94a3b8;">
        Your journey into the galaxy begins here.
    </p>
</div>
""", unsafe_allow_html=True)

_, center, _ = st.columns([1, 1.5, 1])

with center:
    if st.button("🚀 INITIATE MISSION"):
        st.balloons()
        st.success("🌌 Greetings, Space Explorer! Welcome aboard!")
        st.snow()

    if st.button("🛑 ABORT MISSION"):
        st.warning("Mission aborted. Returning to standby mode.")


# =========================
# FOOTER
# =========================

st.markdown("""
<br><br>
<div style="text-align:center; color:#64748b;
            font-size:12px; letter-spacing:3px;">
    COSMIC EXPLORER SYSTEMS © 2026<br>
    <span style="color:#818cf8;">
        EXPLORE • DISCOVER • INNOVATE
    </span>
</div>
""", unsafe_allow_html=True)
