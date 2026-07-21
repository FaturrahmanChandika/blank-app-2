
# Lihat penjelasan: ini adalah patch siap pakai.
# Ganti app_v2.py dengan file ini bila diinginkan.

import streamlit as st, random, hashlib
st.set_page_config(layout="wide",page_title="Tebak Saldo")

if "rows" not in st.session_state:
    st.session_state.rows=[]

BANK=[("OVO","🟣"),("DANA","🔵"),("GoPay","🟢"),("BCA","🏦"),("BRI","🏦"),("Mandiri","🏦"),("BNI","🏦")]
MOTOR=["Honda Beat","Beat Street","Scoopy","Genio","Vario 125","Vario 160","PCX 160","ADV 160","CB150R","CBR150R","CBR250RR","CRF150L","Mio","Fazzio","Gear","Freego","NMAX","Aerox","XMAX","R15","MT15","Ninja 250","KLX 150","W175","Vespa Sprint","Vespa Primavera","Satria FU","GSX-R150","Lexi","Forza"]
MOBIL=["Brio","Agya","Ayla","Sigra","Calya","Avanza","Xenia","Rush","Terios","Raize","Rocky","Innova Reborn","Innova Zenix","Fortuner","Pajero Sport","HR-V","WR-V","CR-V","BR-V","Civic","Accord","Camry","Alphard","Vellfire","BMW M4","BMW X5","Mercedes C200","GLC","Land Cruiser","Creta","Ioniq 5","Stargazer","CX-5","Jimny","Yaris Cross"]
KET=[
"😎 Kelihatannya sederhana, tapi isi rekeningnya bikin banyak orang penasaran.",
"😂 Kalau saldo ini benar, traktiran satu kampung juga masih aman.",
"💰 Rajin menabung sejak lama, hasilnya mulai kelihatan sekarang.",
"🔥 Rekeningnya adem, nominalnya bikin mata melotot.",
"🤭 Dompet boleh biasa, tapi saldo digitalnya tidak main-main.",
"👑 Diam-diam menghanyutkan, saldonya lebih besar dari yang dikira.",
"🚀 Rezekinya lancar, semoga terus bertambah setiap hari.",
"💸 Jangan kaget kalau tiba-tiba dia yang bayarin semuanya.",
"😄 Hidup sederhana, tapi angka di rekening bikin iri tetangga.",
"🏦 Bank pasti senang punya nasabah seperti ini.",
"🎉 Kalau ini saldo asli, akhir bulan tetap senyum.",
"💎 Semoga rezekinya terus bertambah dan selalu membawa keberkahan."
]

st.markdown("<style>.stButton>button{height:60px;font-size:20px;width:100%}.t{width:100%;border-collapse:collapse}.t th{background:#16a34a;color:#fff;padding:10px}.t td{border:1px solid #ddd;padding:10px;text-align:center}</style>",unsafe_allow_html=True)
st.markdown("<h1 style='background:#2f63e0;color:white;padding:18px;border-radius:12px;text-align:center'>💰 APLIKASI TEBAK ISI SALDO 💰</h1>",unsafe_allow_html=True)
c1,c2,c3=st.columns([6,2.2,2.2])
with c1:n=st.text_input("",placeholder="Cari nama",label_visibility="collapsed")
with c2:add=st.button("🎲 Tebak Saldo",use_container_width=True)
with c3:
    if st.button("🗑 Hapus Semua",use_container_width=True):
        st.session_state.rows=[];st.rerun()
if add and n.strip():
    random.seed(int(hashlib.md5(n.lower().encode()).hexdigest(),16))
    row={"nama":n.upper(),"bank":random.choice(BANK),"saldo":"Rp {:,}".format(random.randint(100000,500000000)).replace(",","."),"motor":random.choice(MOTOR),"mobil":random.choice(MOBIL),"ket":random.choice(KET)}
    st.session_state.rows=[r for r in st.session_state.rows if r["nama"]!=row["nama"]]
    st.session_state.rows.insert(0,row)
h="<table class='t'><tr><th>No</th><th>Nama</th><th>Saldo</th><th>Motor</th><th>Mobil</th><th>Keterangan</th></tr>"
for i,r in enumerate(st.session_state.rows,1):
    h+=f"<tr><td>{i}</td><td>{r['nama']}</td><td>{r['bank'][1]} {r['bank'][0]}<br><b>{r['saldo']}</b></td><td>🏍️ {r['motor']}</td><td>🚗 {r['mobil']}</td><td style='text-align:left'>{r['ket']}</td></tr>"
h+="</table>"
st.markdown(h,unsafe_allow_html=True)
