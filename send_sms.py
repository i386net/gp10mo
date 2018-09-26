"""
Получить телефон клиента и отправить ему СМС

"""
from smsc_api import *
import time

#smsc = SMSC()

#s = smsc.send_sms('7926xxx', 'test', id=12346, sender='sms')
#print(s)
#status = smsc.get_status(12346, '7926xxx', all=1)
#print(status)
"""
['1', '1537938113', '0', '1537938112', '7926xxx', '2.20', 'SMSC.RU~sms', 'Доставлено', 'test,0']
"""


def get_number_db():
    """
    получить номер из БД
    :return:
    """
    # запрос к БД
    phone_number = '123456789'
    return phone_number


def send_sms(num):
    welcome_message = "Здравствуйте! Если хотите узнать стоимость доставки, пришлите цифру 1. " \
                      "Если Вам нужно выставить счетдоговор, пришлите цифру 2"
    sms = SMSC()
    number = get_number_db()
    num_id = 'id' + number
    s = sms.send_sms(number, welcome_message, id=num_id, sender='sms')
    print(s)
    time.sleep(10)
    status = sms.get_status(num_id, number)
    print(status)
    full_status = sms.get_status(num_id, number, all=1)
    print(full_status)

# передаваемые параметры: phone, mes, id, to для входящих sms и phone,
# status, time, ts, id для статусов, метод POST
#send_sms('79268401046')


def get_answer(id, sms_id,  number, mes):
    pass


