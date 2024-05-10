import json
import random
import time
import urllib3

def lambda_handler(event, context):
    acustomerid = ["Cust01","Cust02","Cust03"]
    adeviceid = ["Desktop","Mobile","iPad","Android"]
    aproductid = ["Prod01","Prod02","Prod03","Prod04"]
    aproductcategory = ["Clothing","Shoes","Handbags","Jewelry&accessories"]
    aproductsubcategory = ["Mens","Womens","Kids"]
    aactivitytype = ["AddToCart","ViewProduct","PurchaseItem"]
    http = urllib3.PoolManager()
    urlbase = 'https://...'
    cnt = 0 
    while cnt < 1000 :
        customerid= random.choice(acustomerid)
        deviceid= random.choice(adeviceid)
        productid= random.choice(aproductid)
        productcategory= random.choice(aproductcategory)
        productsubcategory= random.choice(aproductsubcategory)
        activitytype= random.choice(aactivitytype)
        url = urlbase + customerid + '&deviceid=' + deviceid + '&productid=' + productid + '&productcategory=' + productcategory + '&productsubcategory='+ productsubcategory + '&activitytype='+ activitytype
        print (url)
        response = http.request('GET',url)
        api_status = json.loads(response.data.decode('utf-8'))
        if response.status == 200:
            print('Request successful')
            print(response.data)
        else:
            print('Request failed')
        time.sleep(0.25)
        cnt = cnt+1
    return response.status                  
