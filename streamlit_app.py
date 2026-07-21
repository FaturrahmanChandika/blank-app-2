import streamlit as st
import random
import hashlib

st.set_page_config(
    page_title="Tebak Isi Saldo",
    layout="wide",
)

# ================= CSS =================
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f172a,#1e3a8a,#7c3aed);
}

.title{
font-size:40px;
font-weight:bold;
color:white;
text-align:center;
padding:20px;
border-radius:15px;
background:rgba(255,255,255,0.1);
backdrop-filter:blur(10px);
margin-bottom:20px;
}

.box{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 5px 20px rgba(0,0,0,.25);
text-align:center;
height:210px;
}

.big{
font-size:28px;
font-weight:bold;
color:#2563eb;
}

.nama{
font-size:35px;
font-weight:bold;
color:#7c3aed;
}

.ket{
font-size:18px;
font-style:italic;
color:#444;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💰 APLIKASI TEBAK ISI SALDO 💰</div>', unsafe_allow_html=True)

# ================= INPUT =================

nama = st.text_input("Masukkan Nama")

# ================= DATA =================

bank = [
"OVO","DANA","GoPay","ShopeePay",
"BCA","BRI","BNI","Mandiri",
"CIMB","Permata"
]

motor = [
"Honda Beat",
"Honda Vario 160",
"Honda PCX",
"Yamaha NMAX",
"Yamaha Aerox",
"Honda Scoopy",
"Kawasaki Ninja ZX25R",
"CBR150R"
]

mobil = [
"Toyota Avanza",
"Honda Brio",
"Toyota Fortuner",
"Mitsubishi Pajero",
"Honda HRV",
"Toyota Alphard",
"BMW M4",
"Mercedes C200",
"Innova Zenix",
"Tidak Punya"
]

kata = [
"Sultan berkedok rakyat biasa 😎",
"Isi rekening bikin iri satu RT 😂",
"Rajin nabung ternyata 👍",
"Masih semangat mengejar cuan 💸",
"Dompetnya tebal banget 😆",
"Orang sederhana tapi saldo luar biasa 🔥",
"Jangan dipinjemin uang 😁",
"Gajinya numpang lewat 🤣"
]

# ================= BUTTON =================

if st.button("🔍 Tebak Sekarang", use_container_width=True):

    if nama == "":
        st.warning("Masukkan nama terlebih dahulu.")
        st.stop()

    seed = int(hashlib.md5(nama.lower().encode()).hexdigest(),16)
    random.seed(seed)

    saldo = random.randint(100000,50000000)

    hasil_bank = random.choice(bank)
    hasil_motor = random.choice(motor)
    hasil_mobil = random.choice(mobil)
    hasil_ket = random.choice(kata)

    st.write("")
    st.write("")

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.markdown(f"""
        <div class="box">
        <h2>👤</h2>
        <div class="nama">{nama.upper()}</div>
        </div>
        """,unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="box">
        <h2>💳 Saldo</h2>
        <h3>{hasil_bank}</h3>
        <div class="big">Rp {saldo:,}</div>
        </div>
        """.replace(",", "."),unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="box">
        <h2>🏍 Motor</h2>
        <br>
        <div class="big">{hasil_motor}</div>
        </div>
        """,unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="box">
        <h2>🚗 Mobil</h2>
        <br>
        <div class="big">{hasil_mobil}</div>
        </div>
        """,unsafe_allow_html=True)

    with col5:
        st.markdown(f"""
        <div class="box">
        <h2>💬 Keterangan</h2>
        <br>
        <div class="ket">{hasil_ket}</div>
        </div>
        """,unsafe_allow_html=True)
