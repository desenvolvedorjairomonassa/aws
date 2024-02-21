Flink
-----


O Apache Flink é uma estrutura de processamento de fluxo de dados em tempo real e em lote. No contexto do Apache Zeppelin, o Flink é usado para executar trabalhos de processamento de dados
link https://zeppelin.apache.org/docs/latest/quickstart/flink_with_zeppelin.html


O %flink.pyflink é um subintérprete do Apache Flink no Apache Zeppelin que fornece um ambiente Python

para rodar uma query 
%flink.ssql(type=update)
select * from tmptickerstream;
