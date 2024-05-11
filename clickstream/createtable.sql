CREATE EXTERNAL TABLE `Clickstream_data`(
`customerid` string COMMENT 'from deserializer', 
`deviceid` string COMMENT 'from deserializer', 
`productid` string COMMENT 'from deserializer',
`productcategory` string COMMENT 'from deserializer',
`productsubcategory` string COMMENT 'from deserializer',
`activitytype` string COMMENT 'from deserializer',
`createts` timestamp COMMENT 'from deserializer')
ROW FORMAT SERDE 
'org.openx.data.jsonserde.JsonSerDe' 
STORED AS INPUTFORMAT 
'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
's3://bucketStoreUnico/enriched'
TBLPROPERTIES (
'classification'='json')