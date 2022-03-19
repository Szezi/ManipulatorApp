# ==> GUI FILE
from ManipulatorApp.main import MainWindow
from ManipulatorApp.main import *
from ManipulatorApp.modules import FK
from ManipulatorApp.modules import IK
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

        result = FK.fk_dh(theta1, theta2, theta3, theta4, eff)

        self.ui.lcdNumber_dh_X_2.display(result[1][0])
        self.ui.lcdnumber_dh_Y_2.display(result[1][1])
        self.ui.lcdnumber_dh_Z_2.display(result[1][2])
        print(result)

        # Sim

    def page_ik(self):
        eff = [54, 0]
        value_x = self.ui.horizontalSlider_ik_x.value()
        value_y = self.ui.horizontalSlider_ik_y.value()
        value_z = self.ui.horizontalSlider_ik_z.value()
        value_alpha = self.ui.verticalSlider.value()

        result = IK.ik_geo(value_x, value_y, value_z, value_alpha, eff)
        result_config1 = result[0]
        result_config2 = result[1]
        print(result)
        self.ui.lcdNumber_ik_s1.display((result_config1[0]))
        self.ui.lcdNumber_ik_s2.display((result_config1[1]))
        self.ui.lcdNumber_ik_s3.display((result_config1[2]))
        self.ui.lcdNumber_ik_s4.display((result_config1[3]))

        self.ui.lcdNumber_ik_s1_2.display((result_config2[0]))
        self.ui.lcdNumber_ik_s2_2.display((result_config2[1]))
        self.ui.lcdNumber_ik_s3_2.display((result_config2[2]))
        self.ui.lcdNumber_ik_s4_2.display((result_config2[3]))

        # Sim

    def page_manual(self):
        eff = [54, 0]
        if self.ui.tab_manual_joints.isVisible():
            value_j1 = self.ui.horizontalSlider_j_s1.value()
            value_j2 = self.ui.horizontalSlider_j_s2.value()
            value_j3 = self.ui.horizontalSlider_j_s3.value()
            value_j4 = self.ui.horizontalSlider_j_s4.value()

            value_manual_xyz = FK.fk_dh(int(value_j1), int(value_j2), int(value_j3), int(value_j4), eff)
            print(value_manual_xyz)
            self.ui.horizontalSlider_manual_x.setValue(value_manual_xyz[1][0])
            self.ui.horizontalSlider_manual_y.setValue(value_manual_xyz[1][1])
            self.ui.horizontalSlider_manual_z.setValue(value_manual_xyz[1][2])
            self.ui.verticalSlider_manual_orient.setValue(value_manual_xyz[0])

        elif self.ui.tab_manual_xyz.isVisible():
            value_x = self.ui.horizontalSlider_manual_x.value()
            value_y = self.ui.horizontalSlider_manual_y.value()
            value_z = self.ui.horizontalSlider_manual_z.value()
            value_alpha = self.ui.verticalSlider_manual_orient.value()

            value_manual_joints = IK.ik_geo(value_x, value_y, value_z, value_alpha, eff)
            print(value_manual_joints)
            self.ui.horizontalSlider_j_s1.setValue(value_manual_joints[0][0])
            self.ui.horizontalSlider_j_s2.setValue(value_manual_joints[0][1])
            self.ui.horizontalSlider_j_s3.setValue(value_manual_joints[0][2])
            self.ui.horizontalSlider_j_s4.setValue(value_manual_joints[0][3])

        servo_1 = self.ui.horizontalSlider_j_s1.value()
        servo_2 = self.ui.horizontalSlider_j_s2.value()
        servo_3 = self.ui.horizontalSlider_j_s3.value()
        servo_4 = self.ui.horizontalSlider_j_s4.value()
        servo_5 = self.ui.horizontalSlider_j_s5.value()
        servo_6 = self.ui.horizontalSlider_j_s6.value()
        # send values to servos
        # Sim

    def page_automatic(self):
        pass
