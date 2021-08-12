""" Содержит функционал, необходимый для тестов """
import random
import uuid


def get_random_carnum():
    """ Генерирует случайную последовательность и возвращает ее"""
    random_car_num = str(uuid.uuid4())
    return random_car_num[:10]


def get_random_bd_value(qdk, table_name: str, column: str):
    """
    Вернуть случайное значение поля column из таблицы table_name.
    Используется для того, что бы не харкдоить идентификаторы видов грузов,
    категорий авто и т.д. Вызывая эту функцию мы будем уверены, что такие
    данные точно будут в БД
    :param qdk: экземпляр qdk, подключенный к GCore QPI
    :param table_name: имя таблицы
    :param column: название поля
    :return: str
    """
    qdk.get_table_info(table_name=table_name, only_active=True)
    result = qdk.get_data()
    table_content = result['info']['info']
    random_data = random.choice(table_content)
    value = random_data[column]
    return value


def start_round(qdk, course,
                car_choose_mode='auto',
                dlinnomer=False, polomka = False,
                car_num=None, trash_cat=None, trash_type=None, carrier=None,
                operator=None, notes=None,
                duo_polygon=None):
    """
    Отправить команду на начало раунда взвешивания
    :param qdk: экземпляр qdk, подключенный к GCore QPI
    :param course: направление авто ('external'/'internal')
    :param car_choose_mode: способ выбора авто ('auto'/'manual')
    :param dlinnomer: спец. протокол длинномер? (True/False)
    :param polomka: спец. протокол хвосты? (True/False)
    :param car_num: гос.номер авто (если не указан, будет рандом)
    :param trash_cat: категория груза
    :param trash_type: вид груза (если не указан, будет рандом из БД)
    :param carrier: перевозчик (если не указан, будет рандом из БД)
    :param operator: весовщик (если не указан, будет рандом из БД)
    :param notes: комментарий на въезде
    :param duo_polygon: полигон-приемщик груза
    :return:
    """
    if not car_num:
        car_num = get_random_carnum()
    if not trash_cat:
        trash_cat = get_random_bd_value(qdk, 'trash_cats', 'id')
    if not trash_type:
        trash_type = get_random_bd_value(qdk, 'trash_types', 'id')
    if not carrier:
        carrier = get_random_bd_value(qdk, 'clients', 'id')
    if not operator:
        operator = get_random_bd_value(qdk, 'users', 'id')
    if not duo_polygon:
        duo_polygon = get_random_bd_value(qdk, 'duo_pol_owners', 'id')
    qdk.start_round(car_num, course, car_choose_mode, dlinnomer,
                    polomka, carrier, trash_cat, trash_type, notes,
                    operator, duo_polygon)
