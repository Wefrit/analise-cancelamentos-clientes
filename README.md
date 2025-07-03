# 📊 Análise de Cancelamentos de Clientes

Este projeto tem como objetivo identificar os principais motivos que levam clientes a cancelarem serviços. A análise é feita com base em uma base de dados fictícia usando Python, `pandas` e `plotly`.
Projeto baseado em curso da hashtag treinamentos.

## 🧠 O que o projeto faz

- Importa e trata os dados da base `cancelamentos.csv`
- Remove colunas e linhas desnecessárias
- Calcula a porcentagem de clientes que cancelaram
- Gera gráficos interativos para entender os fatores relacionados ao cancelamento

## 📁 Estrutura

projeto_2/

├── cancelamentos.csv

├── analise_cancelamento.py

└── README.md

## 🛠️ Tecnologias utilizadas

- Python 3.13
- pandas
- plotly

## ▶️ Como executar

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/analise-cancelamentos-clientes.git
```
2. Instale as bibliotecas necessárias:
```bash
pip install pandas plotly
```
3. Execute o script:
```bash
python analise_cancelamentos.py
```

⚠️ Atenção: O arquivo cancelamentos.csv tem mais de 50MB. O GitHub recomenda usar Git LFS para armazenar arquivos grandes.
Você pode usar o seu próprio arquivo para fazer a análise, basta mudar o nome dentro do script e colocar o arquivo na mesma pasta.

Feito com Python por Nathan Lopes
