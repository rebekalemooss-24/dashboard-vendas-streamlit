# Dashboard de Vendas com Streamlit

Aplicação interativa para acompanhar receita, quantidade vendida e desempenho de produtos. O dashboard permite filtrar os registros por categoria e período, comparar resultados e exportar os dados selecionados.

> Projeto educacional desenvolvido com dados sintéticos para demonstração em portfólio.

## Funcionalidades

- filtros por categoria e intervalo de datas;
- indicadores de receita, quantidade, venda média e produtos ativos;
- evolução diária da receita;
- comparação da receita por categoria;
- ranking dos produtos com maior receita;
- tabela detalhada e exportação em CSV;
- tratamento de filtros sem resultados.

## Tecnologias

- Python;
- Pandas;
- Streamlit.

## Como executar

1. Instale o Python 3.11 ou superior.
2. Abra um terminal na pasta do projeto.
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie a aplicação:

```bash
streamlit run app.py
```

## Estrutura

```text
.
|-- app.py
|-- requirements.txt
|-- dados_de_vendas.csv
`-- README.md
```

## Decisões técnicas

- o carregamento dos dados utiliza cache do Streamlit para evitar leituras repetidas;
- datas e colunas numéricas são validadas antes da análise;
- os cálculos usam apenas os registros correspondentes aos filtros ativos;
- o CSV exportado usa separador por ponto e vírgula e codificação compatível com o Excel.

## Limitações

- a base é sintética e pequena;
- os dados permanecem em um arquivo CSV local;
- não há autenticação, banco de dados ou atualização automática.

## Próximas etapas

- publicar a aplicação no Streamlit Community Cloud;
- conectar o dashboard a um banco SQL;
- adicionar metas, comparação entre períodos e testes automatizados.

## Autoria

Projeto desenvolvido por Rebeka Lemos como estudo de análise de dados e visualização de indicadores de negócio.
