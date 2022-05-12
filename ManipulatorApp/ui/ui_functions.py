import os

from PySide2.QtWidgets import QSlider

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
        """Left toggle menu properties"""

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
        """Select menu page"""

        menu_select = getStyle + "QPushButton { border-right: 5px solid rgb(71, 71, 71); }"
        return menu_select

    # ==> DESELECT
    def deselect_menu(getStyle):
        """Deselect menu page"""

        menu_deselect = getStyle.replace("QPushButton { border-right: 5px solid rgb(71, 71, 71); }", "")
        return menu_deselect

    # ==> START/RESET SELECTION
    def select_standard_menu(self, widget):
        """Start/reset menu page selection"""

        for menu in self.ui.frame_menu.findChildren(QPushButton):
            if menu.objectName() != widget:
                menu.setStyleSheet(UIFunctions.deselect_menu(menu.styleSheet()))
            if menu.objectName() == widget:
                menu.setStyleSheet(UIFunctions.select_menu(menu.styleSheet()))

    # ==> CHANGE PAGE LABEL TEXT
    def label_page(self, text):
        """ Change page label text"""

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
        """Close app"""
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

    # RESET SLIDER VALUES - PAGE FK
    def page_fk_reset(self):
        """ Page Forward Kinematics - reset sliders values"""

        UIFunctions.log_list(self, 'Page FK: Slider values has been reset')
        self.ui.horizontalSlider_fk_s1.setValue(0)
        self.ui.horizontalSlider_fk_s1_2.setValue(90)
        self.ui.horizontalSlider_fk_s1_3.setValue(0)
        self.ui.horizontalSlider_fk_s1_4.setValue(0)
        self.ui.horizontalSlider_fk_s1_5.setValue(0)
        self.ui.horizontalSlider_fk_s1_6.setValue(0)

    # RESET SLIDER VALUES - PAGE IK
    def page_ik_reset(self):
        """ Page Inverse Kinematics - reset sliders values"""

        UIFunctions.log_list(self, 'Page IK: Slider values has been reset')
        self.ui.horizontalSlider_ik_x.setValue(0)
        self.ui.horizontalSlider_ik_y.setValue(0)
        self.ui.horizontalSlider_ik_z.setValue(472)
        self.ui.verticalSlider.setValue(90)

    # RESET SLIDER VALUES - PAGE MANUAL
    def page_manual_reset(self):
        """ Page Manual - reset sliders values"""

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

    # STATUS DISPLAY
    def log_list(self, log):
        """ Print given string in log"""

        log_time = dt.datetime.now().strftime("%H:%M:%S")
        new_text = log_time + " | " + log.upper()
        self.ui.Log.append(new_text)

    # CALIBRATION OF ROBOTIC ARM
    def calibration(self):
        """
        Calibrate robotic arms servos.
        :return: servo_cal
        """

        servo1 = self.ui.spinBox_kal_s1.value()
        servo2 = self.ui.spinBox_kal_s2.value()
        servo3 = self.ui.spinBox_kal_s3.value()
        servo4 = self.ui.spinBox_kal_s4.value()
        servo5 = self.ui.spinBox_kal_s5.value()
        servo6 = self.ui.spinBox_kal_s6.value()

        servo_cal = [servo1, servo2, servo3, servo4, servo5, servo6]

        return servo_cal

    # EFFECTOR CALIBRATION
    def effector_calibration(self, L, H):
        """ Set values of spinbox with given effector dim."""

        self.ui.spinBox_kal2_ef.setValue(L)
        self.ui.spinBox_kal2_ef_2.setValue(H)
        if self.ui.checkBox_kal2_ef.checkState():
            self.ui.checkBox_kal2_ef.click()

    # CHECK IF EFFECTOR IS ASSEMBLED OR DISASSEMBLED
    def effector_check(self):
        """
        Check effector dimensions. Without set effector eff = [54,0]
        :return: eff = [a,b]
        """

        if self.ui.checkBox_kal2_ef.checkState():
            a = int(self.ui.spinBox_kal2_ef.value()) + 54
            b = int(self.ui.spinBox_kal2_ef_2.value())
            eff = [a, b]
        else:
            eff = [54, 0]
        # print(eff)
        return eff

    # SETTINGS IF EFFECTOR IS ASSEMBLED OR DISASSEMBLED
    def effector_settings(self):
        """ Set slides range and lcd display values with set effector dimensions"""

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

    # SETTING COLOR OF SLIDERS
    def slider_color_warning(getStyle, color):
        """ Set sliders warning color rgb(61, 61, 61)"""

        set_color = getStyle.replace("rgb(61, 61, 61);", color)
        return set_color

    def slider_color_standard(getStyle, actual, color):
        """ Set sliders standard color"""
        set_color = getStyle.replace(actual, color)
        return set_color

    def set_slider_color(self, widget, warning_range):
        """
        Set slider color
        :param widget: widget name
        :param warning_range: warning value
        """

        left = "qlineargradient(spread:pad, x1:-2, y1:0.0163043, x2:1, y2:0, stop:0 rgba(54, 0, 70, 255), stop:1 rgba(61, 61, 61, 255));"
        right = "qlineargradient(spread:pad, x1:0, y1:0.0163043, x2:3, y2:0, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(54, 0, 70, 255));"
        for slider in self.ui.frame_stackedWidget.findChildren(QSlider):
            if slider.objectName() == widget:
                if slider.value() <= slider.minimum() + warning_range:
                    slider.setStyleSheet(UIFunctions.slider_color_warning(slider.styleSheet(), left))
                elif slider.value() >= slider.maximum() - warning_range:
                    slider.setStyleSheet(UIFunctions.slider_color_warning(slider.styleSheet(), right))
                else:
                    slider.setStyleSheet(UIFunctions.slider_color_standard(slider.styleSheet(), left, "rgb(61, 61, 61);"))
                    slider.setStyleSheet(UIFunctions.slider_color_standard(slider.styleSheet(), right, "rgb(61, 61, 61);"))

    # == > QTABLEWIDGET AUTO MODE
    # ADD / DELETE ROW
    def AddRow(self):
        """ Create empty row """

        self.ui.tableWidget.insertRow(self.ui.tableWidget.currentRow() + 1)

    def RemoveRow(self):
        """ Remove selected row """

        if self.ui.tableWidget.rowCount() > 0:
            self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())

    # ADD POSITION WITH GIVEN PARAMETERS
    def add_pos(self):
        """ Add position with users input param."""

        try:
            # Get values from user
            position_values = [self.ui.comboBox_auto_command.currentText(),
                               self.ui.comboBox_auto_traj.currentText(),
                               self.ui.comboBox_auto_config.currentText(),
                               self.ui.horizontalSlider_auto_x.value(),
                               self.ui.horizontalSlider_auto_y.value(),
                               self.ui.horizontalSlider_auto_z.value(),
                               self.ui.horizontalSlider_auto_orient.value(),
                               self.ui.horizontalSlider_auto_s5.value(),
                               self.ui.horizontalSlider_auto_s6.value(),
                               self.ui.horizontalSlider_auto_time_2.value()]

            # Insert empty row
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())

            # Add values to last row
            for i in range(0, self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, i,
                                            QTableWidgetItem(str(position_values[i])))
        except:
            status = 'Error: Position can not be added'

        else:
            status = 'Position added'

        # Print the status
        UIFunctions.log_list(self, status)

    # ADD HOME POSITION
    def add_safe(self):
        """ Add home position """

        try:
            # Get values from saved parameter and add to table
            home = self.home_position
            for i in range(0, self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(self.ui.tableWidget.currentRow(), i,
                                            QTableWidgetItem(str(home[i])))
        except:
            status = 'Error: Home pos can not be added'

        else:
            status = 'Home position added'

        # Print the status
        UIFunctions.log_list(self, status)

    # ADD WAIT POSITION
    def add_wait(self):
        """ Add wait position """

        try:
            # Get values from previous row in table
            position_values = ['wait',
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow() - 1, 1).text(),
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow() - 1, 2).text(),
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow() - 1, 3).text(),
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow() - 1, 4).text(),
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow() - 1, 5).text(),
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow() - 1, 6).text(),
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow() - 1, 7).text(),
                               self.ui.tableWidget.item(self.ui.tableWidget.currentRow() - 1, 8).text(),
                               self.ui.horizontalSlider_auto_time_2.value()]
            for i in range(0, self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(self.ui.tableWidget.currentRow(), i,
                                            QTableWidgetItem(str(position_values[i])))
        except:
            status = 'Error: Wait pos can not be added'

        else:
            status = 'Wait position added'

        # Print the status
        UIFunctions.log_list(self, status)

    # CREATE/SET HOME POSITION
    def set_home(self):
        """
        Create/set home position
        :return: self.home_position
        """

        try:
            # Get values from user
            self.home_position = ['home',
                                  self.ui.comboBox_auto_traj.currentText(),
                                  self.ui.comboBox_auto_config.currentText(),
                                  self.ui.horizontalSlider_auto_x.value(),
                                  self.ui.horizontalSlider_auto_y.value(),
                                  self.ui.horizontalSlider_auto_z.value(),
                                  self.ui.horizontalSlider_auto_orient.value(),
                                  self.ui.horizontalSlider_auto_s5.value(),
                                  self.ui.horizontalSlider_auto_s6.value(),
                                  5.0]
        except:
            status = 'Error: Home can not be set'

            # Print the status
            UIFunctions.log_list(self, status)
        else:
            status = 'Home position created'

            # Print the status
            UIFunctions.log_list(self, status)
            return self.home_position

    # GENERATE AND SAVE ROBOTIC PATH
    def generate_path(self):
        """
        Generate robotic path(program).
        Save program to file .txt in selected directory.
        :return: generated_path_DATETIME.txt
        """

        # Check the effector dimensions
        eff = UIFunctions.effector_check(self)

        # Create empty table
        table = []

        # Get data from QTable and add to table
        for i in range(0, self.ui.tableWidget.rowCount()):
            table_row = [str(self.ui.tableWidget.item(i, 0).text()),
                         str(self.ui.tableWidget.item(i, 1).text()),
                         str(self.ui.tableWidget.item(i, 2).text()),
                         int(self.ui.tableWidget.item(i, 3).text()),
                         int(self.ui.tableWidget.item(i, 4).text()),
                         int(self.ui.tableWidget.item(i, 5).text()),
                         int(self.ui.tableWidget.item(i, 6).text()),
                         int(self.ui.tableWidget.item(i, 7).text()),
                         int(self.ui.tableWidget.item(i, 8).text()),
                         float(self.ui.tableWidget.item(i, 9).text()),
                         eff]
            print(table_row)
            table.append(table_row)

        # Generate robotic path and write to file
        file_path_write = UIFunctions.directory_path(self)
        file_name_write = 'generated_path_'
        file_format_write = '.txt'
        trajectory.write_generated_path_to_file(table, file_path_write, file_name_write, file_format_write)

    # READ ROBOTIC PATH FROM FILE
    def read_path(self):
        """
        Read robotic path from selected file to param.
        :return: self.robotic_path
        """

        # Get path of file with robotic path to read
        file_path_read = UIFunctions.file_path(self)

        # Get robotic path
        self.read_robotic_path = trajectory.read_generated_path_from_file(file_path_read)

        # Delete first row with headers
        self.read_robotic_path.pop(0)

        print(self.read_robotic_path)

        # Print the status
        UIFunctions.write_read_path_to_table(self, self.read_robotic_path)

    # FILL TABLE WITH READ ROBOTIC PATH
    def write_read_path_to_table(self, robotic_path):
        """
        Fill table with robotic path info from read file
        :param robotic_path:
        :return: Filled table
        """

        table_ui = self.ui.tableWidget
        # Copy columns headers names
        header = []
        for i in range(0, self.ui.tableWidget.columnCount()):
            header.append(table_ui.horizontalHeaderItem(i).text())
        # Clear table and set columns headers names
        table_ui.clear()
        for i in range(0, self.ui.tableWidget.columnCount()):
            table_ui.setHorizontalHeaderItem(i, QTableWidgetItem(header[i]))
        # Add items from robotic_path to table
        for j in range(0, len(robotic_path)):
            index = int(robotic_path[j][0])
            values = [robotic_path[j][1],
                      robotic_path[j][2],
                      robotic_path[j][3],
                      robotic_path[j][4],
                      robotic_path[j][5],
                      robotic_path[j][6],
                      robotic_path[j][7],
                      robotic_path[j][12],
                      robotic_path[j][13],
                      robotic_path[j][14]]
            if index > table_ui.rowCount():
                self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            else:
                pass
            for i in range(0, self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, i,
                                            QTableWidgetItem(str(values[i])))

    # GET PATH OF FILE TO READ
    def file_path(self):
        """ Get path of selected file"""

        file_filter = 'Text file (*.txt);; All files (*.*)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Get Path',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Text File (*.txt);; All files (*.*)'
        )
        self.ui.lineEdit.setText(response[0])
        return response[0]

    # GET PATH OF DIRECTORY TO SAVE FILE
    def directory_path(self):
        """ Get path of selected directory """

        response = QFileDialog.getExistingDirectory(
            self,
            caption='Get Path',
            options=QFileDialog.ShowDirsOnly
        )
        self.ui.lineEdit.setText(response)
        return response
