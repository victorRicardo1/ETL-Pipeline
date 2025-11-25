
 
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
Agora que já temos os dados carregados na fase de Extração, podemos calcular a receita estimada de cada jogo multiplicando o preço pela quantidade de vendas desses jogos, assim, criando uma nova coluna para o arquivo representando a receita estimada desse jogo. Após calcular a receita estimada, calculamos a categoria de vendas no qual classifica como foram as vendas do jogo, também criando uma coluna nova para guardar este dado sobre como a venda se saiu, essa categoria se separa entre baixa(menor que 1 milhão), media(menor que 10 milhões e maior que 1 milhão) e alta onde é maior que 10 milhões. Além disso, também foi criada outra coluna para calcularmos a categoria das notas, assim, analizando se um jogo foi bom, ruim ou excelente, tendo esses jogos ordenados de acordo com a nota.

### 📊 Load
Nessa etapa vamos salvar os dados transformados em um novo arquivo CSV e criar 3 gráficos que possa ser visualizado em tela, um para a média dos generos, nota dos jogos e top receitas. Para isso, vou utilizar a biblioteca **Matplotlib** do pandas.

## 🧰 Ferramentas utilizadas

![PYTHON](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![GIT](https://img.shields.io/badge/Git-F05032.svg?style=for-the-badge&logo=Git&logoColor=white)
##### IDE utilizada: Spyder

