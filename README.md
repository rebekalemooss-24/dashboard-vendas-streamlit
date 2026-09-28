# Dashboard de Vendas com Streamlit

Aplicação interativa para acompanhar receita, quantidade vendida e desempenho de produtos. O dashboard permite filtrar registros por categoria e período, comparar resultados e exportar os dados selecionados.

> Projeto educacional desenvolvido com dados sintéticos para demonstração em portfólio.

## Demonstração

[Acesse o dashboard publicado](https://rebeka-dashboard-vendas.streamlit.app/)

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
- Streamlit;
- Altair.

## Como executar

1. Instale o Python 3.11 ou superior.
2. Abra um terminal na pasta do projeto.
3. Instale as dependências:

```bash
pip install -r requirements.txt
4. Inicie a aplicação:

```bash
streamlit run app.py
```

## Estrutura

```text
.
|-- app.py
|-- requirements.txt
|-- sales_data.csv
`-- README.md
```

## Decisões técnicas

- carregamento dos dados com cache do Streamlit;
- validação das datas e colunas numéricas;
- indicadores calculados conforme os filtros ativos;
- exportação em CSV compatível com o Excel;
- dependências fixadas para garantir a implantação.

## Limitações

- a base é sintética e pequena;
- os dados permanecem em um arquivo CSV local;
- não há autenticação, banco de dados ou atualização automática.

## Próximas etapas

- conectar o dashboard a um banco SQL;
- adicionar metas e comparação entre períodos;
- incluir testes automatizados e monitoramento da qualidade dos dados.

## Autoria

Projeto desenvolvido por Rebeka Lemos como estudo de análise de dados e visualização de indicadores de negócio.
