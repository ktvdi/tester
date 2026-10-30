
import streamlit as st

st.set_page_config(
    page_title="My Website",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Daftar halaman
pages = {
    "Home": "pages/home.py",
    "Dashboard": "pages/dashboard.py",
    "Data": "pages/data.py",
    "Settings": "pages/settings.py"
}

# Navigasi native Streamlit
pg = st.navigation(
    [
        st.Page(path, title=name)
        for name, path in pages.items()
    ],
    position="hidden"
)

# CSS
st.markdown("""
<style>

/* Sembunyikan navigasi bawaan */
[data-testid="stSidebar"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
#MainMenu,
header,
footer {
    display: none !important;
}

/* Tombol menu */
div.st-key-menu_button {
    position: fixed;
    top: 10px;
    right: 25px;
    z-index: 1000;
}

/* Tombol hamburger */
div.st-key-menu_button button {
    background: #172033;
    color: white;
    border: none;
    font-size: 25px;
    border-radius: 8px;
}

/* Dropdown container */
div.st-key-menu_container {
    background: #172033;
    padding: 25px;
    border-radius: 0 0 12px 12px;
    margin-bottom: 20px;
}

/* Tombol menu dropdown */
div.st-key-menu_container button {
    width: 100%;
    background: transparent;
    color: white;
    border: none;
    text-align: left;
    padding: 12px;
    font-size: 17px;
}

div.st-key-menu_container button:hover {
    background: #334155;
    color: white;
}

/* Konten */
.block-container {
    padding-top: 4rem;
}

</style>
""", unsafe_allow_html=True)

# Status dropdown
if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

# Tombol hamburger
if st.button(
    "✕" if st.session_state.menu_open else "☰",
    key="menu_button"
):
    st.session_state.menu_open = not st.session_state.menu_open
    st.rerun()

# Dropdown
if st.session_state.menu_open:

    with st.container(key="menu_container"):

        st.markdown(
            "<h2 style='color:white;'>NAVIGATION</h2>",
            unsafe_allow_html=True
        )

        for name, path in pages.items():

            if st.button(name, key=f"nav_{name}"):
                st.session_state.menu_open = False
                st.switch_page(path)

# Jalankan halaman
pg.run()
