import streamlit as st
import random
import hashlib
import time

# ==========================================
# KONFIGURASI
# ==========================================

st.set_page_config(
    page_title="AI Tebak Hiburan",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# CSS PREMIUM
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

*{
font-family:'Poppins',sans-serif;
}

.stApp{

background:linear-gradient(
135deg,
#4f46e5,
#2563eb,
#06b6d4
);

background-size:400% 400%;

animation:bg 12s ease infinite;

}

@keyframes bg{

0%{background-position:0% 50%;}

50%{background-position:100% 50%;}

100%{background-position:0% 50%;}

}

.block-container{

padding-top:30px;

padding-bottom:40px;

max-width:1200px;

}

.title{

font-size:55px;

font-weight:800;

text-align:center;

color:white;

margin-bottom:5px;

text-shadow:0px 4px 15px rgba(0,0,0,.35);

}

.sub{

text-align:center;

font-size:20px;

color:white;

margin-bottom:35px;

opacity:.95;

}

div[data-baseweb="input"]{

background:rgba(255,255,255,.15);

backdrop-filter:blur(15px);

border-radius:18px;

border:1px solid rgba(255,255,255,.25);

}

div[data-baseweb="input"] input{

color:white;

font-size:20px;

font-weight:600;

}

div[data-baseweb="input"] input::placeholder{

color:#eeeeee;

}

.stButton>button{

width:100%;

height:62px;

border:none;

border-radius:18px;

font-size:22px;

font-weight:700;

background:linear-gradient(
90deg,
#ff6b00,
#ff0066
);

color:white;

box-shadow:0 10px 25px rgba(0,0,0,.25);

transition:.3s;

}

.stButton>button:hover{

transform:scale(1.02);

box-shadow:0 12px 35px rgba(0,0,0,.35);

}

.card{

background:rgba(255,255,255,.18);

backdrop-filter:blur(18px);

border:1px solid rgba(255,255,255,.25);

border-radius:22px;

padding:20px;

margin-bottom:18px;

text-align:center;

box-shadow:0 10px 25px rgba(0,0,0,.25);

transition:.3s;

}

.card:hover{

transform:translateY(-4px);

}

.card-title{

font-size:17px;

font-weight:600;

color:#F3F4F6;

margin-bottom:10px;

}

.card-value{

font-size:30px;

font-weight:800;

color:white;

word-wrap:break-word;

}

.footer{

text-align:center;

color:white;

opacity:.9;

margin-top:40px;

font-size:15px;

}

hr{

border:none;

height:1px;

background:rgba(255,255,255,.25);

margin:30px 0;

}

</style>
""",unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown("""

<div class="title">

🤖 AI TEBAK KEHIDUPAN 🤖

</div>

<div class="sub">

Masukkan nama • AI akan membaca aura keberuntunganmu 😎

</div>

""",unsafe_allow_html=True)

nama = st.text_input(

"",

placeholder="Masukkan Nama..."

)

st.markdown("<br>",unsafe_allow_html=True)

# ==========================================
# DATABASE
# ==========================================

STATUS = [

"Jomblo 😎",
"Pacaran ❤️",
"HTS 🤭",
"Move On 😌",
"Single Bahagia 😁",
"Menikah 💍",
"LDR 🌍",
"Rahasia 🤫",
"Fokus Cari Uang 💰",
"Gebetan Banyak 😆"

]

HOBBY = [

"Main Mobile Legends",
"Main PUBG",
"Main Free Fire",
"Main Valorant",
"Main Roblox",
"Main FC Mobile",
"Main GTA V",
"Ngopi",
"Nonton Anime",
"Nonton Film",
"Nonton Drakor",
"Traveling",
"Mancing",
"Gym",
"Jogging",
"Badminton",
"Basket",
"Futsal",
"Berenang",
"Sepeda",
"Motoran",
"Mobilan",
"Fotografi",
"Masak",
"Kulineran",
"Streaming",
"TikTok",
"YouTube",
"Main Gitar",
"Nyanyi",
"Tidur",
"Belanja",
"Main Catur",
"Coding",
"Edit Video"

]

MOBIL = [

"Honda Brio",
"Honda Jazz",
"Honda City",
"Honda Civic Turbo",
"Honda HR-V",
"Honda CR-V",

"Toyota Agya",
"Toyota Raize",
"Toyota Avanza",
"Toyota Rush",
"Toyota Fortuner",
"Toyota Innova Zenix",
"Toyota Alphard",

"Mitsubishi Xpander",
"Mitsubishi Pajero Sport",

"Suzuki XL7",
"Suzuki Ertiga",

"Daihatsu Rocky",
"Daihatsu Terios",

"Wuling Air EV",
"Wuling Alvez",

"Hyundai Creta",
"Hyundai Stargazer",
"Hyundai Ioniq 5",

"Kia Sonet",

"BMW M3",
"BMW M4",
"BMW X5",

"Mercedes C200",
"Mercedes E300",
"Mercedes G63 AMG",

"Audi RS6",

"Lexus RX",

"Tesla Model 3",

"Porsche 911",

"Nissan GTR",

"Ferrari 488",

"Lamborghini Huracan",

"McLaren 720S",

"Rolls Royce Phantom"

]

MOTOR = [

"Honda Beat",
"Honda Scoopy",
"Honda Genio",
"Honda Vario 125",
"Honda Vario 160",
"Honda PCX",
"Honda ADV160",
"Honda CB150R",
"Honda CBR150R",
"Honda CBR250RR",

"Yamaha Mio",
"Yamaha Gear",
"Yamaha Fazzio",
"Yamaha Lexi",
"Yamaha NMAX",
"Yamaha Aerox",
"Yamaha XMAX",
"Yamaha MT15",
"Yamaha R15",
"Yamaha R25",

"Kawasaki Ninja 250",
"Kawasaki ZX25R",
"Kawasaki ZX6R",

"Suzuki GSX150",
"Suzuki Satria FU",

"Vespa Sprint",
"Vespa Primavera",

"Harley Davidson",

"BMW S1000RR",

"Ducati Panigale",

"KTM Duke 390",

"Triumph Street Triple"

]

PEKERJAAN = [

"Programmer",
"Software Engineer",
"Dokter",
"Pilot",
"Polisi",
"TNI",
"CEO",
"Pengusaha",
"Content Creator",
"TikToker",
"YouTuber",
"Streamer",
"Guru",
"Dosen",
"Barista",
"Chef",
"Animator",
"Desainer Grafis",
"Fotografer",
"Editor Video",
"Data Analyst",
"AI Engineer",
"Cyber Security",
"Trader",
"Investor",
"Marketing",
"Manager",
"Arsitek",
"Freelancer",
"Akuntan",
"Notaris",
"Hakim",
"Jaksa",
"Influencer",
"UI/UX Designer"

]

KOMENTAR = [

"Rezekimu lagi deras hari ini 💰",
"Sebentar lagi jadi sultan 👑",
"Rajin usaha ya, hasilnya mantap 💪",
"Dompetmu bakal makin tebal 😎",
"Jangan lupa bahagiakan orang tua ❤️",
"Temanmu yakin kamu bakal sukses 🚀",
"Mobil impian tinggal menunggu waktu 🚗",
"Kerja keras tidak mengkhianati hasil 💯",
"Keberuntungan sedang berpihak kepadamu 🍀",
"Tetap rendah hati ya 😄",
"Kalau kaya jangan lupa traktir 🤣",
"Semoga semua impianmu tercapai 🤲",
"Rezeki datang dari arah yang tak terduga ✨",
"Jangan boros ya 😆",
"Tahun ini banyak hoki 🔥",
"Kamu cocok jadi bos besar 😎",
"Aura suksesmu mulai terlihat 😁",
"Semoga cepat punya rumah impian 🏠",
"Dompetmu anti tipis 💸",
"Semoga semua urusanmu dipermudah 🙏"

]

# ==========================================
# AI GENERATOR
# ==========================================

def generate_data(nama):

    seed = int(
        hashlib.sha256(
            nama.lower().encode()
        ).hexdigest(),16
    )

    random.seed(seed)

    return{

        "saldo":random.randint(
            500_000,
            250_000_000_000
        ),

        "status":random.choice(
            STATUS
        ),

        "mobil":random.choice(
            MOBIL
        ),

        "motor":random.choice(
            MOTOR
        ),

        "pekerjaan":random.choice(
            PEKERJAAN
        ),

        "hobby":random.choice(
            HOBBY
        ),

        "komentar":random.choice(
            KOMENTAR
        )

    }


# ==========================================
# FORMAT RUPIAH
# ==========================================

def rupiah(angka):

    return "Rp {:,}".format(
        angka
    ).replace(",", ".")


# ==========================================
# CARD PREMIUM
# ==========================================

def card(icon, judul, nilai):

    st.markdown(f"""
    <div class="card">

        <div style="
        font-size:22px;
        margin-bottom:8px;">
        {icon}
        </div>

        <div class="card-title">
        {judul}
        </div>

        <div class="card-value">
        {nilai}
        </div>

    </div>
    """, unsafe_allow_html=True)

def garis():

    st.markdown("<hr>",unsafe_allow_html=True)

# ==========================================
# TOMBOL AI
# ==========================================

if st.button("🔍 TEBAK SEKARANG"):

    if nama.strip() == "":

        st.warning("⚠️ Silakan masukkan nama terlebih dahulu.")

    else:

        progress = st.progress(0)

        status = st.empty()

        proses = [

            "🤖 Menghubungkan AI...",
            "📡 Mengambil Database...",
            "🧠 Menganalisa Nama...",
            "💰 Menghitung Saldo...",
            "🚗 Menentukan Kendaraan...",
            "💼 Menentukan Pekerjaan...",
            "🎮 Mencari Hobi...",
            "✨ Menyelesaikan Analisa..."

        ]

        for i in range(100):

            progress.progress(i + 1)

            if i < 12:
                status.info(proses[0])

            elif i < 25:
                status.info(proses[1])

            elif i < 40:
                status.info(proses[2])

            elif i < 55:
                status.info(proses[3])

            elif i < 70:
                status.info(proses[4])

            elif i < 82:
                status.info(proses[5])

            elif i < 94:
                status.info(proses[6])

            else:
                status.success(proses[7])

            time.sleep(0.02)

        progress.empty()

        status.empty()

        hasil = generate_data(nama)

        st.balloons()

        st.success("🎉 Analisa AI Berhasil!")

        garis()

        kiri, kanan = st.columns(2)

        with kiri:

            card(
                "👤",
                "Nama",
                nama.title()
            )

            card(
                "❤️",
                "Status",
                hasil["status"]
            )

            saldo = hasil["saldo"]

if saldo >= 1000000000:

    icon = "👑"

elif saldo >= 100000000:

    icon = "💎"

elif saldo >= 10000000:

    icon = "💰"

else:

    icon = "💵"

card(
    icon,
    "Saldo Bank",
    rupiah(saldo)
)
            )

        with kanan:

            card(
                "🚗",
                "Mobil",
                hasil["mobil"]
            )

            card(
                "🛵",
                "Motor",
                hasil["motor"]
            )

            card(
                "💼",
                "Pekerjaan",
                hasil["pekerjaan"]
            )

        card(
            "🎮",
            "Hobi",
            hasil["hobby"]
        )

        st.markdown("## 😂 Keterangan")

        st.info(
            hasil["komentar"]
        )

        garis()

# ==========================================
# FOOTER
# ==========================================

st.markdown("""

<div class="footer">

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 AI Tebak Kehidupan

Dibuat hanya untuk hiburan 🎉

Jangan dianggap serius 😆

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

</div>

""",unsafe_allow_html=True)
