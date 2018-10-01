#
#  Проверка получения ответных смс
#

import requests
import service_access as sa
import sqlite3 as s3


def get_sms_answer():
    url = 'https://smsc.ru/sys/get.php?get_answers=1'
    # &login=<login>&psw=<password>
    # login = sa.login
    # password = sa.password
    params = {'login': sa.login,
              'psw': sa.password,
              'fmt': '3',  # формат получения ответа в виде списка словарей"
              'hour': '3'
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

        insert_query = 'INSERT INTO answers(sms_id, received, phone_number, message, to_phone, sent) VALUES(?,?,?,?,?,?)'
        try:
            for element in answer:
                element = tuple(element.values())
                cursor.execute(insert_query, element)
                con.commit()
                con.close()
        except s3.IntegrityError as err:
            print(err)





    """
    [{
        "id": 47436134,
        "received": "29.09.2018 15:07:39",
        "phone": "79268401046",
        "message": "1",
        "to_phone": "79037676877",
        "sent": "29.09.2018 15:07:37"
        }]
    """


ans = get_sms_answer()
update_db_with_answer(ans)
