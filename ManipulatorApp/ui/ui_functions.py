from ManipulatorApp.main import MainWindow
from ManipulatorApp.main import *
import datetime as dt
from ManipulatorApp.modules import communication as comm
from ManipulatorApp.modules import FK
from ManipulatorApp.modules import trajectory

GLOBAL_STATE = 0


class UIFunctions(MainWindow):
    # ==> TOGGLE MENU
    def __init__(self):
        super().__init__()
        self.sizegrip = None
        self.shadow = None
        self.animation = None

    def toggleMenu(self, max_width, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_menu.width()
            max_extend = max_width
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                width_extended = max_extend
            else:
                width_extended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    # ==> SELECT
    def select_menu(getStyle):
        menu_select = getStyle + "QPushButton { border-right: 5px solid rgb(71, 71, 71); }"
        return menu_select

    # ==> DESELECT
    def deselect_menu(getStyle):
        menu_deselect = getStyle.replace("QPushButton { border-right: 5px solid rgb(71, 71, 71); }", "")
        return menu_deselect

    # ==> START/RESET SELECTION
    def select_standard_menu(self, widget):
        for menu in self.ui.frame_menu.findChildren(QPushButton):
            if menu.objectName() != widget:
                menu.setStyleSheet(UIFunctions.deselect_menu(menu.styleSheet()))
            if menu.objectName() == widget:
                menu.setStyleSheet(UIFunctions.select_menu(menu.styleSheet()))

    # ==> CHANGE PAGE LABEL TEXT
    def label_page(self, text):
        new_text = '| ' + text.upper()
        self.ui.label_top_info_2.setText(new_text)

    # ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.frame_top.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_max.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.frame_top.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_max.setToolTip("Maximize")

    # ==> CLOSE APP AND END COMMUNICATION
    @staticmethod
    def close_app():
        sys.exit()

    # ==> UI DEFINITIONS
    def uiDefinitions(self):
        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROP SHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROP SHADOW TO FRAME
        self.ui.frame_top.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.btn_max.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.btn_min.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.btn_close.clicked.connect(lambda: UIFunctions.close_app())

        # ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("background: transparent;")

    # RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTORED
    @staticmethod
    def returnStatus():
        return GLOBAL_STATE

    def page_fk_reset(self):
        UIFunctions.log_list(self, 'Page FK: Slider values has been reset')
        self.ui.horizontalSlider_fk_s1.setValue(0)
        self.ui.horizontalSlider_fk_s1_2.setValue(90)
        self.ui.horizontalSlider_fk_s1_3.setValue(0)
        self.ui.horizontalSlider_fk_s1_4.setValue(0)
        self.ui.horizontalSlider_fk_s1_5.setValue(0)
        self.ui.horizontalSlider_fk_s1_6.setValue(0)

    def page_ik_reset(self):
        UIFunctions.log_list(self, 'Page IK: Slider values has been reset')
        self.ui.horizontalSlider_ik_x.setValue(0)
        self.ui.horizontalSlider_ik_y.setValue(0)
        self.ui.horizontalSlider_ik_z.setValue(472)
        self.ui.verticalSlider.setValue(90)

    def page_manual_reset(self):
        UIFunctions.log_list(self, 'Page Manual mode: Slider values has been reset')
        if self.ui.tab_manual_joints.isVisible():
            self.ui.horizontalSlider_j_s1.setValue(0)
            self.ui.horizontalSlider_j_s2.setValue(90)
            self.ui.horizontalSlider_j_s3.setValue(0)
            self.ui.horizontalSlider_j_s4.setValue(0)
            self.ui.horizontalSlider_j_s5.setValue(0)
            self.ui.horizontalSlider_j_s6.setValue(0)
        elif self.ui.tab_manual_xyz.isVisible():
            self.ui.horizontalSlider_manual_x.setValue(0)
            self.ui.horizontalSlider_manual_y.setValue(0)
            self.ui.horizontalSlider_manual_z.setValue(472)
            self.ui.verticalSlider_manual_orient.setValue(90)

    def log_list(self, log):
        log_time = dt.datetime.now().strftime("%H:%M:%S")
        new_text = log_time + " | " + log.upper()
        self.ui.Log.append(new_text)

    def calibration(self):
        servo1 = self.ui.spinBox_kal_s1.value()
        servo2 = self.ui.spinBox_kal_s2.value()
        servo3 = self.ui.spinBox_kal_s3.value()
        servo4 = self.ui.spinBox_kal_s4.value()
        servo5 = self.ui.spinBox_kal_s5.value()
        servo6 = self.ui.spinBox_kal_s6.value()

        servo_cal = [servo1, servo2, servo3, servo4, servo5, servo6]

        return servo_cal

    # == > EFFECTOR
    def effector_calibration(self, L, H):
        self.ui.spinBox_kal2_ef.setValue(L)
        self.ui.spinBox_kal2_ef_2.setValue(H)
        if self.ui.checkBox_kal2_ef.checkState():
            self.ui.checkBox_kal2_ef.click()

    # CHECK IF EFFECTOR IS ASSEMBLED OR DISASSEMBLED
    def effector_check(self):
        if self.ui.checkBox_kal2_ef.checkState():
            a = int(self.ui.spinBox_kal2_ef.value()) + 54
            b = int(self.ui.spinBox_kal2_ef_2.value())
            eff = [a, b]
        else:
            eff = [54, 0]
        print(eff)
        return eff

    # SETTINGS IF EFFECTOR IS ASSEMBLED OR DISASSEMBLED
    def effector_settings(self):
        eff = UIFunctions.effector_check(self)
        # FK
        fk_eff = FK.fk_dh(self.ui.horizontalSlider_fk_s1.value(), self.ui.horizontalSlider_fk_s1_2.value(),
                          self.ui.horizontalSlider_fk_s1_3.value(), self.ui.horizontalSlider_fk_s1_4.value(),
                          eff)
        self.ui.lcdNumber_dh_X_2.display(round(fk_eff[1][0]))
        self.ui.lcdnumber_dh_Y_2.display(round(fk_eff[1][1]))
        self.ui.lcdnumber_dh_Z_2.display(round(fk_eff[1][2]))

        # IK
        self.ui.horizontalSlider_ik_z.setMaximum(418 + eff[0])
        self.ui.horizontalSlider_ik_x.setMaximum(300 + eff[0])
        self.ui.horizontalSlider_ik_y.setMaximum(300 + eff[0])
        self.ui.horizontalSlider_ik_y.setMinimum(-1 * (300 + eff[0]))

        # Manual XYZ
        self.ui.horizontalSlider_manual_z.setMaximum(418 + eff[0])
        self.ui.horizontalSlider_manual_x.setMaximum(300 + eff[0])
        self.ui.horizontalSlider_manual_y.setMaximum(300 + eff[0])
        self.ui.horizontalSlider_manual_y.setMinimum(-1 * (300 + eff[0]))

        # AUTO
        self.ui.horizontalSlider_auto_z.setMaximum(418 + eff[0])
        self.ui.horizontalSlider_auto_x.setMaximum(300 + eff[0])
        self.ui.horizontalSlider_auto_y.setMaximum(300 + eff[0])
        self.ui.horizontalSlider_auto_y.setMinimum(-1 * (300 + eff[0]))

    # == > QTABLEWIDGET AUTO MODE
    # ADD / DELETE ROW
    def AddRow(self):
        self.ui.tableWidget.insertRow(self.ui.tableWidget.currentRow()+1)

    def RemoveRow(self):
        if self.ui.tableWidget.rowCount() > 0:
            self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())

    def add_pos(self):
        try:
            position_values = [self.ui.comboBox_auto_command.currentText(),
                               self.ui.comboBox_auto_traj.currentText(),
                               self.ui.comboBox_auto_config.currentText(),
                               self.ui.horizontalSlider_auto_x.value(),
                               self.ui.horizontalSlider_auto_y.value(),
                               self.ui.horizontalSlider_auto_z.value(),
                               self.ui.horizontalSlider_auto_orient.value(),
                               self.ui.horizontalSlider_auto_time_2.value()]

            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            for i in range(0, self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, i,
                                            QTableWidgetItem(str(position_values[i])))
        except:
            status = 'Error: Position can not be added'

        else:
            status = 'Position added'
        UIFunctions.log_list(self, status)

    def add_safe(self):
        try:
            home = self.home_position
            for i in range(0, self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(self.ui.tableWidget.currentRow(), i,
                                            QTableWidgetItem(str(home[i])))
        except:
            status = 'Error: Home pos can not be added'

        else:
            status = 'Home position added'
        UIFunctions.log_list(self, status)

    def add_wait(self):
        try:
            position_values = ['wait',
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow()-1, 1).text(),
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow()-1, 2).text(),
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow()-1, 3).text(),
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow()-1, 4).text(),
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow()-1, 5).text(),
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow()-1, 6).text(),
                               self.ui.horizontalSlider_auto_time_2.value()]
            for i in range(0, self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(self.ui.tableWidget.currentRow(), i,
                                            QTableWidgetItem(str(position_values[i])))
        except:
            status = 'Error: Wait pos can not be added'

        else:
            status = 'Wait position added'
        UIFunctions.log_list(self, status)

    def set_home(self):
        try:
            self.home_position = ['home',
                                  self.ui.comboBox_auto_traj.currentText(),
                                  self.ui.comboBox_auto_config.currentText(),
                                  self.ui.horizontalSlider_auto_x.value(),
                                  self.ui.horizontalSlider_auto_y.value(),
                                  self.ui.horizontalSlider_auto_z.value(),
                                  self.ui.horizontalSlider_auto_orient.value(),
                                  5.0]
        except:
            status = 'Error: Home can not be set'
            UIFunctions.log_list(self, status)
        else:
            status = 'Home position created'
            UIFunctions.log_list(self, status)
            return self.home_position

    def generate_path(self):
        eff = UIFunctions.effector_check(self)
        table = []
        for i in range(0, self.ui.tableWidget.rowCount()):
            table_row = [self.ui.tableWidget.item(i, 0).text(),
                         self.ui.tableWidget.item(i, 1).text(),
                         self.ui.tableWidget.item(i, 2).text(),
                         self.ui.tableWidget.item(i, 3).text(),
                         self.ui.tableWidget.item(i, 4).text(),
                         self.ui.tableWidget.item(i, 5).text(),
                         self.ui.tableWidget.item(i, 6).text(),
                         self.ui.tableWidget.item(i, 7).text(),
                         eff]
            table.append(table_row)
        file_path_write = 'r' + "'" + self.ui.lineEdit.text() + "'"
        # file_path_write = r'C:\Users\SZILING\Desktop\ManipulatorApp\data'
        file_name_write = 'generated_path_'
        file_format_write = '.txt'
        trajectory.write_generated_path_to_file(table, file_path_write, file_name_write, file_format_write)

    def read_path(self):
        print(self.ui.lineEdit.text())
        file_path_read = self.ui.lineEdit.text()
        # file_path_read = r'C:\Users\SZILING\Desktop\ManipulatorApp\data\test_path.txt'
        self.read_robotic_path = trajectory.read_generated_path_from_file(file_path_read)
        print(self.read_robotic_path)


