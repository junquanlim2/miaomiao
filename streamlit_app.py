
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ORION | Space Mission Control",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide default Streamlit interface
st.markdown("""
<style>
    #MainMenu, footer, header,
    [data-testid="stHeader"],
    [data-testid="stToolbar"] {
        display: none !important;
    }

    .stApp {
        background: #030712;
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    iframe {
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# THREE.JS SPACE ENVIRONMENT
# ==========================================

html_code = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background: #030712;
    color: white;
    font-family: 'Courier New', monospace;
    overflow: hidden;
}

#space {
    position: fixed;
    inset: 0;
    z-index: 0;
}

canvas {
    display: block;
}

.hud {
    position: fixed;
    inset: 0;
    z-index: 2;
    pointer-events: none;
    padding: 25px;
}

/* HEADER */

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 20px;
    font-weight: bold;
    letter-spacing: 5px;
    color: #67e8f9;
    text-shadow: 0 0 15px #0891b2;
}

.subtitle {
    font-size: 10px;
    color: #64748b;
    letter-spacing: 3px;
    margin-top: 5px;
}

.status {
    color: #4ade80;
    font-size: 11px;
    letter-spacing: 2px;
}

.dot {
    display: inline-block;
    height: 7px;
    width: 7px;
    border-radius: 50%;
    background: #4ade80;
    box-shadow: 0 0 12px #4ade80;
    margin-right: 8px;
}

/* LEFT PANEL */

.panel {
    position: absolute;
    top: 130px;
    left: 25px;
    width: 230px;
}

.card {
    background: rgba(8, 20, 43, 0.72);
    border: 1px solid rgba(103,232,249,0.23);
    backdrop-filter: blur(12px);
    padding: 17px;
    margin-bottom: 15px;
    border-radius: 8px;
    box-shadow: 0 0 25px rgba(8,145,178,0.08);
}

.card-title {
    color: #67e8f9;
    font-size: 10px;
    letter-spacing: 3px;
    margin-bottom: 15px;
}

.data-label {
    color: #64748b;
    font-size: 10px;
    margin-top: 12px;
}

.data-value {
    color: white;
    font-size: 17px;
    margin-top: 4px;
}

/* RADAR */

.radar {
    width: 125px;
    height: 125px;
    border: 1px solid #0891b2;
    border-radius: 50%;
    margin: 5px auto;
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(circle, transparent 25%, rgba(8,145,178,.15) 26%, transparent 27%),
        radial-gradient(circle, transparent 49%, rgba(8,145,178,.3) 50%, transparent 51%);
}

.radar::before {
    content: "";
    position: absolute;
    inset: 0;
    background: conic-gradient(
        from 0deg,
        transparent 0deg,
        rgba(34,211,238,.5) 50deg,
        transparent 80deg
    );
    animation: scan 3s linear infinite;
}

.radar::after {
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    width: 5px;
    height: 5px;
    background: #67e8f9;
    border-radius: 50%;
    box-shadow: 20px -25px 8px #67e8f9,
                -30px 15px 8px #67e8f9;
}

@keyframes scan {
    to { transform: rotate(360deg); }
}

/* RIGHT PANEL */

.right-panel {
    position: absolute;
    top: 130px;
    right: 25px;
    width: 205px;
    text-align: right;
}

.system-row {
    display: flex;
    justify-content: space-between;
    font-size: 10px;
    margin: 12px 0;
    color: #94a3b8;
}

.bar {
    height: 4px;
    background: #1e293b;
    margin-top: 6px;
    overflow: hidden;
}

.bar-fill {
    height: 100%;
    background: #22d3ee;
    box-shadow: 0 0 10px #22d3ee;
}

/* CENTER TITLE */

.center-title {
    position: absolute;
    top: 17%;
    left: 50%;
    transform: translateX(-50%);
    text-align: center;
    white-space: nowrap;
}

.center-title h1 {
    font-size: clamp(24px, 4vw, 48px);
    letter-spacing: 8px;
    color: #e0f2fe;
    text-shadow: 0 0 30px #0891b2;
}

.center-title p {
    font-size: 10px;
    letter-spacing: 5px;
    color: #67e8f9;
    margin-top: 12px;
}

/* BOTTOM CONTROLS */

.controls {
    position: absolute;
    bottom: 35px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 12px;
    pointer-events: auto;
    white-space: nowrap;
}

button {
    background: rgba(8, 30, 55, .85);
    color: #67e8f9;
    border: 1px solid #0891b2;
    padding: 13px 20px;
    font-family: inherit;
    font-size: 10px;
    letter-spacing: 2px;
    cursor: pointer;
    transition: .3s;
    border-radius: 4px;
}

button:hover, button.active {
    background: #0891b2;
    color: white;
    box-shadow: 0 0 25px #0891b2;
}

button:active {
    transform: scale(.96);
}

/* FOOTER */

.footer {
    position: absolute;
    bottom: 20px;
    left: 25px;
    color: #475569;
    font-size: 9px;
    letter-spacing: 2px;
}

/* RESPONSIVE */

@media(max-width: 750px) {
    .panel {
        top: 110px;
        left: 12px;
        width: 145px;
    }

    .right-panel {
        top: 110px;
        right: 12px;
        width: 140px;
    }

    .card {
        padding: 10px;
    }

    .data-value {
        font-size: 12px;
    }

    .center-title {
        top: 32%;
    }

    .center-title h1 {
        letter-spacing: 4px;
    }

    .controls {
        bottom: 45px;
        gap: 5px;
        width: 95%;
        justify-content: center;
    }

    button {
        padding: 10px 8px;
        font-size: 8px;
        letter-spacing: 0;
    }

    .footer {
        display: none;
    }
}
</style>
</head>

<body>

<div id="space"></div>

<div class="hud">

    <!-- HEADER -->
    <div class="header">
        <div>
            <div class="logo">✦ ORION</div>
            <div class="subtitle">DEEP SPACE EXPLORATION DIVISION</div>
        </div>

        <div class="status">
            <span class="dot"></span>
            ALL SYSTEMS ONLINE
        </div>
    </div>

    <!-- MAIN TITLE -->
    <div class="center-title">
        <h1>INTO THE UNKNOWN</h1>
        <p>MISSION 001 // GALACTIC EXPLORATION</p>
    </div>

    <!-- LEFT PANEL -->
    <div class="panel">

        <div class="card">
            <div class="card-title">MISSION DATA</div>

            <div class="data-label">DESTINATION</div>
            <div class="data-value">KEPLER-452B</div>

            <div class="data-label">SPACECRAFT</div>
            <div class="data-value">ORION-X1</div>

            <div class="data-label">FLIGHT SPEED</div>
            <div class="data-value" id="speed">12,450 KM/S</div>

            <div class="data-label">FLIGHT STATUS</div>
            <div class="data-value" id="flight">CRUISING</div>
        </div>

        <div class="card">
            <div class="card-title">DEEP SPACE RADAR</div>
            <div class="radar"></div>
            <div style="text-align:center;color:#67e8f9;font-size:9px;">
                SCANNING SECTOR 07
            </div>
        </div>
    </div>

    <!-- RIGHT PANEL -->
    <div class="right-panel">

        <div class="card">
            <div class="card-title">SHIP SYSTEMS</div>

            <div class="system-row">
                <span>ENGINE</span>
                <span>98%</span>
            </div>
            <div class="bar">
                <div class="bar-fill" style="width:98%"></div>
            </div>

            <div class="system-row">
                <span>SHIELD</span>
                <span>85%</span>
            </div>
            <div class="bar">
                <div class="bar-fill" style="width:85%"></div>
            </div>

            <div class="system-row">
                <span>OXYGEN</span>
                <span>100%</span>
            </div>
            <div class="bar">
                <div class="bar-fill" style="width:100%"></div>
            </div>

            <div class="system-row">
                <span>FUEL</span>
                <span>76%</span>
            </div>
            <div class="bar">
                <div class="bar-fill" style="width:76%"></div>
            </div>
        </div>

        <div class="card">
            <div class="card-title">NAVIGATION</div>
            <div class="data-label">GALACTIC SECTOR</div>
            <div class="data-value">X-07 / Z-12</div>

            <div class="data-label">THREAT LEVEL</div>
            <div class="data-value" style="color:#4ade80">MINIMAL</div>
        </div>
    </div>

    <!-- BUTTONS -->
    <div class="controls">
        <button id="cameraBtn">◉ CAMERA</button>
        <button id="boostBtn">⚡ HYPERDRIVE</button>
        <button id="scanBtn">⌖ SCAN</button>
        <button id="resetBtn">↺ RESET</button>
    </div>

    <div class="footer">
        ORION SPACE PROGRAM // EARTH COMMAND CENTER // 2026
    </div>

</div>

<script>

// ======================================
// THREE.JS SCENE SETUP
// ======================================

const scene = new THREE.Scene();

scene.background = new THREE.Color(0x030712);
scene.fog = new THREE.FogExp2(0x030712, 0.0015);

const camera = new THREE.PerspectiveCamera(
    65,
    window.innerWidth / window.innerHeight,
    0.1,
    3000
);

camera.position.set(0, 5, 18);

const renderer = new THREE.WebGLRenderer({
    antialias: true,
    alpha: true
});

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.toneMapping = THREE.ACESFilmicToneMapping;

document.getElementById("space").appendChild(renderer.domElement);


// ======================================
// LIGHTING
// ======================================

const ambient = new THREE.AmbientLight(0x64748b, 1.2);
scene.add(ambient);

const sun = new THREE.PointLight(0x67e8f9, 3, 200);
sun.position.set(10, 10, 15);
scene.add(sun);

const purpleLight = new THREE.PointLight(0x7c3aed, 3, 100);
purpleLight.position.set(-15, 5, -10);
scene.add(purpleLight);


// ======================================
// STARFIELD
// ======================================

const starGeometry = new THREE.BufferGeometry();

const starCount = 6500;
const starPositions = new Float32Array(starCount * 3);

for (let i = 0; i < starCount * 3; i++) {
    starPositions[i] = (Math.random() - 0.5) * 1800;
}

starGeometry.setAttribute(
    "position",
    new THREE.BufferAttribute(starPositions, 3)
);

const starMaterial = new THREE.PointsMaterial({
    color: 0xffffff,
    size: 1.2,
    transparent: true,
    opacity: 0.9
});

const stars = new THREE.Points(starGeometry, starMaterial);
scene.add(stars);


// ======================================
// NEBULA PARTICLES
// ======================================

const nebulaGeometry = new THREE.BufferGeometry();
const nebulaPositions = [];

for (let i = 0; i < 1000; i++) {
    nebulaPositions.push(
        (Math.random() - 0.5) * 250,
        (Math.random() - 0.5) * 130,
        -Math.random() * 200
    );
}

nebulaGeometry.setAttribute(
    "position",
    new THREE.Float32BufferAttribute(nebulaPositions, 3)
);

const nebula = new THREE.Points(
    nebulaGeometry,
    new THREE.PointsMaterial({
        color: 0x8b5cf6,
        size: 2,
        transparent: true,
        opacity: 0.4
    })
);

scene.add(nebula);


// ======================================
// PLANET
// ======================================

const planetGeometry = new THREE.SphereGeometry(7, 64, 64);

const planetMaterial = new THREE.MeshStandardMaterial({
    color: 0x334eaa,
    roughness: 0.8,
    metalness: 0.15,
    emissive: 0x101b55
});

const planet = new THREE.Mesh(
    planetGeometry,
    planetMaterial
);

planet.position.set(25, -5, -65);
scene.add(planet);

// Planet atmosphere
const atmosphere = new THREE.Mesh(
    new THREE.SphereGeometry(7.25, 64, 64),
    new THREE.MeshBasicMaterial({
        color: 0x38bdf8,
        transparent: true,
        opacity: 0.13,
        side: THREE.BackSide
    })
);

atmosphere.position.copy(planet.position);
scene.add(atmosphere);

// Planet ring
const ring = new THREE.Mesh(
    new THREE.TorusGeometry(11, 0.12, 2, 120),
    new THREE.MeshBasicMaterial({
        color: 0xa78bfa,
        transparent: true,
        opacity: 0.7
    })
);

ring.position.copy(planet.position);
ring.rotation.x = 1.1;
scene.add(ring);


// ======================================
// SPACECRAFT MODEL
// ======================================

const ship = new THREE.Group();

const silver = new THREE.MeshStandardMaterial({
    color: 0xcbd5e1,
    metalness: 0.85,
    roughness: 0.25
});

const dark = new THREE.MeshStandardMaterial({
    color: 0x172554,
    metalness: 0.8,
    roughness: 0.3
});

const cyan = new THREE.MeshStandardMaterial({
    color: 0x67e8f9,
    emissive: 0x0891b2,
    emissiveIntensity: 2
});

// Main body
const body = new THREE.Mesh(
    new THREE.CylinderGeometry(0.65, 1, 6, 12),
    silver
);

body.rotation.x = Math.PI / 2;
ship.add(body);

// Cockpit
const cockpit = new THREE.Mesh(
    new THREE.SphereGeometry(0.75, 32, 32),
    new THREE.MeshStandardMaterial({
        color: 0x0e7490,
        metalness: 0.8,
        roughness: 0.1,
        emissive: 0x0369a1
    })
);

cockpit.position.z = -1.7;
cockpit.scale.set(0.8, 0.8, 1.3);
ship.add(cockpit);

// Nose
const nose = new THREE.Mesh(
    new THREE.ConeGeometry(0.65, 2.2, 12),
    silver
);

nose.rotation.x = -Math.PI / 2;
nose.position.z = -4;
ship.add(nose);

// Wings
function makeWing(x) {
    const wing = new THREE.Mesh(
        new THREE.BoxGeometry(3.2, 0.15, 2.8),
        dark
    );

    wing.position.set(x, 0, 0.8);
    wing.rotation.y = x > 0 ? -0.25 : 0.25;

    ship.add(wing);

    const light = new THREE.Mesh(
        new THREE.SphereGeometry(0.13, 12, 12),
        cyan
    );

    light.position.set(x * 2, 0.1, 0.8);
    ship.add(light);
}

makeWing(1.7);
makeWing(-1.7);

// Engine cylinders and flames
const engines = [];

for (let i = -1; i <= 1; i++) {

    const engine = new THREE.Mesh(
        new THREE.CylinderGeometry(0.28, 0.38, 1.2, 16),
        dark
    );

    engine.rotation.x = Math.PI / 2;
    engine.position.set(i * 0.65, 0, 3);
    ship.add(engine);

    const flame = new THREE.Mesh(
        new THREE.ConeGeometry(0.32, 2, 16),
        new THREE.MeshBasicMaterial({
            color: 0x06b6d4,
            transparent: true,
            opacity: 0.8
        })
    );

    flame.rotation.x = Math.PI / 2;
    flame.position.set(i * 0.65, 0, 4.5);

    ship.add(flame);
    engines.push(flame);
}

ship.scale.set(0.85, 0.85, 0.85);
ship.position.set(0, 0, 0);

scene.add(ship);


// ======================================
// FLOATING SPACE DEBRIS
// ======================================

const debris = [];

for (let i = 0; i < 30; i++) {

    const object = new THREE.Mesh(
        new THREE.IcosahedronGeometry(
            Math.random() * 0.4 + 0.1,
            0
        ),
        new THREE.MeshStandardMaterial({
            color: 0x64748b,
            metalness: 0.7,
            roughness: 0.8
        })
    );

    object.position.set(
        (Math.random() - 0.5) * 80,
        (Math.random() - 0.5) * 50,
        -Math.random() * 100
    );

    scene.add(object);
    debris.push(object);
}


// ======================================
// INTERACTIVE CONTROLS
// ======================================

let boosting = false;
let scanning = false;
let cameraMode = 0;
let scanTimer = 0;

const speedDisplay = document.getElementById("speed");
const flightDisplay = document.getElementById("flight");

document.getElementById("boostBtn").onclick = function() {

    boosting = !boosting;

    this.classList.toggle("active", boosting);

    flightDisplay.textContent =
        boosting ? "HYPERDRIVE" : "CRUISING";

    speedDisplay.textContent =
        boosting ? "89,900 KM/S" : "12,450 KM/S";
};

document.getElementById("scanBtn").onclick = function() {

    scanning = !scanning;

    this.classList.toggle("active", scanning);

    this.textContent = scanning ? "◉ SCANNING" : "⌖ SCAN";

    scanTimer = 0;
};

document.getElementById("cameraBtn").onclick = function() {

    cameraMode = (cameraMode + 1) % 3;

    this.classList.add("active");

    this.textContent = [
        "◉ CAMERA",
        "◉ ORBIT VIEW",
        "◉ SIDE VIEW"
    ][cameraMode];
};

document.getElementById("resetBtn").onclick = function() {

    boosting = false;
    scanning = false;
    cameraMode = 0;

    document.getElementById("boostBtn").classList.remove("active");
    document.getElementById("scanBtn").classList.remove("active");
    document.getElementById("cameraBtn").classList.remove("active");

    document.getElementById("scanBtn").textContent = "⌖ SCAN";
    document.getElementById("cameraBtn").textContent = "◉ CAMERA";

    flightDisplay.textContent = "CRUISING";
    speedDisplay.textContent = "12,450 KM/S";

    ship.position.set(0, 0, 0);
};


// ======================================
// MOUSE INTERACTION
// ======================================

let mouseX = 0;
let mouseY = 0;

window.addEventListener("mousemove", function(event) {

    mouseX = (event.clientX / window.innerWidth - 0.5) * 2;
    mouseY = (event.clientY / window.innerHeight - 0.5) * 2;

});


// ======================================
// ANIMATION LOOP
// ======================================

const clock = new THREE.Clock();

function animate() {

    requestAnimationFrame(animate);

    const time = clock.getElapsedTime();

    // Star rotation
    stars.rotation.y = time * 0.008;
    stars.rotation.x = Math.sin(time * 0.05) * 0.02;

    // Nebula movement
    nebula.rotation.y = time * 0.015;

    // Planet rotation
    planet.rotation.y = time * 0.08;
    ring.rotation.z = time * 0.05;

    // Spaceship floating
    ship.position.y = Math.sin(time * 1.5) * 0.35;

    ship.rotation.z = Math.sin(time * 0.7) * 0.04;
    ship.rotation.x = Math.sin(time * 0.5) * 0.025;

    // Mouse camera movement
    let targetX = mouseX * 3;
    let targetY = 5 + mouseY * 2;

    // Camera views
    if (cameraMode === 1) {
        targetX = Math.sin(time * 0.3) * 15;
        targetY = 8;
    }

    if (cameraMode === 2) {
        targetX = 15;
        targetY = 1;
    }

    camera.position.x += (targetX - camera.position.x) * 0.025;
    camera.position.y += (targetY - camera.position.y) * 0.025;

    camera.lookAt(0, 0, -8);

    // Engine animation
    engines.forEach((flame, index) => {

        const intensity = boosting ? 1.7 : 1;

        flame.scale.y =
            (0.8 + Math.sin(time * 12 + index) * 0.15) * intensity;

        flame.material.opacity =
            boosting ? 1 : 0.65;

    });

    // Space debris
    debris.forEach((item, index) => {
        item.rotation.x += 0.003;
        item.rotation.y += 0.005;

        if (boosting) {
            item.position.z += 0.35;
        }

        if (item.position.z > 20) {
            item.position.z = -100;
        }
    });

    // Scanning effect
    if (scanning) {
        scanTimer += 0.016;

        if (scanTimer > 5) {
            scanning = false;

            document.getElementById("scanBtn").classList.remove("active");
            document.getElementById("scanBtn").textContent = "⌖ SCAN";

            scanTimer = 0;
        }
    }

    renderer.render(scene, camera);
}

animate();


// ======================================
// RESPONSIVE RESIZING
// ======================================

window.addEventListener("resize", function() {

    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize(window.innerWidth, window.innerHeight);

    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

});

</script>

</body>
</html>
"""

# ==========================================
# DISPLAY APPLICATION
# ==========================================

components.html(
    html_code,
    height=900,
    scrolling=False
)
