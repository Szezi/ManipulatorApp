from pyfirmata2 import Arduino, util

try:
    board = Arduino(Arduino.AUTODETECT)
    board.samplingOn(10)
    print(board)
    iter8 = util.Iterator(board)
    iter8.start()

    pin_s1 = 'd:8:s'
    pin_s2 = 'd:9:s'
    pin_s3 = 'd:10:s'
    pin_s4 = 'd:11:s'
    pin_s5 = 'd:12:s'
    pin_s6 = 'd:13:s'

    servo1 = board.get_pin(pin_s1)
    servo2 = board.get_pin(pin_s2)
    servo3 = board.get_pin(pin_s3)
    servo4 = board.get_pin(pin_s4)
    servo5 = board.get_pin(pin_s5)
    servo6 = board.get_pin(pin_s6)


    def servos_write_initial(s1, s2, s3, s4, s5, s6):
        servo1.write(int(s1))
        servo2.write(int(s2))
        servo3.write(int(s3))
        servo4.write(int(s4))
        servo5.write(int(s5))
        servo6.write(int(s6))


    servos_write_initial(90, 60, 0, 180, 90, 90)


    def servos_write(s1, s2, s3, s4, s5, s6):
        servo1.write(int(90 + s1))
        servo2.write(int(s2))
        servo3.write(int(120 + s3))
        servo4.write(int(90 - s4))
        servo5.write(int(90 - s5))
        servo6.write(int(90 - s6))


    def servos_read():
        s1 = servo1.read()
        s2 = servo2.read()
        s3 = servo3.read()
        s4 = servo4.read()
        s5 = servo5.read()
        s6 = servo6.read()
        return s1, s2, s3, s4, s5, s6

except:
    status_log = 'Communication: Failed'
    status = False

else:
    status_log = 'Communication: Success'
    status = True

print(status_log)
