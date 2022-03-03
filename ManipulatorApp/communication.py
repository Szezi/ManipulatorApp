from pyfirmata2 import Arduino, util


class RobotComm(object):
    """ The class establishes communication with robotic arm and read from / write to robotic servos """
    def __init__(self, pin_s1: str, pin_s2: str, pin_s3: str, pin_s4: str, pin_s5: str, pin_s6: str):
        self.board = Arduino(Arduino.AUTODETECT)
        self.board.samplingOn(10)
        self.iter8 = util.Iterator(self.board)

        self.servo1 = self.board.get_pin(pin_s1)  # servo base
        self.servo2 = self.board.get_pin(pin_s2)  # servo link 1
        self.servo3 = self.board.get_pin(pin_s3)  # servo link 2
        self.servo4 = self.board.get_pin(pin_s4)  # servo link 3
        self.servo5 = self.board.get_pin(pin_s5)  # servo effector_movement
        self.servo6 = self.board.get_pin(pin_s6)  # servo effector_action

    def start(self):
        self.iter8.start()

    def stop(self):
        self.board.exit()

    def servos_write(self, s1, s2, s3, s4, s5, s6):
        self.servo1.write(int(s1))
        self.servo2.write(int(s2))
        self.servo3.write(int(s3))
        self.servo4.write(int(s4))
        self.servo5.write(int(s5))
        self.servo6.write(int(s6))

    def servos_read(self):
        s1 = self.servo1.read()
        s2 = self.servo2.read()
        s3 = self.servo3.read()
        s4 = self.servo4.read()
        s5 = self.servo5.read()
        s6 = self.servo6.read()
        return s1, s2, s3, s4, s5, s6
