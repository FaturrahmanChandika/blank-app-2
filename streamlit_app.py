import streamlit as st
import random
import hashlib
import time

# ============================================
# KONFIGURASI
# ============================================

st.set_page_config(
    page_title="🎉 Aplikasi Tebak Hiburan",
    page_icon="🎉",
    layout="wide"
)

# ============================================
# CSS PREMIUM
# ============================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

html,body,[class*="css"]{
font-family:'Poppins',sans-serif;
}

.stApp{
background:linear-gradient(135deg,#6C63FF,#5EC8FF);
}

.block-container{
padding-top:30px;
padding-bottom:30px;
}

.title{

text-align:center;

font-size:52px;

font-weight:700;

color:white;

margin-bottom:0;

}

.sub{

text-align:center;

font-size:20px;

color:white;

margin-bottom:25px;

}

.stButton>button{

width:100%;

height:60px;

font-size:22px;

font-weight:bold;

background:linear-gradient(90deg,#FF6A00,#EE0979);

border:none;

border-radius:15px;

color:white;

transition:.3s;

}

.stButton>button:hover{

transform:scale(1.02);

}

.card{

background:white;

border-radius:18px;

padding:18px;

box-shadow:0 8px 20px rgba(0,0,0,.18);

margin-bottom:15px;

text-align:center;

}

.card-title{

font-size:17px;

color:#666;

}

.card-value{

font-size:28px;

font-weight:bold;

color:#5E35B1;

margin-top:8px;

}

.footer{

text-align:center;

color:white;

margin-top:25px;

font-size:15px;

}

</style>
""",unsafe_allow_html=True)

# ============================================
# JUDUL
# ============================================

st.markdown(
"<div class='title'>🎉 APLIKASI TEBAK HIBURAN 🎉</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='sub'>Masukkan nama temanmu dan lihat hasil hiburannya 😆</div>",
unsafe_allow_html=True
)

nama = st.text_input(
"",
placeholder="Masukkan Nama..."
)

# ============================================
# DATA
# ============================================

STATUS = [
"Jomblo 😎",
"Pacaran ❤️",
"HTS 🤭",
"Rahasia 🤫",
"Move On 😌",
"Fokus Cari Uang 💰"
]

# DATA INI AKAN DILANJUTKAN DI PART 2

HOBBY = [
"Main Mobile Legends",
"Main PUBG",
"Main Free Fire",
"Ngopi"
]

MOBIL = [
"Toyota Fortuner",
"Honda Brio",
"Pajero Sport",
"BMW M4"
]

MOTOR = [
"Honda PCX",
"Yamaha NMAX",
"Honda Beat",
"ZX25R"
]

RUMAH = [
"Rumah Minimalis",
"Rumah Modern",
"Villa",
"Apartemen"
]

PEKERJAAN = [
"Programmer",
"Dokter",
"Pengusaha",
"Content Creator"
]

KOMENTAR = [
"Rezekimu bagus, tinggal rajin usaha 😄",
"Aura sultan mulai terlihat 👑",
"Kalau ada promo pasti langsung checkout 😂",
"Temanmu yakin kamu bakal sukses 💪"
]

# ============================================
# GENERATOR
# ============================================

def generate_data(nama):

    seed = int(
        hashlib.md5(
            nama.lower().encode()
        ).hexdigest(),16
    )

    random.seed(seed)

    return{

        "saldo":random.randint(
            500000,
            200000000000
        ),

        "status":random.choice(
            STATUS
        ),

        "nikah":random.randint(
            2027,
            2038
        ),

        "mobil":random.choice(
            MOBIL
        ),

        "motor":random.choice(
            MOTOR
        ),

        "rumah":random.choice(
            RUMAH
        ),

        "hobby":random.choice(
            HOBBY
        ),

        "pekerjaan":random.choice(
            PEKERJAAN
        ),

        "hoki":random.randint(
            1,
            100
        ),

        "komentar":random.choice(
            KOMENTAR
        )

    }

# ============================================
# CARD
# ============================================

def card(judul,nilai):

    st.markdown(f"""

<div class="card">

<div class="card-title">

{judul}

</div>

<div class="card-value">

{nilai}

</div>

</div>

""",unsafe_allow_html=True)

# ============================================
# TOMBOL
# ============================================

if st.button("🔍 TEBAK SEKARANG"):

    if nama=="":

        st.warning("Masukkan nama terlebih dahulu.")

    else:

        progress = st.progress(0)

        info = st.empty()

        proses = [

        "🤖 Menghubungkan AI",

        "📡 Mengambil Data",

        "🔎 Membaca Aura",

        "🎉 Hampir Selesai"

        ]

        for i in range(100):

            progress.progress(i+1)

            if i<25:
                info.write(proses[0])

            elif i<50:
                info.write(proses[1])

            elif i<75:
                info.write(proses[2])

            else:
                info.write(proses[3])

            time.sleep(0.003)

        progress.empty()

        info.empty()

        hasil = generate_data(nama)

        st.balloons()

        st.success("🎊 HASIL BERHASIL DITEMUKAN")

        kiri,kanan = st.columns(2)

        with kiri:

            card("👤 Nama",nama)

            card("❤️ Status",hasil["status"])

            card("🎮 Hobi",hasil["hobby"])

            card("🚗 Mobil",hasil["mobil"])

            card("🏠 Rumah",hasil["rumah"])

        with kanan:

            card(
                "💰 Saldo",
                "Rp {:,}".format(
                    hasil["saldo"]
                ).replace(",",".")
            )

            card("💍 Nikah",hasil["nikah"])

            card(
                "🍀 Keberuntungan",
                str(hasil["hoki"])+" %"
            )

            card("🛵 Motor",hasil["motor"])

            card(
                "💼 Pekerjaan",
                hasil["pekerjaan"]
            )

        st.markdown("## 😂 Keterangan")

        st.info(
            hasil["komentar"]
        )

st.markdown("""

<div class="footer">

⚠️ Dibuat hanya untuk hiburan.

</div>

""",unsafe_allow_html=True)
