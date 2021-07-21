from serial import Serial
import serial.tools.list_ports


class SerialPort(Serial):
    '''
    расширение библиотеки Serial
    :param port
    String
    # default автоматическое определение
    Определение порта, по которому будет идти передача
    eg: "COM1"
    :param boudrate
    int
    # default 115200
    скорость соединения
    eg: 1000000
    '''
    def __init__(self, port=False, boudrate=115200):

        self.reconnect_tries = 0

        if not port:
            port = self.port_auto_definition()

        Serial.__init__(self, port, boudrate)

    @staticmethod
    def port_auto_definition(self):
        '''Метод автоматического определение порта передачи'''
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            return p

    def connect(self):
        '''Открывает порт, Расширение метода Serial.open(), для собственного обработчика ошибок'''
        try:
            self.open()
        except:
            print('error in Serial.connect()')

    def disconnect(self):
        '''Закрывает порт'''
        self.close()

    def reconnect(self):
        '''пытается переподключиться к порту'''
        if self.reconnect_tries >= 3:
            self.reconnect_tries = 0

        self.disconnect()
        self.connect()
        self.reconnect_tries += 1

    def send(self):
        pass

    def get(self):
        pass
