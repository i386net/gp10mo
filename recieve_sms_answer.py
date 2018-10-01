#
#  Проверка получения ответных смс
#

import requests
import service_access as sa
import sqlite3 as s3


def max_sms_id():
    """
    Ищем максимальный ID смс сообщения
    :return:
    """
    con = s3.connect('./project_files/gp10mo.db')
    cursor = con.cursor()
    query = 'SELECT MAX(sms_id) FROM answers'
    get_max_sms_id = cursor.execute(query).fetchone()[0]
    con.close()
    # print(get_max_sms_id)
    return get_max_sms_id


def get_sms_answer():
    url = 'https://smsc.ru/sys/get.php?get_answers=1'
    params = {'login': sa.login,
              'psw': sa.password,
              'fmt': '3',  # формат получения ответа в виде списка словарей"
              'after_id': max_sms_id()  # макс ID смс сообщения
              }
    r = requests.get(url, params)

    return r.json()


def update_db_with_answer(answer):
    try:
        answer = answer
    except IndexError:
        pass

    if answer:
        con = s3.connect('./project_files/gp10mo.db')
        cursor = con.cursor()

        insert_query = 'INSERT INTO ' \
                       'answers(sms_id, received, phone_number, message, to_phone, sent) ' \
                       'VALUES(?,?,?,?,?,?)'
        try:
            for element in answer:
                element = tuple(element.values())
                cursor.execute(insert_query, element)
                con.commit()
        except s3.IntegrityError as err:
            print(err)
        con.close()


#ans = get_sms_answer()
#update_db_with_answer(ans)
