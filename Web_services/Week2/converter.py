from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get(f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}') 
    soup = BeautifulSoup(response.content, 'xml')

    second_val = soup.find('CharCode', text=cur_to).find_next_sibling('Value')
    second_nominal = soup.find('CharCode', text=cur_to).find_next_sibling('Nominal')
    if cur_from != 'RUR':
        first_val = soup.find('CharCode', text=cur_from).find_next_sibling('Value')
        first_nominal = soup.find('CharCode', text=cur_from).find_next_sibling('Nominal')
        first_val_rub = (Decimal(first_val.text.replace(',','.'))/int(first_nominal.text)) * amount
        print(first_val_rub)
    else:
        first_val_rub = amount
    
    total_sum = first_val_rub/(Decimal(second_val.text.replace(',','.')) /int(second_nominal.text))  
    
    return total_sum.quantize(Decimal("1.00")) 