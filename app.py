import streamlit as st

st.set_page_config(
    page_title="My Dashboard",
    layout="wide"
)

# CSS
st.markdown("""
<style>
/* Sembunyikan sidebar bawaan */
[data-testid="stSidebar"] {
    display: none;
}

/* Tombol hamburger */
.menu-btn {
    position: fixed;
    top: 15px;
    left: 20px;
    z-index: 9999;
    font-size: 28px;
    cursor: pointer;
    background: #222;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 5px 12px;
}

/* Sidebar custom */
.custom-menu {
    position: fixed;
    top: 0;
    left: -270px;
    width: 250px;
    height: 100vh;
    background: #1e293b;
    padding: 70px 20px 20px;
    transition: 0.3s ease;
    z-index: 9998;
}

/* Ketika checkbox aktif */
#menu-toggle:checked ~ .custom-menu {
    left: 0;
}

.custom-menu a {
    display: block;
    color: white;
    padding: 15px;
    text-decoration: none;
    border-radius: 8px;
}

.custom-menu a:hover {
    background: #334155;
}
</style>

<input type="checkbox" id="menu-toggle" hidden>

<label for="menu-toggle" class="menu-btn">
    ☰
</label>

<div class="custom-menu">
    <h3 style="color:white;">MY DASHBOARD</h3>
    <a href="#">🏠 Home</a>
    <a href="#">📊 Dashboard</a>
    <a href="#">📁 Data</a>
    <a href="#">⚙️ Settings</a>
</div>
""", unsafe_allow_html=True)

st.title("My Dashboard")
st.write("Selamat datang di aplikasi Streamlit!")
