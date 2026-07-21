import streamlit as st
import random
import hashlib

st.set_page_config(
    page_title="Aplikasi Tebak Isi Saldo",
    layout="wide"
)

# =========================
# SESSION
# =========================
if "rows" not in st.session_state:
    st.session_state.rows = []

# =========================
# DATA
# =========================
BANK = [
    ("BCA", "🏦"),
    ("BRI", "🏦"),
    ("BNI", "🏦"),
    ("Mandiri", "🏦"),
    ("CIMB Niaga", "🏦"),
    ("Permata", "🏦"),
    ("Danamon", "🏦"),
    ("DANA", "🔵"),
    ("OVO", "🟣"),
    ("GoPay", "🟢")
]

MOTOR = [
    "Honda Beat","Beat Street","Scoopy","Genio","Vario 125","Vario 160",
    "PCX160","ADV160","NMAX","Aerox","XMAX","CBR150R","CB150R",
    "Ninja250","KLX150","Vespa Sprint","Fazzio","Gear"
]

MOBIL = [
    "Brio","Agya","Ayla","Avanza","Xenia","Rush","Terios","Raize",
    "Rocky","Innova Zenix","Fortuner","Pajero","HR-V","CR-V",
    "BR-V","Camry","Alphard","BMW X5","Jimny","Creta"
]

KET = [
    "😎 Kelihatannya sederhana, tapi isi rekeningnya bikin penasaran.",
    "💰 Rajin menabung sejak lama.",
    "🚀 Rezekinya lagi deras.",
    "👑 Diam-diam sultan.",
    "🎉 Akhir bulan tetap senyum.",
    "🔥 Dompet tipis, rekening tebal.",
    "😆 Hati tenang karena saldo aman.",
    "💎 Sultan mode aktif."
]

ROW_COLORS = [
    "#ffe4e6",
    "#fef3c7",
    "#dcfce7",
    "#dbeafe",
    "#ede9fe",
    "#fce7f3",
    "#cffafe",
    "#fae8ff",
    "#fef9c3",
    "#ecfccb"
]

# =========================
# CSS
# =========================
st.markdown("""
<style>

/* Background warna-warni */
.stApp{
background:
linear-gradient(135deg,#ff9a9e 0%,#fad0c4 20%,#fbc2eb 40%,#a18cd1 60%,#84fab0 80%,#8fd3f4 100%);
background-attachment:fixed;
}

/* Judul */
.title{
background:linear-gradient(90deg,#ff512f,#dd2476,#7b2ff7,#00c6ff,#00f260);
padding:18px;
border-radius:18px;
text-align:center;
font-size:38px;
font-weight:bold;
color:white;
box-shadow:0 5px 20px rgba(0,0,0,.25);
}

/* Input */
div[data-testid="stTextInput"] input{
height:64px;
font-size:22px;
border-radius:12px;
border:3px solid #2f63e0;
}

/* Samakan tinggi input dengan tombol */
div[data-testid="stTextInput"]{
margin-top:0px;
}

.stButton>button{
height:64px;
font-size:20px;
font-weight:bold;
border-radius:12px;
}

/* Table */
.t{
width:100%;
border-collapse:collapse;
font-size:18px;
}

.t th{
padding:14px;
color:white;
background:linear-gradient(90deg,#2563eb,#7c3aed,#db2777);
}

.t td{
padding:14px;
text-align:center;
border:1px solid rgba(255,255,255,.3);
font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown(
"""
<div class="title">
💰 APLIKASI TEBAK ISI SALDO 💰
</div><br>
""",
unsafe_allow_html=True
)

# =========================
# INPUT
# =========================
c1, c2, c3 = st.columns([3,2,2])

with c1:
    nama = st.text_input(
        "",
        placeholder="🔍 Tulis Nama...",
        label_visibility="collapsed"
    )

with c2:
    tebak = st.button("🎲 Tebak Saldo", use_container_width=True)

with c3:
    if st.button("🗑 Hapus Semua", use_container_width=True):
        st.session_state.rows = []
        st.rerun()

# =========================
# GENERATE
# =========================
if tebak and nama.strip():

    random.seed(
        int(hashlib.md5(nama.lower().encode()).hexdigest(),16)
    )

    row = {
        "nama": nama.upper(),
        "bank": random.choice(BANK),
        "saldo":"Rp {:,}".format(
            random.randint(100000,500000000)
        ).replace(",","."),
        "motor": random.choice(MOTOR),
        "mobil": random.choice(MOBIL),
        "ket": random.choice(KET)
    }

    st.session_state.rows = [
        r for r in st.session_state.rows
        if r["nama"] != row["nama"]
    ]

    st.session_state.rows.insert(0,row)

# =========================
# TABLE
# =========================
html = """
<table class='t'>
<tr>
<th width="6%">No</th>
<th width="18%">Nama</th>
<th width="22%">Isi Saldo</th>
<th width="18%">Motor</th>
<th width="18%">Mobil</th>
<th width="18%">Keterangan</th>
</tr>
"""

for i, r in enumerate(st.session_state.rows):

    warna = ROW_COLORS[i % len(ROW_COLORS)]

    html += f"""
    <tr style="background:{warna}">
        <td>{i+1}</td>
        <td><b>{r['nama']}</b></td>
        <td>
            {r['bank'][1]} <b>{r['bank'][0]}</b><br>
            <span style="font-size:22px;color:#1d4ed8">
            {r['saldo']}
            </span>
        </td>
        <td>🏍️ {r['motor']}</td>
        <td>🚗 {r['mobil']}</td>
        <td>{r['ket']}</td>
    </tr>
    """

html += "</table>"

st.markdown(html, unsafe_allow_html=True)
