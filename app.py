
import streamlit as st

st.set_page_config(
    page_title="My Website",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================
# SESSION STATE
# ==================================

if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"


# ==================================
# CSS DARK NAVY
# ==================================

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
    top: 10px;
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

/* Dropdown */
div.st-key-menu_container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: auto;
    max-height: 100vh;
    overflow-y: auto;
    box-sizing: border-box;
    background: #172033;
    padding: 75px 30px 30px;
    z-index: 10001;
}

/* Tombol navigasi */
div.st-key-menu_container button {
    width: 100%;
    text-align: left;
    background: transparent;
    color: white;
    border: none;
    padding: 15px;
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


# ==================================
# HAMBURGER BUTTON
# ==================================

if st.button(
    "✕" if st.session_state.menu_open else "☰",
    key="menu_button"
):
    st.session_state.menu_open = not st.session_state.menu_open
    st.rerun()


# ==================================
# DROPDOWN MENU
# ==================================

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

        menu_items = [
            "🏠 Home",
            "📊 Dashboard",
            "📁 Data",
            "⚙️ Settings"
        ]

        for item in menu_items:

            if st.button(item, key=f"nav_{item}"):

                st.session_state.current_page = (
                    item.split(" ", 1)[1]
                )

                st.session_state.menu_open = False
                st.rerun()


# ==================================
# PAGE CONTENT
# ==================================

page = st.session_state.current_page

if page == "Home":

    st.title("🏠 Home")
    st.write("Selamat datang di aplikasi saya.")

elif page == "Dashboard":

    st.title("📊 Dashboard")
    st.write("Halaman Dashboard")

elif page == "Data":

    st.title("📁 Data")
    st.write("Halaman Data")

elif page == "Settings":

    st.title("⚙️ Settings")
    st.write("Halaman Pengaturan")
