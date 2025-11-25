
 
 <h1 align="center">Analisando dados de games que fizeram sucesso nos ultimos anos</h1>

**Este exemplo foi feito em python como projeto para entender a pipeline ETL.**

## 👨🏽‍💻 Meu projeto

**Contexto**: Meu desafio é criar uma pipeline ETL para extrair dados de um arquivo CSV disponibilizado pela steam e sony para um podcast que gostaria de ter informações sobre o desempenho dos jogos em termos de vendas e classificação nos últimos anos<br/>
Feita a **Extração dos dados**, passarei para a fase de **Transformação**, na qual vou precisar calcular a receita estimada de cada jogo e criar uma classificação de nota melhor para cada jogo.<br/>
Por fim, devo realizar o **Carregamento do dados** transformados em um novo arquivo CSV, além de criar uma visualização gráfica de quais jogos foram mais vendidos e mais bem avaliados, ou, qual categoria foi a melhor avaliada.

## 📋 Etapas do Pipeline de ETL

### 🎲 Extract
Nesta etapa, vamos extrair os dados de resultados por área de conhecimento do arquivo CSV **games.csv**. Este arquivo traz informações referentes games. As colunas contidas no arquivo são as seguintes: **id**, **titulo**, **genero**, **preco**, **nota**, **vendas**.

### 📝 Transform
Agora que já temos os dados carregados na fase de Extração, podemos calcular a média de cada área do conhecimento nos últimos 5 anos usando a função **mean( )** do pandas.

### 📊 Load
Nessa etapa vamos salvar os dados transformados em um novo arquivo CSV e criar um gráfico que possa ser visualizado em tela. Para isso, vou utilizar a biblioteca **Matplotlib** do pandas.

## 🧰 Ferramentas utilizadas

![PYTHON](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![GIT](https://img.shields.io/badge/Git-F05032.svg?style=for-the-badge&logo=Git&logoColor=white)
![GOOGLE COLAB](https://img.shields.io/badge/Google%20Colab-F9AB00.svg?style=for-the-badge&logo=Google-Colab&logoColor=white)
![VSCODE](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC.svg?style=for-the-badge&logo=Visual-Studio-Code&logoColor=white)

## 🔗 Confira meu projeto no Google Colab
<a target="_blank" href="https://colab.research.google.com/drive/1qwz1d6T6c64Mc0VCYbBY1do9-dL9UPrG#scrollTo=kNuP0SDUZMBY">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
