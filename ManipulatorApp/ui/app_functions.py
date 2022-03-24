# ==> GUI FILE
from ManipulatorApp.main import MainWindow
from ManipulatorApp.main import *
from ManipulatorApp.modules import FK
from ManipulatorApp.modules import IK
from ManipulatorApp.modules import trajectory
from ManipulatorApp.modules import mplwidget
from ManipulatorApp.ui.ui_functions import *


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
        UIFunctions.log_list(self, 'Page FK: ' + result[4])

        # Sim
        self.ui.MplWidget_fk.mpl_draw(result[3], result[2], result[1])
        self.ui.MplWidget_fk.canvas.flush_events()

    def page_ik(self):
        eff = [54, 0]
        value_x = self.ui.horizontalSlider_ik_x.value()
        value_y = self.ui.horizontalSlider_ik_y.value()
        value_z = self.ui.horizontalSlider_ik_z.value()
        value_alpha = self.ui.verticalSlider.value()

        result = IK.ik_geo(value_x, value_y, value_z, value_alpha, eff)
        result_config1 = result[0]
        result_config2 = result[1]
        UIFunctions.log_list(self, 'Page IK: ' + result[2][0] + " " + result[2][1] + " " + result[2][2])

        self.ui.lcdNumber_ik_s1.display((result_config1[0]))
        self.ui.lcdNumber_ik_s2.display((result_config1[1]))
        self.ui.lcdNumber_ik_s3.display((result_config1[2]))
        self.ui.lcdNumber_ik_s4.display((result_config1[3]))

        self.ui.lcdNumber_ik_s1_2.display((result_config2[0]))
        self.ui.lcdNumber_ik_s2_2.display((result_config2[1]))
        self.ui.lcdNumber_ik_s3_2.display((result_config2[2]))
        self.ui.lcdNumber_ik_s4_2.display((result_config2[3]))

        # Sim
        if self.ui.tabWidget_4.currentIndex() == 0:
            calculated = FK.fk_dh(result_config1[0], result_config1[1], result_config1[2], result_config1[3], eff)
            self.ui.MplWidget_ik.mpl_draw(calculated[3], calculated[2], calculated[1])
        elif self.ui.tabWidget_4.currentIndex() == 1:
            calculated = FK.fk_dh(result_config2[0], result_config2[1], result_config2[2], result_config2[3], eff)
            self.ui.MplWidget_ik.mpl_draw(calculated[3], calculated[2], calculated[1])

    def page_manual(self):
        eff = [54, 0]
        if self.ui.tab_manual_joints.isVisible():
            value_j1 = self.ui.horizontalSlider_j_s1.value()
            value_j2 = self.ui.horizontalSlider_j_s2.value()
            value_j3 = self.ui.horizontalSlider_j_s3.value()
            value_j4 = self.ui.horizontalSlider_j_s4.value()

            value_manual_joints = FK.fk_dh(int(value_j1), int(value_j2), int(value_j3), int(value_j4), eff)
            UIFunctions.log_list(self, 'Manual mode: ' + value_manual_joints[4])
            self.ui.horizontalSlider_manual_x.setValue(value_manual_joints[1][0])
            self.ui.horizontalSlider_manual_y.setValue(value_manual_joints[1][1])
            self.ui.horizontalSlider_manual_z.setValue(value_manual_joints[1][2])
            self.ui.verticalSlider_manual_orient.setValue(value_manual_joints[0])

        elif self.ui.tab_manual_xyz.isVisible():
            value_x = self.ui.horizontalSlider_manual_x.value()
            value_y = self.ui.horizontalSlider_manual_y.value()
            value_z = self.ui.horizontalSlider_manual_z.value()
            value_alpha = self.ui.verticalSlider_manual_orient.value()

            value_manual_xyz = IK.ik_geo(value_x, value_y, value_z, value_alpha, eff)
            UIFunctions.log_list(self, 'Manual mode: ' + value_manual_xyz[2][0] + " " + value_manual_xyz[2][1] + " " +
                                 value_manual_xyz[2][2])

            if self.ui.comboBox_auto_config_2.currentIndex() == 0:
                index = 0
            elif self.ui.comboBox_auto_config_2.currentIndex() == 1:
                index = 1
            else:
                raise ValueError

            self.ui.horizontalSlider_j_s1.setValue(value_manual_xyz[index][0])
            self.ui.horizontalSlider_j_s2.setValue(value_manual_xyz[index][1])
            self.ui.horizontalSlider_j_s3.setValue(value_manual_xyz[index][2])
            self.ui.horizontalSlider_j_s4.setValue(value_manual_xyz[index][3])

        servo_1 = self.ui.horizontalSlider_j_s1.value()
        servo_2 = self.ui.horizontalSlider_j_s2.value()
        servo_3 = self.ui.horizontalSlider_j_s3.value()
        servo_4 = self.ui.horizontalSlider_j_s4.value()
        servo_5 = self.ui.horizontalSlider_j_s5.value()
        servo_6 = self.ui.horizontalSlider_j_s6.value()
        # send values to servos

        # Sim
        calculated = FK.fk_dh(servo_1, servo_2, servo_3, servo_4, eff)
        self.ui.MplWidget_ik_2.mpl_draw(calculated[3], calculated[2], calculated[1])

    def page_automatic(self):
        pass

    def page_settings(self):
        self.ui.btn_kal2_set_1.clicked.connect(lambda: UIFunctions.effector_calibration(self, 103, 0))
        self.ui.btn_kal2_set_1.clicked.connect(lambda: UIFunctions.log_list(self, 'Effector dim. changed to grippers'))
        self.ui.btn_kal2_set_2.clicked.connect(lambda: UIFunctions.effector_calibration(self, 22, 50))
        self.ui.btn_kal2_set_2.clicked.connect(
            lambda: UIFunctions.log_list(self, 'Effector dim. changed to pen holder'))
        self.ui.checkBox_kal2_ef.clicked.connect(lambda: UIFunctions.effector_check(self))
        self.ui.checkBox_kal2_ef.clicked.connect(lambda: UIFunctions.log_list(self,
                                                                              'Effector assembled' if self.ui.checkBox_kal2_ef.checkState() else 'Effector disassembled'))
        self.ui.checkBox_kal2_ef.clicked.connect(lambda: self.ui.radioButton_home_effector.setChecked(True) if self.ui.checkBox_kal2_ef.checkState() else self.ui.radioButton_home_effector.setChecked(False))
