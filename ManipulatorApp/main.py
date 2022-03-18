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

        # MENU 2 FK
        self.ui.btn_fk.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_fk))
        self.ui.btn_fk.clicked.connect(lambda: UIFunctions.label_page(self, "FORWARD KINEMATICS"))
        self.ui.btn_fk.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_fk"))

        # MENU 3 IK
        self.ui.btn_ik.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ik))
        self.ui.btn_ik.clicked.connect(lambda: UIFunctions.label_page(self, "INVERSE KINEMATICS"))
        self.ui.btn_ik.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_ik"))

        # MENU 4 MANUAL
        self.ui.btn_manual.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_manual))
        self.ui.btn_manual.clicked.connect(lambda: UIFunctions.label_page(self, "MANUAL MODE"))
        self.ui.btn_manual.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_manual"))

        # MENU 5 AUTO
        self.ui.btn_auto.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_automatic))
        self.ui.btn_auto.clicked.connect(lambda: UIFunctions.label_page(self, "AUTOMATIC MODE"))
        self.ui.btn_auto.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_auto"))

        # MENU 6 SETTINGS
        self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))
        self.ui.btn_settings.clicked.connect(lambda: UIFunctions.label_page(self, "SETTINGS"))
        self.ui.btn_settings.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_settings"))

        # Pages
        ################################################################################################################

        # HOME
        self.ui.btn_home_FK.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_fk))
        self.ui.btn_home_FK.clicked.connect(lambda: UIFunctions.label_page(self, "FORWARD KINEMATICS"))
        self.ui.btn_home_FK.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_fk"))

        self.ui.btn_home_IK.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ik))
        self.ui.btn_home_IK.clicked.connect(lambda: UIFunctions.label_page(self, "INVERSE KINEMATICS"))
        self.ui.btn_home_IK.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_ik"))

        self.ui.btn_home_manual.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_manual))
        self.ui.btn_home_manual.clicked.connect(lambda: UIFunctions.label_page(self, "MANUAL MODE"))
        self.ui.btn_home_manual.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_manual"))

        self.ui.btn_home_auto.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_automatic))
        self.ui.btn_home_auto.clicked.connect(lambda: UIFunctions.label_page(self, "AUTOMATIC MODE"))
        self.ui.btn_home_auto.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_auto"))

        self.ui.btn_home_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))
        self.ui.btn_home_settings.clicked.connect(lambda: UIFunctions.label_page(self, "SETTINGS"))
        self.ui.btn_home_settings.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_settings"))

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

        # IK
        self.ui.horizontalSlider_ik_x.valueChanged.connect(lambda: AppFunctions.page_ik(self))
        self.ui.horizontalSlider_ik_y.valueChanged.connect(lambda: AppFunctions.page_ik(self))
        self.ui.horizontalSlider_ik_z.valueChanged.connect(lambda: AppFunctions.page_ik(self))
        self.ui.verticalSlider.valueChanged.connect(lambda: AppFunctions.page_ik(self))


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
