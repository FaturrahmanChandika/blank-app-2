import streamlit as st
import random
import hashlib

st.set_page_config(
    page_title="Aplikasi Tebak Isi Saldo",
    page_icon="💰",
    layout="wide"
)

# ==============================
# SESSION
# ==============================

if "data" not in st.session_state:
    st.session_state.data = []

# ==============================
# CSS
# ==============================

st.markdown("""
<style>

*{
font-family:Segoe UI,Tahoma,sans-serif;
}

.stApp{

background:#f4f7fb;

}

/* sembunyikan menu streamlit */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* HEADER */

.header{

background:linear-gradient(90deg,#2563eb,#4f46e5);

padding:18px;

border-radius:18px;

text-align:center;

color:white;

font-size:34px;

font-weight:bold;

box-shadow:0 8px 25px rgba(0,0,0,.18);

margin-bottom:20px;

}

/* SEARCH */

div[data-testid="stTextInput"] input{

height:52px;

border-radius:30px;

border:2px solid #2563eb;

padding-left:18px;

font-size:18px;

background:white;

}

/* BUTTON */

.stButton>button{

height:52px;

width:100%;

background:#ef4444;

color:white;

border:none;

border-radius:12px;

font-size:16px;

font-weight:bold;

transition:.25s;

}

.stButton>button:hover{

background:#dc2626;

color:white;

transform:scale(1.02);

}

/* TABLE */

table{

width:100%;

border-collapse:collapse;

overflow:hidden;

border-radius:16px;

box-shadow:0 8px 25px rgba(0,0,0,.15);

background:white;

}

thead tr{

background:#16a34a;

color:white;

}

th{

padding:15px;

font-size:17px;

}

td{

padding:15px;

border-bottom:1px solid #e5e7eb;

text-align:center;

font-size:16px;

}

tbody tr:nth-child(even){

background:#f8fff9;

}

tbody tr:hover{

background:#dcfce7;

transition:.2s;

}

/* BANK */

.bank{

font-weight:bold;

font-size:17px;

color:#2563eb;

}

.saldo{

font-size:22px;

font-weight:bold;

color:#059669;

margin-top:5px;

}

.ket{

text-align:left;

}

</style>
""",unsafe_allow_html=True)

# ==============================
# HEADER
# ==============================

st.markdown("""

<div class='header'>

💰 APLIKASI TEBAK ISI SALDO 💰

</div>

""",unsafe_allow_html=True)

# ==============================
# DATA
# ==============================

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
"🔥 Rajin nabung sejak kecil.",
"💸 Dompet selalu penuh.",
"🤣 Gaji cuma numpang lewat.",
"😅 Jangan pinjem uang ke dia.",
"🤑 Saldo bikin tetangga iri.",
"👑 Bos kecil tapi rekening besar.",
"💰 Isi rekening anti tanggal tua.",
"😆 Orangnya sederhana, saldonya luar biasa."

]

# =====================================================
# SEARCH + BUTTON
# =====================================================

col1, col2, col3 = st.columns([6,2,2])

with col1:
    keyword = st.text_input(
        "",
        placeholder="🔍 Cari nama...",
        label_visibility="collapsed"
    )

with col2:

    tebak = st.button(
        "🎲 Tebak Saldo",
        use_container_width=True
    )

with col3:

    hapus = st.button(
        "🗑 Hapus Semua",
        use_container_width=True
    )

# =====================================================
# HAPUS DATA
# =====================================================

if hapus:
    st.session_state.data = []
    st.rerun()

# =====================================================
# TAMBAH DATA BARU
# =====================================================

if tebak:

    if keyword.strip() == "":

        st.warning("Masukkan nama terlebih dahulu.")

    else:

        # supaya nama yang sama hasilnya selalu sama

        seed = int(
            hashlib.md5(
                keyword.lower().encode()
            ).hexdigest(),
            16
        )

        random.seed(seed)

        bank = random.choice(BANK)

        motor = random.choice(MOTOR)

        mobil = random.choice(MOBIL)

        ket = random.choice(KETERANGAN)

        saldo = random.randint(
            50000,
            500000000
        )

        saldo = "Rp {:,}".format(saldo).replace(",", ".")

        # jangan menambah nama yang sama

        sudah_ada = False

        for item in st.session_state.data:

            if item["nama"].lower() == keyword.lower():

                sudah_ada = True

                break

        if not sudah_ada:

            st.session_state.data.append(

                {

                    "nama": keyword.upper(),

                    "bank": bank[0],

                    "logo": bank[1],

                    "saldo": saldo,

                    "motor": motor,

                    "mobil": mobil,

                    "ket": ket

                }

            )

# =====================================================
# FILTER PENCARIAN
# =====================================================

if keyword.strip() == "":

    hasil = st.session_state.data

else:

    hasil = [

        item

        for item in st.session_state.data

        if keyword.lower()

        in item["nama"].lower()

    ]

# =====================================================
# TABEL HTML
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

if len(hasil) == 0:

    st.info("Belum ada data.")

else:

    html = """

    <table>

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

    for no, item in enumerate(hasil, start=1):

        html += f"""

        <tr>

            <td><b>{no}</b></td>

            <td>

                👤<br>

                <b>{item['nama']}</b>

            </td>

            <td>

                <div class="bank">

                    {item['logo']} {item['bank']}

                </div>

                <div class="saldo">

                    {item['saldo']}

                </div>

            </td>

            <td>

                🏍️<br>

                {item['motor']}

            </td>

            <td>

                🚗<br>

                {item['mobil']}

            </td>

            <td class="ket">

                {item['ket']}

            </td>

        </tr>

        """

    html += """

    </tbody>

    </table>

    """

    st.markdown(html, unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown(
"""
<br><br>

<div style="text-align:center;
color:gray;
font-size:14px;">

Dibuat menggunakan ❤️ Streamlit + HTML + CSS

</div>
""",
unsafe_allow_html=True
)
