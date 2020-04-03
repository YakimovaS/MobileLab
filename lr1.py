import csv
import datetime
import time
from datetime import datetime

def count_tel (k, T):
    return k * T
    
    
def count_sms (k, N):
    return k * N

number = '933156729'
data = []
sms = 0
dur1 = 0.0
dur2 = 0.0

K_D = 4
K_P = 2
K_SMS = 1.5


wor = {}

with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
                if row.get('msisdn_origin') == number or row.get('msisdn_dest') == number:
                        data.append(row)


for i in data:
        if i.get('msisdn_origin') == number:
                sms = sms + int(i.get('sms_number'))
                calltime = datetime.strptime(i.get('timestamp'), '%Y-%m-%d %H:%M:%S')
                if calltime.hour < 1 and calltime.minute < 30:
                        dur1 = dur1 + float(i.get('call_duration'))
                else: dur2 = dur2 + float(i.get('call_duration'))
        elif i.get('msisdn_dest') == number:
                calltime = datetime.strptime(i.get('timestamp'), '%Y-%m-%d %H:%M:%S')
                if calltime.hour < 1 and calltime.minute < 30:
                        dur1 = dur1 + float(i.get('call_duration'))
                else: dur2 = dur2 + float(i.get('call_duration'))
ing = count_tel (K_D, dur1)
outg = count_tel (K_P, dur2)
vsesms = count_sms (K_SMS, sms)
print ("Стоимость звонков до 0:30 : ", ing)
print ("Стоимость звонков после 0:30 : ", outg)
print ("Стоимость SMS : ", vsesms)
print ("Суммарная стоимость : ", ing+outg+vsesms)
        
    
