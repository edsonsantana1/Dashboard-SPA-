# Dashboard Single Page Application (Projeto Data Science)

- Dashboard SPA - Análise de Casos criminais
- Este projeto é uma aplicação web do tipo SPA (Single Page Application) desenvolvida com **Flask**, **MongoDB** e **XGBoost**.

---

## Funcionalidades

- Visualização de dashboards interativos com gráficos dinâmicos usando Chart.js
- Filtros de data e variáveis para análise customizada
- Backend com Flask para API REST e manipulação dos dados
- Armazenamento dos dados no MongoDB
- Integração com modelo de machine learning XGBoost para análises preditivas

---

## Estrutura do Projeto

- `/backend` - Código Python com Flask para API e lógica de negócio
- `/frontend` - Código HTML, CSS e JavaScript para a interface SPA
- `/model.pkl` - Modelo treinado do XGBoost (não versionado no GitHub)
- `/venv` - Ambiente virtual Python (ignorando no Git)

---

## Visualização e Gráficos

A aplicação frontend apresenta dashboards interativos que permitem a análise visual dos dados dos casos armazenados no MongoDB, com base nos dados processados e fornecidos pela API Flask.

### Principais Gráficos

- **Distribuição de Casos por Tipo**  
  Gráfico de barras ou pizza que mostra a quantidade de casos para cada tipo (ex: Furto, Assalto, Violência doméstica, Tráfico), permitindo identificar rapidamente quais tipos de crime são mais frequentes.

- **Casos por Localização**  
  Mapa ou gráfico de barras para comparar o número de casos registrados em diferentes localidades (ex: Centro, Bairro A, Zona Rural).

- **Faixa Etária das Vítimas**  
  Histograma ou gráfico de barras que exibe a distribuição das idades das vítimas, ajudando a entender qual faixa etária é mais afetada.

- **Distribuição Étnica das Vítimas**  
  Gráfico de pizza ou barras que mostra a proporção das etnias das vítimas.

- **Importância das Features no Modelo XGBoost**  
  Gráfico de barras horizontal que exibe a importância relativa das variáveis usadas no modelo preditivo, como idade, etnia e localização, para explicar o impacto de cada uma na predição.

### Como os gráficos são gerados

- O frontend consome os dados via endpoints da API REST Flask, que busca os registros do MongoDB e realiza pré-processamento básico.
- Para os dados preditivos, o modelo XGBoost treinado é carregado no backend e utilizado para fornecer probabilidades e predições em tempo real.
- As importâncias das features são recuperadas pelo endpoint `/api/modelo/coeficientes` e exibidas em um gráfico dedicado, permitindo entender o comportamento do modelo.
- Bibliotecas JavaScript como **Chart.js** são utilizadas para criar gráficos responsivos e interativos diretamente na página SPA.

### Benefícios da Visualização

- Facilita a identificação de padrões e tendências nos dados.
- Apoia decisões baseadas em evidências, especialmente em contextos criminais.
- Permite acompanhar a evolução dos tipos de casos e o impacto das variáveis no modelo preditivo.
- Proporciona uma interface intuitiva para usuários não técnicos explorarem os dados.

---

## Tecnologias Utilizadas

- Python 3.x + Flask
- MongoDB
- XGBoost
- HTML / CSS / JavaScript
- Chart.js para gráficos interativos
- Git para controle de versão

---

## Como Rodar o Projeto Localmente

1. Clone o repositório  
   ```bash
   git clone https://github.com/edsonsantana1/Dashboard-SPA-.git
   cd crime-analysis-app
