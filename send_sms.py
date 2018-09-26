"""
Получить телефон клиента и отправить ему СМС

"""
import clean_phone
from smsc_api import *

smsc = SMSC()

#s = smsc.send_sms('7926xxx', 'test', id=12346, sender='sms')
#print(s)
status = smsc.get_status(12346, '7926xxx', all=1)
print(status)
"""
['1', '1537938113', '0', '1537938112', '7926xxx', '2.20', 'SMSC.RU~sms', 'Доставлено', 'test,0']
"""