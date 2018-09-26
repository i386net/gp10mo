import re


def clean_user_phone(number):
    """
    Убирает из номера лишние знаки
    :param number:
    :return:
    """
    number = re.split(r'[-+\s._)(:;#]', number)
    number = ''.join(number).strip()
    return number
