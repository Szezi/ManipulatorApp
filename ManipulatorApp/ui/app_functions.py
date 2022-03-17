## ==> GUI FILE
from ManipulatorApp.main import MainWindow
from ManipulatorApp.main import *
from ManipulatorApp.modules import FK
from ManipulatorApp.modules import trajectory


class AppFunctions(MainWindow):
    def __init__(self):
        super().__init__()

    def page_fk(self):
        eff = [54, 0]
        theta1 = self.ui.horizontalSlider_fk_s1.value()
        theta2 = self.ui.horizontalSlider_fk_s1_2.value()
        theta3 = self.ui.horizontalSlider_fk_s1_3.value()
        theta4 = self.ui.horizontalSlider_fk_s1_4.value()
        servo_5 = self.ui.horizontalSlider_fk_s1_5.value()
        servo_6 = self.ui.horizontalSlider_fk_s1_6.value()

        result = FK.fk_dh(theta1, theta2, theta3, theta4, eff)

        self.ui.lcdNumber_dh_X_2.display(result[1][0])
        self.ui.lcdnumber_dh_Y_2.display(result[1][1])
        self.ui.lcdnumber_dh_Z_2.display(result[1][2])
        print(result)

