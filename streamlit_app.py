import streamlit as st
import random
import hashlib
import time

st.set_page_config(
    page_title="🎉 Aplikasi Tebak Hiburan",
    page_icon="🎉",
    layout="centered"
)

# ================= CSS =================
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#ff4ecd,#7b2ff7,#00d4ff);
    background-size:400% 400%;
    animation: gradient 12s ease infinite;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

h1{
text-align:center;
color:white;
font-size:50px;
text-shadow:3px 3px 10px black;
}

.block{
background:rgba(255,255,255,0.18);
padding:25px;
border-radius:25px;
backdrop-filter: blur(15px);
box-shadow:0 0 30px rgba(255,255,255,.5);
margin-top:20px;
}

.result{
background:white;
padding:15px;
border-radius:18px;
font-size:22px;
margin:10px 0;
font-weight:bold;
}

.footer{
text-align:center;
color:white;
font-size:18px;
margin-top:20px;
}

</style>
""",unsafe_allow_html=True)

# ================= JUDUL =================

st.markdown("""
<h1>🎉 APLIKASI TEBAK HIBURAN 🎉</h1>
""",unsafe_allow_html=True)

st.snow()

st.markdown("""
<div class='block'>
<h3 style='text-align:center;color:white'>
✨ Masukkan Nama Temanmu ✨
</h3>
</div>
""",unsafe_allow_html=True)

nama=st.text_input("",placeholder="Contoh : Budi")

if st.button("🎊 TEBAK SEKARANG 🎊",use_container_width=True):

    if nama=="":

        st.warning("Masukkan nama dulu 😊")

    else:

        seed=int(hashlib.md5(nama.lower().encode()).hexdigest(),16)
        random.seed(seed)

        saldo=random.randint(50000,50000000)

        hobby=random.choice([
            "Main Mobile Legends",
            "Tidur",
            "Mancing",
            "Belanja",
            "Kuliner",
            "Nonton Drama",
            "Ngopi",
            "Traveling"
        ])

        nikah=random.randint(2026,2038)

        status=random.choice([
            "Jomblo",
            "Pacaran",
            "Rahasia 🤫",
            "HTS",
            "Susah Move On"
        ])

        hoki=random.randint(1,100)

        komentar=random.choice([
            "Kalau lihat diskon langsung lupa isi dompet 😂",
            "Sultan yang menyamar jadi rakyat biasa 😎",
            "Hobinya bilang 'besok mulai nabung'. 🤣",
            "Orangnya baik tapi susah bangun pagi 😴",
            "Paling semangat kalau diajak makan gratis 🍔"
        ])

        progress=st.progress(0)

        tulisan=st.empty()

        proses=[
        "🤖 Menghubungkan Satelit...",
        "📡 Membaca Aura...",
        "💻 Mengambil Data...",
        "🔎 Menghitung Keberuntungan...",
        "🎉 Hampir Selesai..."
        ]

        for i in range(100):

            progress.progress(i+1)

            if i<20:
                tulisan.info(proses[0])
            elif i<40:
                tulisan.info(proses[1])
            elif i<60:
                tulisan.info(proses[2])
            elif i<80:
                tulisan.info(proses[3])
            else:
                tulisan.info(proses[4])

            time.sleep(0.02)

        st.balloons()

        st.success("🎊 HASIL BERHASIL DITEMUKAN 🎊")

        st.markdown(f"""
<div class='result'>👤 Nama : {nama}</div>
""",unsafe_allow_html=True)

        time.sleep(.2)

        st.markdown(f"""
<div class='result'>💰 Saldo : Rp {saldo:,}</div>
""".replace(",","."),
unsafe_allow_html=True)

        time.sleep(.2)

        st.markdown(f"""
<div class='result'>❤️ Status : {status}</div>
""",unsafe_allow_html=True)

        time.sleep(.2)

        st.markdown(f"""
<div class='result'>💍 Nikah : {nikah}</div>
""",unsafe_allow_html=True)

        time.sleep(.2)

        st.markdown(f"""
<div class='result'>🎮 Hobi : {hobby}</div>
""",unsafe_allow_html=True)

        time.sleep(.2)

        st.markdown(f"""
<div class='result'>🍀 Keberuntungan : {hoki}%</div>
""",unsafe_allow_html=True)

        time.sleep(.2)

        st.markdown(f"""
<div class='result'>😂 Keterangan : {komentar}</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class='footer'>
⚠️ Semua hasil di aplikasi ini dibuat secara otomatis hanya untuk hiburan.
</div>
""",unsafe_allow_html=True)
