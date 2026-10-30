import streamlit as st

st.set_page_config(
    page_title="My Website",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# DAFTAR HALAMAN
pages = {
    "Home": "pages/home.py",
    "Dashboard": "pages/dashboard.py",
    "Data": "pages/data.py",
    "Settings": "pages/settings.py"
}

# NAVIGASI STREAMLIT
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

/* Tombol hamburger */
div.st-key-menu_button {
    position: fixed;
    top: 12px;
    right: 25px;
    z-index: 10003;
}

div.st-key-menu_button button {
    background: #172033;
    color: white;
    border: none;
    font-size: 25px;
    border-radius: 8px;
    padding: 5px 15px;
}

div.st-key-menu_button button:hover {
    background: #334155;
    color: white;
    border: none;
}

/* Dropdown full width */
div.st-key-menu_container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    max-height: 100vh;
    overflow-y: auto;
    box-sizing: border-box;
    background: #172033;
    padding: 75px 30px 30px;
    z-index: 10001;
    border-radius: 0 0 12px 12px;
}

/* Tombol navigasi */
div.st-key-menu_container button {
    width: 100%;
    background: transparent;
    color: white;
    border: none;
    text-align: left;
    padding: 15px;
    font-size: 17px;
}

div.st-key-menu_container button:hover {
    background: #334155;
    color: white;
}

/* Konten utama */
.block-container {
    padding-top: 4rem;
}

</style>
""", unsafe_allow_html=True)


# STATUS MENU
if "menu_open" not in st.session_state:
    st.session_state.menu_open = False


# TOMBOL HAMBURGER
if st.button(
    "✕" if st.session_state.menu_open else "☰",
    key="menu_button"
):
    st.session_state.menu_open = not st.session_state.menu_open
    st.rerun()


# DROPDOWN
if st.session_state.menu_open:

    with st.container(key="menu_container"):

        st.markdown(
            "<h2 style='color:white;'>NAVIGATION</h2>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<p style='color:#94a3b8;'>Choose your page</p>",
            unsafe_allow_html=True
        )

        for name, path in pages.items():

            if st.button(name, key=f"nav_{name}"):

                st.session_state.menu_open = False

                st.switch_page(path)


# JALANKAN HALAMAN
pg.run()
