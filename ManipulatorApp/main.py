import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FUNCTIONS
from app_modules import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.dragPos = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        UIFunctions.select_standard_menu(self, "btn_home")

        # MENU
        ################################################################################################################
        self.ui.btn_lista.clicked.connect(lambda: UIFunctions.toggleMenu(self, 230, True))

        # MENU 1 HOME
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        self.ui.btn_home.clicked.connect(lambda: UIFunctions.label_page(self, "HOME"))
        self.ui.btn_home.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_home"))
        self.ui.btn_home.clicked.connect(lambda: UIFunctions.log_list(self, 'Page changed to HOME'))

        # MENU 2 FK
        self.ui.btn_fk.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_fk))
        self.ui.btn_fk.clicked.connect(lambda: UIFunctions.label_page(self, "FORWARD KINEMATICS"))
        self.ui.btn_fk.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_fk"))
        self.ui.btn_fk.clicked.connect(lambda: AppFunctions.page_fk(self))
        self.ui.btn_fk.clicked.connect(lambda: UIFunctions.log_list(self, 'Page changed to FK'))

        # MENU 3 IK
        self.ui.btn_ik.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ik))
        self.ui.btn_ik.clicked.connect(lambda: UIFunctions.label_page(self, "INVERSE KINEMATICS"))
        self.ui.btn_ik.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_ik"))
        self.ui.btn_ik.clicked.connect(lambda: AppFunctions.page_ik(self))
        self.ui.btn_ik.clicked.connect(lambda: UIFunctions.log_list(self, 'Page changed to IK'))

        # MENU 4 MANUAL
        self.ui.btn_manual.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_manual))
        self.ui.btn_manual.clicked.connect(lambda: UIFunctions.label_page(self, "MANUAL MODE"))
        self.ui.btn_manual.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_manual"))
        self.ui.btn_manual.clicked.connect(lambda: AppFunctions.page_manual(self))
        self.ui.btn_manual.clicked.connect(lambda: UIFunctions.log_list(self, 'Page changed to Manual mode'))

        # MENU 5 AUTO
        self.ui.btn_auto.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_automatic))
        self.ui.btn_auto.clicked.connect(lambda: UIFunctions.label_page(self, "AUTOMATIC MODE"))
        self.ui.btn_auto.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_auto"))
        self.ui.btn_auto.clicked.connect(lambda: AppFunctions.page_automatic(self))
        self.ui.btn_auto.clicked.connect(lambda: UIFunctions.log_list(self, 'Page changed to automatic mode'))

        # MENU 6 SETTINGS
        self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))
        self.ui.btn_settings.clicked.connect(lambda: UIFunctions.label_page(self, "SETTINGS"))
        self.ui.btn_settings.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_settings"))
        self.ui.btn_settings.clicked.connect(lambda: AppFunctions.page_settings(self))
        self.ui.btn_settings.clicked.connect(lambda: UIFunctions.log_list(self, 'Page changed to settings'))
        self.ui.radioButton_home_comm_2.clicked.connect(lambda: AppFunctions.communication_radiobutton(self))

        # Pages
        ################################################################################################################

        # HOME
        self.ui.btn_home_FK.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_fk))
        self.ui.btn_home_FK.clicked.connect(lambda: UIFunctions.label_page(self, "FORWARD KINEMATICS"))
        self.ui.btn_home_FK.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_fk"))
        self.ui.btn_home_FK.clicked.connect(lambda: AppFunctions.page_fk(self))

        self.ui.btn_home_IK.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ik))
        self.ui.btn_home_IK.clicked.connect(lambda: UIFunctions.label_page(self, "INVERSE KINEMATICS"))
        self.ui.btn_home_IK.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_ik"))
        self.ui.btn_home_IK.clicked.connect(lambda: AppFunctions.page_ik(self))

        self.ui.btn_home_manual.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_manual))
        self.ui.btn_home_manual.clicked.connect(lambda: UIFunctions.label_page(self, "MANUAL MODE"))
        self.ui.btn_home_manual.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_manual"))
        self.ui.btn_home_manual.clicked.connect(lambda: AppFunctions.page_manual(self))

        self.ui.btn_home_auto.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_automatic))
        self.ui.btn_home_auto.clicked.connect(lambda: UIFunctions.label_page(self, "AUTOMATIC MODE"))
        self.ui.btn_home_auto.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_auto"))
        self.ui.btn_home_auto.clicked.connect(lambda: AppFunctions.page_automatic(self))

        self.ui.btn_home_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))
        self.ui.btn_home_settings.clicked.connect(lambda: UIFunctions.label_page(self, "SETTINGS"))
        self.ui.btn_home_settings.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_settings"))
        self.ui.btn_home_settings.clicked.connect(lambda: AppFunctions.page_settings(self))

        self.ui.btn_home_info.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))
        self.ui.btn_home_info.clicked.connect(lambda: self.ui.tabWidget_6.setCurrentIndex(0))
        self.ui.btn_home_info.clicked.connect(lambda: UIFunctions.label_page(self, "SETTINGS"))
        self.ui.btn_home_info.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_settings"))

        # FK
        self.ui.horizontalSlider_fk_s1.valueChanged.connect(lambda: AppFunctions.page_fk(self))
        self.ui.horizontalSlider_fk_s1_2.valueChanged.connect(lambda: AppFunctions.page_fk(self))
        self.ui.horizontalSlider_fk_s1_3.valueChanged.connect(lambda: AppFunctions.page_fk(self))
        self.ui.horizontalSlider_fk_s1_4.valueChanged.connect(lambda: AppFunctions.page_fk(self))
        self.ui.horizontalSlider_fk_s1_5.valueChanged.connect(lambda: AppFunctions.page_fk(self))
        self.ui.horizontalSlider_fk_s1_6.valueChanged.connect(lambda: AppFunctions.page_fk(self))
        self.ui.btn_fk_reset.clicked.connect(lambda: UIFunctions.page_fk_reset(self))
        self.ui.horizontalSlider_fk_s1.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_fk_s1", 10))
        self.ui.horizontalSlider_fk_s1_2.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_fk_s1_2", 10))
        self.ui.horizontalSlider_fk_s1_3.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_fk_s1_3", 10))
        self.ui.horizontalSlider_fk_s1_4.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_fk_s1_4", 10))
        self.ui.horizontalSlider_fk_s1_5.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_fk_s1_5", 10))
        self.ui.horizontalSlider_fk_s1_6.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_fk_s1_6", 10))

        # IK
        self.ui.horizontalSlider_ik_x.valueChanged.connect(lambda: AppFunctions.page_ik(self))
        self.ui.horizontalSlider_ik_y.valueChanged.connect(lambda: AppFunctions.page_ik(self))
        self.ui.horizontalSlider_ik_z.valueChanged.connect(lambda: AppFunctions.page_ik(self))
        self.ui.verticalSlider.valueChanged.connect(lambda: AppFunctions.page_ik(self))
        self.ui.btn_ik_reset.clicked.connect(lambda: UIFunctions.page_ik_reset(self))
        self.ui.btn_ik_reload_1.clicked.connect(lambda: AppFunctions.page_ik(self))
        self.ui.btn_ik_reload_2.clicked.connect(lambda: AppFunctions.page_ik(self))
        self.ui.horizontalSlider_ik_x.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_ik_x", 25))
        self.ui.horizontalSlider_ik_y.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_ik_y", 25))
        self.ui.horizontalSlider_ik_z.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_ik_z", 25))

        # Manual_mode
        self.ui.horizontalSlider_j_s1.valueChanged.connect(lambda: AppFunctions.page_manual(self))
        self.ui.horizontalSlider_j_s2.valueChanged.connect(lambda: AppFunctions.page_manual(self))
        self.ui.horizontalSlider_j_s3.valueChanged.connect(lambda: AppFunctions.page_manual(self))
        self.ui.horizontalSlider_j_s4.valueChanged.connect(lambda: AppFunctions.page_manual(self))
        self.ui.horizontalSlider_j_s5.valueChanged.connect(lambda: AppFunctions.page_manual(self))
        self.ui.horizontalSlider_j_s6.valueChanged.connect(lambda: AppFunctions.page_manual(self))
        self.ui.horizontalSlider_manual_x.valueChanged.connect(lambda: AppFunctions.page_manual(self))
        self.ui.horizontalSlider_manual_y.valueChanged.connect(lambda: AppFunctions.page_manual(self))
        self.ui.horizontalSlider_manual_z.valueChanged.connect(lambda: AppFunctions.page_manual(self))
        self.ui.verticalSlider_manual_orient.valueChanged.connect(lambda: AppFunctions.page_manual(self))
        self.ui.btn_manual_reset_1.clicked.connect(lambda: UIFunctions.page_manual_reset(self))
        self.ui.btn_manual_reset_2.clicked.connect(lambda: UIFunctions.page_manual_reset(self))
        self.ui.horizontalSlider_manual_x.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_manual_x", 25))
        self.ui.horizontalSlider_manual_y.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_manual_y", 25))
        self.ui.horizontalSlider_manual_z.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_manual_z", 25))
        self.ui.horizontalSlider_j_s1.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_j_s1", 10))
        self.ui.horizontalSlider_j_s2.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_j_s2", 10))
        self.ui.horizontalSlider_j_s3.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_j_s3", 10))
        self.ui.horizontalSlider_j_s4.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_j_s4", 10))
        self.ui.horizontalSlider_j_s5.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_j_s5", 10))
        self.ui.horizontalSlider_j_s6.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_j_s6", 10))

        # Automatic_mode
        self.ui.btn_auto_add_empty.clicked.connect(lambda: UIFunctions.AddRow(self))
        self.ui.btn_auto_delete.clicked.connect(lambda: UIFunctions.RemoveRow(self))
        self.ui.btn_auto_add_actual.clicked.connect(lambda: UIFunctions.add_pos(self))
        self.ui.btn_auto_add_actual_2.clicked.connect(lambda: UIFunctions.set_home(self))
        self.ui.btn_auto_Add_safe.clicked.connect(lambda: UIFunctions.add_safe(self))
        self.ui.btn_auto_Add_wait.clicked.connect(lambda: UIFunctions.add_wait(self))
        self.ui.btn_auto_file_dialog.clicked.connect(lambda: UIFunctions.directory_path(self))
        self.ui.horizontalSlider_auto_x.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_auto_x", 25))
        self.ui.horizontalSlider_auto_y.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_auto_y", 25))
        self.ui.horizontalSlider_auto_z.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_auto_z", 25))
        self.ui.horizontalSlider_auto_s1.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_auto_s1", 10))
        self.ui.horizontalSlider_auto_s2.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_auto_s2", 10))
        self.ui.horizontalSlider_auto_s3.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_auto_s3", 10))
        self.ui.horizontalSlider_auto_s4.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_auto_s4", 10))
        self.ui.horizontalSlider_auto_s5.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_auto_s5", 10))
        self.ui.horizontalSlider_auto_s6.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_auto_s6", 10))
        self.ui.horizontalSlider_auto_time_2.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_auto_time_2", 10))
        self.ui.horizontalSlider_auto_orient.valueChanged.connect(lambda: UIFunctions.set_slider_color(self, "horizontalSlider_auto_orient", 10))

        ################################################################################################################

        # MOVE WINDOW
        def move_window(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.frame_top.mouseMoveEvent = move_window

        # ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    # APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


GUI = MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec_())
