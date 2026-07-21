import streamlit as st
import random
import hashlib

st.set_page_config(
    page_title="Tebak Isi Saldo",
    page_icon="💰",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>

.stApp{
    background:#FFFFFF;
}

/* Header */
.header{
    background:#2563EB;
    color:white;
    text-align:center;
    padding:18px;
    border-radius:12px;
    font-size:34px;
    font-weight:bold;
    margin-bottom:25px;
}

/* Input */
div[data-testid="stTextInput"] input{
    border:2px solid #16A34A;
    border-radius:10px;
}

/* Button */
.stButton>button{
    background:#16A34A;
    color:white;
    border:none;
    border-radius:10px;
    font-weight:bold;
    height:45px;
    width:100%;
}

.stButton>button:hover{
    background:#15803D;
    color:white;
}

/* Table */
table{
    width:100%;
    border-collapse:collapse;
    margin-top:20px;
}

th{
    background:#16A34A;
    color:white;
    padding:12px;
    font-size:16px;
}

td{
    background:#ECFDF5;
    border:1px solid #BBF7D0;
    padding:12px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
💰 APLIKASI TEBAK ISI SALDO 💰
</div>
""", unsafe_allow_html=True)

nama = st.text_input("Masukkan Nama")

bank = [
"OVO","DANA","GoPay","ShopeePay",
"BCA","BRI","BNI","Mandiri",
"CIMB","Permata"
]

motor = [
"Honda Beat",
"Honda Vario 160",
"Honda PCX",
"Yamaha Aerox",
"Yamaha NMAX",
"Honda Scoopy",
"CBR150R",
"Kawasaki Ninja"
]

mobil = [
"Toyota Avanza",
"Honda Brio",
"Toyota Fortuner",
"Innova Zenix",
"Mitsubishi Pajero",
"Honda HRV",
"Toyota Alphard",
"BMW M4",
"Mercedes C200",
"Tidak Punya"
]

keterangan = [
"Sultan berkedok rakyat biasa 😎",
"Isi rekening bikin iri satu RT 😂",
"Rajin menabung sejak kecil 💰",
"Dompetnya tebal banget 😆",
"Gajinya numpang lewat 🤣",
"Jangan dipinjemin uang 😅",
"Orangnya sederhana tapi saldonya luar biasa 🔥",
"Rekeningnya bikin tetangga iri 👀"
]

# ============================
# Tombol Tebak
# ============================

if st.button("🔍 Tebak Sekarang"):

    if nama.strip() == "":
        st.warning("Silakan masukkan nama terlebih dahulu.")
        st.stop()

    # Agar hasil untuk nama yang sama selalu sama
    seed = int(hashlib.md5(nama.lower().encode()).hexdigest(), 16)
    random.seed(seed)

    hasil_bank = random.choice(bank)
    hasil_motor = random.choice(motor)
    hasil_mobil = random.choice(mobil)
    hasil_keterangan = random.choice(keterangan)

    nominal = random.randint(100000, 50000000)
    saldo = f"Rp {nominal:,}".replace(",", ".")

    data = {
        "Nama": [nama.upper()],
        "Saldo": [f"{hasil_bank}\n{saldo}"],
        "Motor": [hasil_motor],
        "Mobil": [hasil_mobil],
        "Keterangan": [hasil_keterangan]
    }

    st.table(data)
