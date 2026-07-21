
import streamlit as st
import random, hashlib

st.set_page_config(page_title="Tebak Isi Saldo", layout="wide")

if "rows" not in st.session_state:
    st.session_state.rows=[]

BANK=[("OVO","🟣"),("DANA","🔵"),("GoPay","🟢"),("BCA","🏦"),("BRI","🏦"),("Mandiri","🏦")]
MOTOR=["Beat","Vario 160","PCX","NMAX","Aerox"]
MOBIL=["Brio","Avanza","HRV","Fortuner","Pajero"]
KET=["😎 Sultan","😂 Bikin iri","💰 Rajin nabung","🔥 Mantap"]

st.markdown("""
<style>
.header{background:#2563eb;color:#fff;padding:18px;border-radius:12px;font-size:30px;font-weight:bold;text-align:center}
.saldo-table{width:100%;border-collapse:collapse}
.saldo-table th{background:#16a34a;color:#fff;padding:10px}
.saldo-table td{border:1px solid #ddd;padding:10px;text-align:center}
.saldo-table tr:nth-child(even){background:#f7fff7}
.bank{font-weight:bold;color:#2563eb}.nominal{color:#059669;font-weight:bold}
</style>
<div class="header">💰 APLIKASI TEBAK ISI SALDO 💰</div>
""",unsafe_allow_html=True)

c1,c2,c3=st.columns([6,2,2])
with c1:
    nama=st.text_input("",placeholder="🔍 Masukkan nama",label_visibility="collapsed")
with c2:
    tebak=st.button("🎲 Tebak")
with c3:
    if st.button("🗑 Hapus"):
        st.session_state.rows=[]
        st.rerun()

if tebak and nama.strip():
    seed=int(hashlib.md5(nama.lower().encode()).hexdigest(),16)
    random.seed(seed)
    row={
      "nama":nama.upper(),
      "bank":random.choice(BANK),
      "saldo":"Rp {:,}".format(random.randint(100000,500000000)).replace(",","."),
      "motor":random.choice(MOTOR),
      "mobil":random.choice(MOBIL),
      "ket":random.choice(KET)
    }
    st.session_state.rows=[r for r in st.session_state.rows if r["nama"]!=row["nama"]]
    st.session_state.rows.append(row)

html="""<table class='saldo-table'><tr><th>No</th><th>Nama</th><th>Saldo</th><th>Motor</th><th>Mobil</th><th>Keterangan</th></tr>"""
for i,r in enumerate(st.session_state.rows,1):
    html+=f"<tr><td>{i}</td><td>{r['nama']}</td><td><div class='bank'>{r['bank'][1]} {r['bank'][0]}</div><div class='nominal'>{r['saldo']}</div></td><td>🏍️ {r['motor']}</td><td>🚗 {r['mobil']}</td><td>{r['ket']}</td></tr>"
html+="</table>"
st.markdown(html,unsafe_allow_html=True)
