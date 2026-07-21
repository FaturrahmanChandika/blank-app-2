import streamlit as st
import random
import hashlib

st.set_page_config(
    page_title="Tebak Isi Saldo",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background-color:#ffffff;
}

.judul{
    background:#2563EB;
    color:white;
    text-align:center;
    padding:18px;
    border-radius:12px;
    font-size:34px;
    font-weight:bold;
    margin-bottom:20px;
}

div[data-testid="stTextInput"] input{
    border-radius:10px;
    border:2px solid #16A34A;
}

.stButton>button{
    background:#16A34A;
    color:white;
    border:none;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
    width:100%;
}

.stButton>button:hover{
    background:#15803D;
    color:white;
}

table{
    width:100%;
    border-collapse:collapse;
    margin-top:20px;
}

th{
    background:#16A34A;
    color:white;
    padding:12px;
    text-align:center;
    font-size:16px;
}

td{
    padding:12px;
    border:1px solid #BBF7D0;
    text-align:center;
    background:#ECFDF5;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='judul'>💰 APLIKASI TEBAK ISI SALDO 💰</div>",
    unsafe_allow_html=True
)

nama = st.text_input("Masukkan Nama")

bank = [
    "OVO",
    "DANA",
    "GoPay",
    "ShopeePay",
    "BCA",
    "BRI",
    "BNI",
    "Mandiri",
    "CIMB",
    "Permata"
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
    "BMW M4",
    "Toyota Alphard",
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

# ==========================
# Tombol Tebak
# ==========================

if st.button("🔍 Tebak Sekarang"):

    if nama.strip() == "":
        st.warning("Silakan masukkan nama terlebih dahulu.")
        st.stop()

    # Supaya nama yang sama hasilnya selalu sama
    seed = int(hashlib.md5(nama.lower().encode()).hexdigest(), 16)
    random.seed(seed)

    hasil_bank = random.choice(bank)
    hasil_motor = random.choice(motor)
    hasil_mobil = random.choice(mobil)
    hasil_keterangan = random.choice(keterangan)

    saldo = random.randint(100000, 50000000)
    saldo = f"Rp {saldo:,}".replace(",", ".")

    st.markdown(f"""
    <table>
        <thead>
            <tr>
                <th>👤 Nama</th>
                <th>💳 Saldo</th>
                <th>🏍️ Motor</th>
                <th>🚗 Mobil</th>
                <th>💬 Keterangan</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td><b>{nama.upper()}</b></td>

                <td>
                    <b>{hasil_bank}</b><br>
                    <span style="color:#16A34A;font-size:18px;font-weight:bold;">
                        {saldo}
                    </span>
                </td>

                <td>{hasil_motor}</td>

                <td>{hasil_mobil}</td>

                <td>{hasil_keterangan}</td>
            </tr>
        </tbody>

    </table>
    """, unsafe_allow_html=True)

    st.success("✅ Tebakan berhasil dibuat!")
