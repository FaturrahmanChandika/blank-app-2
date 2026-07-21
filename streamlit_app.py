import streamlit as st
import random
import hashlib

# ==========================================
# KONFIGURASI
# ==========================================

st.set_page_config(
    page_title="Aplikasi Tebak Isi Saldo",
    page_icon="💰",
    layout="wide"
)

# ==========================================
# SESSION
# ==========================================

if "hasil" not in st.session_state:
    st.session_state.hasil = []

# ==========================================
# DATA
# ==========================================

BANK = [
    ("OVO","🟣"),
    ("DANA","🔵"),
    ("GoPay","🟢"),
    ("ShopeePay","🟠"),
    ("BCA","🏦"),
    ("BRI","🏦"),
    ("BNI","🏦"),
    ("Mandiri","🏦"),
    ("Permata","🏦"),
    ("CIMB Niaga","🏦")
]

MOTOR = [
    "Honda Beat",
    "Honda Scoopy",
    "Honda Vario 160",
    "Honda PCX",
    "Yamaha NMAX",
    "Yamaha Aerox",
    "CBR150R",
    "Kawasaki Ninja",
    "KLX 150",
    "Vespa Sprint"
]

MOBIL = [
    "Honda Brio",
    "Toyota Avanza",
    "Innova Zenix",
    "Fortuner",
    "Pajero Sport",
    "Rush",
    "Raize",
    "HRV",
    "Alphard",
    "BMW M4"
]

KETERANGAN = [
    "😎 Sultan berkedok rakyat biasa.",
    "😂 Rekening bikin iri satu RT.",
    "🔥 Rajin menabung sejak kecil.",
    "💰 Dompet selalu tebal.",
    "🤣 Gaji cuma numpang lewat.",
    "😅 Jangan pinjam uang ke dia.",
    "👑 Orang sederhana tapi saldonya luar biasa.",
    "🤑 Isi rekening bikin tetangga iri."
]

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{
    background:#eef3f8;
}

.header{
    background:linear-gradient(90deg,#2563eb,#4f46e5);
    color:white;
    text-align:center;
    padding:18px;
    border-radius:18px;
    font-size:32px;
    font-weight:bold;
    margin-bottom:20px;
    box-shadow:0 5px 20px rgba(0,0,0,.2);
}

div[data-testid="stTextInput"] input{
    height:52px;
    border-radius:30px;
    border:2px solid #2563eb;
    font-size:18px;
}

.stButton>button{
    width:100%;
    height:52px;
    border:none;
    border-radius:12px;
    background:#ef4444;
    color:white;
    font-weight:bold;
    font-size:16px;
}

.stButton>button:hover{
    background:#dc2626;
    color:white;
}

.saldo-table{
    width:100%;
    border-collapse:collapse;
    background:white;
    border-radius:15px;
    overflow:hidden;
    box-shadow:0 6px 18px rgba(0,0,0,.15);
}

.saldo-table th{
    background:#16a34a;
    color:white;
    padding:14px;
    text-align:center;
}

.saldo-table td{
    padding:14px;
    border-bottom:1px solid #e5e7eb;
    text-align:center;
}

.saldo-table tr:nth-child(even){
    background:#f8fff8;
}

.saldo-table tr:hover{
    background:#dcfce7;
}

.bank{
    color:#2563eb;
    font-weight:bold;
}

.nominal{
    color:#059669;
    font-size:22px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="header">
💰 APLIKASI TEBAK ISI SALDO 💰
</div>
""", unsafe_allow_html=True)

# ==========================================
# INPUT
# ==========================================

col1, col2, col3 = st.columns([6,2,2])

with col1:
    nama = st.text_input(
        "",
        placeholder="🔍 Masukkan nama...",
        label_visibility="collapsed"
    )

with col2:
    btn_tebak = st.button(
        "🎲 Tebak Saldo",
        use_container_width=True
    )

with col3:
    btn_hapus = st.button(
        "🗑 Hapus Semua",
        use_container_width=True
    )

# ==========================================
# HAPUS SEMUA
# ==========================================

if btn_hapus:
    st.session_state.hasil.clear()
    st.rerun()

# ==========================================
# GENERATE DATA
# ==========================================

if btn_tebak:

    if nama.strip() == "":
        st.warning("Silakan masukkan nama.")
        st.stop()

    # agar nama yang sama hasilnya selalu sama
    seed = int(
        hashlib.md5(
            nama.lower().encode()
        ).hexdigest(),
        16
    )

    random.seed(seed)

    bank = random.choice(BANK)
    motor = random.choice(MOTOR)
    mobil = random.choice(MOBIL)
    ket = random.choice(KETERANGAN)

    nominal = random.randint(
        100000,
        500000000
    )

    saldo = f"Rp {nominal:,}".replace(",", ".")

    # cek apakah nama sudah ada
    ketemu = False

    for item in st.session_state.hasil:

        if item["nama"].lower() == nama.lower():

            ketemu = True

            item["bank"] = bank[0]
            item["logo"] = bank[1]
            item["saldo"] = saldo
            item["motor"] = motor
            item["mobil"] = mobil
            item["ket"] = ket

            break

    if not ketemu:

        st.session_state.hasil.append({

            "nama": nama.upper(),

            "bank": bank[0],

            "logo": bank[1],

            "saldo": saldo,

            "motor": motor,

            "mobil": mobil,

            "ket": ket

        })

# ==========================================
# FILTER DATA
# ==========================================

if nama.strip() == "":

    data_tampil = st.session_state.hasil

else:

    data_tampil = [

        x

        for x in st.session_state.hasil

        if nama.lower() in x["nama"].lower()

    ]

# ==========================================
# TABEL HTML
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

if len(data_tampil) == 0:

    st.info("Belum ada data.")

else:

    html = """
    <table class="saldo-table">
        <thead>
            <tr>
                <th>No</th>
                <th>Nama</th>
                <th>Isi Saldo</th>
                <th>Motor</th>
                <th>Mobil</th>
                <th>Keterangan</th>
            </tr>
        </thead>
        <tbody>
    """

    for i, item in enumerate(data_tampil, start=1):

        html += f"""
        <tr>
            <td>{i}</td>

            <td>
                👤<br>
                <b>{item["nama"]}</b>
            </td>

            <td>
                <div class="bank">{item["logo"]} {item["bank"]}</div>
                <div class="nominal">{item["saldo"]}</div>
            </td>

            <td>
                🏍️<br>
                {item["motor"]}
            </td>

            <td>
                🚗<br>
                {item["mobil"]}
            </td>

            <td style="text-align:left;">
                {item["ket"]}
            </td>

        </tr>
        """

    html += """
        </tbody>
    </table>
    """

    st.markdown(html, unsafe_allow_html=True)

st.markdown(
"""
<div style="text-align:center;
margin-top:25px;
color:gray;
font-size:14px;">

Made with ❤️ Streamlit

</div>
""",
unsafe_allow_html=True)
