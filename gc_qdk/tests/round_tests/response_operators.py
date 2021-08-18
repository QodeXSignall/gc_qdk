""" Модуль содержит функции, которые используются для осуществления
действий, модулирующих тестовые явления, в ответ на события от GCore.
Простыми словами, тут все функции, которые срабатывают, если GCore
отправляет нужный статус. Ну например, GCore говорит, что ожидается
пересечение тестового фотоэлемента, и тестовый декоратор берет отсюда
какую нибудь функцию, ну например, блокировка фотоэелемнта, и заставляет
ее сработать, когда таймер будет на нужной отметке. """

from inspect import getfullargspec
from gc_qdk import cfg
from gc_qdk.tests.round_tests.scenaries import scenaries

def normal_entering_operator(qdk, *args, **kwargs):
    if kwargs['STATUS'].upper() == 'WAIT_PHOTOCELL_BLOCK_EXTERNAL_PHOTOCELL':
        set_photocell_operator(qdk, 'BEFORE_WEIGHING', 55, kwargs['TIMER'],
                                 kwargs['STAGE'], kwargs['STATUS'])
        set_photocell_operator(qdk, 'AFTER_WEIGHING', 43, kwargs['TIMER'],
                               kwargs['STAGE'], kwargs['STATUS'],
                               mode='block')
    if kwargs['STATUS'].upper() == 'WAIT_PHOTOCELL_RELIEVE_EXTERNAL_PHOTOCELL':
        set_photocell_operator(qdk, 'AFTER_WEIGHING', 22, kwargs['TIMER'],
                               kwargs['STAGE'], kwargs['STATUS'],
                               mode='unblock')
        set_photocell_operator(qdk, 'BEFORE_WEIGHING', 52, kwargs['TIMER'],
                               kwargs['STAGE'], kwargs['STATUS'],
                               mode='unblock')


def response_time_and_stage(func):
    """ Декоратор, который обеспечивает срабатывание функции при достижении
    нужной STAGE и TIMER из ответа """
    def wrapper(*args, **kwargs):
        argspec = getfullargspec(func).args
        all_args = dict(zip(argspec, locals()['args']))
        if all_args['timer_response'] == all_args['block_time'] and \
                all_args['stage_response'] == all_args['stage']:
            func(*args, **kwargs)
    return wrapper


@response_time_and_stage
def set_photocell_operator(qdk, stage, block_time, timer_response,
                           stage_response, status,
                           course_reverse=False, mode='block',
                           *args, **kwargs):
    """
    Настроить изменение состояния фотоэелемнента по времени.
    :param qdk: Экземпляр QDK для общения с QPI GCore.
    :param course_reverse: Фотоэлемент на противоположной стороне?
    :param mode Заблокировать его или разблокировать
    :param args:
    :param kwargs:
    :return:
    """
    if 'external' in status.lower() and not course_reverse:
        if mode == 'block':
            qdk.block_external_photocell()
        else:
            qdk.unblock_external_photocell()
    else:
        if mode == 'block':
            qdk.block_external_photocell()
        else:
            qdk.unblock_external_photocell()


def main_response_operator(qdk, *args, **kwargs):
    """ Главный обработчик ответов от GCore в контексте проведения тестов """
    scenario_dict = scenaries[cfg.current_scenario]
    functions = scenario_dict[kwargs['STAGE']][kwargs['STATUS']]
    for command, values in functions.items():
        if command == 'photocell':
            if kwargs['TIMER'] == values['timer']:
                values['operation'](qdk)
        elif command == 'weight':
            values['operation'](values['value'])
            values['used'] = True
