# 📊 Painel de Monitoramento de Notícias sobre IA no Piauí

## 📖 Descrição do Projeto

Este projeto é um dashboard interativo construído em Python e Streamlit que coleta, processa e analisa notícias em tempo real sobre o tema "Inteligência Artificial no Piauí". O objetivo é fornecer uma visão geral do tom da cobertura da mídia sobre o assunto, identificando tendências e os principais temas discutidos.

Este é um projeto de portfólio desenvolvido para demonstrar habilidades em todo o ciclo de vida de um projeto de dados, desde a coleta até a visualização.

## ✨ Funcionalidades Principais

- **Coleta de Dados em Tempo Real:** Utiliza o feed RSS do Google Notícias para buscar as notícias mais recentes.
- **Processamento de Linguagem Natural (PLN):** Limpa os textos das notícias, removendo tags HTML e entidades.
- **Análise de Sentimento:** Classifica cada notícia como Positiva, Negativa ou Neutra usando uma abordagem baseada em regras (léxico).
- **Dashboard Interativo:** Apresenta os resultados em uma interface web amigável com:
  - Gráfico de pizza com a distribuição dos sentimentos.
  - Nuvem de palavras com os termos mais frequentes.
  - Tabela de dados interativa com os detalhes das notícias.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Coleta de Dados:** `requests`, `xml.etree.ElementTree`
- **Manipulação de Dados:** `pandas`
- **Visualização de Dados:** `streamlit`, `plotly`, `wordcloud`, `matplotlib`
- **Versionamento:** `git` e `GitHub`

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar o projeto localmente.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/vini-haa/Monitoramento---IA-no-Piaui.git](https://github.com/vini-haa/Monitoramento---IA-no-Piaui.git)
    cd Monitoramento---IA-no-Piaui
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o dashboard Streamlit:**
    ```bash
    streamlit run dashboard.py
    ```

A aplicação será aberta automaticamente no seu navegador.

## 📁 Estrutura do Projeto

```
.
├── coleta_dados.py       # Módulo responsável pela coleta de notícias via RSS.
├── processamento_dados.py  # Módulo para limpeza dos dados e análise de sentimento.
├── dashboard.py          # Script principal que constrói a aplicação Streamlit.
├── requirements.txt      # Lista de dependências do projeto.
├── noticias_processadas.csv   # Arquivo CSV gerado pelo script com os dados coletados.
└── README.md             # Este arquivo.
```

## 🤖 Contribuição da Inteligência Artificial

A Inteligência Artificial foi utilizada como ferramenta de apoio neste projeto, atuando na depuração de erros, na escolha de palavras positivas e negativas e no refinamento de detalhes da função de visualização (Streamlit). 
Optei por usar a IA nessas áreas por serem aquelas em que possuo menos prática entre as tecnologias obrigatórias do case.
Assim como na formatação deste arquivo README.md.
