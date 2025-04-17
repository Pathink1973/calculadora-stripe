import streamlit as st
import pandas as pd

def calcular_receita_liquida(valor_bruto, tipo_cartao):
    if tipo_cartao == "Europeu":
        taxa_percentual = 0.014
    elif tipo_cartao == "Internacional":
        taxa_percentual = 0.029
    else:
        taxa_percentual = 0.0

    taxa_fixa = 0.25
    taxa_total = (valor_bruto * taxa_percentual) + taxa_fixa
    valor_liquido = valor_bruto - taxa_total
    return round(valor_liquido, 2), round(taxa_total, 2)

st.set_page_config(page_title="Calculadora Stripe", page_icon="💳", layout="centered")
st.title("💳 Calculadora de Taxas Stripe")
st.markdown("Simula quanto recebes após as taxas do Stripe.")

# Simulação personalizada
st.subheader("Simulação Personalizada")
valor = st.number_input("Valor da subscrição (€)", min_value=0.0, value=10.0, step=0.5)
quantidade = st.number_input("Quantidade de subscrições", min_value=1, value=1, step=1)
tipo_cartao = st.selectbox("Tipo de cartão", ["Europeu", "Internacional"])

# Inicialização segura
recebido_total = None
taxa_total = None

if st.button("Calcular"):
    recebido_unitario, taxa_unitaria = calcular_receita_liquida(valor, tipo_cartao)
    recebido_total = round(recebido_unitario * quantidade, 2)
    taxa_total = round(taxa_unitaria * quantidade, 2)

    st.success(f"Stripe cobra por subscrição: €{taxa_unitaria:.2f}")
    st.info(f"Recebes líquido por subscrição: €{recebido_unitario:.2f}")
    st.markdown(f"### Total para {quantidade} subscrições")
    st.success(f"Taxa total: €{taxa_total:.2f}")
    st.info(f"Receita líquida total: €{recebido_total:.2f}")
# Simulação em lote com exportação
st.subheader("Exportar Simulação em Markdown")
valores = [5, 10, 20, 50, 100, valor]  # inclui o valor personalizado
tipos = ["Europeu", "Internacional"]
resultados = []

for tipo in tipos:
    for v in sorted(set(valores)):
        r, t = calcular_receita_liquida(v, tipo)
        resultados.append({
            "Tipo de Cartão": tipo,
            "Valor Bruto (€)": v,
            "Taxa Stripe (€)": t,
            "Recebe Líquido (€)": r
        })

df = pd.DataFrame(resultados)
markdown = df.to_markdown(index=False)

# Adiciona o resumo da simulação personalizada ao Markdown
try:
    resumo = (
        f"\n\n## Resumo Personalizado\n\n"
        f"- Valor: €{valor:.2f}\n"
        f"- Subscrições: {quantidade}\n"
        f"- Tipo de Cartão: {tipo_cartao}\n"
        f"- Receita Líquida Total: €{recebido_total:.2f}\n"
        f"- Taxa Stripe Total: €{taxa_total:.2f}\n"
    )
except:
    resumo = (
        f"\n\n## Resumo Personalizado\n\n"
        f"- Valor: €{valor:.2f}\n"
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