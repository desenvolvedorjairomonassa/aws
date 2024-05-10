SELECT productcategory,
       productsubcategory,
       deviceid,
       activitytype,
      count(*) quant,
      max (date_trunc('day', createts)) AS last_date
FROM "clickstream_db"."clickstream_data" 
group by deviceid,
       productcategory,
       productsubcategory,
       activitytype
order by productcategory       
