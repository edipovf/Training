import streamlit as st
import plotly.express as px
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Dashboard Pro", layout="wide")

# Sidebar para filtros
st.sidebar.header("Filtros")
data_range = st.sidebar.date_input("Selecione o período")

# Título
st.title("📊 Dashboard de Performance")

# Layout de Colunas para KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Vendas", "R$ 50.000", "+5%")
col2.metric("Conversão", "12%", "-2%")
col3.metric("Clientes Ativos", "1,240", "+121")

# Gráfico Principal
df = px.data.iris() # Exemplo
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Análise de Dispersão Avançada")
st.plotly_chart(fig, use_container_width=True)
