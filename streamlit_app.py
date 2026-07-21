import streamlit as st
import pandas as pd
import random
import hashlib
import time

# ==========================================
# KONFIGURASI
# ==========================================

st.set_page_config(
    page_title="AI Tebak Kehidupan",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# SESSION STATE
# ==========================================

if "history" not in st.session_state:
    st.session_state.history = []

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700;800&display=swap');

html,body,[class*="css"]{
font-family:'Poppins',sans-serif;
}

.stApp{

background:linear-gradient(
135deg,
#4F46E5,
#2563EB,
#06B6D4
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

max-width:1200px;
padding-top:30px;
padding-bottom:40px;

}

.title{

text-align:center;
font-size:52px;
font-weight:800;
color:white;
margin-bottom:5px;
text-shadow:0 5px 15px rgba(0,0,0,.35);

}

.sub{

text-align:center;
font-size:18px;
color:white;
margin-bottom:30px;
opacity:.95;

}

div[data-baseweb="input"]{

background:rgba(255,255,255,.15);
backdrop-filter:blur(15px);
border-radius:15px;
border:1px solid rgba(255,255,255,.25);

}

div[data-baseweb="input"] input{

font-size:20px;
font-weight:600;
color:white;

}

div[data-baseweb="input"] input::placeholder{

color:#eeeeee;

}

.stButton>button{

width:100%;
height:55px;
border:none;
border-radius:15px;
font-size:20px;
font-weight:bold;
background:linear-gradient(90deg,#ff6b00,#ff0066);
color:white;
transition:.3s;

}

.stButton>button:hover{

transform:scale(1.02);

}

.card{

background:rgba(255,255,255,.16);
backdrop-filter:blur(16px);
border-radius:18px;
padding:18px;
margin-bottom:15px;
border:1px solid rgba(255,255,255,.20);

}

.card-title{

font-size:16px;
font-weight:600;
color:#F1F5F9;

}

.card-value{

font-size:26px;
font-weight:800;
color:white;
margin-top:8px;
word-wrap:break-word;

}

.footer{

text-align:center;
color:white;
opacity:.8;
margin-top:40px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="title">
🤖 AI TEBAK KEHIDUPAN
</div>

<div class="sub">
Masukkan nama lalu biarkan AI menebak kehidupanmu 😎
</div>
""", unsafe_allow_html=True)

nama = st.text_input(
"",
placeholder="Masukkan Nama..."
)

# ==========================================
# DATABASE BANK
# ==========================================

BANK = [

"BCA",
"BRI",
"BNI",
"Mandiri",
"BTN",
"CIMB Niaga",
"Permata",
"Danamon",
"BSI",
"OCBC",
"Maybank",
"Panin Bank",
"Mega",
"Jago",
"SeaBank",
"Neo Bank",
"Allo Bank",
"HSBC",
"DBS",
"UOB"

]

# ==========================================
# DATABASE STATUS
# ==========================================

STATUS = [

"Jomblo 😎",
"Pacaran ❤️",
"HTS 🤭",
"Move On 😌",
"Menikah 💍",
"LDR 🌍",
"Single Bahagia 😁",
"Rahasia 🤫"

]

# ==========================================
# DATABASE MOBIL
# ==========================================

MOBIL = [

"Honda Brio",
"Honda Jazz",
"Honda City",
"Honda Civic Turbo",
"Honda Accord",
"Honda WR-V",
"Honda HR-V",
"Honda CR-V",

"Toyota Agya",
"Toyota Calya",
"Toyota Avanza",
"Toyota Veloz",
"Toyota Rush",
"Toyota Raize",
"Toyota Innova Reborn",
"Toyota Innova Zenix",
"Toyota Fortuner",
"Toyota Camry",
"Toyota Alphard",

"Mitsubishi Xpander",
"Mitsubishi Pajero Sport",
"Mitsubishi Triton",

"Suzuki Ertiga",
"Suzuki XL7",
"Suzuki Jimny",

"Daihatsu Rocky",
"Daihatsu Terios",

"Hyundai Creta",
"Hyundai Stargazer",
"Hyundai Ioniq 5",

"Kia Sonet",
"Kia Seltos",

"Wuling Air EV",
"Wuling Alvez",
"Wuling Almaz",

"Mazda 2",
"Mazda 3",
"Mazda CX3",
"Mazda CX5",

"Nissan Livina",
"Nissan XTrail",
"Nissan GTR",

"BMW M3",
"BMW M4",
"BMW M5",
"BMW X5",

"Mercedes C200",
"Mercedes E300",
"Mercedes G63 AMG",

"Audi A6",
"Audi RS5",
"Audi RS6",

"Lexus RX350",
"Lexus LX600",

"Tesla Model 3",
"Tesla Model Y",

"Porsche 911",
"Porsche Cayenne",

"Ferrari 488",
"Ferrari F8",

"Lamborghini Huracan",
"Lamborghini Aventador",

"McLaren 720S",

"Rolls Royce Phantom",
"Rolls Royce Cullinan"

]
# ==========================================
# DATABASE MOTOR
# ==========================================

MOTOR = [

# Honda
"Honda Beat","Honda Beat Street","Honda Scoopy","Honda Genio",
"Honda Vario 125","Honda Vario 160","Honda PCX 160",
"Honda ADV160","Honda Supra X","Honda Sonic 150R",
"Honda CB150R","Honda CBR150R","Honda CBR250RR",

# Yamaha
"Yamaha Mio M3","Yamaha Gear","Yamaha Fazzio",
"Yamaha Lexi","Yamaha NMAX","Yamaha Aerox",
"Yamaha XMAX","Yamaha Jupiter Z1","Yamaha MX King",
"Yamaha MT15","Yamaha R15","Yamaha R25",

# Kawasaki
"Kawasaki Ninja 250",
"Kawasaki ZX25R",
"Kawasaki ZX6R",
"Kawasaki ZX10R",
"Kawasaki W175",

# Suzuki
"Suzuki Satria FU",
"Suzuki GSX150",
"Suzuki Burgman",

# Vespa
"Vespa Sprint",
"Vespa Primavera",
"Vespa GTS",

# Premium
"BMW S1000RR",
"Ducati Panigale",
"Ducati Monster",
"Harley Davidson Street 750",
"Harley Davidson Fat Boy",
"KTM Duke 390",
"KTM RC390",
"Triumph Street Triple",
"Royal Enfield Himalayan"

]

# ==========================================
# DATABASE PEKERJAAN
# ==========================================

PEKERJAAN = [

"Programmer",
"Software Engineer",
"Web Developer",
"Mobile Developer",
"Frontend Developer",
"Backend Developer",
"Fullstack Developer",
"AI Engineer",
"Machine Learning Engineer",
"Data Scientist",
"Data Analyst",
"Cyber Security",
"Network Engineer",
"Cloud Engineer",
"DevOps Engineer",
"UI UX Designer",
"Game Developer",
"QA Engineer",
"System Analyst",
"Dokter",
"Dokter Gigi",
"Perawat",
"Apoteker",
"Bidan",
"Guru",
"Dosen",
"Pilot",
"Pramugari",
"Masinis",
"Nahkoda",
"Polisi",
"TNI",
"Hakim",
"Jaksa",
"Notaris",
"Pengusaha",
"CEO",
"Direktur",
"Manager",
"Supervisor",
"HRD",
"Marketing",
"Sales",
"Akuntan",
"Auditor",
"Arsitek",
"Interior Designer",
"Chef",
"Barista",
"Fotografer",
"Videografer",
"Editor Video",
"Animator",
"Desainer Grafis",
"YouTuber",
"Streamer",
"TikToker",
"Influencer",
"Content Creator",
"Trader",
"Investor",
"Freelancer"

]

# ==========================================
# DATABASE HOBI
# ==========================================

HOBBY = [

"Coding",
"Main Mobile Legends",
"Main PUBG",
"Main Free Fire",
"Main Valorant",
"Main Roblox",
"Main Minecraft",
"Main GTA V",
"Main FC Mobile",
"Main eFootball",
"Nonton Anime",
"Nonton Film",
"Nonton Drakor",
"Kulineran",
"Traveling",
"Ngopi",
"Fotografi",
"Videografi",
"Memancing",
"Camping",
"Hiking",
"Gym",
"Jogging",
"Renang",
"Basket",
"Badminton",
"Futsal",
"Sepak Bola",
"Voli",
"Bersepeda",
"Touring",
"Drifting",
"Balap Motor",
"Main Gitar",
"Main Piano",
"Bernyanyi",
"Melukis",
"Membaca Buku",
"Streaming",
"Edit Video",
"Belanja",
"Masak",
"Berkebun",
"Main Catur",
"Tidur"

]

# ==========================================
# HP IMPIAN
# ==========================================

HP = [

"iPhone 16 Pro Max",
"iPhone 16 Pro",
"iPhone 15 Pro Max",
"Samsung S25 Ultra",
"Samsung Z Fold 7",
"Samsung Z Flip 7",
"Xiaomi 15 Ultra",
"Xiaomi 15 Pro",
"Redmi Note 14 Pro",
"POCO F7",
"POCO X7 Pro",
"ASUS ROG Phone 9",
"ASUS Zenfone",
"OPPO Find X8 Pro",
"OPPO Reno 14 Pro",
"Vivo X200 Pro",
"Vivo V50",
"Realme GT 7 Pro",
"Huawei Pura 70 Ultra",
"Google Pixel 9 Pro"

]

# ==========================================
# RUMAH IMPIAN
# ==========================================

RUMAH = [

"Rumah Minimalis",
"Rumah Modern",
"Rumah Mewah",
"Villa Bali",
"Penthouse Jakarta",
"Rumah Pinggir Pantai",
"Rumah Pegunungan",
"Rumah Smart Home",
"Rumah 2 Lantai",
"Istana Pribadi"

]

# ==========================================
# NEGARA LIBURAN
# ==========================================

NEGARA = [

"Jepang",
"Korea Selatan",
"Swiss",
"Dubai",
"Amerika Serikat",
"Inggris",
"Prancis",
"Italia",
"Turki",
"Singapura",
"Malaysia",
"Thailand",
"Australia",
"Selandia Baru",
"Kanada",
"Maladewa",
"Arab Saudi",
"Belanda",
"Jerman",
"Spanyol"

]

# ==========================================
# KOMENTAR AI
# ==========================================

KOMENTAR = [

"Rezekimu sedang deras 💸",
"Sebentar lagi jadi sultan 👑",
"Kerja kerasmu akan membuahkan hasil 💪",
"Dompetmu anti tipis 😎",
"Tahun ini penuh keberuntungan 🍀",
"Semoga cepat punya rumah impian 🏡",
"Mobil impian tinggal menunggu waktu 🚗",
"Jangan lupa bahagiakan orang tua ❤️",
"Kalau sukses jangan lupa traktir 🤣",
"Aura tajirmu mulai kelihatan ✨",
"Rezeki datang dari arah yang tak terduga 🤲",
"Semoga semua impianmu tercapai 🚀",
"Banyak peluang besar menunggumu 📈",
"Kamu cocok jadi bos besar 😁",
"Semoga kariermu makin sukses 💼",
"Jangan lupa tetap rendah hati 😊",
"Keberuntungan sedang berpihak kepadamu 🍀",
"Dompetmu bakal makin tebal 💰",
"Semoga sehat selalu 🙏",
"Hari ini adalah hari yang bagus untuk memulai sesuatu yang baru 🌟"

]
# ==========================================
# AI GENERATOR
# ==========================================

def generate_data(nama):

    seed = int(
        hashlib.sha256(
            nama.lower().strip().encode()
        ).hexdigest(),
        16
    )

    rnd = random.Random(seed)

    return {

        "nama": nama.title(),

        "bank": rnd.choice(BANK),

        "saldo": rnd.randint(
            500_000,
            25_000_000_000
        ),

        "status": rnd.choice(STATUS),

        "mobil": rnd.choice(MOBIL),

        "motor": rnd.choice(MOTOR),

        "pekerjaan": rnd.choice(PEKERJAAN),

        "hobby": rnd.choice(HOBBY),

        "hp": rnd.choice(HP),

        "rumah": rnd.choice(RUMAH),

        "negara": rnd.choice(NEGARA),

        "keberuntungan": rnd.randint(1,100),

        "komentar": rnd.choice(KOMENTAR)

    }

# ==========================================
# FORMAT RUPIAH
# ==========================================

def rupiah(angka):

    return "Rp {:,}".format(
        angka
    ).replace(",", ".")

# ==========================================
# CARD
# ==========================================

def card(icon,judul,isi):

    st.markdown(f"""
    <div class="card">

        <div class="card-title">
        {icon} {judul}
        </div>

        <div class="card-value">
        {isi}
        </div>

    </div>
    """,unsafe_allow_html=True)

# ==========================================
# GARIS
# ==========================================

def garis():

    st.markdown(
        "<hr style='border:1px solid rgba(255,255,255,.2);'>",
        unsafe_allow_html=True
    )

# ==========================================
# BUTTON
# ==========================================

col1,col2 = st.columns([4,1])

with col1:

    cari = st.button(
        "🔍 TEBAK SEKARANG",
        use_container_width=True
    )

with col2:

    reset = st.button(
        "🗑 HAPUS",
        use_container_width=True
    )

# ==========================================
# RESET
# ==========================================

if reset:

    st.session_state.history=[]

    st.rerun()

# ==========================================
# PROSES AI
# ==========================================

if cari:

    if nama.strip()=="":

        st.warning(
            "Masukkan nama terlebih dahulu."
        )

        st.stop()

    progress=st.progress(0)

    info=st.empty()

    proses=[

        "🤖 Menghubungkan AI...",

        "📡 Mengambil Database...",

        "🧠 Menganalisa Nama...",

        "💰 Menghitung Saldo...",

        "🚗 Menentukan Mobil...",

        "🏍 Menentukan Motor...",

        "💼 Menentukan Pekerjaan...",

        "🎮 Menentukan Hobi...",

        "📱 Menentukan HP Impian...",

        "🏡 Menentukan Rumah...",

        "🌎 Menentukan Negara Liburan...",

        "✨ Menyelesaikan Analisa..."

    ]

    for i in range(100):

        progress.progress(i+1)

        if i<10:
            info.info(proses[0])

        elif i<20:
            info.info(proses[1])

        elif i<30:
            info.info(proses[2])

        elif i<40:
            info.info(proses[3])

        elif i<50:
            info.info(proses[4])

        elif i<60:
            info.info(proses[5])

        elif i<70:
            info.info(proses[6])

        elif i<80:
            info.info(proses[7])

        elif i<88:
            info.info(proses[8])

        elif i<94:
            info.info(proses[9])

        elif i<98:
            info.info(proses[10])

        else:
            info.success(proses[11])

        time.sleep(0.02)

    progress.empty()

    info.empty()

    hasil = generate_data(nama)

    st.session_state.history.append(
        hasil
    )

    st.balloons()

# ==========================================
# TAMPILKAN HASIL
# ==========================================

if len(st.session_state.history) > 0:

    hasil = st.session_state.history[-1]

    garis()

    st.success("🎉 Analisa AI Berhasil!")

    col1, col2 = st.columns(2)

    # ======================================
    # KOLOM KIRI
    # ======================================

    with col1:

        card("👤","Nama",hasil["nama"])

        card("🏦","Bank",hasil["bank"])

        card("💰","Saldo",rupiah(hasil["saldo"]))

        card("❤️","Status",hasil["status"])

        card("🍀","Keberuntungan",
             f'{hasil["keberuntungan"]}%')

    # ======================================
    # KOLOM KANAN
    # ======================================

    with col2:

        card("🚗","Mobil",hasil["mobil"])

        card("🏍","Motor",hasil["motor"])

        card("💼","Pekerjaan",hasil["pekerjaan"])

        card("🎮","Hobi",hasil["hobby"])

        card("📱","HP Impian",hasil["hp"])

    card("🏠","Rumah Impian",hasil["rumah"])

    card("✈️","Negara Liburan",hasil["negara"])

    st.markdown("## 😂 Komentar AI")

    st.info(hasil["komentar"])

    # ======================================
    # LEVEL KEKAYAAN
    # ======================================

    saldo = hasil["saldo"]

    if saldo >= 10_000_000_000:

        st.success("👑 Level Kekayaan : CRAZY RICH")

    elif saldo >= 1_000_000_000:

        st.success("💎 Level Kekayaan : SULTAN")

    elif saldo >= 100_000_000:

        st.success("💰 Level Kekayaan : ORANG KAYA")

    elif saldo >= 10_000_000:

        st.info("😊 Level Kekayaan : MAPAN")

    else:

        st.warning("😅 Level Kekayaan : PEJUANG")

    st.markdown("### 🍀 Tingkat Keberuntungan")

    st.progress(
        hasil["keberuntungan"] / 100
    )

# ==========================================
# RIWAYAT
# ==========================================

garis()

st.subheader("📋 Riwayat Pencarian")

if len(st.session_state.history)==0:

    st.info("Belum ada riwayat.")

else:

    tabel=[]

    for item in st.session_state.history:

        tabel.append({

            "Nama":item["nama"],

            "Bank":item["bank"],

            "Saldo":rupiah(item["saldo"]),

            "Mobil":item["mobil"],

            "Motor":item["motor"],

            "Pekerjaan":item["pekerjaan"],

            "Status":item["status"]

        })

    df=pd.DataFrame(tabel)

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )

# ==========================================
# STATISTIK
# ==========================================

if len(st.session_state.history)>0:

    garis()

    st.subheader("📊 Statistik")

    total=len(st.session_state.history)

    rata=sum(
        x["saldo"]
        for x in st.session_state.history
    )//total

    c1,c2,c3=st.columns(3)

    c1.metric(
        "Jumlah Pencarian",
        total
    )

    c2.metric(
        "Rata-rata Saldo",
        rupiah(rata)
    )

    c3.metric(
        "Saldo Tertinggi",
        rupiah(
            max(
                x["saldo"]
                for x in st.session_state.history
            )
        )
    )

# ==========================================
# FOOTER
# ==========================================

garis()

st.markdown("""

<div class="footer">

🤖 AI Tebak Kehidupan v2.0

Dibuat menggunakan Streamlit

Hanya untuk hiburan 🎉

</div>

""",unsafe_allow_html=True)

