
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# IVA por país (incluso no preço final)
TAXAS_IVA = {
    "Portugal": 0.23,
    "Brasil": 0.17,
    "Estados Unidos": 0.00,
    "Espanha": 0.21,
    "França": 0.20,
    "Alemanha": 0.19,
    "Japão": 0.10,
    "Canadá": 0.05,
    "Itália": 0.22,
    "Países Baixos": 0.21
}

def calcular(valor_final, tipo_cartao, pais):
    iva = TAXAS_IVA[pais]
    valor_sem_iva = valor_final / (1 + iva)  # valor líquido sem IVA

    taxa_percentual = 0.014 if tipo_cartao == "Europeu" else 0.029
    taxa_fixa = 0.25
    taxa_stripe = valor_sem_iva * taxa_percentual + taxa_fixa
    valor_liquido_final = valor_sem_iva - taxa_stripe

    return round(valor_sem_iva, 2), round(taxa_stripe, 2), round(valor_liquido_final, 2), round(valor_final - valor_liquido_final, 2)

st.set_page_config(page_title="Calculadora Stripe + IVA", page_icon="💳", layout="centered")
st.title("💳 Calculadora Stripe com IVA Incluído")
st.markdown("Simula quanto recebes após recolher IVA e pagar taxas Stripe.")

# Entradas
valor_final = st.number_input("💰 Preço final cobrado ao cliente (€)", min_value=1.0, value=10.0, step=1.0)
quantidade = st.number_input("📦 Quantidade de subscrições", min_value=1, value=1, step=1)
tipo_cartao = st.selectbox("🌍 Tipo de cartão", ["Europeu", "Internacional"])
pais = st.selectbox("🌐 País do comprador", list(TAXAS_IVA.keys()))

if st.button("Calcular"):
    valor_sem_iva, taxa_stripe, valor_liquido_final, perda_total = calcular(valor_final, tipo_cartao, pais)
    receita_total = valor_liquido_final * quantidade
    perda_total_global = perda_total * quantidade

    st.write(f"🔸 Valor sem IVA: €{valor_sem_iva}")
    st.write(f"💸 Taxa Stripe: €{taxa_stripe}")
    st.write(f"✅ Receita líquida por subscrição: €{valor_liquido_final}")
    st.success(f"🧾 Receita líquida total: €{receita_total}")
    st.error(f"📉 Perda total (IVA + Stripe): €{perda_total_global}")

# Comparação por país
st.subheader("📊 Comparação de perdas por país")
tipo_selecionado = st.radio("Selecionar tipo de cartão para comparação:", ["Europeu", "Internacional"])

dados = []
for p in TAXAS_IVA.keys():
    valor_sem_iva, taxa, r_liquida, perda = calcular(valor_final, tipo_selecionado, p)
    dados.append({"País": p, "Perda Total (€)": perda})

df = pd.DataFrame(dados).sort_values(by="Perda Total (€)", ascending=False)

# Gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df["País"], df["Perda Total (€)"], color="orange")
ax.set_title("📉 Perda Total por País (IVA + Stripe)", fontsize=14)
ax.set_ylabel("Perda (€)")
ax.set_xlabel("País")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

# Exportação
markdown = df.to_markdown(index=False)
with open("comparacao_perdas.md", "w") as f:
    f.write("# Comparação de Perdas por País\n\n")
    f.write(markdown)

caminho_grafico = "grafico_perdas.png"
fig.savefig(caminho_grafico)

st.download_button(
    "📥 Baixar tabela Markdown",
    data=open("comparacao_perdas.md", "rb"),
    file_name="comparacao_perdas.md",
    mime="text/markdown"
)

st.download_button(
    "🖼️ Baixar gráfico PNG",
    data=open(caminho_grafico, "rb"),
    file_name="grafico_perdas.png",
    mime="image/png"
)
