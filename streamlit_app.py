
import streamlit as st, random, hashlib
st.set_page_config(layout="wide",page_title="Tebak Saldo")
if "rows" not in st.session_state: st.session_state.rows=[]
BANK=[("OVO","🟣"),("DANA","🔵"),("GoPay","🟢"),("BCA","🏦"),("BRI","🏦"),("Mandiri","🏦"),("BNI","🏦")]
MOTOR=['Honda Beat', 'Honda Beat Street', 'Scoopy', 'Genio', 'Vario 125', 'Vario 160', 'PCX 160', 'ADV 160', 'CB150R', 'CBR150R', 'CBR250RR', 'CRF150L', 'Yamaha Mio', 'Fazzio', 'Gear', 'Freego', 'NMAX', 'Aerox', 'XMAX', 'R15', 'MT15', 'Ninja 250', 'KLX 150', 'W175', 'Vespa Sprint', 'Vespa Primavera', 'Satria FU', 'GSX-R150']
MOBIL=['Brio', 'Agya', 'Ayla', 'Sigra', 'Calya', 'Avanza', 'Xenia', 'Rush', 'Terios', 'Raize', 'Rocky', 'Innova Reborn', 'Innova Zenix', 'Fortuner', 'Pajero Sport', 'HR-V', 'WR-V', 'CR-V', 'BR-V', 'Civic', 'Accord', 'Camry', 'Alphard', 'Vellfire', 'BMW M4', 'BMW X5', 'Mercedes C200', 'GLC', 'Land Cruiser', 'Creta', 'Ioniq 5', 'Stargazer']
KET=["😎 Sultan","😂 Bikin iri","🔥 Mantap","💰 Rajin nabung","🤣 Gaji numpang lewat","👑 Sultan berkedok"]
st.markdown("""<style>
.header{background:#2f63e0;color:#fff;padding:20px;border-radius:16px;font-size:34px;font-weight:700;text-align:center}
.stButton>button{height:60px;font-size:20px;font-weight:bold;width:100%}
.saldo-table{width:100%;border-collapse:collapse} .saldo-table th{background:#16a34a;color:#fff;padding:12px} .saldo-table td{padding:12px;border:1px solid #ddd;text-align:center}
.bank{color:#2563eb;font-weight:bold} .nom{color:#059669;font-weight:bold;font-size:22px}
</style><div class='header'>💰 APLIKASI TEBAK ISI SALDO 💰</div>""",unsafe_allow_html=True)
c1,c2,c3=st.columns([6,2.2,2.2])
with c1: n=st.text_input("",placeholder="Cari nama",label_visibility="collapsed")
with c2: add=st.button("🎲 Tebak Saldo",use_container_width=True)
with c3:
    if st.button("🗑 Hapus Semua",use_container_width=True):
        st.session_state.rows=[]; st.rerun()
if add and n.strip():
 s=int(hashlib.md5(n.lower().encode()).hexdigest(),16);random.seed(s)
 row={"nama":n.upper(),"bank":random.choice(BANK),"saldo":"Rp {:,}".format(random.randint(100000,500000000)).replace(",", "."),"motor":random.choice(MOTOR),"mobil":random.choice(MOBIL),"ket":random.choice(KET)}
 st.session_state.rows=[r for r in st.session_state.rows if r["nama"]!=row["nama"]]; st.session_state.rows.append(row)
h="<table class='saldo-table'><tr><th>No</th><th>Nama</th><th>Saldo</th><th>Motor</th><th>Mobil</th><th>Keterangan</th></tr>"
for i,r in enumerate(st.session_state.rows,1):
 h+=f"<tr><td>{i}</td><td>{r['nama']}</td><td><div class='bank'>{r['bank'][1]} {r['bank'][0]}</div><div class='nom'>{r['saldo']}</div></td><td>🏍️ {r['motor']}</td><td>🚗 {r['mobil']}</td><td>{r['ket']}</td></tr>"
h+="</table>"; st.markdown(h,unsafe_allow_html=True)
