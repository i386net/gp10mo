"""
Получить телефон клиента и отправить ему СМС

"""
from smsc_api import *
import time
import sqlite3 as s3

'''
#smsc = SMSC()

#s = smsc.send_sms('7926xxx', 'test', id=12346, sender='sms')
#print(s)
#status = smsc.get_status(12346, '7926xxx', all=1)
#print(status)

['1', '1537938113', '0', '1537938112', '7926xxx', '2.20', 'SMSC.RU~sms', 'Доставлено', 'test,0']
'''

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

    input_query = 'INSERT INTO clients(phone_number, name) VALUES (?, ?)'  # добавление данных
    verifying_query = 'SELECT EXISTS(SELECT phone_number FROM clients WHERE phone_number=? )'  # проверка присутствия
    cur = con.cursor()
    verify_db_presence = cur.execute(verifying_query, (number,))  # наличие номера в БД
    verify_db_presence = verify_db_presence.fetchone()[0]
    # Если номера нет в базе добавляем его
    if not verify_db_presence:
        cur.execute(input_query, (number, name))
        con.commit()
        client_id = con.execute('SELECT LAST_INSERT_ROWID()')
        # получаем номер последней записи
        client_id = client_id.fetchone()[0]
        # добавляем id клиента в Статус
        cur.execute('INSERT INTO client_status(client_status, client_id) VALUES (?, ?)', ('New', client_id))
        print('number {} was added'.format(number))
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
    numbers = cur.execute('select phone_number, name from clients as c left join client_status as s on c.id = s.client_id where s.client_status = "New"')
    numbers = numbers.fetchall()
    print(numbers)
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


def send_sms(num):
    """

    :param num:
    :return:
    """
    sms = SMSC()
    message = sms_message('welcome')
    # number = get_number_from_db() uncomment this
    number = num  # comment this
    sms_id = 'id' + number
    sms.send_sms(number, message, id=sms_id, sender='sms')
    #print(s)
    time.sleep(5)
    status = sms.get_status(sms_id, number)
    print(status)
    #full_status = sms.get_status(sms_id, number, all=1)
    #print(full_status)

# передаваемые параметры: phone, mes, id, to для входящих sms и phone,
# status, time, ts, id для статусов, метод POST
#send_sms('79268401046')


def sms_message(key):
    """
    Возаращает один из ответов в диалоге с клиентом
    :param key: str dict key
    :return: str dict value
    """
    messages = {
        'welcome': '1 или 2 -> 79037676877',
        'order_1': 'Город -> 79037676877',
        'order_2': 'Ф1 Ю2 -> 79037676877',
        'erunda_1': 'ерунда1',
        'erunda_2': 'ерунда2',
        'msk_order': 'Мск 1 или 2 -> 79037676877',
        'nn_order': 'НН 1 или 2 -> 79037676877',
        'ask_city': 'Город -> 79037676877',
        'ask_full_address': 'Адр -> 79037676877',
        'ask_email': 'Email -> 79037676877',
        'ask_full_name': 'ФИО -> 79037676877',
        'aks_company_details': 'Рекв -> 79037676877',
        'thnks_1': 'Thnks!-1',
        'thnks_2': 'Thnks!-2',
        'shipping_to_N': 'N -> 79037676877',
        'no_cdek_in_city': 'СДЭК нет'
    }

    return messages.get(key)


def get_answer(id, sms_id,  number, mes):
    pass


#put_data_to_db('79268401046', 'dk')
num = get_number_from_db()
#send_sms(num)



