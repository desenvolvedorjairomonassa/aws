

Arquitetura 

<img src="Captura de tela 2024-05-09 221842.png" alt="Descrição da imagem">

Arquitetura de Clickstream da AWS

A imagem é uma arquitetura de clickstream da AWS. O clickstream é um registro das ações que um usuário realiza em um site ou aplicativo, como cliques em links, visualizações de páginas e compras. Essa arquitetura usa vários serviços da AWS para coletar, armazenar, processar e analisar dados de clickstream.

## Componentes da arquitetura

A arquitetura de clickstream da AWS é composta pelos seguintes componentes:

- **Portal da web do cliente**: Este é o ponto de partida para os usuários da sua aplicação. Quando um usuário acessa o portal da web, seus cliques e outras ações são registrados.
- **Amazon API Gateway**: Este serviço gerencia o tráfego entre o portal da web do cliente e os outros serviços da AWS.
- **AWS Lambda**: Este serviço é usado para executar funções sem servidor. Na arquitetura de clickstream, o Lambda joga os dados dos clicks do API Gateway pata kinesis data streams
- **Amazon Kinesis Data Streams**: Este serviço é usado para coletar e armazenar dados de clickstream em tempo real.
- **Amazon Kinesis Firehose**: Este serviço é usado para ingerir dados de clickstream em Kinesis Data Streams. O Firehose vai jogar os dados do Kinesis streams no S3
- **Amazon S3**: Este serviço é usado para armazenar dados de clickstream de forma duradoura. O S3 é um armazenamento de objetos escalável e durável que pode armazenar grandes volumes de dados. O firehose vai jogar em uma janela  no tipo ode arquivo json, particionado dentro de folder em data : ano/mês/dia
- **Amazon Athena**: Este serviço é usado para consultar dados de clickstream armazenados no S3. O Athena é um serviço de consulta interativa que permite aos usuários consultar dados do clickstream no formato da tabela :
    - customerid
    - deviceid
    - productid
    - productcategory
    - productsubcategory
    - activitytype

- **Amazon QuickSight**: Este serviço é usado para visualizar dados de clickstream. O QuickSight é um serviço de visualização de dados que permite aos usuários criar painéis e relatórios interativos.

# custos:
- Considerei os custos de uma empresa média de e-comerce com 10 mil visitas por mês, sendo 100 mil cliques por mês
- API Gateway - rest APIs considerando 1 milhões/mês request = 4.25 USD
- Lambda - considerando os mesmos 1 milhão entra no free-tier
- kinesis 23 cliques por minutos de 40 kb  = 43.86 
- kinesis Firehose 23 per minute = 0.28 USD
- S3 38 GB STANDARD = 1.54 USD
- S3 456 GB GLACIER INSTANT Retrieval (1 ano)= 3.78
- Athena consulta 20 por dia para 38 GB = 203.06 USD
- Quicksight = 26 USD

Custo total : 282,77 USD
# **arquivos**:
  
- consultaAthena.sql - consulta do stream no Athena, agrupado por categoria, subcategoria e dispositivo
- ClickStream-setup.yaml - IaC em cloudFormation
- lambda_sent_kinesis.py - lambda que pega os dados do API Gateway e envia para Kineis ( ele já está incluindo no yaml)
- createtable.sql - cria a tabela no athena (criar o nome do bucket)
