from pathlib import Path

import pandas as pd
import streamlit as st


DATA_PATH = Path(__file__).with_name("dados_de_vendas.csv")


def format_currency(value: float) -> str:
    formatted = f"{value:,.2f}"
    formatted = formatted.replace(",", "_").replace(".", ",").replace("_", ".")
    return f"R$ {formatted}"


@st.cache_data
def load_data() -> pd.DataFrame:
    data = pd.read_csv(DATA_PATH)
    data["Date_Sold"] = pd.to_datetime(data["Date_Sold"], errors="coerce")

    numeric_columns = ["Price", "Quantity_Sold", "Total_Sales"]
    for column in numeric_columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    return data.dropna(subset=["Date_Sold", *numeric_columns])


st.set_page_config(
    page_title="Dashboard de Vendas",
    page_icon="📊",
    layout="wide",
)

sales = load_data()

st.title("Dashboard de Vendas")
st.caption(
    "Análise demonstrativa de receita, volume vendido e desempenho de produtos. "
    "Os dados são sintéticos e destinados ao portfólio."
)

st.sidebar.header("Filtros")
categories = sorted(sales["Category"].dropna().unique())
selected_categories = st.sidebar.multiselect(
    "Categorias",
    categories,
    default=categories,
)

minimum_date = sales["Date_Sold"].min().date()
maximum_date = sales["Date_Sold"].max().date()
selected_period = st.sidebar.date_input(
    "Período",
    value=(minimum_date, maximum_date),
    min_value=minimum_date,
    max_value=maximum_date,
)

filtered = sales[sales["Category"].isin(selected_categories)].copy()

if len(selected_period) == 2:
    start_date, end_date = map(pd.Timestamp, selected_period)
    filtered = filtered[
        filtered["Date_Sold"].between(start_date, end_date, inclusive="both")
    ]

st.sidebar.caption(f"{len(filtered)} de {len(sales)} registros selecionados")

if filtered.empty:
    st.warning("Nenhum registro corresponde aos filtros selecionados.")
    st.stop()

total_revenue = filtered["Total_Sales"].sum()
total_quantity = int(filtered["Quantity_Sold"].sum())
average_sale = filtered["Total_Sales"].mean()
active_products = filtered["Product_ID"].nunique()

kpi_columns = st.columns(4)
kpi_columns[0].metric("Receita total", format_currency(total_revenue))
kpi_columns[1].metric("Itens vendidos", f"{total_quantity:,}".replace(",", "."))
kpi_columns[2].metric("Venda média", format_currency(average_sale))
kpi_columns[3].metric("Produtos ativos", active_products)

st.divider()

chart_columns = st.columns(2)

with chart_columns[0]:
    st.subheader("Receita ao longo do tempo")
    daily_revenue = (
        filtered.groupby("Date_Sold", as_index=False)["Total_Sales"].sum()
        .set_index("Date_Sold")
        .rename(columns={"Total_Sales": "Receita"})
    )
    st.line_chart(daily_revenue, width="stretch")

with chart_columns[1]:
    st.subheader("Receita por categoria")
    category_revenue = (
        filtered.groupby("Category")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
        .rename("Receita")
    )
    st.bar_chart(category_revenue, width="stretch")

st.subheader("Produtos com maior receita")
top_n = st.slider("Quantidade de produtos", min_value=5, max_value=20, value=10)
top_products = (
    filtered.groupby("Product_Name")["Total_Sales"]
    .sum()
    .nlargest(top_n)
    .sort_values()
    .rename("Receita")
)
st.bar_chart(top_products, horizontal=True, width="stretch")

st.subheader("Dados filtrados")
display_data = filtered.rename(
    columns={
        "Product_ID": "ID",
        "Product_Name": "Produto",
        "Category": "Categoria",
        "Price": "Preço",
        "Quantity_Sold": "Quantidade",
        "Date_Sold": "Data",
        "Total_Sales": "Receita",
    }
)
st.dataframe(
    display_data,
    hide_index=True,
    width="stretch",
    column_config={
        "Data": st.column_config.DateColumn(format="DD/MM/YYYY"),
        "Preço": st.column_config.NumberColumn(format="R$ %.2f"),
        "Receita": st.column_config.NumberColumn(format="R$ %.2f"),
    },
)

csv = filtered.to_csv(index=False, sep=";").encode("utf-8-sig")
st.download_button(
    "Baixar dados filtrados",
    data=csv,
    file_name="vendas_filtradas.csv",
    mime="text/csv",
)
