import pandas as pd
import streamlit as st 

st.title("dashboard de vendas")
import pandas as pd
import streamlit as st

# DADOS
df = pd.read_csv('sales_data.csv')
df["Date_Sold"] = pd.to_datetime(df["Date_Sold"], errors="coerce")
df = df.dropna(subset=["Date_Sold"])

#Filtros
st.sidebar.header("Filtros")
cats = sorted(df["Category"].dropna().unique())
sel_cat = st.sidebar.multiselect("Categoria", cats, default=cats[:2])
dmin, dmax = df["Date_Sold"].min().date(), df["Date_Sold"].max().date()
per = st.sidebar.date_input("Período", [dmin, dmax])

dados = df.copy()
if sel_cat: dados = dados[dados["Category"].isin(sel_cat)]
if len(per) == 2:
    ini, fim = pd.to_datetime(per[0]), pd.to_datetime(per[1])
    dados = dados[(dados["Date_Sold"] >= ini) & (dados["Date_Sold"] <= fim)]

#KPI
# ---- KPIs ----
st.title("Dashboard de Vendas")

c1, c2 = st.columns(2)
c1.metric("Receita Total", f"R$ {dados['Total_Sales'].sum():,.2f}")
c2.metric("Quantidade Vendida", f"{int(dados['Quantity_Sold'].sum()):,}")

st.divider()

# ---- Gráficos ----
c1, c2 = st.columns(2)
with c1:
    st.subheader("Receita ao longo do tempo")
    diario = dados.groupby("Date_Sold")["Total_Sales"].sum()
    st.line_chart(diario, width="stretch")

with c2:
    st.subheader("Top produtos por receita")

    top_n = st.slider("Top n:", 5, 20, 10)
    top = dados.groupby("Product_Name")["Total_Sales"].sum().nlargest(top_n)
    st.bar_chart(top, width="stretch")

# ---- Tabela e Download ----
st.dataframe(dados, width="stretch")
st.download_button("Baixar CSV filtrado",  dados.to_csv(index=False).encode("utf-8"), "vendas_filtrado.csv", "text/csv")