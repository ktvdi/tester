import streamlit as st

st.markdown("""
<style>
/* Background aplikasi */
.stApp {
    background-color: #F5F7FA;
}

/* Judul */
h1 {
    color: #1E3A8A;
    font-size: 40px;
    font-weight: bold;
}

/* Tombol */
.stButton > button {
    background-color: #2563EB;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
}

/* Tombol saat hover */
.stButton > button:hover {
    background-color: #1D4ED8;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("Dashboard Saya")
st.write("Selamat datang di aplikasi Streamlit!")

if st.button("Klik Saya"):
    st.success("Berhasil!")
