"""
Получить телефон клиента и отправить ему СМС

"""

'''
#smsc = SMSC()

#s = smsc.send_sms('7926xxx', 'test', id=12346, sender='sms')
#print(s)
#status = smsc.get_status(12346, '7926xxx', all=1)
#print(status)

['1', '1537938113', '0', '1537938112', '7926xxx', '2.20', 'SMSC.RU~sms', 'Доставлено', 'test,0']
'''
from smsc_api import *
import time
import sqlite3 as s3
# db_path = './project_files/gp10mo.db'


def put_data_to_db(number, name):
    """
    Добавление имени и номера в БД
    :param number:
    :param name:
    :return:
    """
    db_path = './project_files/gp10mo.db'
    con = s3.connect(db_path)

    input_query = 'INSERT INTO Client(phone_number, name) VALUES (?, ?)'  # добавление данных
    verifying_query = 'SELECT EXISTS(SELECT phone_number FROM Client WHERE phone_number=? )'  # проверка присутствия
    cur = con.cursor()
    verify_db_presence = cur.execute(verifying_query, (number,))
    verify_db_presence = verify_db_presence.fetchone()[0]
    # Если номера нет в базе добавляем его
    if not verify_db_presence:
        cur.execute(input_query, (number, name))
        con.commit()
        client_id = con.execute('SELECT LAST_INSERT_ROWID()')
        client_id = client_id.fetchone()[0]  # получаем номер последней записи
        cur.execute('INSERT INTO Status(status, client_id) VALUES (?, ?)', ('New', client_id))  # добавляем id клиента в Статус
        con.commit()
    else:
        print('Number exist')
    con.close()


def get_number_from_db():
    """
    получить номер из БД со статусом New
    :return: список кортежей номер, имя
    """
    # запрос к БД
    con = s3.connect('./project_files/gp10mo.db')
    cur = con.cursor()
    numbers = cur.execute('select phone_number, name from Client as c left join Status as s on c.client_id = s.client_id where s.status = "New"')
    numbers = numbers.fetchall()
    con.close()
    return numbers


def check_status():
    """
    Проверка статуса
    :return:
    """
    db_path = './project_files/gp10mo.db'
    con = s3.connect(db_path)
    c = con.cursor()
    n = c.execute('select exists(select status from status where status="New" )')
    m = n.fetchone()[0]
    if m:
        for i in get_number_from_db():
            print(i)
    else:
        print('not found')

'''
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


'''


put_data_to_db('7905111201', 'John!')

