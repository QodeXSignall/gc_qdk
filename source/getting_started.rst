Начало работы
==========
Быстрый старт
----------------------------------

Для подключения к Gravity Compound и начала работы выполните:



.. code-block:: python
   :emphasize-lines: 1-3,5

   from gc_qdk.main import GCoreQDK


   """ Создаем экземпляр класса, с помощью методов которого мы будем взаимодействовать с GCore. """
   # Указываем IP адрес компьютера (host_ip), на котором работает Gravity Compound.
   # Указываем порт (host_port), который был назначен для QPI GC.
   qdk_inst = GCoreQDK(host_ip='192.168.100.109', host_port=15500)

   # Выполняем подключение.
   qdk_inst.make_connection()

   # Выплняем команду (например, на получение статуса готовности GC на начало взвешивания).
   qdk_inst.get_status()

   # Получаем ответ
   response = qdk_inst.get_data()
   print(response)   # True|False

Для получения полного перечня функций смотрите :ref:`rst-markup-label`
