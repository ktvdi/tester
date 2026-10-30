import streamlit as st

st.set_page_config(
    page_title="My Website",
    layout="wide"
)

st.markdown("""
<style>
[data-testid="stToolbar"],
#MainMenu,
footer,
header,
[data-testid="stDecoration"] {
    display: none !important;
}

/* Tombol hamburger */
.menu-label {
    position: fixed;
    top: 12px;
    right: 25px;
    z-index: 10002;
    font-size: 28px;
    color: white;
    background: #172033;
    padding: 5px 14px;
    border-radius: 8px;
    cursor: pointer;
}

/* Checkbox */
#dropdown-menu {
    display: none;
}

/* Dropdown */
.dropdown {
    position: fixed;
    top: -100%;
    left: 0;
    width: 100%;
    height: auto;
    max-height: 100vh;
    overflow-y: auto;
    background: #172033;
    padding: 75px 25px 25px;
    box-sizing: border-box;
    z-index: 10001;
    transition: top 0.35s ease;
}

/* Saat dibuka */
#dropdown-menu:checked ~ .dropdown {
    top: 0;
}

/* Menu link */
.dropdown a {
    display: block;
    padding: 18px;
    color: white;
    text-decoration: none;
    border-bottom: 1px solid #334155;
    font-size: 17px;
}

.dropdown a:hover {
    background: #334155;
}

/* Tombol close */
.close-menu {
    position: fixed;
    top: 12px;
    right: 25px;
    z-index: 10003;
    display: none;
    color: white;
    font-size: 28px;
    cursor: pointer;
}

#dropdown-menu:checked ~ .close-menu {
    display: block;
}

#dropdown-menu:checked ~ .menu-label {
    display: none;
}
</style>

<input type="checkbox" id="dropdown-menu">

<label for="dropdown-menu" class="menu-label">☰</label>
<label for="dropdown-menu" class="close-menu">✕</label>

<div class="dropdown">
    <h2 style="color:white;">NAVIGATION</h2>
    <a href="?page=home">🏠 Home</a>
    <a href="?page=dashboard">📊 Dashboard</a>
    <a href="?page=data">📁 Data</a>
    <a href="?page=settings">⚙️ Settings</a>
</div>
""", unsafe_allow_html=True)

st.title("My Website")
st.write("Konten utama aplikasi")
