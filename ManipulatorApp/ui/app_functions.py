""" Module contains class AppFunctions that contains created functions to control application"""

# ==> GUI FILE
import time
from importlib import reload

from ManipulatorApp.main import *
from ManipulatorApp.main import MainWindow
from ManipulatorApp.modules import IK
from ManipulatorApp.modules import communication as comm
from ManipulatorApp.ui.ui_functions import *


class AppFunctions(MainWindow):
    """ Class contains functions to control application depending on users actions """

    def __init__(self):
        super().__init__()
        self.stop = None

    def page_fk(self):
        """
        Page - Forward kinematics calculations of robotic arm.\n
        Function checks effector dimensions,takes values from sliders and calculate forward kinematics.\n
        Calculation results are displayed, simulated and status is printed in log file and bar.\n

        :return: Forward kinematics
        """

        # Check the effector dimensions
        eff = UIFunctions.effector_check(self)

        # Take values from sliders and calculate forward kinematics
        theta1 = self.ui.horizontalSlider_fk_s1.value()
        theta2 = self.ui.horizontalSlider_fk_s1_2.value()
        theta3 = self.ui.horizontalSlider_fk_s1_3.value()
        theta4 = self.ui.horizontalSlider_fk_s1_4.value()

        result = FK.fk_dh(theta1, theta2, theta3, theta4, eff)

        # Display the result of calculation
        self.ui.lcdNumber_dh_X_2.display(result[1][0])
        self.ui.lcdnumber_dh_Y_2.display(result[1][1])
        self.ui.lcdnumber_dh_Z_2.display(result[1][2])

        # Print the result
        UIFunctions.log_list(self, 'Page FK: ' + result[5])

        # Simulate the robotic arm with given parameters
        self.ui.MplWidget_fk.mpl_draw(result[4], result[3], result[2], result[1])
        self.ui.MplWidget_fk.canvas.flush_events()

    def page_ik(self):
        """
        Page - Inverse kinematics calculations of robotic arm\n
        Function checks effector dimensions,takes values from sliders and calculate forward kinematics.\n
        Calculation results are displayed, simulated and status is printed in log file and bar.\n

        :return: Inverse kinematics
        """

        # Check the effector dimensions
        eff = UIFunctions.effector_check(self)

        # Take values from sliders and calculate inverse kinematics
        value_x = self.ui.horizontalSlider_ik_x.value()
        value_y = self.ui.horizontalSlider_ik_y.value()
        value_z = self.ui.horizontalSlider_ik_z.value()
        value_alpha = self.ui.verticalSlider.value()

        result = IK.ik_geo(value_x, value_y, value_z, value_alpha, eff)
        result_config1 = result[0]
        result_config2 = result[1]

        # Print the result
        UIFunctions.log_list(self, 'Page IK: ' + result[2][0] + " " + result[2][1] + " " + result[2][2])

        # Display the result of calculation
        self.ui.lcdNumber_ik_s1.display((result_config1[0]))
        self.ui.lcdNumber_ik_s2.display((result_config1[1]))
        self.ui.lcdNumber_ik_s3.display((result_config1[2]))
        self.ui.lcdNumber_ik_s4.display((result_config1[3]))

        self.ui.lcdNumber_ik_s1_2.display((result_config2[0]))
        self.ui.lcdNumber_ik_s2_2.display((result_config2[1]))
        self.ui.lcdNumber_ik_s3_2.display((result_config2[2]))
        self.ui.lcdNumber_ik_s4_2.display((result_config2[3]))

        # Simulate the robotic arm with given parameters
        if self.ui.tabWidget_4.currentIndex() == 0:
            calculated = FK.fk_dh(result_config1[0], result_config1[1], result_config1[2], result_config1[3], eff)
            self.ui.MplWidget_ik.mpl_draw(calculated[4], calculated[3], calculated[2], calculated[1])
        elif self.ui.tabWidget_4.currentIndex() == 1:
            calculated = FK.fk_dh(result_config2[0], result_config2[1], result_config2[2], result_config2[3], eff)
            self.ui.MplWidget_ik.mpl_draw(calculated[4], calculated[3], calculated[2], calculated[1])

    def page_manual(self):
        """
        Page - Manual mode of controlling robotic arm.\n
        Function checks effector dimensions and robotic arm calibration.\n
        Function calculates servo values from sliders values in servo/xyz mode.\n
        Calculation results are displayed, simulated, send to Arduino and status is printed in log file and bar.\n
        """

        # Check the effector dimensions
        eff = UIFunctions.effector_check(self)

        # Check calibration
        servo_cal = UIFunctions.calibration(self)

        # Set values of sliders in different control modes
        if self.ui.tab_manual_joints.isVisible():
            value_j1 = self.ui.horizontalSlider_j_s1.value() / 100
            value_j2 = self.ui.horizontalSlider_j_s2.value() / 100
            value_j3 = self.ui.horizontalSlider_j_s3.value() / 100
            value_j4 = self.ui.horizontalSlider_j_s4.value() / 100

            value_manual_joints = FK.fk_dh(value_j1, value_j2, value_j3, value_j4, eff)

            # Set values of sliders
            self.ui.horizontalSlider_manual_x.setValue(value_manual_joints[1][0])
            self.ui.horizontalSlider_manual_y.setValue(value_manual_joints[1][1])
            self.ui.horizontalSlider_manual_z.setValue(value_manual_joints[1][2])
            self.ui.verticalSlider_manual_orient.setValue(value_manual_joints[0])

            # Set values of sliders in automatic mode
            value_j5 = self.ui.horizontalSlider_j_s5.value()
            value_j6 = self.ui.horizontalSlider_j_s6.value()
            self.ui.horizontalSlider_auto_s1.setValue(value_j1 * 100)
            self.ui.horizontalSlider_auto_s2.setValue(value_j2 * 100)
            self.ui.horizontalSlider_auto_s3.setValue(value_j3 * 100)
            self.ui.horizontalSlider_auto_s4.setValue(value_j4 * 100)
            self.ui.horizontalSlider_auto_s5.setValue(value_j5)
            self.ui.horizontalSlider_auto_s6.setValue(value_j6)

            # Set the status with parameters sending to robotic arm
            status = value_manual_joints[5]

        elif self.ui.tab_manual_xyz.isVisible():
            value_x = self.ui.horizontalSlider_manual_x.value()
            value_y = self.ui.horizontalSlider_manual_y.value()
            value_z = self.ui.horizontalSlider_manual_z.value()
            value_alpha = self.ui.verticalSlider_manual_orient.value()

            value_manual_xyz = IK.ik_geo(value_x, value_y, value_z, value_alpha, eff)

            # Set the status with parameters sending to robotic arm
            status = value_manual_xyz[2][0] + " " + value_manual_xyz[2][1] + " " + value_manual_xyz[2][2]

            # Set values of sliders
            if self.ui.comboBox_auto_config_2.currentIndex() == 0:
                index = 0
            elif self.ui.comboBox_auto_config_2.currentIndex() == 1:
                index = 1
            else:
                raise ValueError

            self.ui.horizontalSlider_j_s1.setValue(value_manual_xyz[index][0] * 100)
            self.ui.horizontalSlider_j_s2.setValue(value_manual_xyz[index][1] * 100)
            self.ui.horizontalSlider_j_s3.setValue(value_manual_xyz[index][2] * 100)
            self.ui.horizontalSlider_j_s4.setValue(value_manual_xyz[index][3] * 100)

        else:
            status = 'Error: Something went wrong'

        # Control robotic arm with given parameters
        servo_1 = self.ui.horizontalSlider_j_s1.value() / 100
        servo_2 = self.ui.horizontalSlider_j_s2.value() / 100
        servo_3 = self.ui.horizontalSlider_j_s3.value() / 100
        servo_4 = self.ui.horizontalSlider_j_s4.value() / 100
        servo_5 = self.ui.horizontalSlider_j_s5.value() / 100
        servo_6 = self.ui.horizontalSlider_j_s6.value() / 100

        try:
            comm.servos_write(servo_1, servo_2, servo_3, servo_4, servo_5, servo_6, servo_cal)
        except:
            status = 'Error: Robotic Arm not connected'

        # Print the status
        UIFunctions.log_list(self, 'Manual mode: ' + status)

        # Simulate the robotic arm with given parameters
        calculated = FK.fk_dh(servo_1, servo_2, servo_3, servo_4, eff)
        self.ui.MplWidget_ik_2.mpl_draw(calculated[4], calculated[3], calculated[2], calculated[1])

    def page_automatic(self):
        """
        Page - Auto mode of controlling robotic arm \n
        Function handles users actions in automatic mode page\n
        """

        self.ui.btn_auto_Add_path_gen.clicked.connect(lambda: UIFunctions.generate_path(self))
        self.ui.btn_auto_Add_path_read.clicked.connect(lambda: UIFunctions.read_path(self))
        self.ui.btn_auto_init.clicked.connect(lambda: AppFunctions.automatic_mode_init(self))
        self.ui.btn_auto_break.clicked.connect(lambda: AppFunctions.automatic_mode_break(self))
        self.ui.btn_auto_stop.clicked.connect(lambda: AppFunctions.automatic_stop(self))
        self.ui.btn_auto_start.clicked.connect(lambda: AppFunctions.automatic_start(self))
        self.ui.btn_auto_prev.clicked.connect(lambda: AppFunctions.automatic_step_prev(self))
        self.ui.btn_auto_next.clicked.connect(lambda: AppFunctions.automatic_step_next(self))

    def automatic_stop(self):
        """
        Stop executing robotic program and print status in log file/bar.\n

        :return: self.stop = True
        """

        self.stop = True
        status = 'Stop robotic program'
        UIFunctions.log_list(self, status)

    def automatic_start(self):
        """
        Start executing robotic program till end of program or stop flag. \n
        Function checks robotic arms calibration and execute program depends on set mode- servo/sim.\n
        Status is printed in log file/bar.\n
        """

        self.stop = False

        # Check calibration
        servo_cal = UIFunctions.calibration(self)

        # Check the selected mode
        if self.ui.comboBox_auto_sim_servo.currentText() == 'SIM':
            # Execute program in simulation
            status = 'Executing robotic program - SIM'
            while not self.stop:
                # Take next line of robotic program
                step_values_next = self.robotic_arm.next()

                # Take effector dimensions
                eff1 = step_values_next[15][1:]
                eff2 = step_values_next[16][:1]
                eff = [int(eff1), int(eff2)]
                print(step_values_next)

                # Calculate forward kinematics
                calculated = FK.fk_dh(float(step_values_next[8]),
                                      float(step_values_next[9]),
                                      float(step_values_next[10]),
                                      float(step_values_next[11]), eff)

                # Simulate the robotic arm with given parameters
                self.ui.MplWidget_auto.mpl_draw(calculated[4], calculated[3], calculated[2], calculated[1])
                QApplication.processEvents()
                time.sleep(float(step_values_next[14]))
        else:
            # Execute program with robotic arm
            status = 'Executing robotic program - SERVO'
            # Control robotic arm with given parameters
            while not self.stop:
                # Take next line of robotic program
                step_values_next = self.robotic_arm.next()

                # Take effector dimensions
                eff1 = step_values_next[15][1:]
                eff2 = step_values_next[16][:1]
                eff = [int(eff1), int(eff2)]
                print(step_values_next)

                # Control robotic arm with given parameters
                comm.servos_write(float(step_values_next[8]),
                                  float(step_values_next[9]),
                                  float(step_values_next[10]),
                                  float(step_values_next[11]),
                                  float(step_values_next[12]),
                                  float(step_values_next[13]),
                                  servo_cal)
                QApplication.processEvents()
                time.sleep(float(step_values_next[14]))

        # Print the status
        UIFunctions.log_list(self, status)

    def automatic_step_next(self):
        """
        Execute one next line of robotic program\n
        Function checks robotic arms calibration and execute one line of program.\n
        Status is printed in log file/bar.\n
        """

        # Check calibration
        servo_cal = UIFunctions.calibration(self)

        try:
            # Take next line of robotic program
            step_values_next = self.robotic_arm.next()

            # Take effector dimensions
            eff1 = step_values_next[15][1:]
            eff2 = step_values_next[16][:1]
            eff = [int(eff1), int(eff2)]
            print(step_values_next)

            # Check the selected mode
            if self.ui.comboBox_auto_sim_servo.currentText() == 'SIM':
                # Execute program in simulation
                status = 'Step forward SIM'

                # Calculate forward kinematics
                calculated = FK.fk_dh(float(step_values_next[8]),
                                      float(step_values_next[9]),
                                      float(step_values_next[10]),
                                      float(step_values_next[11]), eff)

                # Simulate the robotic arm with given parameters
                self.ui.MplWidget_auto.mpl_draw(calculated[4], calculated[3], calculated[2], calculated[1])
            else:
                # Execute program with robotic arm
                status = 'Step forward SERVO'

                # Send to servos
                step_values_next = self.robotic_arm.next()
                print(step_values_next)

                #     Control robotic arm with given parameters
                comm.servos_write(float(step_values_next[8]),
                                  float(step_values_next[9]),
                                  float(step_values_next[10]),
                                  float(step_values_next[11]),
                                  float(step_values_next[12]),
                                  float(step_values_next[13]),
                                  servo_cal)
                QApplication.processEvents()
        except AttributeError:
            status = 'Error: Automatic mode not initialized'

        # Print the status
        UIFunctions.log_list(self, status)

    def automatic_step_prev(self):
        """
        Execute one previous line of robotic program\n
        Function checks robotic arms calibration and execute one line of program.\n
        Status is printed in log file/bar.\n
        """

        # Check calibration
        servo_cal = UIFunctions.calibration(self)

        try:
            # Take previous line of robotic program
            step_values_prev = self.robotic_arm.prev()

            # Take effector dimensions
            eff1 = step_values_prev[15][1:]
            eff2 = step_values_prev[16][:1]
            eff = [int(eff1), int(eff2)]
            print(step_values_prev)

            if self.ui.comboBox_auto_sim_servo.currentText() == 'SIM':
                # Execute program in simulation
                status = 'Step backward SIM'

                # Calculate forward kinematics
                calculated = FK.fk_dh(float(step_values_prev[8]),
                                      float(step_values_prev[9]),
                                      float(step_values_prev[10]),
                                      float(step_values_prev[11]), eff)

                # Simulate the robotic arm with given parameters
                self.ui.MplWidget_auto.mpl_draw(calculated[4], calculated[3], calculated[2], calculated[1])
            else:
                # Execute program with robotic arm
                status = 'Step backward SERVO'
                # Send to servos
                step_values_next = self.robotic_arm.next()
                print(step_values_next)

                # Control robotic arm with given parameters
                comm.servos_write(float(step_values_next[8]),
                                  float(step_values_next[9]),
                                  float(step_values_next[10]),
                                  float(step_values_next[11]),
                                  float(step_values_next[12]),
                                  float(step_values_next[13]),
                                  servo_cal)
                QApplication.processEvents()
        except AttributeError:
            status = 'Error: Automatic mode not initialized'

        # Print the status
        UIFunctions.log_list(self, status)

    def automatic_mode_init(self):
        """
        Create robotic program from read file.\n
        Function checks if installed effector is the same as in read robotic path.\n
        Status is printed in log file/bar.\n

        :return: self.robotic_arm
        """

        try:
            # Checking if installed effector is the same as in read robotic path
            effector_installed = UIFunctions.effector_check(self)
            eff1 = self.read_robotic_path[0][15][1:]
            eff2 = self.read_robotic_path[0][16][:-1]
            effector_path = [int(eff1), int(eff2)]

            if effector_installed == effector_path:
                self.robotic_path = self.read_robotic_path
                robotic_path_copy = self.robotic_path.copy()

                # Executing robotic arm in loop
                repeat = self.ui.spinBox.value()
                for _ in range(1, repeat):
                    self.robotic_path.extend(robotic_path_copy)

                # Create robotic arm program
                self.robotic_arm = trajectory.RoboticMove(self.robotic_path)

                status = 'Automatic mode initialized'
            else:
                raise NameError('Warning: Installed effector is different as in robotic path')

        except IndexError:
            status = 'Error: Wrong path - read file path'
        except NameError as effector_error:
            status = effector_error
        except AttributeError:
            status = 'Error: No file path - read file path'

        # Print the status
        UIFunctions.log_list(self, status)

    def automatic_mode_break(self):
        """ Delete initialized robotic_arm object """

        try:
            if self.robotic_arm is None:
                pass
            else:
                del self.robotic_path
                del self.robotic_arm
        except AttributeError:
            status = 'Error: Automatic mode not initialized'

            # Print the status
            UIFunctions.log_list(self, status)

    def page_settings(self):
        """ Page - Settings (checks effector and communication) """

        AppFunctions.effector_tab(self)
        AppFunctions.communication_tab(self)

    def effector_tab(self):
        """ Button functions in effector tab in settings page """

        self.ui.btn_kal2_set_1.clicked.connect(lambda: UIFunctions.effector_calibration(self, 103, 0))
        self.ui.btn_kal2_set_1.clicked.connect(
            lambda: UIFunctions.log_list(self, 'Effector dim. changed to grippers'))
        self.ui.btn_kal2_set_2.clicked.connect(lambda: UIFunctions.effector_calibration(self, 22, 50))
        self.ui.btn_kal2_set_2.clicked.connect(
            lambda: UIFunctions.log_list(self, 'Effector dim. changed to pen holder'))
        self.ui.checkBox_kal2_ef.clicked.connect(lambda: UIFunctions.effector_check(self))
        self.ui.checkBox_kal2_ef.clicked.connect(lambda: UIFunctions.effector_settings(self))
        self.ui.checkBox_kal2_ef.clicked.connect(lambda: UIFunctions.log_list(self,
                                                                              'Effector assembled' if self.ui.checkBox_kal2_ef.checkState() else 'Effector disassembled'))
        self.ui.checkBox_kal2_ef.clicked.connect(lambda: self.ui.radioButton_home_effector.setChecked(
            True) if self.ui.checkBox_kal2_ef.checkState() else self.ui.radioButton_home_effector.setChecked(False))

    def communication_tab(self):
        """ Set status of communication green/red """

        if comm.status:
            self.ui.radioButton_home_comm.setChecked(True)
            self.ui.radioButton_home_comm_2.setChecked(True)
        else:
            self.ui.radioButton_home_comm.setChecked(False)
            self.ui.radioButton_home_comm_2.setChecked(False)

    def communication_radiobutton(self):
        """ Set/check the communication with robotic arm (Arduino) """

        try:
            if not self.ui.radioButton_home_comm_2.isChecked():
                comm.board.exit()
                self.ui.label_home_port_2.setText('Communication on port: Disconnected')

            if self.ui.radioButton_home_comm_2.isChecked():
                reload(comm)
                if comm.status:
                    port = str(comm.board)
                else:
                    port = 'No connection'

                self.ui.label_home_port_2.setText('Communication on port:' + port)

                # Print the status
                UIFunctions.log_list(self, comm.status_log)
        except:
            self.ui.label_home_port_2.setText('Communication on port: No connection/Disconnected')
