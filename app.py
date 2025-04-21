import streamlit as st
import pandas as pd

# Tabela de IVA por país
TAXAS_IVA = {
    "Portugal": 0.23,
    "Brasil": 0.17,
    "Estados Unidos": 0.00,
    "Espanha": 0.21,
    "França": 0.20,
    "Alemanha": 0.19
}

def calcular_receita_liquida(valor_bruto, tipo_cartao, pais):
    iva = TAXAS_IVA.get(pais, 0.0)
    valor_com_iva = valor_bruto * (1 + iva)

    if tipo_cartao == "Europeu":
        taxa_percentual = 0.014
    elif tipo_cartao == "Internacional":
        taxa_percentual = 0.029
    else:
        taxa_percentual = 0.0

    taxa_fixa = 0.25
    taxa_total = (valor_com_iva * taxa_percentual) + taxa_fixa
    valor_liquido = valor_com_iva - taxa_total

    return round(valor_liquido, 2), round(taxa_total, 2), round(valor_com_iva, 2)

st.set_page_config(page_title="Calculadora Stripe", page_icon="💳", layout="centered")
st.title("💳 Calculadora de Taxas Stripe")
st.markdown("Simula quanto recebes após as taxas do Stripe + IVA.")

# Inputs do utilizador
st.subheader("Simulação Personalizada")
valor = st.number_input("Valor da subscrição (€)", min_value=0.0, value=10.0, step=0.5)
quantidade = st.number_input("Quantidade de subscrições", min_value=1, value=1, step=1)
tipo_cartao = st.selectbox("Tipo de cartão", ["Europeu", "Internacional"])
pais = st.selectbox("País do comprador", list(TAXAS_IVA.keys()))

# Cálculo
if st.button("Calcular"):
    recebido_unitario, taxa_unitaria, valor_com_iva = calcular_receita_liquida(valor, tipo_cartao, pais)
    recebido_total = round(recebido_unitario * quantidade, 2)
    taxa_total = round(taxa_unitaria * quantidade, 2)

    st.success(f"Stripe cobra por subscrição (com IVA): €{taxa_unitaria:.2f}")
    st.info(f"Recebes líquido por subscrição: €{recebido_unitario:.2f}")
    st.markdown(f"### Total para {quantidade} subscrições")
    st.success(f"Taxa total Stripe: €{taxa_total:.2f}")
    st.info(f"Receita líquida total: €{recebido_total:.2f}")

# Simulação em lote
st.subheader("Exportar Simulação em Markdown")
valores = [5, 10, 20, 50, 100, valor]
tipos = ["Europeu", "Internacional"]
resultados = []

for tipo in tipos:
    for v in sorted(set(valores)):
        for pais_simulado in TAXAS_IVA.keys():
            r, t, v_com_iva = calcular_receita_liquida(v, tipo, pais_simulado)
            resultados.append({
                "País": pais_simulado,
                "Tipo de Cartão": tipo,
                "Valor Base (€)": v,
                "Valor com IVA (€)": v_com_iva,
                "Taxa Stripe (€)": t,
                "Recebe Líquido (€)": r
            })

df = pd.DataFrame(resultados)
markdown = df.to_markdown(index=False)

# Resumo personalizado
try:
    resumo = (
        f"\n\n## Resumo Personalizado\n\n"
        f"- País: {pais}\n"
        f"- Valor base: €{valor:.2f}\n"
        f"- Valor com IVA: €{valor * (1 + TAXAS_IVA[pais]):.2f}\n"
        f"- Subscrições: {quantidade}\n"
        f"- Tipo de Cartão: {tipo_cartao}\n"
        f"- Receita Líquida Total: €{recebido_total:.2f}\n"
        f"- Taxa Stripe Total: €{taxa_total:.2f}\n"
    )
except:
    resumo = (
        f"\n\n## Resumo Personalizado\n\n"
        f"- País: {pais}\n"
        f"- Valor base: €{valor:.2f}\n"
        f"- Subscrições: {quantidade}\n"
        f"- Tipo de Cartão: {tipo_cartao}\n"
        f"- Receita Líquida Total: **não calculada**\n"
        f"- Taxa Stripe Total: **não calculada**\n"
    )

with open("simulacao_taxas_stripe.md", "w") as f_out:
    f_out.write("# Simulação de Taxas Stripe\n\n")
    f_out.write(markdown)
    f_out.write(resumo)

st.download_button(
    label="📥 Baixar simulação com resumo",
    data=open("simulacao_taxas_stripe.md", "rb"),
    file_name="simulacao_taxas_stripe.md",
    mime="text/markdown"
)
