import streamlit as st

st.set_page_config(
    page_title="My Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

/* Sembunyikan navigasi bawaan Streamlit */
[data-testid="stToolbar"],
#MainMenu,
footer,
header,
[data-testid="stDecoration"],
[data-testid="collapsedControl"] {
    display: none !important;
}

/* Tombol hamburger */
.menu-button {
    position: fixed;
    top: 15px;
    left: 20px;
    z-index: 10000;
    font-size: 28px;
    cursor: pointer;
    color: white;
    background: #1e293b;
    padding: 5px 13px;
    border-radius: 8px;
}

/* Checkbox */
#menu-toggle {
    display: none;
}

/* Sidebar full height */
.sidebar-custom {
    position: fixed;
    top: 0;
    left: -280px;
    width: 260px;
    height: 100vh;
    background: #172033;
    z-index: 9999;
    padding: 75px 20px 20px;
    transition: left 0.3s ease;
    box-sizing: border-box;
}

/* Sidebar terbuka */
#menu-toggle:checked ~ .sidebar-custom {
    left: 0;
}

/* Link menu */
.sidebar-custom a {
    display: block;
    color: white;
    text-decoration: none;
    padding: 15px;
    margin-bottom: 8px;
    border-radius: 8px;
}

.sidebar-custom a:hover {
    background: #334155;
}

/* Overlay */
.overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.4);
    z-index: 9998;
}

#menu-toggle:checked ~ .overlay {
    display: block;
}

</style>

<input type="checkbox" id="menu-toggle">

<label for="menu-toggle" class="menu-button">
    ☰
</label>

<div class="sidebar-custom">
    <h2 style="color:white;">MY DASHBOARD</h2>
    <hr>
    <a href="?page=home">🏠 Home</a>
    <a href="?page=dashboard">📊 Dashboard</a>
    <a href="?page=data">📁 Data</a>
    <a href="?page=settings">⚙️ Settings</a>
</div>

<label for="menu-toggle" class="overlay"></label>

""", unsafe_allow_html=True)

st.title("My Dashboard")
st.write("Selamat datang di aplikasi Streamlit.")
