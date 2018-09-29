#
#  Проверка получения ответных смс
#

import requests
import service_access as sa


def get_sms_answer():
    url = 'https://smsc.ru/sys/get.php?get_answers=1'
    # &login=<login>&psw=<password>
    # login = sa.login
    # password = sa.password
    params = {'login': sa.login,
              'psw': sa.password,
              'fmt': '3',


    }
    r = requests.get(url, params)
    print(r.text)


get_sms_answer()
