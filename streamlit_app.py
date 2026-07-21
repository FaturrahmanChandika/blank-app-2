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
"Move On 😌",
"Menikah 💍",
"Single Bahagia 😁",
"Masih Galau 😢",
"LDR 🌏",
"Rahasia 🤫",
"Gebetan Banyak 😎",
"Fokus Cari Uang 💰",
"Sibuk Kerja 💼",
"Sultan Lagi Cari Pasangan 👑",
"Menunggu Kepastian 😅",
"Crush Teman Sendiri 🤭",
"Jodoh Sudah Dekat 💕"

]

HOBBY = [

"Main Mobile Legends",
"Main PUBG",
"Main Free Fire",
"Main Valorant",
"Main Roblox",
"Main GTA V",
"Main FC Mobile",
"Main PES",
"Main Stumble Guys",
"Main Clash Royale",
"Ngopi",
"Nonton Anime",
"Nonton Film",
"Nonton Drakor",
"Traveling",
"Fotografi",
"Mancing",
"Berenang",
"Gym",
"Jogging",
"Main Basket",
"Main Futsal",
"Main Badminton",
"Main Voli",
"Main Catur",
"Main Gitar",
"Main Piano",
"Nyanyi",
"Melukis",
"Membaca Novel",
"Makan Seblak",
"Kulineran",
"Masak",
"Ngoding",
"Edit Video",
"TikTok",
"YouTube",
"Streaming",
"Trading",
"Investasi",
"Berkebun",
"Pelihara Kucing",
"Pelihara Burung",
"Pelihara Ikan",
"Motoran",
"Mobilan",
"Camping",
"Hiking",
"Belanja"

]

MOBIL = [

"Honda Brio",
"Honda Jazz",
"Honda City",
"Honda Civic Turbo",
"Honda Accord",
"Honda HRV",
"Honda CRV",

"Toyota Agya",
"Toyota Raize",
"Toyota Calya",
"Toyota Avanza",
"Toyota Rush",
"Toyota Fortuner",
"Toyota Innova Zenix",
"Toyota Alphard",
"Toyota Vellfire",

"Mitsubishi Xpander",
"Mitsubishi Pajero Sport",

"Suzuki Ertiga",
"Suzuki XL7",

"Daihatsu Rocky",
"Daihatsu Terios",

"Wuling Air EV",
"Wuling Alvez",

"Hyundai Stargazer",
"Hyundai Creta",
"Hyundai Ioniq 5",

"Kia Sonet",

"BMW 320i",
"BMW M3",
"BMW M4",
"BMW X5",
"BMW X7",

"Mercedes C200",
"Mercedes E300",
"Mercedes G63 AMG",

"Audi A4",
"Audi RS6",

"Lexus RX",
"Lexus LM",

"Tesla Model 3",
"Tesla Model Y",

"Porsche Cayenne",
"Porsche 911",

"Nissan GTR R35",

"Ferrari 488",
"Ferrari Roma",

"Lamborghini Huracan",
"Lamborghini Aventador",

"McLaren 720S",

"Jeep Rubicon",

"Mini Cooper",

"Rolls Royce Phantom",

"Bentley Bentayga"

]

MOTOR = [

"Honda Beat",
"Honda Genio",
"Honda Scoopy",
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
"Kawasaki ZX10R",

"Suzuki Satria FU",
"Suzuki GSX150",

"Vespa Sprint",
"Vespa Primavera",

"Royal Enfield Classic",

"Harley Davidson Sportster",

"BMW S1000RR",

"Ducati Panigale",

"KTM Duke 390",

"Triumph Street Triple"

]

RUMAH = [

"Rumah Minimalis",
"Rumah Modern",
"Rumah 2 Lantai",
"Rumah Mewah",
"Rumah Smart Home",
"Rumah Pinggir Pantai",
"Rumah Pegunungan",
"Rumah Cluster",
"Villa Bali",
"Villa Puncak",
"Apartemen",
"Penthouse",
"Rumah Kaca",
"Rumah Jepang",
"Rumah Korea",
"Istana Sultan 👑"

]

PEKERJAAN = [

"Programmer",
"Dokter",
"Pilot",
"Pengusaha",
"CEO",
"Content Creator",
"TikToker",
"YouTuber",
"Streamer",
"Data Analyst",
"AI Engineer",
"Polisi",
"TNI",
"Hakim",
"Jaksa",
"Guru",
"Dosen",
"Chef",
"Barista",
"Desainer Grafis",
"Animator",
"Editor Video",
"Fotografer",
"Trader",
"Investor",
"Freelancer",
"Arsitek",
"Marketing",
"Manager",
"Software Engineer",
"Cyber Security",
"Game Developer"

]

KOMENTAR = [

"Rezekimu sedang naik daun 🚀",
"Aura sultanmu mulai terlihat 👑",
"Jangan lupa traktir teman ya 😆",
"Kesuksesan tinggal selangkah lagi 💪",
"Semoga semua impianmu tercapai 🤲",
"Kamu punya peluang jadi orang sukses 💰",
"Dompetmu bakal makin tebal 😎",
"Tetap rendah hati ya 😊",
"Orang baik biasanya rezekinya ikut baik ✨",
"Semoga cepat beli rumah impian 🏠",
"Mobil impianmu tinggal menunggu waktu 🚗",
"Keberuntungan sedang berpihak kepadamu 🍀",
"Rajin usaha, hasilnya luar biasa 💯",
"Temanmu yakin kamu bakal kaya 🤣",
"Jangan lupa bahagiakan orang tua ❤️"

]

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
