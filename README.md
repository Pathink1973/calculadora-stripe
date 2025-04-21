
# 💳 Calculadora de Taxas Stripe

Aplicação interativa feita com **Streamlit** para simular quanto recebes após as taxas cobradas pelo Stripe e IVA do país em cada subscrição.

## ✨ Funcionalidades

- Cálculo da taxa Stripe por transação (Europeu e Internacional)
- Inclusão automática do IVA de vários países (PT, BR, EUA, UE, Japão, etc.)
- Simulação da receita líquida com base no número de subscrições
- Cálculo da perda total por país (Stripe + IVA)
- Gráfico comparativo das perdas por país
- Exportação dos resultados em formato Markdown
- Download do gráfico em PNG
- Pronta para deploy no [Streamlit Cloud](https://streamlit.io/cloud)

## 🚀 Como usar localmente

1. Instala o Python (recomenda-se Python 3.10+)
2. Instala as dependências:
   ```bash
   pip install streamlit pandas matplotlib
   ```
3. Executa o app:
   ```bash
   streamlit run calculadora_stripe_iva.py
   ```

## 🌐 Como publicar no Streamlit Cloud

1. Cria um repositório no GitHub e adiciona os ficheiros:
   - `calculadora_stripe_iva.py`
   - `requirements.txt`
2. No [Streamlit Cloud](https://streamlit.io/cloud), faz login com GitHub
3. Clica em **"New App"** e escolhe o repositório com o `calculadora_stripe_iva.py`
4. Clica em **Deploy**

## 📦 Requisitos (requirements.txt)

```
streamlit
pandas
matplotlib
```

## 📝 Exemplo de uso

- Subscrição de €10 com cartão internacional e IVA de 23% (Portugal):
  - Valor com IVA: €12,30
  - Stripe cobra ~€0,61
  - Recebes líquido: ~€11,69
- Com 10 subscrições: total líquido ≈ €116,90
- Perda total: ~€6,10

---

Desenvolvido com ❤️ para ajudar freelancers, criadores e pequenos negócios a entenderem suas receitas reais com Stripe.
