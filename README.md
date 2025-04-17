# 💳 Calculadora de Taxas Stripe

Aplicação interativa feita com **Streamlit** para simular quanto recebes após as taxas cobradas pelo Stripe em cada subscrição.

## ✨ Funcionalidades

- Cálculo da taxa Stripe por transação
- Simulação de receita líquida por número de subscrições
- Exportação de resultados em formato Markdown
- Suporte para cartões Europeus e Internacionais
- Pronta para deploy no [Streamlit Cloud](https://streamlit.io/cloud)

## 🚀 Como usar localmente

1. Instala o Python (recomenda-se Python 3.10+)
2. Instala as dependências:
   ```bash
   pip install streamlit pandas tabulate
   ```
3. Executa o app:
   ```bash
   streamlit run app.py
   ```

## 🌐 Como publicar no Streamlit Cloud

1. Cria um repositório no GitHub e adiciona os ficheiros:
   - `app.py`
   - `requirements.txt`
2. No [Streamlit Cloud](https://streamlit.io/cloud), faz login com GitHub
3. Clica em **"New App"** e escolhe o repositório com o `app.py`
4. Clica em **Deploy**

## 📝 Exemplo de uso

- Subscrição de €10 com cartão europeu:
  - Stripe cobra €0,39
  - Recebes €9,61
- Com 10 subscrições: total líquido = €96,10

---

Desenvolvido com ❤️ para ajudar freelancers, criadores e pequenos negócios a entenderem suas receitas reais com Stripe.