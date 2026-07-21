import streamlit as st
import random
import hashlib

st.set_page_config(page_title="Tebak Isi Saldo", layout="centered")

st.title("💰 Aplikasi Tebak Isi Saldo")

nama = st.text_input("Masukkan Nama")

ewallet = [
    "OVO",
    "DANA",
    "GoPay",
    "ShopeePay",
    "BCA",
    "BRI",
    "Mandiri",
    "BNI",
    "CIMB",
    "Permata"
]

motor = [
    "Honda Beat",
    "Honda Vario 160",
    "Honda PCX",
    "Yamaha NMAX",
    "Yamaha Aerox",
    "Kawasaki Ninja",
    "Honda Scoopy",
    "Yamaha Mio"
]

mobil = [
    "Toyota Avanza",
    "Toyota Fortuner",
    "Toyota Alphard",
    "Honda Brio",
    "Honda HRV",
    "Mitsubishi Pajero",
    "BMW M4",
    "Mercedes C200",
    "Tidak Punya"
]

kata = [
    "Rajin nabung ternyata.",
    "Sultan diam-diam.",
    "Dompetnya lebih tebal dari buku matematika.",
    "Masih berjuang demi akhir bulan.",
    "Kelihatannya sederhana, ternyata tajir.",
    "Gaji numpang lewat.",
    "Isi rekening bikin iri satu RT.",
    "Sultan berkedok rakyat biasa."
]

if st.button("🔍 Tebak"):

    if nama != "":

        # Supaya hasil nama yang sama selalu sama
        seed = int(hashlib.md5(nama.lower().encode()).hexdigest(),16)
        random.seed(seed)

        saldo = random.randint(10000,50000000)

        st.success(f"Nama : {nama.upper()}")

        st.markdown("---")

        st.subheader("💰 Saldo")
        st.write(random.choice(ewallet))
        st.write(f"### Rp {saldo:,}".replace(",", "."))

        st.subheader("🏍 Motor")
        st.write(random.choice(motor))

        st.subheader("🚗 Mobil")
        st.write(random.choice(mobil))

        st.subheader("📝 Keterangan")
        st.info(random.choice(kata))
