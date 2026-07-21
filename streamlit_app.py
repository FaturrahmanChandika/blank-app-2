import streamlit as st
import random
import time
import hashlib

st.set_page_config(
    page_title="Aplikasi Tebak Hiburan",
    page_icon="🎉",
    layout="centered"
)

# Judul
st.title("🎉 Aplikasi Tebak Hiburan")
st.markdown("### Masukkan nama dan lihat hasilnya!")
st.info("⚠️ Semua hasil dibuat otomatis dan hanya untuk hiburan.")

nama = st.text_input("Masukkan Nama")

if st.button("🔍 TEBAK"):

    if nama.strip() == "":
        st.warning("Silakan masukkan nama terlebih dahulu.")
    else:

        # Seed berdasarkan nama agar hasil selalu sama
        seed = int(hashlib.md5(nama.lower().encode()).hexdigest(), 16)
        random.seed(seed)

        saldo = random.randint(5000, 50000000)

        status = random.choice([
            "Jomblo",
            "Pacaran",
            "HTS",
            "Gebetan Banyak",
            "Rahasia 🤫"
        ])

        nikah = random.randint(2026, 2038)

        hobi = random.choice([
            "Gaming",
            "Mancing",
            "Tidur",
            "Kuliner",
            "Traveling",
            "Ngopi",
            "Belanja",
            "Musik",
            "Olahraga",
            "Nonton Drama"
        ])

        keberuntungan = random.randint(1,100)

        pekerjaan = random.choice([
            "Pengusaha",
            "Content Creator",
            "Programmer",
            "Dokter",
            "Pilot",
            "Polisi",
            "Guru",
            "Chef",
            "Influencer",
            "Bos Besar"
        ])

        komentar = random.choice([
            "Orangnya baik, tapi kalau ada diskon langsung kalap 😂",
            "Suka menolong teman.",
            "Rezekinya lancar kalau rajin usaha.",
            "Hobi rebahan tapi cita-citanya tinggi 😆",
            "Sering bilang hemat, tapi checkout terus.",
            "Aura sultan mulai terlihat 😎",
            "Jangan lupa traktir teman kalau sukses ya."
        ])

        with st.spinner("🔍 Sedang menganalisis..."):
            time.sleep(3)

        st.success("✅ Analisis Selesai")

        st.markdown("---")

        st.subheader("📋 HASIL")

        st.write(f"👤 **Nama :** {nama}")
        st.write(f"💰 **Saldo :** Rp {saldo:,}".replace(",", "."))
        st.write(f"❤️ **Status :** {status}")
        st.write(f"💍 **Prediksi Nikah :** {nikah}")
        st.write(f"🎮 **Hobi :** {hobi}")
        st.write(f"🍀 **Keberuntungan :** {keberuntungan}%")
        st.write(f"💼 **Pekerjaan Cocok :** {pekerjaan}")

        st.markdown("### 😂 Komentar")
        st.success(komentar)

        st.balloons()
