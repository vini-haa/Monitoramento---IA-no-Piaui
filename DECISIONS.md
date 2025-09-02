### 1. Análise de Sentimento: Abordagem por Regras vs. Machine Learning

**Decisão:** Adotar uma análise de sentimento baseada em regras (léxico) em vez de um modelo de Machine Learning.

**Justificativas:**

* **Interpretabilidade:** Por se basear na presença de palavras pré-definidas, temos uma abordagem mais transparente e rastreável.
* **Velocidade de Implementação:** A abordagem não exige dados de treino rotulados, permitindo um desenvolvimento mais rápido e iterativo.
* **Adequação ao Escopo:** Para uma visão geral, a análise através de léxico é suficiente, evitando a complexidade desnecessária de modelos de Machine Learning.
* **Manutenção Simplificada:** A precisão da aplicação pode ser ajustada diretamente na lista de palavras (adicionando ou retirando termos), sem a necessidade de um novo e demorado ciclo de treinamento.

---

### 2. Resiliência na Coleta de Dados

**Decisão:** Implementar um pipeline de coleta de dados robusto, capaz de lidar com falhas de forma controlada e previsível.

**Justificativas:**

* **Validação de Resposta HTTP:** O método `response.raise_for_status()` garante que apenas respostas bem-sucedidas (código de status 200) sejam processadas, tratando automaticamente erros de cliente (4xx) ou de servidor (5xx).