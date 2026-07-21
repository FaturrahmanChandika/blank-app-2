import streamlit as st
import random
import hashlib

st.set_page_config(
    page_title="Tebak Isi Saldo",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>

.stApp{
    background:#F4F7FC;
}

/* Header */
.header{
    background:#2563EB;
    color:white;
    text-align:center;
    padding:18px;
    border-radius:15px;
    font-size:40px;
    font-weight:bold;
    margin-bottom:30px;
}

/* Card */
.card{
    background:white;
    border-radius:18px;
    padding:20px;
    height:260px;
    border:1px solid #E5E7EB;
    box-shadow:0 4px 12px rgba(0,0,0,.08);
    text-align:center;
}

.icon{
    font-size:55px;
}

.title{
    font-size:30px;
    font-weight:bold;
    color:#1F2937;
    margin-bottom:15px;
}

.value{
    font-size:25px;
    color:#2563EB;
    font-weight:bold;
    line-height:1.5;
    word-wrap:break-word;
}

.saldo{
    color:#16A34A;
    font-size:32px;
    font-weight:bold;
    margin-top:10px;
}

.nama{
    font-size:34px;
    color:#2563EB;
    font-weight:bold;
    margin-top:20px;
}

.ket{
    font-size:18px;
    color:#444;
    line-height:30px;
    margin-top:15px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("""
<div class='header'>
💰 APLIKASI TEBAK ISI SALDO 💰
</div>
""", unsafe_allow_html=True)

nama = st.text_input("Masukkan Nama")

# =========================
# DATA
# =========================

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
"Kawasaki Ninja",
"CBR150R"
]

mobil = [
"Toyota Avanza",
"Honda Brio",
"Honda HRV",
"Toyota Fortuner",
"Innova Zenix",
"Mitsubishi Pajero",
"BMW M4",
"Mercedes C200",
"Toyota Alphard",
"Tidak Punya"
]

kata = [
"Sultan berkedok rakyat biasa 😎",
"Isi rekening bikin iri satu RT 😂",
"Rajin menabung sejak kecil 💰",
"Orangnya sederhana tapi saldonya luar biasa.",
"Gaji numpang lewat 🤣",
"Jangan dipinjemin uang 😆",
"Rekeningnya bikin tetangga iri.",
"Dompetnya tebal banget."
]

# =========================
# BUTTON
# =========================

if st.button("🔍 Tebak Sekarang", use_container_width=True):

    if nama.strip() == "":
        st.warning("Masukkan nama terlebih dahulu.")
        st.stop()

    seed = int(hashlib.md5(nama.lower().encode()).hexdigest(),16)

    random.seed(seed)

    saldo = random.randint(50000,50000000)

    hasil_bank = random.choice(bank)
    hasil_motor = random.choice(motor)
    hasil_mobil = random.choice(mobil)
    hasil_ket = random.choice(kata)

    st.write("")
    st.write("")

    c1,c2,c3,c4,c5 = st.columns(5)

    with c1:
        st.markdown(f"""
        <div class="card">
            <div class="icon">👤</div>
            <div class="title">Nama</div>
            <div class="nama">{nama.upper()}</div>
        </div>
        """,unsafe_allow_html=True)

    with c2:
        saldo_format = f"Rp {saldo:,}".replace(",", ".")
        st.markdown(f"""
        <div class="card">
            <div class="icon">💳</div>
            <div class="title">Saldo</div>
            <div class="value">{hasil_bank}</div>
            <div class="saldo">{saldo_format}</div>
        </div>
        """,unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="card">
            <div class="icon">🏍️</div>
            <div class="title">Motor</div>
            <div class="value">{hasil_motor}</div>
        </div>
        """,unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="card">
            <div class="icon">🚗</div>
            <div class="title">Mobil</div>
            <div class="value">{hasil_mobil}</div>
        </div>
        """,unsafe_allow_html=True)

    with c5:
        st.markdown(f"""
        <div class="card">
            <div class="icon">💬</div>
            <div class="title">Keterangan</div>
            <div class="ket">{hasil_ket}</div>
        </div>
        """,unsafe_allow_html=True)
