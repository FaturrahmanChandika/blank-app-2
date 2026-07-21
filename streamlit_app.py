import streamlit as st, random, hashlib
st.set_page_config(layout="wide",page_title="Tebak Saldo")
if "rows" not in st.session_state: st.session_state.rows=[]
BANK=[("BCA","🏦"),("BRI","🏦"),("BNI","🏦"),("Mandiri","🏦"),("CIMB Niaga","🏦"),("DANA","🔵")]
MOTOR=["Honda Beat","Beat Street","Scoopy","Genio","Vario 125","Vario 160","PCX160","ADV160","NMAX","Aerox","XMAX","CBR150R","CB150R","Ninja250","KLX150","Vespa Sprint","Fazzio","Gear"]
MOBIL=["Brio","Agya","Ayla","Avanza","Xenia","Rush","Terios","Raize","Rocky","Innova Zenix","Fortuner","Pajero","HR-V","CR-V","BR-V","Camry","Alphard","BMW X5","Jimny","Creta"]
KET=["😎 Kelihatannya sederhana, tapi isi rekeningnya bikin banyak orang penasaran."," Waw kaya banget","Bagi duit nya dong","Pasti Rajin berbagi","💰 Rajin menabung sejak lama, hasilnya mulai kelihatan.","🚀 Rezekinya lancar, semoga terus bertambah.","👑 Diam-diam menghanyutkan, saldonya lebih besar dari yang dikira.","🎉 Kalau ini saldo asli, akhir bulan tetap senyum."]
st.markdown("""
<style>
.stApp{background:url('https://i.imgur.com/XM6kK6A.png') repeat,linear-gradient(#f5f0e6,#fff8dc);background-size:120px,100%;animation:bgmove 25s linear infinite;background-attachment:fixed}
@keyframes bgmove{0%{background-position:0 0}100%{background-position:0 1000px}}
@keyframes shine{0%{background-position:-300px}100%{background-position:300px}}
@keyframes money{0%{transform:rotate(-12deg)}100%{transform:rotate(12deg)}}
@keyframes rainbow{0%{background-position:0%}100%{background-position:200%}}
@keyframes pulse{0%{transform:scale(1)}50%{transform:scale(1.06)}100%{transform:scale(1)}}
.title{font-size:42px;font-weight:bold;padding:20px;border-radius:14px;text-align:center;color:#fff;background:linear-gradient(120deg,#1e40af,#fff,#2563eb,#fff,#1e40af);background-size:600px;animation:shine 3s linear infinite}
.money{display:inline-block;animation:money 1s infinite alternate}
 .stButton>button{animation:pulse 1s infinite;height:64px;font-size:20px;font-weight:bold;width:100%;border-radius:12px;background:#8DE3D1;color:#000;border:none}
.stButton>button:hover{background:#76D8C4;color:#000}
div[data-testid="stTextInput"] input{height:64px;font-size:22px;border-radius:12px;width:100%;box-sizing:border-box;background:#8DE3D1;color:#000}
.t{width:100%;border-collapse:collapse}.t th{background:linear-gradient(90deg,red,orange,yellow,green,cyan,blue,violet,red);background-size:400%;animation:rainbow 6s linear infinite;color:#fff;padding:12px}.t td{border:1px solid #ddd;padding:12px;text-align:center}
div[data-testid="column"]:nth-child(1) div[data-testid="stTextInput"]{margin-top:0px}
</style>
<h1 class='title'><span class='money'>💰</span> APLIKASI TEBAK ISI SALDO <span class='money'>💰</span></h1>
""",unsafe_allow_html=True)
c1,c2,c3=st.columns(3)
with c1: n=st.text_input("",placeholder="🔍 Tulis Nama...",label_visibility="collapsed")
with c2: add=st.button("🎲 Tebak Saldo",use_container_width=True)
with c3:
    if st.button("🗑 Hapus Semua",use_container_width=True):
        st.session_state.rows=[];st.rerun()
if add and n.strip():
    random.seed(int(hashlib.md5(n.lower().encode()).hexdigest(),16))
    row={"nama":n.upper(),"bank":random.choice(BANK),"saldo":"Rp {:,}".format(random.randint(100000,500000000)).replace(",", "."),"motor":random.choice(MOTOR),"mobil":random.choice(MOBIL),"ket":random.choice(KET)}
    st.session_state.rows=[r for r in st.session_state.rows if r["nama"]!=row["nama"]]
    st.session_state.rows.insert(0,row)
h="<table class='t'><tr><th>No</th><th>Nama</th><th>Saldo</th><th>Motor</th><th>Mobil</th><th style='background:#facc15;color:#000'>Keterangan</th></tr>"
for i,r in enumerate(st.session_state.rows,1):
    colors=["#ffe4e6","#dbeafe","#dcfce7","#fef3c7","#ede9fe","#fce7f3"];bg=colors[(i-1)%len(colors)];h+=f"<tr style='background:{bg}'><td>{i}</td><td>{r['nama']}</td><td>{r['bank'][1]} {r['bank'][0]}<br><b>{r['saldo']}</b></td><td>🏍️ {r['motor']}</td><td>🚗 {r['mobil']}</td><td style='background:{bg}'>{r['ket']}</td></tr>"
h+="</table>"
st.markdown(h,unsafe_allow_html=True)
