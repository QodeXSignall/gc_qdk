""" Тесты главного класса """
import unittest
from gc_qdk.main import GCoreQDK
from gc_qdk.tests.round_tests import functions


class MainTest(unittest.TestCase):
    """ Основные тесты """
    def __init__(self, *args, **kwargs):
        super(MainTest, self).__init__(*args, **kwargs)
        self.qdk = GCoreQDK('192.168.100.118', 4455, 'login', 'pass')
        self.qdk.make_connection()

    @unittest.SkipTest
    def test_start_round(self):
        self.qdk.start_round('В060ХА702', 'external', 'auto')
        count = 0
        self.qdk.subscribe()
        while True:
            print("RESPONSE:", self.qdk.get_response())
            count += 1
            if count == 10:
                self.qdk.start_round('В060ХА702', 'external', 'auto')

    def test_get_status(self):
        self.qdk.get_status()
        response = self.qdk.get_data()
        print('get_status_result', response)
        self.assertTrue(response['info'])

    def test_add_comment(self):
        record_id = 527
        add_comm = 'ADD COMM'
        self.qdk.add_comment(record_id, add_comm)
        self.qdk.get_data()
        self.qdk.get_record_comments(527)
        response = self.qdk.get_data()
        self.assertTrue(response['info']['record'] == record_id and
                        add_comm in response['info']['additional_notes'])

    def test_change_record(self):
        """ Тестирование изменение записи """
        record_id = 577
        new_car_number = 'В333ВВ333'
        new_carrier = 11
        new_tc = 4
        new_tt = 2
        new_comment = "NEW COMMENT"
        new_polygon = 2
        self.qdk.get_record_info(record_id)
        record_info = self.qdk.get_data()
        self.qdk.get_auto_info(auto_id=record_info['info']['auto'])
        auto_info = self.qdk.get_data()
        self.qdk.change_opened_record(record_id, car_number=new_car_number,
                                      carrier=new_carrier, trash_cat_id=new_tc,
                                      trash_type_id=new_tt,
                                      comment=new_comment, polygon=new_polygon)
        self.qdk.get_data()
        self.qdk.get_record_info(record_id)
        new_record_info = self.qdk.get_data()
        print('new_record_info_response', new_record_info)

        self.assertEqual(new_record_info['info']['carrier'], new_carrier)
        self.assertEqual(new_record_info['info']['trash_cat'], new_tc)
        self.assertEqual(new_record_info['info']['trash_type'], new_tt)
        self.qdk.change_opened_record(record_id,
                                      carrier=record_info['info']['carrier'],
                                      trash_cat_id=record_info['info']['trash_cat'],
                                      trash_type_id=record_info['info']['trash_type'],
                                      comment='OLD COMMENT')

    def test_close_opened_record(self):
        self.qdk.close_opened_record(record_id=751)
        response = self.qdk.get_data()
        self.assertEqual(response['info'], 751)
        self.qdk.close_opened_record(record_id=0)
        response = self.qdk.get_data()
        self.assertTrue(not response['info'])

    def test_get_unfinished_records(self):
        self.qdk.get_unfinished_records()
        unfinished_records = self.qdk.get_data()
        self.assertTrue(type(unfinished_records['info']) is list
                        or unfinished_records['info'] is None)

    def test_get_table_info(self):
        self.qdk.get_table_info('auto')
        auto_table = self.qdk.get_data()
        print('auto_table_result', auto_table)
        self.assertEqual(type(auto_table['info']), dict)
        self.assertEqual(auto_table['info']['status'], 'success')
        self.qdk.get_table_info('gcore_settings')
        settings_table = self.qdk.get_data()
        print('settings_table_result', settings_table)
        self.assertEqual(settings_table['info']['status'], 'failed')

    def test_get_last_event(self):
        self.qdk.get_last_event(auto_id=382)
        response = self.qdk.get_data()
        self.assertEqual(type(response), dict)

    def test_open_external_barrier(self):
        self.qdk.open_external_barrier()
        response = self.qdk.get_data()
        print('open_ext_barrier_response', response)
        self.assertTrue(response['info']['operation'] == 'open',
                        response['info']['barrier_name'] == 'close')

    def test_open_internal_barrier(self):
        self.qdk.open_internal_barrier()
        response = self.qdk.get_data()
        self.assertTrue(response['info']['operation'] == 'open',
                        response['info']['barrier_name'] == 'internal')

    def test_close_external_barrier(self):
        self.qdk.close_external_barrier()
        response = self.qdk.get_data()
        self.assertTrue(response['info']['operation'] == 'close',
                        response['info']['barrier_name'] == 'close')

    def test_close_internal_barrier(self):
        self.qdk.close_internal_barrier()
        response = self.qdk.get_data()
        self.assertTrue(response['info']['operation'] == 'close',
                        response['info']['barrier_name'] == 'internal')

    def test_auth_user(self):
        self.qdk.try_auth_user('test_user_1', '123')
        success_auth_response = self.qdk.get_data()
        self.assertTrue(success_auth_response['info']['status'] == 'success',
                        success_auth_response['info']['info'][0]['auth_status'])
        self.qdk.try_auth_user('test_user_1', '12345')
        fail_auth_response = self.qdk.get_data()
        self.assertTrue(fail_auth_response['info']['status'] == 'failed',
                        not fail_auth_response['info']['info'])

    def test_fix_gui_start(self):
        self.qdk.capture_gui_launched()
        response = self.qdk.get_data()
        self.assertTrue(response['info']['status'] == 'success')

    def test_fix_gui_terminated(self):
        self.qdk.capture_gui_terminated()
        response = self.qdk.get_data()
        self.assertTrue(response['info']['status'] == 'success')

    def test_add_carrier(self):
        self.qdk.add_carrier('test_carrier_1')
        response_only_name = self.qdk.get_data()
        print(response_only_name)
        self.qdk.add_carrier('test_carrier_1', inn=123)
        response_inn_add = self.qdk.get_data()
        print(response_inn_add)
        self.qdk.add_carrier('test_carrier_1', inn=123, kpp=321)
        response_kpp_add = self.qdk.get_data()
        print(response_kpp_add)
        self.qdk.add_carrier('test_carrier_1', inn=123,
                                                  kpp=321, ex_id='034')
        response_ex_id_add = self.qdk.get_data()
        print(response_ex_id_add)
        self.qdk.add_carrier('test_carrier_1', inn=123,
                                                   kpp=321, ex_id='034',
                                                   status='Действующий')
        response_status_add = self.qdk.get_data()
        print(response_status_add)
        self.qdk.add_carrier('test_carrier_1', inn=123, kpp=321, ex_id='034',
                             status='Действующий', wserver_id=345)
        response_wserver_id_add = self.qdk.get_data()
        print(response_wserver_id_add)

    def test_add_user(self):
        self.qdk.add_operator(full_name='TEST_FULL_NAME',
                              username='TEST_USERNAME',
                              password='TEST_PASSWORD',
                              wserver_id=1377)
        add_user_response = self.qdk.get_data()
        self.assertTrue(add_user_response['info']['status'] == 'success')

    def test_add_trash_cat(self):
        self.qdk.add_trash_cat('TEST_TRASH_CAT_1', wserver_id=1337)
        add_tc_response = self.qdk.get_data()
        self.assertTrue(add_tc_response['info']['status'] == 'success')

    def test_add_trash_type(self):
        self.qdk.add_trash_type('TEST_TRASH_TYPE_1', wserver_id=1337,
                                wserver_cat_id=1224)
        s_resp = self.qdk.get_data()
        print("S_RESP", s_resp)
        self.qdk.add_trash_type('TEST_TRASH_TYPE_2', wserver_id=1339,
                                wserver_cat_id=0)
        f_resp = self.qdk.get_data()
        print("F_RESP", f_resp)

    def test_add_auto(self):
        self.qdk.add_auto(car_number='В000ВВ001', wserver_id=9999999, model=0,
                          rfid='AAAAAA0004', id_type='tails', rg_weight=0)
        add_auto_response = self.qdk.get_data()
        self.assertTrue(add_auto_response['info']['status'] == 'success')

    def test_get_random(self):
        car_number = functions.get_random_bd_value(self.qdk, 'auto', 'car_number')
        print(car_number)
        self.assertTrue(type(car_number) == str)

    def test_response_operator(self):
        pass

if __name__ == '__main__':
    unittest.main()
