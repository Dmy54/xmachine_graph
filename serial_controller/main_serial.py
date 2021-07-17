from serial_controller.modules.serial_port import SerialPort

serial = SerialPort(port="COM3")

serial.connect()
serial.disconnect()
