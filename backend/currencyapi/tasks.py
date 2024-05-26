from celery import shared_task
from .models import *
import re
import datetime
import requests
import xmltodict

pattern = r'[0-9]' #this regex is used to remove number from string

def parsing_api():
    current_dt = datetime.datetime.now()
    formatted_date = current_dt.strftime("%d.%m.%Y")
    url = f'https://cbar.az/currencies/{formatted_date}.xml'
    response = requests.get(url)
    data_dict = xmltodict.parse(response.content)

# Access elements
    get_main_data = data_dict['ValCurs']['ValType']
    get_main_data.pop(0) #Here, the first element is information about metal which we don't need
    
    new_data = get_main_data[0]["Valute"]
    return new_data




@shared_task
def update_or_create():
    currency = Currency.objects.all()

    if len(currency) == 0:
        create()
        api_update_dt = UpdateApiDateTime()
        api_update_dt.api_update_time = datetime.datetime.now()
        api_update_dt.save() #When any changes happen in db, Updatetime model save datetime of the situation
    else:
        for x in parsing_api():
            # Checks if there is new adding change then add it, in other case just updated data with new data 
            currency = Currency.objects.update_or_create(
                name = re.sub(pattern, '', x['Name']),
                defaults={"code": x['@Code'], "name" : re.sub(pattern, '', x['Name']), "nominal": x['Nominal'], "value" : float(x["Value"])}
            )
        api_update_dt = UpdateApiDateTime()
        api_update_dt.api_update_time = datetime.datetime.now()
        api_update_dt.save()

#This function creates bulky objects of Currency models
def create():
    #bulk_create doesn't need save() method
    currency = Currency.objects.bulk_create(
        [Currency(code = x['@Code'], name=re.sub(pattern, '', x['Name']), nominal=x['Nominal'], value = float(x["Value"])) for x in parsing_api()]
    )
