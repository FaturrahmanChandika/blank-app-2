import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Aplikasi Tebak Isi Saldo",
    layout="wide"
)

st.markdown("""
<style>

.title{
text-align:center;
font-size:35px;
font-weight:bold;
color:white;
padding:15px;
background:linear-gradient(90deg,#3b82f6,#8b5cf6);
border-radius:15px;
}

table{
width:100%;
}

</style>
""",unsafe_allow_html=True)

st.markdown('<div class="title">💰 APLIKASI TEBAK ISI SALDO</div>',unsafe_allow_html=True)

st.write("")

data = [
{
"Nama":"SANTI",
"Saldo":"OVO\nRp109.243",
"Motor":"Honda Beat",
"Mobil":"-",
"Keterangan":"🤣 Kalo miskin itu penyakit, kamu udah endemik."
},
{
"Nama":"ANTON",
"Saldo":"Permata\nRp1.266.700",
"Motor":"NMAX",
"Mobil":"Avanza",
"Keterangan":"🙈 Kamu versi ekonomis orang kaya."
},
{
"Nama":"NAWAN",
"Saldo":"CIMB\nRp2.793.147",
"Motor":"Vario",
"Mobil":"Fortuner",
"Keterangan":"😎 Gajimu cukup buat streaming."
},
{
"Nama":"RIAN",
"Saldo":"Danamon\nRp1.667.194",
"Motor":"PCX",
"Mobil":"Brio",
"Keterangan":"😂 Kelihatannya kaya tapi isi dompet standar."
}
]

df = pd.DataFrame(data)

col1,col2 = st.columns([5,1])

with col1:
    keyword = st.text_input("Cari Nama")

with col2:
    st.write("")
    st.write("")
    if st.button("🗑 Hapus Semua"):
        df = df.iloc[0:0]

if keyword:
    df = df[df["Nama"].str.contains(keyword.upper())]

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
