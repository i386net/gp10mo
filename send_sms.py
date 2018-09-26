"""
Получить телефон клиента и отправить ему СМС

"""
import clean_phone
from smsc_api import *

smsc = SMSC()

smsc.send_sms('num', 'test', sender='sms')
