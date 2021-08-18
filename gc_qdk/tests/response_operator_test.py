""" Тесты встроенного обработчика ответов от GCore. Выделен в отдельный файл,
поскольку в обычных тестах функционала, каждый ответ обрабатывается отдельно.
Здесь же, обработка будет полностью на плечах обработчика. """


import unittest
from gc_qdk.main import GCoreQDK


class ResOpTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ResOpTest, self).__init__(*args, **kwargs)
        func_dict = {'block_external_photocell': {'method': self.point_lock_operator,
                                    'term': self.point_lock_term}}
        self.qdk = GCoreQDK('192.168.100.118', 4455,
                            start_resp_operator=func_dict)
        self.qdk.make_connection()
        self.qdk.start_response_operator()

    def point_lock_operator(self, *args, **kwargs):
        print('POINT_LOCK_METHOD_LOCALS', locals())

    def point_lock_term(self, *args, **kwargs):
        print('POINT_LOCK_TERM_LOCALS', locals())

    def get_status_operator(self, *args, **kwargs):
        return "RETURN MESSAGE"

    def test_get_status_operator(self):
        self.qdk.block_external_photocell()

if __name__ == '__main__':
    unittest.main()
