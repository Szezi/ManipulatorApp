# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ManipulatorApp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ManipulatorApp.modules.mplwidget import MplWidget

from ManipulatorApp.ui.icons import icons_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 680)
        MainWindow.setMinimumSize(QSize(1000, 680))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 60))
        self.frame_top.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top_lista = QFrame(self.frame_top)
        self.frame_top_lista.setObjectName(u"frame_top_lista")
        self.frame_top_lista.setMinimumSize(QSize(0, 0))
        self.frame_top_lista.setMaximumSize(QSize(70, 60))
        self.frame_top_lista.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_top_lista.setFrameShape(QFrame.NoFrame)
        self.frame_top_lista.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_lista)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_lista = QPushButton(self.frame_top_lista)
        self.btn_lista.setObjectName(u"btn_lista")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_lista.sizePolicy().hasHeightForWidth())
        self.btn_lista.setSizePolicy(sizePolicy)
        self.btn_lista.setMinimumSize(QSize(0, 0))
        self.btn_lista.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-image: url(:/24x24/24x24/icons8-activity-feed-50.png);\n"
"	background-position: left center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-left: 25px solid rgb(35, 35, 35);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"	border-left: 25px solid rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 25px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_lista)


        self.horizontalLayout.addWidget(self.frame_top_lista)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_top_right2 = QFrame(self.frame_top_right)
        self.frame_top_right2.setObjectName(u"frame_top_right2")
        self.frame_top_right2.setMinimumSize(QSize(0, 30))
        self.frame_top_right2.setMaximumSize(QSize(16777215, 30))
        self.frame_top_right2.setStyleSheet(u"background-color: rgb(61, 61,61);")
        self.frame_top_right2.setFrameShape(QFrame.NoFrame)
        self.frame_top_right2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_right2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_name = QFrame(self.frame_top_right2)
        self.frame_name.setObjectName(u"frame_name")
        self.frame_name.setStyleSheet(u"")
        self.frame_name.setFrameShape(QFrame.NoFrame)
        self.frame_name.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_name)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_name_logo = QFrame(self.frame_name)
        self.frame_name_logo.setObjectName(u"frame_name_logo")
        self.frame_name_logo.setMaximumSize(QSize(30, 30))
        self.frame_name_logo.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/24x24/24x24/icons8-robot-50.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.frame_name_logo.setFrameShape(QFrame.NoFrame)
        self.frame_name_logo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_name_logo)

        self.label_name = QLabel(self.frame_name)
        self.label_name.setObjectName(u"label_name")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"background: transparent;\n"
"color: rgb(222, 222, 222);\n"
"margin-left: 5px;")

        self.horizontalLayout_10.addWidget(self.label_name)


        self.horizontalLayout_4.addWidget(self.frame_name)

        self.frame_btn = QFrame(self.frame_top_right2)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMaximumSize(QSize(120, 16777215))
        self.frame_btn.setFrameShape(QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_min = QPushButton(self.frame_btn)
        self.btn_min.setObjectName(u"btn_min")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_min.sizePolicy().hasHeightForWidth())
        self.btn_min.setSizePolicy(sizePolicy1)
        self.btn_min.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/20x20/20x20/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_min.setIcon(icon)
        self.btn_min.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.frame_btn)
        self.btn_max.setObjectName(u"btn_max")
        sizePolicy1.setHeightForWidth(self.btn_max.sizePolicy().hasHeightForWidth())
        self.btn_max.setSizePolicy(sizePolicy1)
        self.btn_max.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/20x20/20x20/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_max.setIcon(icon1)
        self.btn_max.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.btn_max)

        self.btn_close = QPushButton(self.frame_btn)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(35, 35, 35);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/20x20/20x20/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btn)


        self.verticalLayout_8.addWidget(self.frame_top_right2)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMinimumSize(QSize(0, 30))
        self.frame_top_info.setMaximumSize(QSize(16777215, 30))
        self.frame_top_info.setStyleSheet(u"")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 16777215))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setBold(True)
        font1.setWeight(75)
        self.label_top_info_2.setFont(font1)
        self.label_top_info_2.setStyleSheet(u"color: rgb(222, 222, 222);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_8.addWidget(self.frame_top_info, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_content = QFrame(self.centralwidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setStyleSheet(u"color: rgb(222, 222, 222);")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_content)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(70, 0))
        self.frame_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_menu.setFrameShape(QFrame.NoFrame)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_top = QFrame(self.frame_menu)
        self.frame_menu_top.setObjectName(u"frame_menu_top")
        self.frame_menu_top.setFrameShape(QFrame.NoFrame)
        self.frame_menu_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_menu_top)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.frame_menu_top)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy2)
        self.btn_home.setMinimumSize(QSize(0, 60))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.btn_home.setFont(font2)
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/24x24/24x24/icons8-four-squares-50.png);\n"
"	background-position:left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid rgb(35, 35, 35);\n"
"	background-color: rgb(35, 35, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"	color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"	border-left: 25px solid rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 25px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_fk = QPushButton(self.frame_menu_top)
        self.btn_fk.setObjectName(u"btn_fk")
        sizePolicy2.setHeightForWidth(self.btn_fk.sizePolicy().hasHeightForWidth())
        self.btn_fk.setSizePolicy(sizePolicy2)
        self.btn_fk.setMinimumSize(QSize(0, 60))
        self.btn_fk.setFont(font2)
        self.btn_fk.setLayoutDirection(Qt.LeftToRight)
        self.btn_fk.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/others/24x24/icons_fk.png);\n"
"	background-position:left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid rgb(35, 35, 35);\n"
"	background-color: rgb(35, 35, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"	color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"	border-left: 25px solid rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 25px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_fk)

        self.btn_ik = QPushButton(self.frame_menu_top)
        self.btn_ik.setObjectName(u"btn_ik")
        sizePolicy2.setHeightForWidth(self.btn_ik.sizePolicy().hasHeightForWidth())
        self.btn_ik.setSizePolicy(sizePolicy2)
        self.btn_ik.setMinimumSize(QSize(0, 60))
        self.btn_ik.setFont(font2)
        self.btn_ik.setLayoutDirection(Qt.LeftToRight)
        self.btn_ik.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/others/24x24/icons_Ik.png);\n"
"	background-position:left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid rgb(35, 35, 35);\n"
"	background-color: rgb(35, 35, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"	color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"	border-left: 25px solid rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 25px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_ik)

        self.btn_manual = QPushButton(self.frame_menu_top)
        self.btn_manual.setObjectName(u"btn_manual")
        sizePolicy2.setHeightForWidth(self.btn_manual.sizePolicy().hasHeightForWidth())
        self.btn_manual.setSizePolicy(sizePolicy2)
        self.btn_manual.setMinimumSize(QSize(0, 60))
        self.btn_manual.setFont(font2)
        self.btn_manual.setLayoutDirection(Qt.LeftToRight)
        self.btn_manual.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/24x24/24x24/icons8-manual-50.png);\n"
"	background-position:left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid rgb(35, 35, 35);\n"
"	background-color: rgb(35, 35, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"	color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"	border-left: 25px solid rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 25px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_manual)

        self.btn_auto = QPushButton(self.frame_menu_top)
        self.btn_auto.setObjectName(u"btn_auto")
        sizePolicy2.setHeightForWidth(self.btn_auto.sizePolicy().hasHeightForWidth())
        self.btn_auto.setSizePolicy(sizePolicy2)
        self.btn_auto.setMinimumSize(QSize(0, 60))
        self.btn_auto.setFont(font2)
        self.btn_auto.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/24x24/24x24/icons8-automatic-50.png);\n"
"	background-position:left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid rgb(35, 35, 35);\n"
"	background-color: rgb(35, 35, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"	color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"	border-left: 25px solid rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 25px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_auto)


        self.verticalLayout_3.addWidget(self.frame_menu_top, 0, Qt.AlignTop)

        self.frame_menu_bottom = QFrame(self.frame_menu)
        self.frame_menu_bottom.setObjectName(u"frame_menu_bottom")
        self.frame_menu_bottom.setMaximumSize(QSize(16777215, 100))
        self.frame_menu_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_menu_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_menu_bottom)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 50)
        self.btn_settings = QPushButton(self.frame_menu_bottom)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy2.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy2)
        self.btn_settings.setMinimumSize(QSize(0, 60))
        self.btn_settings.setFont(font2)
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/24x24/24x24/icons8-adjust-50.png);\n"
"	background-position:left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid rgb(35, 35, 35);\n"
"	background-color: rgb(35, 35, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"	border-left: 25px solid rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 25px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_settings)


        self.verticalLayout_3.addWidget(self.frame_menu_bottom)


        self.horizontalLayout_2.addWidget(self.frame_menu)

        self.frame_screens = QFrame(self.frame_content)
        self.frame_screens.setObjectName(u"frame_screens")
        self.frame_screens.setFrameShape(QFrame.NoFrame)
        self.frame_screens.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_screens)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_stackedWidget = QFrame(self.frame_screens)
        self.frame_stackedWidget.setObjectName(u"frame_stackedWidget")
        self.frame_stackedWidget.setFrameShape(QFrame.NoFrame)
        self.frame_stackedWidget.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_stackedWidget)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_stackedWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_7 = QHBoxLayout(self.page_home)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_home_shortcuts = QFrame(self.page_home)
        self.frame_home_shortcuts.setObjectName(u"frame_home_shortcuts")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_home_shortcuts.sizePolicy().hasHeightForWidth())
        self.frame_home_shortcuts.setSizePolicy(sizePolicy3)
        self.frame_home_shortcuts.setMinimumSize(QSize(440, 0))
        self.frame_home_shortcuts.setFrameShape(QFrame.NoFrame)
        self.frame_home_shortcuts.setFrameShadow(QFrame.Raised)
        self.frame_home_shortcuts.setMidLineWidth(1)
        self.gridLayout = QGridLayout(self.frame_home_shortcuts)
        self.gridLayout.setSpacing(50)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(50, 50, 50, 50)
        self.btn_home_manual = QPushButton(self.frame_home_shortcuts)
        self.btn_home_manual.setObjectName(u"btn_home_manual")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_home_manual.sizePolicy().hasHeightForWidth())
        self.btn_home_manual.setSizePolicy(sizePolicy4)
        self.btn_home_manual.setMinimumSize(QSize(100, 100))
        self.btn_home_manual.setMaximumSize(QSize(200, 200))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.btn_home_manual.setFont(font3)
        self.btn_home_manual.setLayoutDirection(Qt.LeftToRight)
        self.btn_home_manual.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_home_manual, 1, 0, 1, 1)

        self.btn_home_IK = QPushButton(self.frame_home_shortcuts)
        self.btn_home_IK.setObjectName(u"btn_home_IK")
        sizePolicy4.setHeightForWidth(self.btn_home_IK.sizePolicy().hasHeightForWidth())
        self.btn_home_IK.setSizePolicy(sizePolicy4)
        self.btn_home_IK.setMinimumSize(QSize(100, 100))
        self.btn_home_IK.setMaximumSize(QSize(200, 200))
        self.btn_home_IK.setFont(font3)
        self.btn_home_IK.setLayoutDirection(Qt.LeftToRight)
        self.btn_home_IK.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_home_IK, 0, 1, 1, 1)

        self.btn_home_FK = QPushButton(self.frame_home_shortcuts)
        self.btn_home_FK.setObjectName(u"btn_home_FK")
        sizePolicy4.setHeightForWidth(self.btn_home_FK.sizePolicy().hasHeightForWidth())
        self.btn_home_FK.setSizePolicy(sizePolicy4)
        self.btn_home_FK.setMinimumSize(QSize(100, 100))
        self.btn_home_FK.setMaximumSize(QSize(200, 200))
        self.btn_home_FK.setSizeIncrement(QSize(10, 10))
        self.btn_home_FK.setBaseSize(QSize(100, 100))
        self.btn_home_FK.setFont(font3)
        self.btn_home_FK.setLayoutDirection(Qt.LeftToRight)
        self.btn_home_FK.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_home_FK, 0, 0, 1, 1)

        self.btn_home_info = QPushButton(self.frame_home_shortcuts)
        self.btn_home_info.setObjectName(u"btn_home_info")
        sizePolicy4.setHeightForWidth(self.btn_home_info.sizePolicy().hasHeightForWidth())
        self.btn_home_info.setSizePolicy(sizePolicy4)
        self.btn_home_info.setMinimumSize(QSize(100, 100))
        self.btn_home_info.setMaximumSize(QSize(200, 200))
        self.btn_home_info.setFont(font3)
        self.btn_home_info.setLayoutDirection(Qt.LeftToRight)
        self.btn_home_info.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_home_info, 2, 1, 1, 1)

        self.btn_home_settings = QPushButton(self.frame_home_shortcuts)
        self.btn_home_settings.setObjectName(u"btn_home_settings")
        sizePolicy4.setHeightForWidth(self.btn_home_settings.sizePolicy().hasHeightForWidth())
        self.btn_home_settings.setSizePolicy(sizePolicy4)
        self.btn_home_settings.setMinimumSize(QSize(100, 100))
        self.btn_home_settings.setMaximumSize(QSize(200, 200))
        self.btn_home_settings.setFont(font3)
        self.btn_home_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_home_settings.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_home_settings, 2, 0, 1, 1)

        self.btn_home_auto = QPushButton(self.frame_home_shortcuts)
        self.btn_home_auto.setObjectName(u"btn_home_auto")
        sizePolicy4.setHeightForWidth(self.btn_home_auto.sizePolicy().hasHeightForWidth())
        self.btn_home_auto.setSizePolicy(sizePolicy4)
        self.btn_home_auto.setMinimumSize(QSize(100, 100))
        self.btn_home_auto.setMaximumSize(QSize(200, 200))
        self.btn_home_auto.setFont(font3)
        self.btn_home_auto.setLayoutDirection(Qt.LeftToRight)
        self.btn_home_auto.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius:25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_home_auto, 1, 1, 1, 1)


        self.horizontalLayout_7.addWidget(self.frame_home_shortcuts)

        self.frame_home_info = QFrame(self.page_home)
        self.frame_home_info.setObjectName(u"frame_home_info")
        sizePolicy3.setHeightForWidth(self.frame_home_info.sizePolicy().hasHeightForWidth())
        self.frame_home_info.setSizePolicy(sizePolicy3)
        self.frame_home_info.setMinimumSize(QSize(440, 0))
        self.frame_home_info.setSizeIncrement(QSize(10, 10))
        self.frame_home_info.setBaseSize(QSize(100, 100))
        self.frame_home_info.setLayoutDirection(Qt.LeftToRight)
        self.frame_home_info.setFrameShape(QFrame.NoFrame)
        self.frame_home_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_home_info)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_home_info_top = QFrame(self.frame_home_info)
        self.frame_home_info_top.setObjectName(u"frame_home_info_top")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_home_info_top.sizePolicy().hasHeightForWidth())
        self.frame_home_info_top.setSizePolicy(sizePolicy5)
        self.frame_home_info_top.setMinimumSize(QSize(440, 450))
        self.frame_home_info_top.setFrameShape(QFrame.StyledPanel)
        self.frame_home_info_top.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_home_info_top)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(50)
        self.gridLayout_3.setVerticalSpacing(25)
        self.gridLayout_3.setContentsMargins(50, 25, 25, 0)
        self.radioButton_home_effector = QRadioButton(self.frame_home_info_top)
        self.radioButton_home_effector.setObjectName(u"radioButton_home_effector")
        self.radioButton_home_effector.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.radioButton_home_effector.sizePolicy().hasHeightForWidth())
        self.radioButton_home_effector.setSizePolicy(sizePolicy6)
        self.radioButton_home_effector.setMinimumSize(QSize(250, 50))
        self.radioButton_home_effector.setMaximumSize(QSize(400, 50))
        font4 = QFont()
        font4.setPointSize(10)
        self.radioButton_home_effector.setFont(font4)
        self.radioButton_home_effector.setContextMenuPolicy(Qt.NoContextMenu)
        self.radioButton_home_effector.setLayoutDirection(Qt.LeftToRight)
        self.radioButton_home_effector.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background-color:       green;\n"
"    border:                 2px solid white;\n"
"	border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       red;\n"
"    border:                 2px solid white;\n"
"	border-radius:          7px;\n"
"}")
        self.radioButton_home_effector.setCheckable(True)
        self.radioButton_home_effector.setChecked(False)
        self.radioButton_home_effector.setAutoRepeat(False)
        self.radioButton_home_effector.setAutoExclusive(False)

        self.gridLayout_3.addWidget(self.radioButton_home_effector, 3, 0, 1, 1)

        self.radioButton_home_comm = QRadioButton(self.frame_home_info_top)
        self.radioButton_home_comm.setObjectName(u"radioButton_home_comm")
        self.radioButton_home_comm.setEnabled(False)
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.radioButton_home_comm.sizePolicy().hasHeightForWidth())
        self.radioButton_home_comm.setSizePolicy(sizePolicy7)
        self.radioButton_home_comm.setMinimumSize(QSize(250, 50))
        self.radioButton_home_comm.setMaximumSize(QSize(400, 100))
        self.radioButton_home_comm.setFont(font4)
        self.radioButton_home_comm.setContextMenuPolicy(Qt.NoContextMenu)
        self.radioButton_home_comm.setLayoutDirection(Qt.LeftToRight)
        self.radioButton_home_comm.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background-color:       green;\n"
"    border:                 2px solid white;\n"
"	border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       red;\n"
"    border:                 2px solid white;\n"
"	border-radius:          7px;\n"
"}")
        self.radioButton_home_comm.setChecked(False)
        self.radioButton_home_comm.setAutoExclusive(False)

        self.gridLayout_3.addWidget(self.radioButton_home_comm, 0, 0, 1, 1)

        self.label_home_port = QLabel(self.frame_home_info_top)
        self.label_home_port.setObjectName(u"label_home_port")
        self.label_home_port.setMinimumSize(QSize(250, 50))
        self.label_home_port.setMaximumSize(QSize(400, 50))
        self.label_home_port.setFont(font4)
        self.label_home_port.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_home_port, 1, 0, 1, 1)

        self.logo_home_effector = QLabel(self.frame_home_info_top)
        self.logo_home_effector.setObjectName(u"logo_home_effector")
        self.logo_home_effector.setMinimumSize(QSize(50, 50))
        self.logo_home_effector.setMaximumSize(QSize(50, 50))
        self.logo_home_effector.setStyleSheet(u"")
        self.logo_home_effector.setPixmap(QPixmap(u":/50x50/50x50/icons8-work-50.png"))
        self.logo_home_effector.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.logo_home_effector, 3, 2, 1, 1)

        self.logo_home_arduino_2 = QLabel(self.frame_home_info_top)
        self.logo_home_arduino_2.setObjectName(u"logo_home_arduino_2")
        self.logo_home_arduino_2.setMinimumSize(QSize(50, 50))
        self.logo_home_arduino_2.setMaximumSize(QSize(50, 50))
        self.logo_home_arduino_2.setStyleSheet(u"")
        self.logo_home_arduino_2.setPixmap(QPixmap(u":/50x50/50x50/icons8-arduino-uno-board-50.png"))
        self.logo_home_arduino_2.setScaledContents(True)
        self.logo_home_arduino_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.logo_home_arduino_2, 0, 2, 1, 1)

        self.logo_home_arduino = QLabel(self.frame_home_info_top)
        self.logo_home_arduino.setObjectName(u"logo_home_arduino")
        self.logo_home_arduino.setMinimumSize(QSize(50, 50))
        self.logo_home_arduino.setMaximumSize(QSize(50, 50))
        self.logo_home_arduino.setStyleSheet(u"")
        self.logo_home_arduino.setPixmap(QPixmap(u":/50x50/50x50/icons8-usb-micro-b-50.png"))
        self.logo_home_arduino.setScaledContents(True)
        self.logo_home_arduino.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.logo_home_arduino, 1, 2, 1, 1)

        self.logo_home_robot = QLabel(self.frame_home_info_top)
        self.logo_home_robot.setObjectName(u"logo_home_robot")
        self.logo_home_robot.setMinimumSize(QSize(50, 50))
        self.logo_home_robot.setMaximumSize(QSize(50, 50))
        self.logo_home_robot.setLayoutDirection(Qt.RightToLeft)
        self.logo_home_robot.setStyleSheet(u"background-image: url(:/50x50/50x50/icons8-robot-50.png);")
        self.logo_home_robot.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.logo_home_robot, 4, 2, 1, 1)

        self.label_home_pos = QLabel(self.frame_home_info_top)
        self.label_home_pos.setObjectName(u"label_home_pos")
        sizePolicy3.setHeightForWidth(self.label_home_pos.sizePolicy().hasHeightForWidth())
        self.label_home_pos.setSizePolicy(sizePolicy3)
        self.label_home_pos.setMinimumSize(QSize(250, 50))
        self.label_home_pos.setMaximumSize(QSize(400, 50))
        font5 = QFont()
        font5.setPointSize(12)
        self.label_home_pos.setFont(font5)
        self.label_home_pos.setLayoutDirection(Qt.LeftToRight)
        self.label_home_pos.setStyleSheet(u"color: rgb(222, 222, 222);")
        self.label_home_pos.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_home_pos, 4, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_home_info_top)

        self.frame_home_info_bottom = QFrame(self.frame_home_info)
        self.frame_home_info_bottom.setObjectName(u"frame_home_info_bottom")
        sizePolicy5.setHeightForWidth(self.frame_home_info_bottom.sizePolicy().hasHeightForWidth())
        self.frame_home_info_bottom.setSizePolicy(sizePolicy5)
        self.frame_home_info_bottom.setMinimumSize(QSize(440, 150))
        self.frame_home_info_bottom.setMaximumSize(QSize(16777215, 200))
        self.frame_home_info_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_home_info_bottom.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_home_info_bottom)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lcdNumber_home_actual_X = QLCDNumber(self.frame_home_info_bottom)
        self.lcdNumber_home_actual_X.setObjectName(u"lcdNumber_home_actual_X")
        self.lcdNumber_home_actual_X.setMinimumSize(QSize(100, 50))
        self.lcdNumber_home_actual_X.setMaximumSize(QSize(100, 50))

        self.gridLayout_2.addWidget(self.lcdNumber_home_actual_X, 4, 0, 1, 1)

        self.label_home_actual_Y = QLabel(self.frame_home_info_bottom)
        self.label_home_actual_Y.setObjectName(u"label_home_actual_Y")
        self.label_home_actual_Y.setMinimumSize(QSize(100, 50))
        self.label_home_actual_Y.setMaximumSize(QSize(100, 50))
        self.label_home_actual_Y.setFont(font4)
        self.label_home_actual_Y.setStyleSheet(u"color: rgb(222, 222, 222);")
        self.label_home_actual_Y.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_home_actual_Y, 3, 1, 1, 1)

        self.label_home_actual_Z = QLabel(self.frame_home_info_bottom)
        self.label_home_actual_Z.setObjectName(u"label_home_actual_Z")
        self.label_home_actual_Z.setMinimumSize(QSize(100, 50))
        self.label_home_actual_Z.setMaximumSize(QSize(100, 50))
        self.label_home_actual_Z.setFont(font4)
        self.label_home_actual_Z.setStyleSheet(u"color: rgb(222, 222, 222);")
        self.label_home_actual_Z.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_home_actual_Z, 3, 2, 1, 1)

        self.label_home_actual_X = QLabel(self.frame_home_info_bottom)
        self.label_home_actual_X.setObjectName(u"label_home_actual_X")
        self.label_home_actual_X.setMinimumSize(QSize(100, 50))
        self.label_home_actual_X.setMaximumSize(QSize(100, 50))
        self.label_home_actual_X.setFont(font4)
        self.label_home_actual_X.setLayoutDirection(Qt.LeftToRight)
        self.label_home_actual_X.setStyleSheet(u"color: rgb(222, 222, 222);")
        self.label_home_actual_X.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_home_actual_X, 3, 0, 1, 1)

        self.lcdNumber_home_actual_Y = QLCDNumber(self.frame_home_info_bottom)
        self.lcdNumber_home_actual_Y.setObjectName(u"lcdNumber_home_actual_Y")
        self.lcdNumber_home_actual_Y.setMinimumSize(QSize(100, 50))
        self.lcdNumber_home_actual_Y.setMaximumSize(QSize(100, 50))

        self.gridLayout_2.addWidget(self.lcdNumber_home_actual_Y, 4, 1, 1, 1)

        self.lcdNumber_home_actual_Z = QLCDNumber(self.frame_home_info_bottom)
        self.lcdNumber_home_actual_Z.setObjectName(u"lcdNumber_home_actual_Z")
        self.lcdNumber_home_actual_Z.setMinimumSize(QSize(100, 50))
        self.lcdNumber_home_actual_Z.setMaximumSize(QSize(100, 50))

        self.gridLayout_2.addWidget(self.lcdNumber_home_actual_Z, 4, 2, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_home_info_bottom)


        self.horizontalLayout_7.addWidget(self.frame_home_info)

        self.stackedWidget.addWidget(self.page_home)
        self.page_fk = QWidget()
        self.page_fk.setObjectName(u"page_fk")
        self.gridLayout_5 = QGridLayout(self.page_fk)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_fk_input = QFrame(self.page_fk)
        self.frame_fk_input.setObjectName(u"frame_fk_input")
        sizePolicy4.setHeightForWidth(self.frame_fk_input.sizePolicy().hasHeightForWidth())
        self.frame_fk_input.setSizePolicy(sizePolicy4)
        self.frame_fk_input.setMinimumSize(QSize(440, 300))
        self.frame_fk_input.setLayoutDirection(Qt.LeftToRight)
        self.frame_fk_input.setFrameShape(QFrame.NoFrame)
        self.frame_fk_input.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_fk_input)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_fk_input)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_fk_joint = QWidget()
        self.tab_fk_joint.setObjectName(u"tab_fk_joint")
        self.gridLayout_6 = QGridLayout(self.tab_fk_joint)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lcdNumber_fk_s1 = QLCDNumber(self.tab_fk_joint)
        self.lcdNumber_fk_s1.setObjectName(u"lcdNumber_fk_s1")
        self.lcdNumber_fk_s1.setMinimumSize(QSize(30, 30))
        self.lcdNumber_fk_s1.setMaximumSize(QSize(50, 50))
        font6 = QFont()
        font6.setPointSize(4)
        self.lcdNumber_fk_s1.setFont(font6)
        self.lcdNumber_fk_s1.setStyleSheet(u"QLCDNumber{\n"
"  border: none;\n"
"  color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_6.addWidget(self.lcdNumber_fk_s1, 1, 0, 1, 1)

        self.horizontalSlider_fk_s1 = QSlider(self.tab_fk_joint)
        self.horizontalSlider_fk_s1.setObjectName(u"horizontalSlider_fk_s1")
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.horizontalSlider_fk_s1.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_fk_s1.setSizePolicy(sizePolicy8)
        self.horizontalSlider_fk_s1.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_fk_s1.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_fk_s1.setLayoutDirection(Qt.LeftToRight)
        self.horizontalSlider_fk_s1.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_fk_s1.setMinimum(-90)
        self.horizontalSlider_fk_s1.setMaximum(90)
        self.horizontalSlider_fk_s1.setPageStep(5)
        self.horizontalSlider_fk_s1.setOrientation(Qt.Horizontal)
        self.horizontalSlider_fk_s1.setInvertedAppearance(False)
        self.horizontalSlider_fk_s1.setInvertedControls(False)
        self.horizontalSlider_fk_s1.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_fk_s1.setTickInterval(10)

        self.gridLayout_6.addWidget(self.horizontalSlider_fk_s1, 1, 1, 1, 1)

        self.label_fk_s1 = QLabel(self.tab_fk_joint)
        self.label_fk_s1.setObjectName(u"label_fk_s1")
        sizePolicy3.setHeightForWidth(self.label_fk_s1.sizePolicy().hasHeightForWidth())
        self.label_fk_s1.setSizePolicy(sizePolicy3)
        self.label_fk_s1.setMinimumSize(QSize(150, 25))
        self.label_fk_s1.setMaximumSize(QSize(16777215, 25))
        self.label_fk_s1.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_fk_s1, 0, 1, 1, 1)

        self.label_fk_s4 = QLabel(self.tab_fk_joint)
        self.label_fk_s4.setObjectName(u"label_fk_s4")
        sizePolicy3.setHeightForWidth(self.label_fk_s4.sizePolicy().hasHeightForWidth())
        self.label_fk_s4.setSizePolicy(sizePolicy3)
        self.label_fk_s4.setMinimumSize(QSize(150, 25))
        self.label_fk_s4.setMaximumSize(QSize(16777215, 25))
        self.label_fk_s4.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_fk_s4, 4, 1, 1, 1)

        self.lcdNumber_fk_s3 = QLCDNumber(self.tab_fk_joint)
        self.lcdNumber_fk_s3.setObjectName(u"lcdNumber_fk_s3")
        self.lcdNumber_fk_s3.setMinimumSize(QSize(30, 30))
        self.lcdNumber_fk_s3.setMaximumSize(QSize(50, 50))
        self.lcdNumber_fk_s3.setFrameShape(QFrame.NoFrame)

        self.gridLayout_6.addWidget(self.lcdNumber_fk_s3, 5, 0, 1, 1)

        self.label_fk_s2 = QLabel(self.tab_fk_joint)
        self.label_fk_s2.setObjectName(u"label_fk_s2")
        sizePolicy3.setHeightForWidth(self.label_fk_s2.sizePolicy().hasHeightForWidth())
        self.label_fk_s2.setSizePolicy(sizePolicy3)
        self.label_fk_s2.setMinimumSize(QSize(150, 25))
        self.label_fk_s2.setMaximumSize(QSize(16777215, 25))
        self.label_fk_s2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_fk_s2, 2, 1, 1, 1)

        self.horizontalSlider_fk_s1_2 = QSlider(self.tab_fk_joint)
        self.horizontalSlider_fk_s1_2.setObjectName(u"horizontalSlider_fk_s1_2")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_fk_s1_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_fk_s1_2.setSizePolicy(sizePolicy8)
        self.horizontalSlider_fk_s1_2.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_fk_s1_2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_fk_s1_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_fk_s1_2.setMinimum(0)
        self.horizontalSlider_fk_s1_2.setMaximum(180)
        self.horizontalSlider_fk_s1_2.setPageStep(5)
        self.horizontalSlider_fk_s1_2.setValue(90)
        self.horizontalSlider_fk_s1_2.setSliderPosition(90)
        self.horizontalSlider_fk_s1_2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_fk_s1_2.setInvertedAppearance(False)
        self.horizontalSlider_fk_s1_2.setInvertedControls(False)
        self.horizontalSlider_fk_s1_2.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_fk_s1_2.setTickInterval(10)

        self.gridLayout_6.addWidget(self.horizontalSlider_fk_s1_2, 3, 1, 1, 1)

        self.horizontalSlider_fk_s1_3 = QSlider(self.tab_fk_joint)
        self.horizontalSlider_fk_s1_3.setObjectName(u"horizontalSlider_fk_s1_3")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_fk_s1_3.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_fk_s1_3.setSizePolicy(sizePolicy8)
        self.horizontalSlider_fk_s1_3.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_fk_s1_3.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_fk_s1_3.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_fk_s1_3.setMinimum(-90)
        self.horizontalSlider_fk_s1_3.setMaximum(90)
        self.horizontalSlider_fk_s1_3.setPageStep(5)
        self.horizontalSlider_fk_s1_3.setOrientation(Qt.Horizontal)
        self.horizontalSlider_fk_s1_3.setInvertedAppearance(False)
        self.horizontalSlider_fk_s1_3.setInvertedControls(False)
        self.horizontalSlider_fk_s1_3.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_fk_s1_3.setTickInterval(10)

        self.gridLayout_6.addWidget(self.horizontalSlider_fk_s1_3, 5, 1, 1, 1)

        self.lcdNumber_fk_s2 = QLCDNumber(self.tab_fk_joint)
        self.lcdNumber_fk_s2.setObjectName(u"lcdNumber_fk_s2")
        self.lcdNumber_fk_s2.setMinimumSize(QSize(30, 30))
        self.lcdNumber_fk_s2.setMaximumSize(QSize(50, 50))
        self.lcdNumber_fk_s2.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_fk_s2.setProperty("value", 90.000000000000000)

        self.gridLayout_6.addWidget(self.lcdNumber_fk_s2, 3, 0, 1, 1)

        self.lcdNumber_fk_s4 = QLCDNumber(self.tab_fk_joint)
        self.lcdNumber_fk_s4.setObjectName(u"lcdNumber_fk_s4")
        self.lcdNumber_fk_s4.setMinimumSize(QSize(30, 30))
        self.lcdNumber_fk_s4.setMaximumSize(QSize(50, 50))
        self.lcdNumber_fk_s4.setFrameShape(QFrame.NoFrame)

        self.gridLayout_6.addWidget(self.lcdNumber_fk_s4, 7, 0, 1, 1)

        self.label_fk_s3 = QLabel(self.tab_fk_joint)
        self.label_fk_s3.setObjectName(u"label_fk_s3")
        sizePolicy3.setHeightForWidth(self.label_fk_s3.sizePolicy().hasHeightForWidth())
        self.label_fk_s3.setSizePolicy(sizePolicy3)
        self.label_fk_s3.setMinimumSize(QSize(150, 25))
        self.label_fk_s3.setMaximumSize(QSize(16777215, 25))
        self.label_fk_s3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_fk_s3, 6, 1, 1, 1)

        self.label_fk_s5 = QLabel(self.tab_fk_joint)
        self.label_fk_s5.setObjectName(u"label_fk_s5")
        sizePolicy3.setHeightForWidth(self.label_fk_s5.sizePolicy().hasHeightForWidth())
        self.label_fk_s5.setSizePolicy(sizePolicy3)
        self.label_fk_s5.setMinimumSize(QSize(150, 25))
        self.label_fk_s5.setMaximumSize(QSize(16777215, 25))
        self.label_fk_s5.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_fk_s5, 8, 1, 1, 1)

        self.lcdNumber_fk_s5 = QLCDNumber(self.tab_fk_joint)
        self.lcdNumber_fk_s5.setObjectName(u"lcdNumber_fk_s5")
        self.lcdNumber_fk_s5.setMinimumSize(QSize(30, 30))
        self.lcdNumber_fk_s5.setMaximumSize(QSize(50, 50))
        self.lcdNumber_fk_s5.setFrameShape(QFrame.NoFrame)

        self.gridLayout_6.addWidget(self.lcdNumber_fk_s5, 9, 0, 1, 1)

        self.horizontalSlider_fk_s1_5 = QSlider(self.tab_fk_joint)
        self.horizontalSlider_fk_s1_5.setObjectName(u"horizontalSlider_fk_s1_5")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_fk_s1_5.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_fk_s1_5.setSizePolicy(sizePolicy8)
        self.horizontalSlider_fk_s1_5.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_fk_s1_5.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_fk_s1_5.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_fk_s1_5.setMinimum(-90)
        self.horizontalSlider_fk_s1_5.setMaximum(90)
        self.horizontalSlider_fk_s1_5.setPageStep(5)
        self.horizontalSlider_fk_s1_5.setOrientation(Qt.Horizontal)
        self.horizontalSlider_fk_s1_5.setInvertedAppearance(False)
        self.horizontalSlider_fk_s1_5.setInvertedControls(False)
        self.horizontalSlider_fk_s1_5.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_fk_s1_5.setTickInterval(10)

        self.gridLayout_6.addWidget(self.horizontalSlider_fk_s1_5, 9, 1, 1, 1)

        self.horizontalSlider_fk_s1_4 = QSlider(self.tab_fk_joint)
        self.horizontalSlider_fk_s1_4.setObjectName(u"horizontalSlider_fk_s1_4")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_fk_s1_4.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_fk_s1_4.setSizePolicy(sizePolicy8)
        self.horizontalSlider_fk_s1_4.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_fk_s1_4.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_fk_s1_4.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_fk_s1_4.setMinimum(-90)
        self.horizontalSlider_fk_s1_4.setMaximum(90)
        self.horizontalSlider_fk_s1_4.setPageStep(5)
        self.horizontalSlider_fk_s1_4.setOrientation(Qt.Horizontal)
        self.horizontalSlider_fk_s1_4.setInvertedAppearance(False)
        self.horizontalSlider_fk_s1_4.setInvertedControls(False)
        self.horizontalSlider_fk_s1_4.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_fk_s1_4.setTickInterval(10)

        self.gridLayout_6.addWidget(self.horizontalSlider_fk_s1_4, 7, 1, 1, 1)

        self.label_fk_s6 = QLabel(self.tab_fk_joint)
        self.label_fk_s6.setObjectName(u"label_fk_s6")
        sizePolicy3.setHeightForWidth(self.label_fk_s6.sizePolicy().hasHeightForWidth())
        self.label_fk_s6.setSizePolicy(sizePolicy3)
        self.label_fk_s6.setMinimumSize(QSize(150, 25))
        self.label_fk_s6.setMaximumSize(QSize(16777215, 25))
        self.label_fk_s6.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_fk_s6, 10, 1, 1, 1)

        self.horizontalSlider_fk_s1_6 = QSlider(self.tab_fk_joint)
        self.horizontalSlider_fk_s1_6.setObjectName(u"horizontalSlider_fk_s1_6")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_fk_s1_6.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_fk_s1_6.setSizePolicy(sizePolicy8)
        self.horizontalSlider_fk_s1_6.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_fk_s1_6.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_fk_s1_6.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_fk_s1_6.setMinimum(-90)
        self.horizontalSlider_fk_s1_6.setMaximum(90)
        self.horizontalSlider_fk_s1_6.setPageStep(5)
        self.horizontalSlider_fk_s1_6.setOrientation(Qt.Horizontal)
        self.horizontalSlider_fk_s1_6.setInvertedAppearance(False)
        self.horizontalSlider_fk_s1_6.setInvertedControls(False)
        self.horizontalSlider_fk_s1_6.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_fk_s1_6.setTickInterval(10)

        self.gridLayout_6.addWidget(self.horizontalSlider_fk_s1_6, 12, 1, 1, 1)

        self.lcdNumber_fk_s6 = QLCDNumber(self.tab_fk_joint)
        self.lcdNumber_fk_s6.setObjectName(u"lcdNumber_fk_s6")
        self.lcdNumber_fk_s6.setMinimumSize(QSize(30, 30))
        self.lcdNumber_fk_s6.setMaximumSize(QSize(50, 50))
        self.lcdNumber_fk_s6.setFrameShape(QFrame.NoFrame)

        self.gridLayout_6.addWidget(self.lcdNumber_fk_s6, 12, 0, 1, 1)

        self.btn_fk_reset = QPushButton(self.tab_fk_joint)
        self.btn_fk_reset.setObjectName(u"btn_fk_reset")
        sizePolicy4.setHeightForWidth(self.btn_fk_reset.sizePolicy().hasHeightForWidth())
        self.btn_fk_reset.setSizePolicy(sizePolicy4)
        self.btn_fk_reset.setMinimumSize(QSize(30, 30))
        self.btn_fk_reset.setMaximumSize(QSize(30, 30))
        self.btn_fk_reset.setFont(font3)
        self.btn_fk_reset.setLayoutDirection(Qt.LeftToRight)
        self.btn_fk_reset.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_fk_reset.setCheckable(True)
        self.btn_fk_reset.setChecked(True)

        self.gridLayout_6.addWidget(self.btn_fk_reset, 14, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(50, 25, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 9, 2, 1, 1)

        icon3 = QIcon()
        icon3.addFile(u":/16x16/16x16/icons8-robot-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_fk_joint, icon3, "")
        self.tab_fk_info = QWidget()
        self.tab_fk_info.setObjectName(u"tab_fk_info")
        self.verticalLayout_10 = QVBoxLayout(self.tab_fk_info)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_dh_rys_3 = QLabel(self.tab_fk_info)
        self.label_dh_rys_3.setObjectName(u"label_dh_rys_3")
        sizePolicy9 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_dh_rys_3.sizePolicy().hasHeightForWidth())
        self.label_dh_rys_3.setSizePolicy(sizePolicy9)
        self.label_dh_rys_3.setMinimumSize(QSize(400, 300))
        self.label_dh_rys_3.setBaseSize(QSize(440, 300))
        self.label_dh_rys_3.setPixmap(QPixmap(u":/others/others/vis_1.png"))
        self.label_dh_rys_3.setScaledContents(True)
        self.label_dh_rys_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_dh_rys_3)

        self.verticalSpacer_3 = QSpacerItem(199, 540, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        icon4 = QIcon()
        icon4.addFile(u":/16x16/16x16/icons8-view-details-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_fk_info, icon4, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_fk_input, 0, 0, 3, 1)

        self.frame_fk_results = QFrame(self.page_fk)
        self.frame_fk_results.setObjectName(u"frame_fk_results")
        sizePolicy3.setHeightForWidth(self.frame_fk_results.sizePolicy().hasHeightForWidth())
        self.frame_fk_results.setSizePolicy(sizePolicy3)
        self.frame_fk_results.setMinimumSize(QSize(440, 300))
        self.frame_fk_results.setMaximumSize(QSize(16777215, 16777215))
        self.frame_fk_results.setBaseSize(QSize(440, 300))
        self.frame_fk_results.setFrameShape(QFrame.StyledPanel)
        self.frame_fk_results.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_fk_results)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_dh_X_2 = QLabel(self.frame_fk_results)
        self.label_dh_X_2.setObjectName(u"label_dh_X_2")
        self.label_dh_X_2.setMinimumSize(QSize(100, 50))
        self.label_dh_X_2.setMaximumSize(QSize(100, 50))
        self.label_dh_X_2.setFont(font4)
        self.label_dh_X_2.setLayoutDirection(Qt.LeftToRight)
        self.label_dh_X_2.setStyleSheet(u"color: rgb(222, 222, 222);")
        self.label_dh_X_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_dh_X_2, 1, 0, 1, 1)

        self.label_dh_wynik_2 = QLabel(self.frame_fk_results)
        self.label_dh_wynik_2.setObjectName(u"label_dh_wynik_2")
        self.label_dh_wynik_2.setMinimumSize(QSize(300, 100))
        self.label_dh_wynik_2.setMaximumSize(QSize(350, 100))
        self.label_dh_wynik_2.setFont(font5)
        self.label_dh_wynik_2.setStyleSheet(u"color: rgb(222, 222, 222);")

        self.gridLayout_16.addWidget(self.label_dh_wynik_2, 0, 0, 1, 3)

        self.label_dh_Z_2 = QLabel(self.frame_fk_results)
        self.label_dh_Z_2.setObjectName(u"label_dh_Z_2")
        self.label_dh_Z_2.setMinimumSize(QSize(100, 50))
        self.label_dh_Z_2.setMaximumSize(QSize(100, 50))
        self.label_dh_Z_2.setFont(font4)
        self.label_dh_Z_2.setStyleSheet(u"color: rgb(222, 222, 222);")
        self.label_dh_Z_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_dh_Z_2, 1, 2, 1, 1)

        self.label_dh_Y_2 = QLabel(self.frame_fk_results)
        self.label_dh_Y_2.setObjectName(u"label_dh_Y_2")
        self.label_dh_Y_2.setMinimumSize(QSize(100, 50))
        self.label_dh_Y_2.setMaximumSize(QSize(100, 50))
        self.label_dh_Y_2.setFont(font4)
        self.label_dh_Y_2.setStyleSheet(u"color: rgb(222, 222, 222);")
        self.label_dh_Y_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_dh_Y_2, 1, 1, 1, 1)

        self.lcdNumber_dh_X_2 = QLCDNumber(self.frame_fk_results)
        self.lcdNumber_dh_X_2.setObjectName(u"lcdNumber_dh_X_2")
        self.lcdNumber_dh_X_2.setMinimumSize(QSize(100, 50))
        self.lcdNumber_dh_X_2.setMaximumSize(QSize(100, 50))
        self.lcdNumber_dh_X_2.setSmallDecimalPoint(False)

        self.gridLayout_16.addWidget(self.lcdNumber_dh_X_2, 2, 0, 1, 1)

        self.lcdnumber_dh_Y_2 = QLCDNumber(self.frame_fk_results)
        self.lcdnumber_dh_Y_2.setObjectName(u"lcdnumber_dh_Y_2")
        self.lcdnumber_dh_Y_2.setMinimumSize(QSize(100, 50))
        self.lcdnumber_dh_Y_2.setMaximumSize(QSize(100, 50))
        self.lcdnumber_dh_Y_2.setSmallDecimalPoint(False)

        self.gridLayout_16.addWidget(self.lcdnumber_dh_Y_2, 2, 1, 1, 1)

        self.lcdnumber_dh_Z_2 = QLCDNumber(self.frame_fk_results)
        self.lcdnumber_dh_Z_2.setObjectName(u"lcdnumber_dh_Z_2")
        self.lcdnumber_dh_Z_2.setMinimumSize(QSize(100, 50))
        self.lcdnumber_dh_Z_2.setMaximumSize(QSize(100, 50))
        self.lcdnumber_dh_Z_2.setSmallDecimalPoint(False)
        self.lcdnumber_dh_Z_2.setProperty("value", 472.000000000000000)
        self.lcdnumber_dh_Z_2.setProperty("intValue", 472)

        self.gridLayout_16.addWidget(self.lcdnumber_dh_Z_2, 2, 2, 1, 1)


        self.gridLayout_5.addWidget(self.frame_fk_results, 2, 1, 1, 1)

        self.MplWidget_fk = MplWidget(self.page_fk)
        self.MplWidget_fk.setObjectName(u"MplWidget_fk")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.MplWidget_fk.sizePolicy().hasHeightForWidth())
        self.MplWidget_fk.setSizePolicy(sizePolicy10)
        self.MplWidget_fk.setMinimumSize(QSize(440, 300))

        self.gridLayout_5.addWidget(self.MplWidget_fk, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_fk)
        self.page_ik = QWidget()
        self.page_ik.setObjectName(u"page_ik")
        self.gridLayout_11 = QGridLayout(self.page_ik)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_ik_input = QFrame(self.page_ik)
        self.frame_ik_input.setObjectName(u"frame_ik_input")
        sizePolicy4.setHeightForWidth(self.frame_ik_input.sizePolicy().hasHeightForWidth())
        self.frame_ik_input.setSizePolicy(sizePolicy4)
        self.frame_ik_input.setMinimumSize(QSize(440, 300))
        self.frame_ik_input.setLayoutDirection(Qt.LeftToRight)
        self.frame_ik_input.setFrameShape(QFrame.NoFrame)
        self.frame_ik_input.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_ik_input)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_3 = QTabWidget(self.frame_ik_input)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setTabPosition(QTabWidget.North)
        self.tabWidget_3.setTabShape(QTabWidget.Triangular)
        self.tabWidget_3.setElideMode(Qt.ElideNone)
        self.tabWidget_3.setUsesScrollButtons(False)
        self.tabWidget_3.setDocumentMode(True)
        self.tabWidget_3.setTabsClosable(False)
        self.tabWidget_3.setTabBarAutoHide(False)
        self.tab_ik_joint = QWidget()
        self.tab_ik_joint.setObjectName(u"tab_ik_joint")
        self.gridLayout_12 = QGridLayout(self.tab_ik_joint)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.lcdNumber_ik_y = QLCDNumber(self.tab_ik_joint)
        self.lcdNumber_ik_y.setObjectName(u"lcdNumber_ik_y")
        self.lcdNumber_ik_y.setMinimumSize(QSize(30, 30))
        self.lcdNumber_ik_y.setMaximumSize(QSize(50, 50))
        self.lcdNumber_ik_y.setFrameShape(QFrame.NoFrame)

        self.gridLayout_12.addWidget(self.lcdNumber_ik_y, 3, 0, 1, 1)

        self.label_ik_z = QLabel(self.tab_ik_joint)
        self.label_ik_z.setObjectName(u"label_ik_z")
        sizePolicy3.setHeightForWidth(self.label_ik_z.sizePolicy().hasHeightForWidth())
        self.label_ik_z.setSizePolicy(sizePolicy3)
        self.label_ik_z.setMinimumSize(QSize(150, 25))
        self.label_ik_z.setMaximumSize(QSize(16777215, 25))
        self.label_ik_z.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_ik_z, 4, 1, 1, 1)

        self.label_ik_y = QLabel(self.tab_ik_joint)
        self.label_ik_y.setObjectName(u"label_ik_y")
        sizePolicy3.setHeightForWidth(self.label_ik_y.sizePolicy().hasHeightForWidth())
        self.label_ik_y.setSizePolicy(sizePolicy3)
        self.label_ik_y.setMinimumSize(QSize(150, 25))
        self.label_ik_y.setMaximumSize(QSize(16777215, 25))
        self.label_ik_y.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_ik_y, 2, 1, 1, 1)

        self.horizontalSlider_ik_z = QSlider(self.tab_ik_joint)
        self.horizontalSlider_ik_z.setObjectName(u"horizontalSlider_ik_z")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_ik_z.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_ik_z.setSizePolicy(sizePolicy8)
        self.horizontalSlider_ik_z.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_ik_z.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_ik_z.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_ik_z.setMinimum(-472)
        self.horizontalSlider_ik_z.setMaximum(472)
        self.horizontalSlider_ik_z.setPageStep(5)
        self.horizontalSlider_ik_z.setValue(472)
        self.horizontalSlider_ik_z.setSliderPosition(472)
        self.horizontalSlider_ik_z.setOrientation(Qt.Horizontal)
        self.horizontalSlider_ik_z.setInvertedAppearance(False)
        self.horizontalSlider_ik_z.setInvertedControls(False)
        self.horizontalSlider_ik_z.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_ik_z.setTickInterval(10)

        self.gridLayout_12.addWidget(self.horizontalSlider_ik_z, 5, 1, 1, 1)

        self.label_ik_orient = QLabel(self.tab_ik_joint)
        self.label_ik_orient.setObjectName(u"label_ik_orient")
        sizePolicy3.setHeightForWidth(self.label_ik_orient.sizePolicy().hasHeightForWidth())
        self.label_ik_orient.setSizePolicy(sizePolicy3)
        self.label_ik_orient.setMinimumSize(QSize(200, 25))
        self.label_ik_orient.setMaximumSize(QSize(16777215, 25))
        self.label_ik_orient.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_ik_orient, 6, 1, 1, 1)

        self.horizontalSlider_ik_y = QSlider(self.tab_ik_joint)
        self.horizontalSlider_ik_y.setObjectName(u"horizontalSlider_ik_y")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_ik_y.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_ik_y.setSizePolicy(sizePolicy8)
        self.horizontalSlider_ik_y.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_ik_y.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_ik_y.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_ik_y.setMinimum(-472)
        self.horizontalSlider_ik_y.setMaximum(472)
        self.horizontalSlider_ik_y.setPageStep(5)
        self.horizontalSlider_ik_y.setOrientation(Qt.Horizontal)
        self.horizontalSlider_ik_y.setInvertedAppearance(False)
        self.horizontalSlider_ik_y.setInvertedControls(False)
        self.horizontalSlider_ik_y.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_ik_y.setTickInterval(10)

        self.gridLayout_12.addWidget(self.horizontalSlider_ik_y, 3, 1, 1, 1)

        self.verticalSlider = QSlider(self.tab_ik_joint)
        self.verticalSlider.setObjectName(u"verticalSlider")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy11)
        self.verticalSlider.setMinimumSize(QSize(0, 200))
        self.verticalSlider.setMaximumSize(QSize(16777215, 400))
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical {\n"
"    border-radius: 9px;  \n"
"	widtht: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.verticalSlider.setMinimum(-90)
        self.verticalSlider.setMaximum(90)
        self.verticalSlider.setPageStep(5)
        self.verticalSlider.setSliderPosition(90)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(True)
        self.verticalSlider.setInvertedControls(True)

        self.gridLayout_12.addWidget(self.verticalSlider, 6, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(50, 25, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_3, 5, 3, 1, 1)

        self.horizontalSlider_ik_x = QSlider(self.tab_ik_joint)
        self.horizontalSlider_ik_x.setObjectName(u"horizontalSlider_ik_x")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_ik_x.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_ik_x.setSizePolicy(sizePolicy8)
        self.horizontalSlider_ik_x.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_ik_x.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_ik_x.setLayoutDirection(Qt.LeftToRight)
        self.horizontalSlider_ik_x.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_ik_x.setMinimum(-472)
        self.horizontalSlider_ik_x.setMaximum(472)
        self.horizontalSlider_ik_x.setPageStep(5)
        self.horizontalSlider_ik_x.setOrientation(Qt.Horizontal)
        self.horizontalSlider_ik_x.setInvertedAppearance(False)
        self.horizontalSlider_ik_x.setInvertedControls(False)
        self.horizontalSlider_ik_x.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_ik_x.setTickInterval(10)

        self.gridLayout_12.addWidget(self.horizontalSlider_ik_x, 1, 1, 1, 1)

        self.lcdNumber_ik_z = QLCDNumber(self.tab_ik_joint)
        self.lcdNumber_ik_z.setObjectName(u"lcdNumber_ik_z")
        self.lcdNumber_ik_z.setMinimumSize(QSize(30, 30))
        self.lcdNumber_ik_z.setMaximumSize(QSize(50, 50))
        self.lcdNumber_ik_z.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_ik_z.setProperty("value", 472.000000000000000)

        self.gridLayout_12.addWidget(self.lcdNumber_ik_z, 5, 0, 1, 1)

        self.lcdNumber_ik_orient = QLCDNumber(self.tab_ik_joint)
        self.lcdNumber_ik_orient.setObjectName(u"lcdNumber_ik_orient")
        self.lcdNumber_ik_orient.setMinimumSize(QSize(30, 30))
        self.lcdNumber_ik_orient.setMaximumSize(QSize(50, 50))
        self.lcdNumber_ik_orient.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_ik_orient.setProperty("value", 90.000000000000000)

        self.gridLayout_12.addWidget(self.lcdNumber_ik_orient, 6, 0, 1, 1)

        self.lcdNumber_ik_x = QLCDNumber(self.tab_ik_joint)
        self.lcdNumber_ik_x.setObjectName(u"lcdNumber_ik_x")
        self.lcdNumber_ik_x.setMinimumSize(QSize(30, 30))
        self.lcdNumber_ik_x.setMaximumSize(QSize(50, 50))
        self.lcdNumber_ik_x.setFont(font6)
        self.lcdNumber_ik_x.setStyleSheet(u"QLCDNumber{\n"
"  border: none;\n"
"  color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_12.addWidget(self.lcdNumber_ik_x, 1, 0, 1, 1)

        self.label_ik_x = QLabel(self.tab_ik_joint)
        self.label_ik_x.setObjectName(u"label_ik_x")
        sizePolicy3.setHeightForWidth(self.label_ik_x.sizePolicy().hasHeightForWidth())
        self.label_ik_x.setSizePolicy(sizePolicy3)
        self.label_ik_x.setMinimumSize(QSize(150, 25))
        self.label_ik_x.setMaximumSize(QSize(16777215, 25))
        self.label_ik_x.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_ik_x, 0, 1, 1, 1)

        self.btn_ik_reset = QPushButton(self.tab_ik_joint)
        self.btn_ik_reset.setObjectName(u"btn_ik_reset")
        sizePolicy4.setHeightForWidth(self.btn_ik_reset.sizePolicy().hasHeightForWidth())
        self.btn_ik_reset.setSizePolicy(sizePolicy4)
        self.btn_ik_reset.setMinimumSize(QSize(30, 30))
        self.btn_ik_reset.setMaximumSize(QSize(30, 30))
        self.btn_ik_reset.setFont(font3)
        self.btn_ik_reset.setLayoutDirection(Qt.LeftToRight)
        self.btn_ik_reset.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_ik_reset.setCheckable(True)
        self.btn_ik_reset.setChecked(True)

        self.gridLayout_12.addWidget(self.btn_ik_reset, 7, 3, 1, 1)

        self.tabWidget_3.addTab(self.tab_ik_joint, icon3, "")
        self.tab_fk_info_3 = QWidget()
        self.tab_fk_info_3.setObjectName(u"tab_fk_info_3")
        self.gridLayout_10 = QGridLayout(self.tab_fk_info_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_dh_rys_5 = QLabel(self.tab_fk_info_3)
        self.label_dh_rys_5.setObjectName(u"label_dh_rys_5")
        sizePolicy9.setHeightForWidth(self.label_dh_rys_5.sizePolicy().hasHeightForWidth())
        self.label_dh_rys_5.setSizePolicy(sizePolicy9)
        self.label_dh_rys_5.setMinimumSize(QSize(400, 300))
        self.label_dh_rys_5.setBaseSize(QSize(440, 300))
        self.label_dh_rys_5.setPixmap(QPixmap(u":/others/others/vis_1.png"))
        self.label_dh_rys_5.setScaledContents(True)
        self.label_dh_rys_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_dh_rys_5, 0, 0, 1, 2)

        self.label_ik_efektor_2 = QLabel(self.tab_fk_info_3)
        self.label_ik_efektor_2.setObjectName(u"label_ik_efektor_2")
        self.label_ik_efektor_2.setMinimumSize(QSize(250, 150))
        self.label_ik_efektor_2.setMaximumSize(QSize(250, 150))
        self.label_ik_efektor_2.setPixmap(QPixmap(u":/others/others/vis_orientaction.png"))
        self.label_ik_efektor_2.setScaledContents(True)
        self.label_ik_efektor_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_ik_efektor_2, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(199, 200, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.verticalSpacer_5, 1, 1, 1, 1)

        self.tabWidget_3.addTab(self.tab_fk_info_3, icon4, "")

        self.gridLayout_9.addWidget(self.tabWidget_3, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_ik_input, 0, 0, 2, 1)

        self.MplWidget_ik = MplWidget(self.page_ik)
        self.MplWidget_ik.setObjectName(u"MplWidget_ik")
        sizePolicy10.setHeightForWidth(self.MplWidget_ik.sizePolicy().hasHeightForWidth())
        self.MplWidget_ik.setSizePolicy(sizePolicy10)
        self.MplWidget_ik.setMinimumSize(QSize(440, 300))

        self.gridLayout_11.addWidget(self.MplWidget_ik, 0, 1, 1, 1)

        self.frame_ik_results = QFrame(self.page_ik)
        self.frame_ik_results.setObjectName(u"frame_ik_results")
        sizePolicy3.setHeightForWidth(self.frame_ik_results.sizePolicy().hasHeightForWidth())
        self.frame_ik_results.setSizePolicy(sizePolicy3)
        self.frame_ik_results.setMinimumSize(QSize(440, 300))
        self.frame_ik_results.setMaximumSize(QSize(16777215, 16777215))
        self.frame_ik_results.setBaseSize(QSize(440, 300))
        self.frame_ik_results.setFrameShape(QFrame.StyledPanel)
        self.frame_ik_results.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_ik_results)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_4 = QTabWidget(self.frame_ik_results)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        sizePolicy3.setHeightForWidth(self.tabWidget_4.sizePolicy().hasHeightForWidth())
        self.tabWidget_4.setSizePolicy(sizePolicy3)
        self.tabWidget_4.setMinimumSize(QSize(440, 300))
        self.tabWidget_4.setTabPosition(QTabWidget.North)
        self.tabWidget_4.setTabShape(QTabWidget.Triangular)
        self.tabWidget_4.setUsesScrollButtons(False)
        self.tabWidget_4.setDocumentMode(True)
        self.config1 = QWidget()
        self.config1.setObjectName(u"config1")
        self.gridLayout_13 = QGridLayout(self.config1)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.lcdNumber_ik_s1 = QLCDNumber(self.config1)
        self.lcdNumber_ik_s1.setObjectName(u"lcdNumber_ik_s1")
        self.lcdNumber_ik_s1.setMinimumSize(QSize(50, 50))
        self.lcdNumber_ik_s1.setMaximumSize(QSize(50, 50))

        self.gridLayout_13.addWidget(self.lcdNumber_ik_s1, 1, 0, 1, 1)

        self.label_s1_ik = QLabel(self.config1)
        self.label_s1_ik.setObjectName(u"label_s1_ik")
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.label_s1_ik.sizePolicy().hasHeightForWidth())
        self.label_s1_ik.setSizePolicy(sizePolicy12)
        self.label_s1_ik.setMinimumSize(QSize(150, 25))
        self.label_s1_ik.setMaximumSize(QSize(16777215, 25))
        self.label_s1_ik.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_s1_ik, 1, 1, 1, 1)

        self.label_ik_1 = QLabel(self.config1)
        self.label_ik_1.setObjectName(u"label_ik_1")
        self.label_ik_1.setMinimumSize(QSize(300, 50))
        self.label_ik_1.setMaximumSize(QSize(350, 100))
        self.label_ik_1.setFont(font5)
        self.label_ik_1.setStyleSheet(u"color: rgb(222, 222, 222);")

        self.gridLayout_13.addWidget(self.label_ik_1, 0, 0, 1, 3)

        self.label_s2_ik = QLabel(self.config1)
        self.label_s2_ik.setObjectName(u"label_s2_ik")
        sizePolicy12.setHeightForWidth(self.label_s2_ik.sizePolicy().hasHeightForWidth())
        self.label_s2_ik.setSizePolicy(sizePolicy12)
        self.label_s2_ik.setMinimumSize(QSize(150, 25))
        self.label_s2_ik.setMaximumSize(QSize(16777215, 25))
        self.label_s2_ik.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_s2_ik, 1, 2, 1, 1)

        self.label_s3_ik = QLabel(self.config1)
        self.label_s3_ik.setObjectName(u"label_s3_ik")
        sizePolicy12.setHeightForWidth(self.label_s3_ik.sizePolicy().hasHeightForWidth())
        self.label_s3_ik.setSizePolicy(sizePolicy12)
        self.label_s3_ik.setMinimumSize(QSize(150, 25))
        self.label_s3_ik.setMaximumSize(QSize(16777215, 25))
        self.label_s3_ik.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_s3_ik, 2, 1, 1, 1)

        self.lcdNumber_ik_s3 = QLCDNumber(self.config1)
        self.lcdNumber_ik_s3.setObjectName(u"lcdNumber_ik_s3")
        self.lcdNumber_ik_s3.setMinimumSize(QSize(50, 50))
        self.lcdNumber_ik_s3.setMaximumSize(QSize(50, 50))

        self.gridLayout_13.addWidget(self.lcdNumber_ik_s3, 2, 0, 1, 1)

        self.lcdNumber_ik_s2 = QLCDNumber(self.config1)
        self.lcdNumber_ik_s2.setObjectName(u"lcdNumber_ik_s2")
        self.lcdNumber_ik_s2.setMinimumSize(QSize(50, 50))
        self.lcdNumber_ik_s2.setMaximumSize(QSize(50, 50))
        self.lcdNumber_ik_s2.setSmallDecimalPoint(False)

        self.gridLayout_13.addWidget(self.lcdNumber_ik_s2, 1, 3, 1, 1)

        self.lcdNumber_ik_s4 = QLCDNumber(self.config1)
        self.lcdNumber_ik_s4.setObjectName(u"lcdNumber_ik_s4")
        self.lcdNumber_ik_s4.setMinimumSize(QSize(50, 50))
        self.lcdNumber_ik_s4.setMaximumSize(QSize(50, 50))

        self.gridLayout_13.addWidget(self.lcdNumber_ik_s4, 2, 3, 1, 1)

        self.label_s4_ik = QLabel(self.config1)
        self.label_s4_ik.setObjectName(u"label_s4_ik")
        sizePolicy12.setHeightForWidth(self.label_s4_ik.sizePolicy().hasHeightForWidth())
        self.label_s4_ik.setSizePolicy(sizePolicy12)
        self.label_s4_ik.setMinimumSize(QSize(150, 25))
        self.label_s4_ik.setMaximumSize(QSize(16777215, 25))
        self.label_s4_ik.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_s4_ik, 2, 2, 1, 1)

        self.btn_ik_reload_1 = QPushButton(self.config1)
        self.btn_ik_reload_1.setObjectName(u"btn_ik_reload_1")
        sizePolicy4.setHeightForWidth(self.btn_ik_reload_1.sizePolicy().hasHeightForWidth())
        self.btn_ik_reload_1.setSizePolicy(sizePolicy4)
        self.btn_ik_reload_1.setMinimumSize(QSize(30, 30))
        self.btn_ik_reload_1.setMaximumSize(QSize(30, 30))
        self.btn_ik_reload_1.setFont(font3)
        self.btn_ik_reload_1.setLayoutDirection(Qt.LeftToRight)
        self.btn_ik_reload_1.setAutoFillBackground(False)
        self.btn_ik_reload_1.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"	image: url(:/16x16/16x16/icons8-replace-50.png);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_ik_reload_1.setCheckable(True)
        self.btn_ik_reload_1.setChecked(True)

        self.gridLayout_13.addWidget(self.btn_ik_reload_1, 0, 3, 1, 1)

        self.tabWidget_4.addTab(self.config1, "")
        self.config2 = QWidget()
        self.config2.setObjectName(u"config2")
        self.gridLayout_14 = QGridLayout(self.config2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_ik_2 = QLabel(self.config2)
        self.label_ik_2.setObjectName(u"label_ik_2")
        self.label_ik_2.setMinimumSize(QSize(300, 50))
        self.label_ik_2.setMaximumSize(QSize(350, 100))
        self.label_ik_2.setFont(font5)
        self.label_ik_2.setStyleSheet(u"color: rgb(222, 222, 222);")

        self.gridLayout_14.addWidget(self.label_ik_2, 0, 0, 1, 3)

        self.lcdNumber_ik_s1_2 = QLCDNumber(self.config2)
        self.lcdNumber_ik_s1_2.setObjectName(u"lcdNumber_ik_s1_2")
        self.lcdNumber_ik_s1_2.setMinimumSize(QSize(50, 50))
        self.lcdNumber_ik_s1_2.setMaximumSize(QSize(50, 50))

        self.gridLayout_14.addWidget(self.lcdNumber_ik_s1_2, 2, 0, 1, 1)

        self.label_s1_ik_2 = QLabel(self.config2)
        self.label_s1_ik_2.setObjectName(u"label_s1_ik_2")
        sizePolicy12.setHeightForWidth(self.label_s1_ik_2.sizePolicy().hasHeightForWidth())
        self.label_s1_ik_2.setSizePolicy(sizePolicy12)
        self.label_s1_ik_2.setMinimumSize(QSize(150, 25))
        self.label_s1_ik_2.setMaximumSize(QSize(16777215, 25))
        self.label_s1_ik_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_s1_ik_2, 2, 1, 1, 1)

        self.label_s2_ik_2 = QLabel(self.config2)
        self.label_s2_ik_2.setObjectName(u"label_s2_ik_2")
        sizePolicy12.setHeightForWidth(self.label_s2_ik_2.sizePolicy().hasHeightForWidth())
        self.label_s2_ik_2.setSizePolicy(sizePolicy12)
        self.label_s2_ik_2.setMinimumSize(QSize(150, 25))
        self.label_s2_ik_2.setMaximumSize(QSize(16777215, 25))
        self.label_s2_ik_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_s2_ik_2, 2, 2, 1, 1)

        self.lcdNumber_ik_s2_2 = QLCDNumber(self.config2)
        self.lcdNumber_ik_s2_2.setObjectName(u"lcdNumber_ik_s2_2")
        self.lcdNumber_ik_s2_2.setMinimumSize(QSize(50, 50))
        self.lcdNumber_ik_s2_2.setMaximumSize(QSize(50, 50))
        self.lcdNumber_ik_s2_2.setSmallDecimalPoint(False)

        self.gridLayout_14.addWidget(self.lcdNumber_ik_s2_2, 2, 3, 1, 1)

        self.lcdNumber_ik_s3_2 = QLCDNumber(self.config2)
        self.lcdNumber_ik_s3_2.setObjectName(u"lcdNumber_ik_s3_2")
        self.lcdNumber_ik_s3_2.setMinimumSize(QSize(50, 50))
        self.lcdNumber_ik_s3_2.setMaximumSize(QSize(50, 50))

        self.gridLayout_14.addWidget(self.lcdNumber_ik_s3_2, 3, 0, 1, 1)

        self.label_s3_ik_2 = QLabel(self.config2)
        self.label_s3_ik_2.setObjectName(u"label_s3_ik_2")
        sizePolicy12.setHeightForWidth(self.label_s3_ik_2.sizePolicy().hasHeightForWidth())
        self.label_s3_ik_2.setSizePolicy(sizePolicy12)
        self.label_s3_ik_2.setMinimumSize(QSize(150, 25))
        self.label_s3_ik_2.setMaximumSize(QSize(16777215, 25))
        self.label_s3_ik_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_s3_ik_2, 3, 1, 1, 1)

        self.label_s4_ik_2 = QLabel(self.config2)
        self.label_s4_ik_2.setObjectName(u"label_s4_ik_2")
        sizePolicy12.setHeightForWidth(self.label_s4_ik_2.sizePolicy().hasHeightForWidth())
        self.label_s4_ik_2.setSizePolicy(sizePolicy12)
        self.label_s4_ik_2.setMinimumSize(QSize(150, 25))
        self.label_s4_ik_2.setMaximumSize(QSize(16777215, 25))
        self.label_s4_ik_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_s4_ik_2, 3, 2, 1, 1)

        self.lcdNumber_ik_s4_2 = QLCDNumber(self.config2)
        self.lcdNumber_ik_s4_2.setObjectName(u"lcdNumber_ik_s4_2")
        self.lcdNumber_ik_s4_2.setMinimumSize(QSize(50, 50))
        self.lcdNumber_ik_s4_2.setMaximumSize(QSize(50, 50))

        self.gridLayout_14.addWidget(self.lcdNumber_ik_s4_2, 3, 3, 1, 1)

        self.btn_ik_reload_2 = QPushButton(self.config2)
        self.btn_ik_reload_2.setObjectName(u"btn_ik_reload_2")
        sizePolicy4.setHeightForWidth(self.btn_ik_reload_2.sizePolicy().hasHeightForWidth())
        self.btn_ik_reload_2.setSizePolicy(sizePolicy4)
        self.btn_ik_reload_2.setMinimumSize(QSize(30, 30))
        self.btn_ik_reload_2.setMaximumSize(QSize(30, 30))
        self.btn_ik_reload_2.setFont(font3)
        self.btn_ik_reload_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_ik_reload_2.setAutoFillBackground(False)
        self.btn_ik_reload_2.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"	image: url(:/16x16/16x16/icons8-replace-50.png);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_ik_reload_2.setCheckable(True)
        self.btn_ik_reload_2.setChecked(True)

        self.gridLayout_14.addWidget(self.btn_ik_reload_2, 0, 3, 1, 1)

        self.tabWidget_4.addTab(self.config2, "")

        self.gridLayout_18.addWidget(self.tabWidget_4, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_ik_results, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_ik)
        self.page_manual = QWidget()
        self.page_manual.setObjectName(u"page_manual")
        self.gridLayout_15 = QGridLayout(self.page_manual)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_manual_input = QFrame(self.page_manual)
        self.frame_manual_input.setObjectName(u"frame_manual_input")
        sizePolicy3.setHeightForWidth(self.frame_manual_input.sizePolicy().hasHeightForWidth())
        self.frame_manual_input.setSizePolicy(sizePolicy3)
        self.frame_manual_input.setMinimumSize(QSize(440, 0))
        self.frame_manual_input.setFrameShape(QFrame.NoFrame)
        self.frame_manual_input.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_manual_input)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_5 = QTabWidget(self.frame_manual_input)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tabWidget_5.setTabPosition(QTabWidget.North)
        self.tabWidget_5.setTabShape(QTabWidget.Triangular)
        self.tabWidget_5.setElideMode(Qt.ElideNone)
        self.tabWidget_5.setUsesScrollButtons(False)
        self.tabWidget_5.setDocumentMode(True)
        self.tabWidget_5.setTabsClosable(False)
        self.tabWidget_5.setTabBarAutoHide(False)
        self.tab_manual_joints = QWidget()
        self.tab_manual_joints.setObjectName(u"tab_manual_joints")
        self.gridLayout_17 = QGridLayout(self.tab_manual_joints)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_j_s1 = QLabel(self.tab_manual_joints)
        self.label_j_s1.setObjectName(u"label_j_s1")
        sizePolicy3.setHeightForWidth(self.label_j_s1.sizePolicy().hasHeightForWidth())
        self.label_j_s1.setSizePolicy(sizePolicy3)
        self.label_j_s1.setMinimumSize(QSize(150, 25))
        self.label_j_s1.setMaximumSize(QSize(16777215, 25))
        self.label_j_s1.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_j_s1, 0, 1, 1, 1)

        self.lcdNumber_j_s1 = QLCDNumber(self.tab_manual_joints)
        self.lcdNumber_j_s1.setObjectName(u"lcdNumber_j_s1")
        self.lcdNumber_j_s1.setMinimumSize(QSize(30, 30))
        self.lcdNumber_j_s1.setMaximumSize(QSize(50, 50))
        self.lcdNumber_j_s1.setFont(font6)
        self.lcdNumber_j_s1.setStyleSheet(u"QLCDNumber{\n"
"  border: none;\n"
"  color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_17.addWidget(self.lcdNumber_j_s1, 1, 0, 1, 1)

        self.horizontalSlider_j_s1 = QSlider(self.tab_manual_joints)
        self.horizontalSlider_j_s1.setObjectName(u"horizontalSlider_j_s1")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_j_s1.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_j_s1.setSizePolicy(sizePolicy8)
        self.horizontalSlider_j_s1.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_j_s1.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_j_s1.setLayoutDirection(Qt.LeftToRight)
        self.horizontalSlider_j_s1.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_j_s1.setMinimum(-90)
        self.horizontalSlider_j_s1.setMaximum(90)
        self.horizontalSlider_j_s1.setPageStep(5)
        self.horizontalSlider_j_s1.setOrientation(Qt.Horizontal)
        self.horizontalSlider_j_s1.setInvertedAppearance(False)
        self.horizontalSlider_j_s1.setInvertedControls(False)
        self.horizontalSlider_j_s1.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_j_s1.setTickInterval(10)

        self.gridLayout_17.addWidget(self.horizontalSlider_j_s1, 1, 1, 1, 1)

        self.label_j_s2 = QLabel(self.tab_manual_joints)
        self.label_j_s2.setObjectName(u"label_j_s2")
        sizePolicy3.setHeightForWidth(self.label_j_s2.sizePolicy().hasHeightForWidth())
        self.label_j_s2.setSizePolicy(sizePolicy3)
        self.label_j_s2.setMinimumSize(QSize(150, 25))
        self.label_j_s2.setMaximumSize(QSize(16777215, 25))
        self.label_j_s2.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_j_s2, 2, 1, 1, 1)

        self.lcdNumber_j_s2 = QLCDNumber(self.tab_manual_joints)
        self.lcdNumber_j_s2.setObjectName(u"lcdNumber_j_s2")
        self.lcdNumber_j_s2.setMinimumSize(QSize(30, 30))
        self.lcdNumber_j_s2.setMaximumSize(QSize(50, 50))
        self.lcdNumber_j_s2.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_j_s2.setProperty("value", 90.000000000000000)

        self.gridLayout_17.addWidget(self.lcdNumber_j_s2, 3, 0, 1, 1)

        self.horizontalSlider_j_s2 = QSlider(self.tab_manual_joints)
        self.horizontalSlider_j_s2.setObjectName(u"horizontalSlider_j_s2")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_j_s2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_j_s2.setSizePolicy(sizePolicy8)
        self.horizontalSlider_j_s2.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_j_s2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_j_s2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_j_s2.setMinimum(0)
        self.horizontalSlider_j_s2.setMaximum(180)
        self.horizontalSlider_j_s2.setPageStep(5)
        self.horizontalSlider_j_s2.setSliderPosition(90)
        self.horizontalSlider_j_s2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_j_s2.setInvertedAppearance(False)
        self.horizontalSlider_j_s2.setInvertedControls(False)
        self.horizontalSlider_j_s2.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_j_s2.setTickInterval(10)

        self.gridLayout_17.addWidget(self.horizontalSlider_j_s2, 3, 1, 1, 1)

        self.label_j_s3 = QLabel(self.tab_manual_joints)
        self.label_j_s3.setObjectName(u"label_j_s3")
        sizePolicy3.setHeightForWidth(self.label_j_s3.sizePolicy().hasHeightForWidth())
        self.label_j_s3.setSizePolicy(sizePolicy3)
        self.label_j_s3.setMinimumSize(QSize(150, 25))
        self.label_j_s3.setMaximumSize(QSize(16777215, 25))
        self.label_j_s3.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_j_s3, 4, 1, 1, 1)

        self.lcdNumber_j_s3 = QLCDNumber(self.tab_manual_joints)
        self.lcdNumber_j_s3.setObjectName(u"lcdNumber_j_s3")
        self.lcdNumber_j_s3.setMinimumSize(QSize(30, 30))
        self.lcdNumber_j_s3.setMaximumSize(QSize(50, 50))
        self.lcdNumber_j_s3.setFrameShape(QFrame.NoFrame)

        self.gridLayout_17.addWidget(self.lcdNumber_j_s3, 5, 0, 1, 1)

        self.horizontalSlider_j_s3 = QSlider(self.tab_manual_joints)
        self.horizontalSlider_j_s3.setObjectName(u"horizontalSlider_j_s3")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_j_s3.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_j_s3.setSizePolicy(sizePolicy8)
        self.horizontalSlider_j_s3.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_j_s3.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_j_s3.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_j_s3.setMinimum(-90)
        self.horizontalSlider_j_s3.setMaximum(90)
        self.horizontalSlider_j_s3.setPageStep(5)
        self.horizontalSlider_j_s3.setOrientation(Qt.Horizontal)
        self.horizontalSlider_j_s3.setInvertedAppearance(False)
        self.horizontalSlider_j_s3.setInvertedControls(False)
        self.horizontalSlider_j_s3.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_j_s3.setTickInterval(10)

        self.gridLayout_17.addWidget(self.horizontalSlider_j_s3, 5, 1, 1, 1)

        self.label_j_s4 = QLabel(self.tab_manual_joints)
        self.label_j_s4.setObjectName(u"label_j_s4")
        sizePolicy3.setHeightForWidth(self.label_j_s4.sizePolicy().hasHeightForWidth())
        self.label_j_s4.setSizePolicy(sizePolicy3)
        self.label_j_s4.setMinimumSize(QSize(150, 25))
        self.label_j_s4.setMaximumSize(QSize(16777215, 25))
        self.label_j_s4.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_j_s4, 6, 1, 1, 1)

        self.lcdNumber_j_s4 = QLCDNumber(self.tab_manual_joints)
        self.lcdNumber_j_s4.setObjectName(u"lcdNumber_j_s4")
        self.lcdNumber_j_s4.setMinimumSize(QSize(30, 30))
        self.lcdNumber_j_s4.setMaximumSize(QSize(50, 50))
        self.lcdNumber_j_s4.setFrameShape(QFrame.NoFrame)

        self.gridLayout_17.addWidget(self.lcdNumber_j_s4, 7, 0, 1, 1)

        self.horizontalSlider_j_s4 = QSlider(self.tab_manual_joints)
        self.horizontalSlider_j_s4.setObjectName(u"horizontalSlider_j_s4")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_j_s4.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_j_s4.setSizePolicy(sizePolicy8)
        self.horizontalSlider_j_s4.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_j_s4.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_j_s4.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_j_s4.setMinimum(-90)
        self.horizontalSlider_j_s4.setMaximum(90)
        self.horizontalSlider_j_s4.setPageStep(5)
        self.horizontalSlider_j_s4.setOrientation(Qt.Horizontal)
        self.horizontalSlider_j_s4.setInvertedAppearance(False)
        self.horizontalSlider_j_s4.setInvertedControls(False)
        self.horizontalSlider_j_s4.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_j_s4.setTickInterval(10)

        self.gridLayout_17.addWidget(self.horizontalSlider_j_s4, 7, 1, 1, 1)

        self.label_j_s5 = QLabel(self.tab_manual_joints)
        self.label_j_s5.setObjectName(u"label_j_s5")
        sizePolicy3.setHeightForWidth(self.label_j_s5.sizePolicy().hasHeightForWidth())
        self.label_j_s5.setSizePolicy(sizePolicy3)
        self.label_j_s5.setMinimumSize(QSize(150, 25))
        self.label_j_s5.setMaximumSize(QSize(16777215, 25))
        self.label_j_s5.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_j_s5, 8, 1, 1, 1)

        self.lcdNumber_j_s5 = QLCDNumber(self.tab_manual_joints)
        self.lcdNumber_j_s5.setObjectName(u"lcdNumber_j_s5")
        self.lcdNumber_j_s5.setMinimumSize(QSize(30, 30))
        self.lcdNumber_j_s5.setMaximumSize(QSize(50, 50))
        self.lcdNumber_j_s5.setFrameShape(QFrame.NoFrame)

        self.gridLayout_17.addWidget(self.lcdNumber_j_s5, 9, 0, 1, 1)

        self.horizontalSlider_j_s5 = QSlider(self.tab_manual_joints)
        self.horizontalSlider_j_s5.setObjectName(u"horizontalSlider_j_s5")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_j_s5.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_j_s5.setSizePolicy(sizePolicy8)
        self.horizontalSlider_j_s5.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_j_s5.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_j_s5.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_j_s5.setMinimum(0)
        self.horizontalSlider_j_s5.setMaximum(180)
        self.horizontalSlider_j_s5.setPageStep(5)
        self.horizontalSlider_j_s5.setValue(90)
        self.horizontalSlider_j_s5.setOrientation(Qt.Horizontal)
        self.horizontalSlider_j_s5.setInvertedAppearance(False)
        self.horizontalSlider_j_s5.setInvertedControls(False)
        self.horizontalSlider_j_s5.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_j_s5.setTickInterval(10)

        self.gridLayout_17.addWidget(self.horizontalSlider_j_s5, 9, 1, 1, 1)

        self.label_j_s6 = QLabel(self.tab_manual_joints)
        self.label_j_s6.setObjectName(u"label_j_s6")
        sizePolicy3.setHeightForWidth(self.label_j_s6.sizePolicy().hasHeightForWidth())
        self.label_j_s6.setSizePolicy(sizePolicy3)
        self.label_j_s6.setMinimumSize(QSize(150, 25))
        self.label_j_s6.setMaximumSize(QSize(16777215, 25))
        self.label_j_s6.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_j_s6, 10, 1, 1, 1)

        self.lcdNumber_j_s6 = QLCDNumber(self.tab_manual_joints)
        self.lcdNumber_j_s6.setObjectName(u"lcdNumber_j_s6")
        self.lcdNumber_j_s6.setMinimumSize(QSize(30, 30))
        self.lcdNumber_j_s6.setMaximumSize(QSize(50, 50))
        self.lcdNumber_j_s6.setFrameShape(QFrame.NoFrame)

        self.gridLayout_17.addWidget(self.lcdNumber_j_s6, 11, 0, 1, 1)

        self.horizontalSlider_j_s6 = QSlider(self.tab_manual_joints)
        self.horizontalSlider_j_s6.setObjectName(u"horizontalSlider_j_s6")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_j_s6.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_j_s6.setSizePolicy(sizePolicy8)
        self.horizontalSlider_j_s6.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_j_s6.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_j_s6.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_j_s6.setMinimum(0)
        self.horizontalSlider_j_s6.setMaximum(180)
        self.horizontalSlider_j_s6.setPageStep(5)
        self.horizontalSlider_j_s6.setValue(90)
        self.horizontalSlider_j_s6.setOrientation(Qt.Horizontal)
        self.horizontalSlider_j_s6.setInvertedAppearance(False)
        self.horizontalSlider_j_s6.setInvertedControls(False)
        self.horizontalSlider_j_s6.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_j_s6.setTickInterval(10)

        self.gridLayout_17.addWidget(self.horizontalSlider_j_s6, 11, 1, 1, 1)

        self.btn_manual_reset_1 = QPushButton(self.tab_manual_joints)
        self.btn_manual_reset_1.setObjectName(u"btn_manual_reset_1")
        sizePolicy4.setHeightForWidth(self.btn_manual_reset_1.sizePolicy().hasHeightForWidth())
        self.btn_manual_reset_1.setSizePolicy(sizePolicy4)
        self.btn_manual_reset_1.setMinimumSize(QSize(30, 30))
        self.btn_manual_reset_1.setMaximumSize(QSize(30, 30))
        self.btn_manual_reset_1.setFont(font3)
        self.btn_manual_reset_1.setLayoutDirection(Qt.LeftToRight)
        self.btn_manual_reset_1.setAutoFillBackground(False)
        self.btn_manual_reset_1.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_manual_reset_1.setCheckable(True)
        self.btn_manual_reset_1.setChecked(True)

        self.gridLayout_17.addWidget(self.btn_manual_reset_1, 12, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(50, 25, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_5, 9, 2, 1, 1)

        self.tabWidget_5.addTab(self.tab_manual_joints, icon3, "")
        self.tab_manual_xyz = QWidget()
        self.tab_manual_xyz.setObjectName(u"tab_manual_xyz")
        self.gridLayout_8 = QGridLayout(self.tab_manual_xyz)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_manual_x = QLabel(self.tab_manual_xyz)
        self.label_manual_x.setObjectName(u"label_manual_x")
        sizePolicy3.setHeightForWidth(self.label_manual_x.sizePolicy().hasHeightForWidth())
        self.label_manual_x.setSizePolicy(sizePolicy3)
        self.label_manual_x.setMinimumSize(QSize(150, 25))
        self.label_manual_x.setMaximumSize(QSize(16777215, 25))
        self.label_manual_x.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_manual_x, 0, 1, 1, 1)

        self.lcdNumber_manual_x = QLCDNumber(self.tab_manual_xyz)
        self.lcdNumber_manual_x.setObjectName(u"lcdNumber_manual_x")
        self.lcdNumber_manual_x.setMinimumSize(QSize(30, 30))
        self.lcdNumber_manual_x.setMaximumSize(QSize(50, 50))
        self.lcdNumber_manual_x.setFont(font6)
        self.lcdNumber_manual_x.setStyleSheet(u"QLCDNumber{\n"
"  border: none;\n"
"  color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_8.addWidget(self.lcdNumber_manual_x, 1, 0, 1, 1)

        self.horizontalSlider_manual_x = QSlider(self.tab_manual_xyz)
        self.horizontalSlider_manual_x.setObjectName(u"horizontalSlider_manual_x")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_manual_x.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_manual_x.setSizePolicy(sizePolicy8)
        self.horizontalSlider_manual_x.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_manual_x.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_manual_x.setLayoutDirection(Qt.LeftToRight)
        self.horizontalSlider_manual_x.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_manual_x.setMinimum(-472)
        self.horizontalSlider_manual_x.setMaximum(472)
        self.horizontalSlider_manual_x.setPageStep(5)
        self.horizontalSlider_manual_x.setOrientation(Qt.Horizontal)
        self.horizontalSlider_manual_x.setInvertedAppearance(False)
        self.horizontalSlider_manual_x.setInvertedControls(False)
        self.horizontalSlider_manual_x.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_manual_x.setTickInterval(10)

        self.gridLayout_8.addWidget(self.horizontalSlider_manual_x, 1, 1, 1, 1)

        self.label_manual_y = QLabel(self.tab_manual_xyz)
        self.label_manual_y.setObjectName(u"label_manual_y")
        sizePolicy3.setHeightForWidth(self.label_manual_y.sizePolicy().hasHeightForWidth())
        self.label_manual_y.setSizePolicy(sizePolicy3)
        self.label_manual_y.setMinimumSize(QSize(150, 25))
        self.label_manual_y.setMaximumSize(QSize(16777215, 25))
        self.label_manual_y.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_manual_y, 2, 1, 1, 1)

        self.lcdNumber_manual_y = QLCDNumber(self.tab_manual_xyz)
        self.lcdNumber_manual_y.setObjectName(u"lcdNumber_manual_y")
        self.lcdNumber_manual_y.setMinimumSize(QSize(30, 30))
        self.lcdNumber_manual_y.setMaximumSize(QSize(50, 50))
        self.lcdNumber_manual_y.setFrameShape(QFrame.NoFrame)

        self.gridLayout_8.addWidget(self.lcdNumber_manual_y, 3, 0, 1, 1)

        self.horizontalSlider_manual_y = QSlider(self.tab_manual_xyz)
        self.horizontalSlider_manual_y.setObjectName(u"horizontalSlider_manual_y")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_manual_y.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_manual_y.setSizePolicy(sizePolicy8)
        self.horizontalSlider_manual_y.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_manual_y.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_manual_y.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_manual_y.setMinimum(-472)
        self.horizontalSlider_manual_y.setMaximum(472)
        self.horizontalSlider_manual_y.setPageStep(5)
        self.horizontalSlider_manual_y.setOrientation(Qt.Horizontal)
        self.horizontalSlider_manual_y.setInvertedAppearance(False)
        self.horizontalSlider_manual_y.setInvertedControls(False)
        self.horizontalSlider_manual_y.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_manual_y.setTickInterval(10)

        self.gridLayout_8.addWidget(self.horizontalSlider_manual_y, 3, 1, 1, 1)

        self.label_manual_z = QLabel(self.tab_manual_xyz)
        self.label_manual_z.setObjectName(u"label_manual_z")
        sizePolicy3.setHeightForWidth(self.label_manual_z.sizePolicy().hasHeightForWidth())
        self.label_manual_z.setSizePolicy(sizePolicy3)
        self.label_manual_z.setMinimumSize(QSize(150, 25))
        self.label_manual_z.setMaximumSize(QSize(16777215, 25))
        self.label_manual_z.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_manual_z, 4, 1, 1, 1)

        self.lcdNumber_manual_z = QLCDNumber(self.tab_manual_xyz)
        self.lcdNumber_manual_z.setObjectName(u"lcdNumber_manual_z")
        self.lcdNumber_manual_z.setMinimumSize(QSize(30, 30))
        self.lcdNumber_manual_z.setMaximumSize(QSize(50, 50))
        self.lcdNumber_manual_z.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_manual_z.setProperty("value", 472.000000000000000)

        self.gridLayout_8.addWidget(self.lcdNumber_manual_z, 5, 0, 1, 1)

        self.horizontalSlider_manual_z = QSlider(self.tab_manual_xyz)
        self.horizontalSlider_manual_z.setObjectName(u"horizontalSlider_manual_z")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_manual_z.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_manual_z.setSizePolicy(sizePolicy8)
        self.horizontalSlider_manual_z.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_manual_z.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_manual_z.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_manual_z.setMinimum(-472)
        self.horizontalSlider_manual_z.setMaximum(472)
        self.horizontalSlider_manual_z.setPageStep(5)
        self.horizontalSlider_manual_z.setSliderPosition(472)
        self.horizontalSlider_manual_z.setOrientation(Qt.Horizontal)
        self.horizontalSlider_manual_z.setInvertedAppearance(False)
        self.horizontalSlider_manual_z.setInvertedControls(False)
        self.horizontalSlider_manual_z.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_manual_z.setTickInterval(10)

        self.gridLayout_8.addWidget(self.horizontalSlider_manual_z, 5, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(50, 25, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 5, 2, 1, 1)

        self.lcdNumber_imanual_orient = QLCDNumber(self.tab_manual_xyz)
        self.lcdNumber_imanual_orient.setObjectName(u"lcdNumber_imanual_orient")
        self.lcdNumber_imanual_orient.setMinimumSize(QSize(30, 30))
        self.lcdNumber_imanual_orient.setMaximumSize(QSize(50, 50))
        self.lcdNumber_imanual_orient.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_imanual_orient.setProperty("value", 90.000000000000000)

        self.gridLayout_8.addWidget(self.lcdNumber_imanual_orient, 6, 0, 1, 1)

        self.label_manual_orient = QLabel(self.tab_manual_xyz)
        self.label_manual_orient.setObjectName(u"label_manual_orient")
        sizePolicy3.setHeightForWidth(self.label_manual_orient.sizePolicy().hasHeightForWidth())
        self.label_manual_orient.setSizePolicy(sizePolicy3)
        self.label_manual_orient.setMinimumSize(QSize(200, 25))
        self.label_manual_orient.setMaximumSize(QSize(16777215, 25))
        self.label_manual_orient.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_manual_orient, 6, 1, 1, 1)

        self.verticalSlider_manual_orient = QSlider(self.tab_manual_xyz)
        self.verticalSlider_manual_orient.setObjectName(u"verticalSlider_manual_orient")
        sizePolicy11.setHeightForWidth(self.verticalSlider_manual_orient.sizePolicy().hasHeightForWidth())
        self.verticalSlider_manual_orient.setSizePolicy(sizePolicy11)
        self.verticalSlider_manual_orient.setMinimumSize(QSize(0, 200))
        self.verticalSlider_manual_orient.setMaximumSize(QSize(16777215, 400))
        self.verticalSlider_manual_orient.setStyleSheet(u"QSlider::groove:vertical {\n"
"    border-radius: 9px;  \n"
"	widtht: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.verticalSlider_manual_orient.setMinimum(-90)
        self.verticalSlider_manual_orient.setMaximum(90)
        self.verticalSlider_manual_orient.setPageStep(5)
        self.verticalSlider_manual_orient.setSliderPosition(90)
        self.verticalSlider_manual_orient.setOrientation(Qt.Vertical)
        self.verticalSlider_manual_orient.setInvertedAppearance(True)
        self.verticalSlider_manual_orient.setInvertedControls(True)

        self.gridLayout_8.addWidget(self.verticalSlider_manual_orient, 6, 2, 1, 1)

        self.comboBox_auto_config_2 = QComboBox(self.tab_manual_xyz)
        self.comboBox_auto_config_2.addItem("")
        self.comboBox_auto_config_2.addItem("")
        self.comboBox_auto_config_2.setObjectName(u"comboBox_auto_config_2")
        self.comboBox_auto_config_2.setMinimumSize(QSize(100, 25))
        self.comboBox_auto_config_2.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_8.addWidget(self.comboBox_auto_config_2, 7, 0, 1, 2)

        self.btn_manual_reset_2 = QPushButton(self.tab_manual_xyz)
        self.btn_manual_reset_2.setObjectName(u"btn_manual_reset_2")
        sizePolicy4.setHeightForWidth(self.btn_manual_reset_2.sizePolicy().hasHeightForWidth())
        self.btn_manual_reset_2.setSizePolicy(sizePolicy4)
        self.btn_manual_reset_2.setMinimumSize(QSize(30, 30))
        self.btn_manual_reset_2.setMaximumSize(QSize(30, 30))
        self.btn_manual_reset_2.setFont(font3)
        self.btn_manual_reset_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_manual_reset_2.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_manual_reset_2.setCheckable(True)
        self.btn_manual_reset_2.setChecked(True)

        self.gridLayout_8.addWidget(self.btn_manual_reset_2, 7, 2, 1, 1)

        self.tabWidget_5.addTab(self.tab_manual_xyz, icon3, "")

        self.gridLayout_21.addWidget(self.tabWidget_5, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_manual_input, 0, 0, 2, 1)

        self.frame_manual_mpl = QFrame(self.page_manual)
        self.frame_manual_mpl.setObjectName(u"frame_manual_mpl")
        self.frame_manual_mpl.setMinimumSize(QSize(440, 300))
        self.frame_manual_mpl.setFrameShape(QFrame.NoFrame)
        self.frame_manual_mpl.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_manual_mpl)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.MplWidget_ik_2 = MplWidget(self.frame_manual_mpl)
        self.MplWidget_ik_2.setObjectName(u"MplWidget_ik_2")
        sizePolicy10.setHeightForWidth(self.MplWidget_ik_2.sizePolicy().hasHeightForWidth())
        self.MplWidget_ik_2.setSizePolicy(sizePolicy10)
        self.MplWidget_ik_2.setMinimumSize(QSize(440, 300))

        self.gridLayout_23.addWidget(self.MplWidget_ik_2, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_manual_mpl, 0, 1, 1, 1)

        self.frame_manual_actual = QFrame(self.page_manual)
        self.frame_manual_actual.setObjectName(u"frame_manual_actual")
        sizePolicy3.setHeightForWidth(self.frame_manual_actual.sizePolicy().hasHeightForWidth())
        self.frame_manual_actual.setSizePolicy(sizePolicy3)
        self.frame_manual_actual.setMinimumSize(QSize(440, 300))
        self.frame_manual_actual.setFrameShape(QFrame.NoFrame)
        self.frame_manual_actual.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_manual_actual)
        self.gridLayout_22.setSpacing(5)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(10, 10, 10, 10)
        self.label_manual_actual = QLabel(self.frame_manual_actual)
        self.label_manual_actual.setObjectName(u"label_manual_actual")
        self.label_manual_actual.setMinimumSize(QSize(300, 100))
        self.label_manual_actual.setMaximumSize(QSize(350, 100))
        self.label_manual_actual.setFont(font5)
        self.label_manual_actual.setStyleSheet(u"color: rgb(222, 222, 222);")

        self.gridLayout_22.addWidget(self.label_manual_actual, 0, 0, 1, 3)

        self.label_manual_actual_X = QLabel(self.frame_manual_actual)
        self.label_manual_actual_X.setObjectName(u"label_manual_actual_X")
        self.label_manual_actual_X.setMinimumSize(QSize(100, 50))
        self.label_manual_actual_X.setMaximumSize(QSize(100, 50))
        self.label_manual_actual_X.setFont(font4)
        self.label_manual_actual_X.setLayoutDirection(Qt.LeftToRight)
        self.label_manual_actual_X.setStyleSheet(u"color: rgb(222, 222, 222);")
        self.label_manual_actual_X.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_manual_actual_X, 3, 0, 1, 1)

        self.label_manual_actual_Y = QLabel(self.frame_manual_actual)
        self.label_manual_actual_Y.setObjectName(u"label_manual_actual_Y")
        self.label_manual_actual_Y.setMinimumSize(QSize(100, 50))
        self.label_manual_actual_Y.setMaximumSize(QSize(100, 50))
        self.label_manual_actual_Y.setFont(font4)
        self.label_manual_actual_Y.setStyleSheet(u"color: rgb(222, 222, 222);")
        self.label_manual_actual_Y.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_manual_actual_Y, 3, 1, 1, 1)

        self.label_manual_actual_Z = QLabel(self.frame_manual_actual)
        self.label_manual_actual_Z.setObjectName(u"label_manual_actual_Z")
        self.label_manual_actual_Z.setMinimumSize(QSize(100, 50))
        self.label_manual_actual_Z.setMaximumSize(QSize(100, 50))
        self.label_manual_actual_Z.setFont(font4)
        self.label_manual_actual_Z.setStyleSheet(u"color: rgb(222, 222, 222);")
        self.label_manual_actual_Z.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_manual_actual_Z, 3, 2, 1, 1)

        self.lcdNumber_manual_actual_X = QLCDNumber(self.frame_manual_actual)
        self.lcdNumber_manual_actual_X.setObjectName(u"lcdNumber_manual_actual_X")
        self.lcdNumber_manual_actual_X.setMinimumSize(QSize(100, 50))
        self.lcdNumber_manual_actual_X.setMaximumSize(QSize(100, 50))

        self.gridLayout_22.addWidget(self.lcdNumber_manual_actual_X, 4, 0, 1, 1)

        self.lcdNumber_manual_actual_Z = QLCDNumber(self.frame_manual_actual)
        self.lcdNumber_manual_actual_Z.setObjectName(u"lcdNumber_manual_actual_Z")
        self.lcdNumber_manual_actual_Z.setMinimumSize(QSize(100, 50))
        self.lcdNumber_manual_actual_Z.setMaximumSize(QSize(100, 50))

        self.gridLayout_22.addWidget(self.lcdNumber_manual_actual_Z, 4, 2, 1, 1)

        self.lcdNumber_manual_actual_Y = QLCDNumber(self.frame_manual_actual)
        self.lcdNumber_manual_actual_Y.setObjectName(u"lcdNumber_manual_actual_Y")
        self.lcdNumber_manual_actual_Y.setMinimumSize(QSize(100, 50))
        self.lcdNumber_manual_actual_Y.setMaximumSize(QSize(100, 50))

        self.gridLayout_22.addWidget(self.lcdNumber_manual_actual_Y, 4, 1, 1, 1)


        self.gridLayout_15.addWidget(self.frame_manual_actual, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_manual)
        self.page_automatic = QWidget()
        self.page_automatic.setObjectName(u"page_automatic")
        self.verticalLayout_12 = QVBoxLayout(self.page_automatic)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_automatic)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 400))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_2)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_7 = QTabWidget(self.frame_2)
        self.tabWidget_7.setObjectName(u"tabWidget_7")
        self.tabWidget_7.setTabShape(QTabWidget.Triangular)
        self.tabWidget_7.setDocumentMode(True)
        self.Frame_auto_movement = QWidget()
        self.Frame_auto_movement.setObjectName(u"Frame_auto_movement")
        self.gridLayout_29 = QGridLayout(self.Frame_auto_movement)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.btn_auto_add_actual_2 = QPushButton(self.Frame_auto_movement)
        self.btn_auto_add_actual_2.setObjectName(u"btn_auto_add_actual_2")
        sizePolicy4.setHeightForWidth(self.btn_auto_add_actual_2.sizePolicy().hasHeightForWidth())
        self.btn_auto_add_actual_2.setSizePolicy(sizePolicy4)
        self.btn_auto_add_actual_2.setMinimumSize(QSize(30, 30))
        self.btn_auto_add_actual_2.setMaximumSize(QSize(30, 30))
        self.btn_auto_add_actual_2.setFont(font3)
        self.btn_auto_add_actual_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto_add_actual_2.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"	image: url(:/24x24/24x24/icons8-add-50.png);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_auto_add_actual_2.setCheckable(True)
        self.btn_auto_add_actual_2.setChecked(True)

        self.gridLayout_29.addWidget(self.btn_auto_add_actual_2, 12, 3, 1, 1)

        self.btn_auto_add_actual = QPushButton(self.Frame_auto_movement)
        self.btn_auto_add_actual.setObjectName(u"btn_auto_add_actual")
        sizePolicy4.setHeightForWidth(self.btn_auto_add_actual.sizePolicy().hasHeightForWidth())
        self.btn_auto_add_actual.setSizePolicy(sizePolicy4)
        self.btn_auto_add_actual.setMinimumSize(QSize(30, 30))
        self.btn_auto_add_actual.setMaximumSize(QSize(30, 30))
        self.btn_auto_add_actual.setFont(font3)
        self.btn_auto_add_actual.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto_add_actual.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"	image: url(:/24x24/24x24/icons8-add-50.png);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_auto_add_actual.setCheckable(True)
        self.btn_auto_add_actual.setChecked(True)

        self.gridLayout_29.addWidget(self.btn_auto_add_actual, 9, 3, 1, 1)

        self.label_j_s5_2 = QLabel(self.Frame_auto_movement)
        self.label_j_s5_2.setObjectName(u"label_j_s5_2")
        sizePolicy3.setHeightForWidth(self.label_j_s5_2.sizePolicy().hasHeightForWidth())
        self.label_j_s5_2.setSizePolicy(sizePolicy3)
        self.label_j_s5_2.setMinimumSize(QSize(150, 25))
        self.label_j_s5_2.setMaximumSize(QSize(16777215, 25))
        self.label_j_s5_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_j_s5_2, 8, 1, 1, 1)

        self.horizontalSlider_auto_s6 = QSlider(self.Frame_auto_movement)
        self.horizontalSlider_auto_s6.setObjectName(u"horizontalSlider_auto_s6")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_auto_s6.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_auto_s6.setSizePolicy(sizePolicy8)
        self.horizontalSlider_auto_s6.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_auto_s6.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_auto_s6.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_auto_s6.setMinimum(-90)
        self.horizontalSlider_auto_s6.setMaximum(90)
        self.horizontalSlider_auto_s6.setOrientation(Qt.Horizontal)
        self.horizontalSlider_auto_s6.setInvertedAppearance(False)
        self.horizontalSlider_auto_s6.setInvertedControls(False)
        self.horizontalSlider_auto_s6.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_auto_s6.setTickInterval(10)

        self.gridLayout_29.addWidget(self.horizontalSlider_auto_s6, 12, 1, 1, 1)

        self.horizontalSlider_auto_s5 = QSlider(self.Frame_auto_movement)
        self.horizontalSlider_auto_s5.setObjectName(u"horizontalSlider_auto_s5")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_auto_s5.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_auto_s5.setSizePolicy(sizePolicy8)
        self.horizontalSlider_auto_s5.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_auto_s5.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_auto_s5.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_auto_s5.setMinimum(-90)
        self.horizontalSlider_auto_s5.setMaximum(90)
        self.horizontalSlider_auto_s5.setOrientation(Qt.Horizontal)
        self.horizontalSlider_auto_s5.setInvertedAppearance(False)
        self.horizontalSlider_auto_s5.setInvertedControls(False)
        self.horizontalSlider_auto_s5.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_auto_s5.setTickInterval(10)

        self.gridLayout_29.addWidget(self.horizontalSlider_auto_s5, 9, 1, 1, 1)

        self.label_j_s3_2 = QLabel(self.Frame_auto_movement)
        self.label_j_s3_2.setObjectName(u"label_j_s3_2")
        sizePolicy3.setHeightForWidth(self.label_j_s3_2.sizePolicy().hasHeightForWidth())
        self.label_j_s3_2.setSizePolicy(sizePolicy3)
        self.label_j_s3_2.setMinimumSize(QSize(150, 25))
        self.label_j_s3_2.setMaximumSize(QSize(16777215, 25))
        self.label_j_s3_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_j_s3_2, 4, 1, 1, 1)

        self.horizontalSlider_auto_orient = QSlider(self.Frame_auto_movement)
        self.horizontalSlider_auto_orient.setObjectName(u"horizontalSlider_auto_orient")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_auto_orient.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_auto_orient.setSizePolicy(sizePolicy8)
        self.horizontalSlider_auto_orient.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_auto_orient.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_auto_orient.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_auto_orient.setMinimum(-90)
        self.horizontalSlider_auto_orient.setMaximum(90)
        self.horizontalSlider_auto_orient.setOrientation(Qt.Horizontal)
        self.horizontalSlider_auto_orient.setInvertedAppearance(False)
        self.horizontalSlider_auto_orient.setInvertedControls(False)
        self.horizontalSlider_auto_orient.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_auto_orient.setTickInterval(10)

        self.gridLayout_29.addWidget(self.horizontalSlider_auto_orient, 7, 3, 1, 1)

        self.lcdNumber_auto_s3 = QLCDNumber(self.Frame_auto_movement)
        self.lcdNumber_auto_s3.setObjectName(u"lcdNumber_auto_s3")
        self.lcdNumber_auto_s3.setMinimumSize(QSize(30, 30))
        self.lcdNumber_auto_s3.setMaximumSize(QSize(50, 50))
        self.lcdNumber_auto_s3.setFrameShape(QFrame.NoFrame)

        self.gridLayout_29.addWidget(self.lcdNumber_auto_s3, 5, 0, 1, 1)

        self.horizontalSlider_auto_s1 = QSlider(self.Frame_auto_movement)
        self.horizontalSlider_auto_s1.setObjectName(u"horizontalSlider_auto_s1")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_auto_s1.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_auto_s1.setSizePolicy(sizePolicy8)
        self.horizontalSlider_auto_s1.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_auto_s1.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_auto_s1.setLayoutDirection(Qt.LeftToRight)
        self.horizontalSlider_auto_s1.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_auto_s1.setMinimum(-90)
        self.horizontalSlider_auto_s1.setMaximum(90)
        self.horizontalSlider_auto_s1.setOrientation(Qt.Horizontal)
        self.horizontalSlider_auto_s1.setInvertedAppearance(False)
        self.horizontalSlider_auto_s1.setInvertedControls(False)
        self.horizontalSlider_auto_s1.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_auto_s1.setTickInterval(10)

        self.gridLayout_29.addWidget(self.horizontalSlider_auto_s1, 1, 1, 1, 1)

        self.label_autoadd = QLabel(self.Frame_auto_movement)
        self.label_autoadd.setObjectName(u"label_autoadd")
        sizePolicy3.setHeightForWidth(self.label_autoadd.sizePolicy().hasHeightForWidth())
        self.label_autoadd.setSizePolicy(sizePolicy3)
        self.label_autoadd.setMinimumSize(QSize(200, 25))
        self.label_autoadd.setMaximumSize(QSize(16777215, 25))
        self.label_autoadd.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_29.addWidget(self.label_autoadd, 8, 3, 1, 1)

        self.lcdNumber_auto_s6 = QLCDNumber(self.Frame_auto_movement)
        self.lcdNumber_auto_s6.setObjectName(u"lcdNumber_auto_s6")
        self.lcdNumber_auto_s6.setMinimumSize(QSize(30, 30))
        self.lcdNumber_auto_s6.setMaximumSize(QSize(50, 50))
        self.lcdNumber_auto_s6.setFrameShape(QFrame.NoFrame)

        self.gridLayout_29.addWidget(self.lcdNumber_auto_s6, 12, 0, 1, 1)

        self.label_j_s6_2 = QLabel(self.Frame_auto_movement)
        self.label_j_s6_2.setObjectName(u"label_j_s6_2")
        sizePolicy3.setHeightForWidth(self.label_j_s6_2.sizePolicy().hasHeightForWidth())
        self.label_j_s6_2.setSizePolicy(sizePolicy3)
        self.label_j_s6_2.setMinimumSize(QSize(150, 25))
        self.label_j_s6_2.setMaximumSize(QSize(16777215, 25))
        self.label_j_s6_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_j_s6_2, 10, 1, 1, 1)

        self.lcdNumber_auto_z = QLCDNumber(self.Frame_auto_movement)
        self.lcdNumber_auto_z.setObjectName(u"lcdNumber_auto_z")
        self.lcdNumber_auto_z.setMinimumSize(QSize(30, 30))
        self.lcdNumber_auto_z.setMaximumSize(QSize(50, 50))
        self.lcdNumber_auto_z.setFrameShape(QFrame.NoFrame)

        self.gridLayout_29.addWidget(self.lcdNumber_auto_z, 5, 2, 1, 1)

        self.label_j_s4_2 = QLabel(self.Frame_auto_movement)
        self.label_j_s4_2.setObjectName(u"label_j_s4_2")
        sizePolicy3.setHeightForWidth(self.label_j_s4_2.sizePolicy().hasHeightForWidth())
        self.label_j_s4_2.setSizePolicy(sizePolicy3)
        self.label_j_s4_2.setMinimumSize(QSize(150, 25))
        self.label_j_s4_2.setMaximumSize(QSize(16777215, 25))
        self.label_j_s4_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_j_s4_2, 6, 1, 1, 1)

        self.horizontalSlider_auto_s3 = QSlider(self.Frame_auto_movement)
        self.horizontalSlider_auto_s3.setObjectName(u"horizontalSlider_auto_s3")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_auto_s3.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_auto_s3.setSizePolicy(sizePolicy8)
        self.horizontalSlider_auto_s3.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_auto_s3.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_auto_s3.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_auto_s3.setMinimum(-90)
        self.horizontalSlider_auto_s3.setMaximum(90)
        self.horizontalSlider_auto_s3.setOrientation(Qt.Horizontal)
        self.horizontalSlider_auto_s3.setInvertedAppearance(False)
        self.horizontalSlider_auto_s3.setInvertedControls(False)
        self.horizontalSlider_auto_s3.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_auto_s3.setTickInterval(10)

        self.gridLayout_29.addWidget(self.horizontalSlider_auto_s3, 5, 1, 1, 1)

        self.horizontalSlider_auto_z = QSlider(self.Frame_auto_movement)
        self.horizontalSlider_auto_z.setObjectName(u"horizontalSlider_auto_z")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_auto_z.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_auto_z.setSizePolicy(sizePolicy8)
        self.horizontalSlider_auto_z.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_auto_z.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_auto_z.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_auto_z.setMinimum(-90)
        self.horizontalSlider_auto_z.setMaximum(90)
        self.horizontalSlider_auto_z.setOrientation(Qt.Horizontal)
        self.horizontalSlider_auto_z.setInvertedAppearance(False)
        self.horizontalSlider_auto_z.setInvertedControls(False)
        self.horizontalSlider_auto_z.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_auto_z.setTickInterval(10)

        self.gridLayout_29.addWidget(self.horizontalSlider_auto_z, 5, 3, 1, 1)

        self.label_j_s2_2 = QLabel(self.Frame_auto_movement)
        self.label_j_s2_2.setObjectName(u"label_j_s2_2")
        sizePolicy3.setHeightForWidth(self.label_j_s2_2.sizePolicy().hasHeightForWidth())
        self.label_j_s2_2.setSizePolicy(sizePolicy3)
        self.label_j_s2_2.setMinimumSize(QSize(150, 25))
        self.label_j_s2_2.setMaximumSize(QSize(16777215, 25))
        self.label_j_s2_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_j_s2_2, 2, 1, 1, 1)

        self.horizontalSlider_auto_s2 = QSlider(self.Frame_auto_movement)
        self.horizontalSlider_auto_s2.setObjectName(u"horizontalSlider_auto_s2")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_auto_s2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_auto_s2.setSizePolicy(sizePolicy8)
        self.horizontalSlider_auto_s2.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_auto_s2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_auto_s2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_auto_s2.setMinimum(-90)
        self.horizontalSlider_auto_s2.setMaximum(90)
        self.horizontalSlider_auto_s2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_auto_s2.setInvertedAppearance(False)
        self.horizontalSlider_auto_s2.setInvertedControls(False)
        self.horizontalSlider_auto_s2.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_auto_s2.setTickInterval(10)

        self.gridLayout_29.addWidget(self.horizontalSlider_auto_s2, 3, 1, 1, 1)

        self.label_auto_x = QLabel(self.Frame_auto_movement)
        self.label_auto_x.setObjectName(u"label_auto_x")
        sizePolicy3.setHeightForWidth(self.label_auto_x.sizePolicy().hasHeightForWidth())
        self.label_auto_x.setSizePolicy(sizePolicy3)
        self.label_auto_x.setMinimumSize(QSize(150, 25))
        self.label_auto_x.setMaximumSize(QSize(16777215, 25))
        self.label_auto_x.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_auto_x, 0, 3, 1, 1)

        self.label_auto_z = QLabel(self.Frame_auto_movement)
        self.label_auto_z.setObjectName(u"label_auto_z")
        sizePolicy3.setHeightForWidth(self.label_auto_z.sizePolicy().hasHeightForWidth())
        self.label_auto_z.setSizePolicy(sizePolicy3)
        self.label_auto_z.setMinimumSize(QSize(150, 25))
        self.label_auto_z.setMaximumSize(QSize(16777215, 25))
        self.label_auto_z.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_auto_z, 4, 3, 1, 1)

        self.label_auto_orient = QLabel(self.Frame_auto_movement)
        self.label_auto_orient.setObjectName(u"label_auto_orient")
        sizePolicy3.setHeightForWidth(self.label_auto_orient.sizePolicy().hasHeightForWidth())
        self.label_auto_orient.setSizePolicy(sizePolicy3)
        self.label_auto_orient.setMinimumSize(QSize(200, 25))
        self.label_auto_orient.setMaximumSize(QSize(16777215, 25))
        self.label_auto_orient.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_auto_orient, 6, 3, 1, 1)

        self.lcdNumber_auto_s1 = QLCDNumber(self.Frame_auto_movement)
        self.lcdNumber_auto_s1.setObjectName(u"lcdNumber_auto_s1")
        self.lcdNumber_auto_s1.setMinimumSize(QSize(30, 30))
        self.lcdNumber_auto_s1.setMaximumSize(QSize(50, 50))
        self.lcdNumber_auto_s1.setFont(font6)
        self.lcdNumber_auto_s1.setStyleSheet(u"QLCDNumber{\n"
"  border: none;\n"
"  color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_29.addWidget(self.lcdNumber_auto_s1, 1, 0, 1, 1)

        self.lcdNumber_auto_y = QLCDNumber(self.Frame_auto_movement)
        self.lcdNumber_auto_y.setObjectName(u"lcdNumber_auto_y")
        self.lcdNumber_auto_y.setMinimumSize(QSize(30, 30))
        self.lcdNumber_auto_y.setMaximumSize(QSize(50, 50))
        self.lcdNumber_auto_y.setFrameShape(QFrame.NoFrame)

        self.gridLayout_29.addWidget(self.lcdNumber_auto_y, 3, 2, 1, 1)

        self.horizontalSlider_auto_s4 = QSlider(self.Frame_auto_movement)
        self.horizontalSlider_auto_s4.setObjectName(u"horizontalSlider_auto_s4")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_auto_s4.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_auto_s4.setSizePolicy(sizePolicy8)
        self.horizontalSlider_auto_s4.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_auto_s4.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_auto_s4.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_auto_s4.setMinimum(-90)
        self.horizontalSlider_auto_s4.setMaximum(90)
        self.horizontalSlider_auto_s4.setOrientation(Qt.Horizontal)
        self.horizontalSlider_auto_s4.setInvertedAppearance(False)
        self.horizontalSlider_auto_s4.setInvertedControls(False)
        self.horizontalSlider_auto_s4.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_auto_s4.setTickInterval(10)

        self.gridLayout_29.addWidget(self.horizontalSlider_auto_s4, 7, 1, 1, 1)

        self.lcdNumber_auto_x = QLCDNumber(self.Frame_auto_movement)
        self.lcdNumber_auto_x.setObjectName(u"lcdNumber_auto_x")
        self.lcdNumber_auto_x.setMinimumSize(QSize(30, 30))
        self.lcdNumber_auto_x.setMaximumSize(QSize(50, 50))
        self.lcdNumber_auto_x.setFont(font6)
        self.lcdNumber_auto_x.setStyleSheet(u"QLCDNumber{\n"
"  border: none;\n"
"  color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_29.addWidget(self.lcdNumber_auto_x, 1, 2, 1, 1)

        self.lcdNumber_auto_s4 = QLCDNumber(self.Frame_auto_movement)
        self.lcdNumber_auto_s4.setObjectName(u"lcdNumber_auto_s4")
        self.lcdNumber_auto_s4.setMinimumSize(QSize(30, 30))
        self.lcdNumber_auto_s4.setMaximumSize(QSize(50, 50))
        self.lcdNumber_auto_s4.setFrameShape(QFrame.NoFrame)

        self.gridLayout_29.addWidget(self.lcdNumber_auto_s4, 7, 0, 1, 1)

        self.lcdNumber_auto_orient = QLCDNumber(self.Frame_auto_movement)
        self.lcdNumber_auto_orient.setObjectName(u"lcdNumber_auto_orient")
        self.lcdNumber_auto_orient.setMinimumSize(QSize(30, 30))
        self.lcdNumber_auto_orient.setMaximumSize(QSize(50, 50))
        self.lcdNumber_auto_orient.setFrameShape(QFrame.NoFrame)

        self.gridLayout_29.addWidget(self.lcdNumber_auto_orient, 7, 2, 1, 1)

        self.label_auto_y = QLabel(self.Frame_auto_movement)
        self.label_auto_y.setObjectName(u"label_auto_y")
        sizePolicy3.setHeightForWidth(self.label_auto_y.sizePolicy().hasHeightForWidth())
        self.label_auto_y.setSizePolicy(sizePolicy3)
        self.label_auto_y.setMinimumSize(QSize(150, 25))
        self.label_auto_y.setMaximumSize(QSize(16777215, 25))
        self.label_auto_y.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_auto_y, 2, 3, 1, 1)

        self.label_j_s1_2 = QLabel(self.Frame_auto_movement)
        self.label_j_s1_2.setObjectName(u"label_j_s1_2")
        sizePolicy3.setHeightForWidth(self.label_j_s1_2.sizePolicy().hasHeightForWidth())
        self.label_j_s1_2.setSizePolicy(sizePolicy3)
        self.label_j_s1_2.setMinimumSize(QSize(150, 25))
        self.label_j_s1_2.setMaximumSize(QSize(16777215, 25))
        self.label_j_s1_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_j_s1_2, 0, 1, 1, 1)

        self.horizontalSlider_auto_x = QSlider(self.Frame_auto_movement)
        self.horizontalSlider_auto_x.setObjectName(u"horizontalSlider_auto_x")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_auto_x.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_auto_x.setSizePolicy(sizePolicy8)
        self.horizontalSlider_auto_x.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_auto_x.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_auto_x.setLayoutDirection(Qt.LeftToRight)
        self.horizontalSlider_auto_x.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_auto_x.setMinimum(-90)
        self.horizontalSlider_auto_x.setMaximum(90)
        self.horizontalSlider_auto_x.setOrientation(Qt.Horizontal)
        self.horizontalSlider_auto_x.setInvertedAppearance(False)
        self.horizontalSlider_auto_x.setInvertedControls(False)
        self.horizontalSlider_auto_x.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_auto_x.setTickInterval(10)

        self.gridLayout_29.addWidget(self.horizontalSlider_auto_x, 1, 3, 1, 1)

        self.lcdNumber_auto_s2 = QLCDNumber(self.Frame_auto_movement)
        self.lcdNumber_auto_s2.setObjectName(u"lcdNumber_auto_s2")
        self.lcdNumber_auto_s2.setMinimumSize(QSize(30, 30))
        self.lcdNumber_auto_s2.setMaximumSize(QSize(50, 50))
        self.lcdNumber_auto_s2.setFrameShape(QFrame.NoFrame)

        self.gridLayout_29.addWidget(self.lcdNumber_auto_s2, 3, 0, 1, 1)

        self.horizontalSlider_auto_y = QSlider(self.Frame_auto_movement)
        self.horizontalSlider_auto_y.setObjectName(u"horizontalSlider_auto_y")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_auto_y.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_auto_y.setSizePolicy(sizePolicy8)
        self.horizontalSlider_auto_y.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_auto_y.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalSlider_auto_y.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.horizontalSlider_auto_y.setMinimum(-90)
        self.horizontalSlider_auto_y.setMaximum(90)
        self.horizontalSlider_auto_y.setOrientation(Qt.Horizontal)
        self.horizontalSlider_auto_y.setInvertedAppearance(False)
        self.horizontalSlider_auto_y.setInvertedControls(False)
        self.horizontalSlider_auto_y.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_auto_y.setTickInterval(10)

        self.gridLayout_29.addWidget(self.horizontalSlider_auto_y, 3, 3, 1, 1)

        self.lcdNumber_auto_s5 = QLCDNumber(self.Frame_auto_movement)
        self.lcdNumber_auto_s5.setObjectName(u"lcdNumber_auto_s5")
        self.lcdNumber_auto_s5.setMinimumSize(QSize(30, 30))
        self.lcdNumber_auto_s5.setMaximumSize(QSize(50, 50))
        self.lcdNumber_auto_s5.setFrameShape(QFrame.NoFrame)

        self.gridLayout_29.addWidget(self.lcdNumber_auto_s5, 9, 0, 1, 1)

        self.label_auto_home = QLabel(self.Frame_auto_movement)
        self.label_auto_home.setObjectName(u"label_auto_home")
        sizePolicy3.setHeightForWidth(self.label_auto_home.sizePolicy().hasHeightForWidth())
        self.label_auto_home.setSizePolicy(sizePolicy3)
        self.label_auto_home.setMinimumSize(QSize(200, 25))
        self.label_auto_home.setMaximumSize(QSize(16777215, 25))
        self.label_auto_home.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_29.addWidget(self.label_auto_home, 10, 3, 1, 1)

        self.tabWidget_7.addTab(self.Frame_auto_movement, "")
        self.Frame_auto_table = QWidget()
        self.Frame_auto_table.setObjectName(u"Frame_auto_table")
        self.gridLayout_30 = QGridLayout(self.Frame_auto_table)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.Frame_auto_table)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        font7.setPointSize(8)
        font7.setBold(True)
        font7.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font7);
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font8 = QFont()
        font8.setBold(True)
        font8.setWeight(75)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font8);
        __qtablewidgetitem1.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font8);
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font8);
        __qtablewidgetitem3.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font8);
        __qtablewidgetitem4.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font8);
        __qtablewidgetitem5.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font8);
        __qtablewidgetitem6.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font8);
        __qtablewidgetitem7.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font8);
        __qtablewidgetitem8.setForeground(brush);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(0, 6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(0, 7, __qtablewidgetitem16)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        self.tableWidget.setMinimumSize(QSize(440, 300))
        self.tableWidget.setFrameShape(QFrame.Panel)
        self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)

        self.gridLayout_30.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.tabWidget_7.addTab(self.Frame_auto_table, "")
        self.Frame_auto_visu = QWidget()
        self.Frame_auto_visu.setObjectName(u"Frame_auto_visu")
        self.gridLayout_31 = QGridLayout(self.Frame_auto_visu)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.MplWidget_auto = MplWidget(self.Frame_auto_visu)
        self.MplWidget_auto.setObjectName(u"MplWidget_auto")
        sizePolicy10.setHeightForWidth(self.MplWidget_auto.sizePolicy().hasHeightForWidth())
        self.MplWidget_auto.setSizePolicy(sizePolicy10)
        self.MplWidget_auto.setMinimumSize(QSize(440, 300))

        self.gridLayout_31.addWidget(self.MplWidget_auto, 0, 0, 1, 1)

        self.tabWidget_7.addTab(self.Frame_auto_visu, "")

        self.gridLayout_28.addWidget(self.tabWidget_7, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_2)

        self.frame = QFrame(self.page_automatic)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.btn_auto_prev = QPushButton(self.frame)
        self.btn_auto_prev.setObjectName(u"btn_auto_prev")
        sizePolicy4.setHeightForWidth(self.btn_auto_prev.sizePolicy().hasHeightForWidth())
        self.btn_auto_prev.setSizePolicy(sizePolicy4)
        self.btn_auto_prev.setMinimumSize(QSize(50, 50))
        self.btn_auto_prev.setMaximumSize(QSize(50, 50))
        self.btn_auto_prev.setFont(font3)
        self.btn_auto_prev.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto_prev.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(114, 255, 144);\n"
"}")
        self.btn_auto_prev.setCheckable(True)
        self.btn_auto_prev.setChecked(True)

        self.gridLayout_7.addWidget(self.btn_auto_prev, 0, 0, 2, 1)

        self.btn_auto_start = QPushButton(self.frame)
        self.btn_auto_start.setObjectName(u"btn_auto_start")
        sizePolicy4.setHeightForWidth(self.btn_auto_start.sizePolicy().hasHeightForWidth())
        self.btn_auto_start.setSizePolicy(sizePolicy4)
        self.btn_auto_start.setMinimumSize(QSize(100, 100))
        self.btn_auto_start.setMaximumSize(QSize(100, 100))
        self.btn_auto_start.setFont(font3)
        self.btn_auto_start.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto_start.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 50px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"	image: url(:/24x24/24x24/icons8-start-50.png);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(114, 255, 142);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_auto_start.setCheckable(True)
        self.btn_auto_start.setChecked(True)

        self.gridLayout_7.addWidget(self.btn_auto_start, 0, 1, 3, 1)

        self.btn_auto_next = QPushButton(self.frame)
        self.btn_auto_next.setObjectName(u"btn_auto_next")
        sizePolicy4.setHeightForWidth(self.btn_auto_next.sizePolicy().hasHeightForWidth())
        self.btn_auto_next.setSizePolicy(sizePolicy4)
        self.btn_auto_next.setMinimumSize(QSize(50, 50))
        self.btn_auto_next.setMaximumSize(QSize(50, 50))
        self.btn_auto_next.setFont(font3)
        self.btn_auto_next.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto_next.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(114, 255, 144);\n"
"}")
        self.btn_auto_next.setCheckable(True)
        self.btn_auto_next.setChecked(True)

        self.gridLayout_7.addWidget(self.btn_auto_next, 0, 2, 2, 1)

        self.btn_auto_stop = QPushButton(self.frame)
        self.btn_auto_stop.setObjectName(u"btn_auto_stop")
        sizePolicy4.setHeightForWidth(self.btn_auto_stop.sizePolicy().hasHeightForWidth())
        self.btn_auto_stop.setSizePolicy(sizePolicy4)
        self.btn_auto_stop.setMinimumSize(QSize(50, 50))
        self.btn_auto_stop.setMaximumSize(QSize(50, 50))
        self.btn_auto_stop.setFont(font3)
        self.btn_auto_stop.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto_stop.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 129, 131);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/24x24/24x24/icons8-stop-circled-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_auto_stop.setIcon(icon5)
        self.btn_auto_stop.setIconSize(QSize(24, 24))
        self.btn_auto_stop.setCheckable(True)
        self.btn_auto_stop.setChecked(True)

        self.gridLayout_7.addWidget(self.btn_auto_stop, 0, 3, 2, 1)

        self.comboBox_auto_sim_servo = QComboBox(self.frame)
        self.comboBox_auto_sim_servo.addItem("")
        self.comboBox_auto_sim_servo.addItem("")
        self.comboBox_auto_sim_servo.setObjectName(u"comboBox_auto_sim_servo")
        self.comboBox_auto_sim_servo.setMinimumSize(QSize(100, 25))
        self.comboBox_auto_sim_servo.setMaximumSize(QSize(100, 25))

        self.gridLayout_7.addWidget(self.comboBox_auto_sim_servo, 0, 4, 1, 1)

        self.btn_auto_Add_path_gen = QPushButton(self.frame)
        self.btn_auto_Add_path_gen.setObjectName(u"btn_auto_Add_path_gen")
        sizePolicy4.setHeightForWidth(self.btn_auto_Add_path_gen.sizePolicy().hasHeightForWidth())
        self.btn_auto_Add_path_gen.setSizePolicy(sizePolicy4)
        self.btn_auto_Add_path_gen.setMinimumSize(QSize(50, 50))
        self.btn_auto_Add_path_gen.setMaximumSize(QSize(50, 50))
        self.btn_auto_Add_path_gen.setFont(font3)
        self.btn_auto_Add_path_gen.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto_Add_path_gen.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_auto_Add_path_gen.setCheckable(True)
        self.btn_auto_Add_path_gen.setChecked(True)

        self.gridLayout_7.addWidget(self.btn_auto_Add_path_gen, 0, 5, 1, 1)

        self.btn_auto_Add_path_read = QPushButton(self.frame)
        self.btn_auto_Add_path_read.setObjectName(u"btn_auto_Add_path_read")
        sizePolicy4.setHeightForWidth(self.btn_auto_Add_path_read.sizePolicy().hasHeightForWidth())
        self.btn_auto_Add_path_read.setSizePolicy(sizePolicy4)
        self.btn_auto_Add_path_read.setMinimumSize(QSize(50, 50))
        self.btn_auto_Add_path_read.setMaximumSize(QSize(50, 50))
        self.btn_auto_Add_path_read.setFont(font3)
        self.btn_auto_Add_path_read.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto_Add_path_read.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_auto_Add_path_read.setCheckable(True)
        self.btn_auto_Add_path_read.setChecked(True)

        self.gridLayout_7.addWidget(self.btn_auto_Add_path_read, 0, 6, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 8, 1, 1)

        self.comboBox_auto_command = QComboBox(self.frame)
        self.comboBox_auto_command.addItem("")
        self.comboBox_auto_command.addItem("")
        self.comboBox_auto_command.addItem("")
        self.comboBox_auto_command.setObjectName(u"comboBox_auto_command")
        self.comboBox_auto_command.setMinimumSize(QSize(100, 25))
        self.comboBox_auto_command.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_7.addWidget(self.comboBox_auto_command, 0, 9, 1, 1)

        self.btn_auto_add_empty = QPushButton(self.frame)
        self.btn_auto_add_empty.setObjectName(u"btn_auto_add_empty")
        sizePolicy4.setHeightForWidth(self.btn_auto_add_empty.sizePolicy().hasHeightForWidth())
        self.btn_auto_add_empty.setSizePolicy(sizePolicy4)
        self.btn_auto_add_empty.setMinimumSize(QSize(50, 50))
        self.btn_auto_add_empty.setMaximumSize(QSize(50, 50))
        self.btn_auto_add_empty.setFont(font3)
        self.btn_auto_add_empty.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto_add_empty.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"	image: url(:/24x24/24x24/icons8-add-50.png);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_7.addWidget(self.btn_auto_add_empty, 0, 10, 1, 1)

        self.btn_auto_delete = QPushButton(self.frame)
        self.btn_auto_delete.setObjectName(u"btn_auto_delete")
        sizePolicy4.setHeightForWidth(self.btn_auto_delete.sizePolicy().hasHeightForWidth())
        self.btn_auto_delete.setSizePolicy(sizePolicy4)
        self.btn_auto_delete.setMinimumSize(QSize(50, 50))
        self.btn_auto_delete.setMaximumSize(QSize(50, 50))
        self.btn_auto_delete.setFont(font3)
        self.btn_auto_delete.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto_delete.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"	image: url(:/24x24/24x24/icons8-cancel-50.png);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_7.addWidget(self.btn_auto_delete, 0, 11, 1, 1)

        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy13 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy13)
        self.spinBox.setMinimumSize(QSize(100, 25))
        self.spinBox.setMaximumSize(QSize(100, 16777215))
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setMinimum(1)

        self.gridLayout_7.addWidget(self.spinBox, 1, 4, 1, 1)

        self.comboBox_auto_traj = QComboBox(self.frame)
        self.comboBox_auto_traj.addItem("")
        self.comboBox_auto_traj.addItem("")
        self.comboBox_auto_traj.setObjectName(u"comboBox_auto_traj")
        self.comboBox_auto_traj.setMinimumSize(QSize(100, 25))
        self.comboBox_auto_traj.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_7.addWidget(self.comboBox_auto_traj, 1, 9, 1, 1)

        self.btn_auto_Add_wait = QPushButton(self.frame)
        self.btn_auto_Add_wait.setObjectName(u"btn_auto_Add_wait")
        sizePolicy4.setHeightForWidth(self.btn_auto_Add_wait.sizePolicy().hasHeightForWidth())
        self.btn_auto_Add_wait.setSizePolicy(sizePolicy4)
        self.btn_auto_Add_wait.setMinimumSize(QSize(50, 50))
        self.btn_auto_Add_wait.setMaximumSize(QSize(50, 50))
        self.btn_auto_Add_wait.setFont(font3)
        self.btn_auto_Add_wait.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto_Add_wait.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_auto_Add_wait.setCheckable(True)
        self.btn_auto_Add_wait.setChecked(True)

        self.gridLayout_7.addWidget(self.btn_auto_Add_wait, 1, 10, 2, 1)

        self.btn_auto_Add_safe = QPushButton(self.frame)
        self.btn_auto_Add_safe.setObjectName(u"btn_auto_Add_safe")
        sizePolicy4.setHeightForWidth(self.btn_auto_Add_safe.sizePolicy().hasHeightForWidth())
        self.btn_auto_Add_safe.setSizePolicy(sizePolicy4)
        self.btn_auto_Add_safe.setMinimumSize(QSize(50, 50))
        self.btn_auto_Add_safe.setMaximumSize(QSize(50, 50))
        self.btn_auto_Add_safe.setFont(font3)
        self.btn_auto_Add_safe.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto_Add_safe.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_auto_Add_safe.setCheckable(True)
        self.btn_auto_Add_safe.setChecked(True)

        self.gridLayout_7.addWidget(self.btn_auto_Add_safe, 1, 11, 2, 1)

        self.comboBox_auto_config = QComboBox(self.frame)
        self.comboBox_auto_config.addItem("")
        self.comboBox_auto_config.addItem("")
        self.comboBox_auto_config.setObjectName(u"comboBox_auto_config")
        self.comboBox_auto_config.setMinimumSize(QSize(100, 25))
        self.comboBox_auto_config.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_7.addWidget(self.comboBox_auto_config, 2, 9, 1, 1)

        self.btn_auto_add_actual_3 = QPushButton(self.frame)
        self.btn_auto_add_actual_3.setObjectName(u"btn_auto_add_actual_3")
        sizePolicy4.setHeightForWidth(self.btn_auto_add_actual_3.sizePolicy().hasHeightForWidth())
        self.btn_auto_add_actual_3.setSizePolicy(sizePolicy4)
        self.btn_auto_add_actual_3.setMinimumSize(QSize(20, 20))
        self.btn_auto_add_actual_3.setMaximumSize(QSize(20, 20))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(6)
        font9.setBold(False)
        font9.setWeight(50)
        self.btn_auto_add_actual_3.setFont(font9)
        self.btn_auto_add_actual_3.setLayoutDirection(Qt.LeftToRight)
        self.btn_auto_add_actual_3.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border-style: outset;\n"
"	background-color: transparent;\n"
"	image: url(:/50x50/50x50/icons8-application-window-50.png);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_auto_add_actual_3.setCheckable(True)
        self.btn_auto_add_actual_3.setChecked(True)

        self.gridLayout_7.addWidget(self.btn_auto_add_actual_3, 2, 3, 1, 1, Qt.AlignRight)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 0))

        self.gridLayout_7.addWidget(self.lineEdit, 2, 4, 1, 4)


        self.verticalLayout_12.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_automatic)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.gridLayout_27 = QGridLayout(self.page_settings)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_6 = QTabWidget(self.page_settings)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        self.tabWidget_6.setTabPosition(QTabWidget.North)
        self.tabWidget_6.setTabShape(QTabWidget.Triangular)
        self.tabWidget_6.setUsesScrollButtons(True)
        self.tabWidget_6.setDocumentMode(True)
        self.tabWidget_6.setTabsClosable(False)
        self.tabWidget_6.setMovable(False)
        self.tabWidget_6.setTabBarAutoHide(False)
        self.tab_info = QWidget()
        self.tab_info.setObjectName(u"tab_info")
        self.horizontalLayout_11 = QHBoxLayout(self.tab_info)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.info = QTextBrowser(self.tab_info)
        self.info.setObjectName(u"info")
        sizePolicy4.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy4)
        self.info.setMinimumSize(QSize(400, 0))
        self.info.setStyleSheet(u"")
        self.info.setFrameShape(QFrame.NoFrame)
        self.info.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_11.addWidget(self.info)

        self.label_3 = QLabel(self.tab_info)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(400, 480))
        self.label_3.setMaximumSize(QSize(700, 840))
        self.label_3.setStyleSheet(u"")
        self.label_3.setPixmap(QPixmap(u":/others/others/vis_info.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(5)

        self.horizontalLayout_11.addWidget(self.label_3)

        self.tabWidget_6.addTab(self.tab_info, "")
        self.tab_com = QWidget()
        self.tab_com.setObjectName(u"tab_com")
        self.gridLayout_19 = QGridLayout(self.tab_com)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.radioButton_home_comm_2 = QRadioButton(self.tab_com)
        self.radioButton_home_comm_2.setObjectName(u"radioButton_home_comm_2")
        self.radioButton_home_comm_2.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.radioButton_home_comm_2.sizePolicy().hasHeightForWidth())
        self.radioButton_home_comm_2.setSizePolicy(sizePolicy7)
        self.radioButton_home_comm_2.setMinimumSize(QSize(250, 50))
        self.radioButton_home_comm_2.setMaximumSize(QSize(400, 100))
        self.radioButton_home_comm_2.setFont(font4)
        self.radioButton_home_comm_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.radioButton_home_comm_2.setLayoutDirection(Qt.LeftToRight)
        self.radioButton_home_comm_2.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background-color:       green;\n"
"    border:                 2px solid white;\n"
"	border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       red;\n"
"    border:                 2px solid white;\n"
"	border-radius:          7px;\n"
"}")
        self.radioButton_home_comm_2.setChecked(False)
        self.radioButton_home_comm_2.setAutoExclusive(False)

        self.gridLayout_19.addWidget(self.radioButton_home_comm_2, 0, 1, 1, 1)

        self.logo_home_arduino_3 = QLabel(self.tab_com)
        self.logo_home_arduino_3.setObjectName(u"logo_home_arduino_3")
        self.logo_home_arduino_3.setMinimumSize(QSize(50, 50))
        self.logo_home_arduino_3.setMaximumSize(QSize(50, 50))
        self.logo_home_arduino_3.setStyleSheet(u"")
        self.logo_home_arduino_3.setPixmap(QPixmap(u":/50x50/50x50/icons8-arduino-uno-board-50.png"))
        self.logo_home_arduino_3.setScaledContents(True)
        self.logo_home_arduino_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.logo_home_arduino_3, 0, 0, 1, 1)

        self.label_com_rys = QLabel(self.tab_com)
        self.label_com_rys.setObjectName(u"label_com_rys")
        sizePolicy4.setHeightForWidth(self.label_com_rys.sizePolicy().hasHeightForWidth())
        self.label_com_rys.setSizePolicy(sizePolicy4)
        self.label_com_rys.setMinimumSize(QSize(500, 300))
        self.label_com_rys.setMaximumSize(QSize(1333, 800))
        self.label_com_rys.setStyleSheet(u"")
        self.label_com_rys.setTextFormat(Qt.PlainText)
        self.label_com_rys.setPixmap(QPixmap(u":/others/others/vis_arduino.jpg"))
        self.label_com_rys.setScaledContents(True)
        self.label_com_rys.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_com_rys, 1, 0, 1, 8)

        self.label_home_port_2 = QLabel(self.tab_com)
        self.label_home_port_2.setObjectName(u"label_home_port_2")
        self.label_home_port_2.setMinimumSize(QSize(300, 50))
        self.label_home_port_2.setMaximumSize(QSize(400, 50))
        self.label_home_port_2.setFont(font4)
        self.label_home_port_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.label_home_port_2, 0, 6, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.logo_home_arduino_4 = QLabel(self.tab_com)
        self.logo_home_arduino_4.setObjectName(u"logo_home_arduino_4")
        self.logo_home_arduino_4.setMinimumSize(QSize(50, 50))
        self.logo_home_arduino_4.setMaximumSize(QSize(50, 50))
        self.logo_home_arduino_4.setStyleSheet(u"")
        self.logo_home_arduino_4.setPixmap(QPixmap(u":/50x50/50x50/icons8-usb-micro-b-50.png"))
        self.logo_home_arduino_4.setScaledContents(True)
        self.logo_home_arduino_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.logo_home_arduino_4, 0, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_7, 0, 8, 1, 1)

        self.tabWidget_6.addTab(self.tab_com, "")
        self.tab_kalibracja = QWidget()
        self.tab_kalibracja.setObjectName(u"tab_kalibracja")
        self.gridLayout_25 = QGridLayout(self.tab_kalibracja)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_kal_kal = QLabel(self.tab_kalibracja)
        self.label_kal_kal.setObjectName(u"label_kal_kal")
        self.label_kal_kal.setMinimumSize(QSize(250, 50))
        self.label_kal_kal.setMaximumSize(QSize(350, 50))

        self.gridLayout_25.addWidget(self.label_kal_kal, 0, 0, 1, 1)

        self.btn_kal_set_0 = QPushButton(self.tab_kalibracja)
        self.btn_kal_set_0.setObjectName(u"btn_kal_set_0")
        sizePolicy4.setHeightForWidth(self.btn_kal_set_0.sizePolicy().hasHeightForWidth())
        self.btn_kal_set_0.setSizePolicy(sizePolicy4)
        self.btn_kal_set_0.setMinimumSize(QSize(50, 50))
        self.btn_kal_set_0.setMaximumSize(QSize(50, 50))
        self.btn_kal_set_0.setFont(font3)
        self.btn_kal_set_0.setLayoutDirection(Qt.LeftToRight)
        self.btn_kal_set_0.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(114, 255, 142);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_kal_set_0.setCheckable(True)
        self.btn_kal_set_0.setChecked(True)

        self.gridLayout_25.addWidget(self.btn_kal_set_0, 0, 1, 1, 1)

        self.label_kal_rys = QLabel(self.tab_kalibracja)
        self.label_kal_rys.setObjectName(u"label_kal_rys")
        sizePolicy14 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.label_kal_rys.sizePolicy().hasHeightForWidth())
        self.label_kal_rys.setSizePolicy(sizePolicy14)
        self.label_kal_rys.setMinimumSize(QSize(500, 600))
        self.label_kal_rys.setMaximumSize(QSize(700, 840))
        self.label_kal_rys.setStyleSheet(u"")
        self.label_kal_rys.setPixmap(QPixmap(u":/others/others/vis_calibration.png"))
        self.label_kal_rys.setScaledContents(True)
        self.label_kal_rys.setAlignment(Qt.AlignCenter)
        self.label_kal_rys.setMargin(5)

        self.gridLayout_25.addWidget(self.label_kal_rys, 0, 2, 7, 1)

        self.label_kal_s1 = QLabel(self.tab_kalibracja)
        self.label_kal_s1.setObjectName(u"label_kal_s1")
        self.label_kal_s1.setMinimumSize(QSize(250, 50))
        self.label_kal_s1.setMaximumSize(QSize(250, 50))

        self.gridLayout_25.addWidget(self.label_kal_s1, 1, 0, 1, 1)

        self.spinBox_kal_s1 = QSpinBox(self.tab_kalibracja)
        self.spinBox_kal_s1.setObjectName(u"spinBox_kal_s1")
        self.spinBox_kal_s1.setMinimumSize(QSize(50, 50))
        self.spinBox_kal_s1.setMaximumSize(QSize(50, 50))
        self.spinBox_kal_s1.setStyleSheet(u"QSpinBox {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QSpinBox:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSpinBox:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"")
        self.spinBox_kal_s1.setAlignment(Qt.AlignCenter)
        self.spinBox_kal_s1.setMinimum(-10)
        self.spinBox_kal_s1.setMaximum(10)
        self.spinBox_kal_s1.setValue(0)

        self.gridLayout_25.addWidget(self.spinBox_kal_s1, 1, 1, 1, 1)

        self.label_kal_s2 = QLabel(self.tab_kalibracja)
        self.label_kal_s2.setObjectName(u"label_kal_s2")
        self.label_kal_s2.setMinimumSize(QSize(250, 50))
        self.label_kal_s2.setMaximumSize(QSize(250, 50))

        self.gridLayout_25.addWidget(self.label_kal_s2, 2, 0, 1, 1)

        self.spinBox_kal_s2 = QSpinBox(self.tab_kalibracja)
        self.spinBox_kal_s2.setObjectName(u"spinBox_kal_s2")
        self.spinBox_kal_s2.setMinimumSize(QSize(50, 50))
        self.spinBox_kal_s2.setMaximumSize(QSize(50, 50))
        self.spinBox_kal_s2.setStyleSheet(u"QSpinBox {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QSpinBox:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSpinBox:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"")
        self.spinBox_kal_s2.setAlignment(Qt.AlignCenter)
        self.spinBox_kal_s2.setMinimum(-5)
        self.spinBox_kal_s2.setMaximum(5)
        self.spinBox_kal_s2.setValue(0)

        self.gridLayout_25.addWidget(self.spinBox_kal_s2, 2, 1, 1, 1)

        self.label_kal_s3 = QLabel(self.tab_kalibracja)
        self.label_kal_s3.setObjectName(u"label_kal_s3")
        self.label_kal_s3.setMinimumSize(QSize(250, 50))
        self.label_kal_s3.setMaximumSize(QSize(250, 50))

        self.gridLayout_25.addWidget(self.label_kal_s3, 3, 0, 1, 1)

        self.spinBox_kal_s3 = QSpinBox(self.tab_kalibracja)
        self.spinBox_kal_s3.setObjectName(u"spinBox_kal_s3")
        self.spinBox_kal_s3.setMinimumSize(QSize(50, 50))
        self.spinBox_kal_s3.setMaximumSize(QSize(50, 50))
        self.spinBox_kal_s3.setStyleSheet(u"QSpinBox {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QSpinBox:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSpinBox:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"")
        self.spinBox_kal_s3.setAlignment(Qt.AlignCenter)
        self.spinBox_kal_s3.setMinimum(-5)
        self.spinBox_kal_s3.setMaximum(5)
        self.spinBox_kal_s3.setValue(0)

        self.gridLayout_25.addWidget(self.spinBox_kal_s3, 3, 1, 1, 1)

        self.label_kal_s4 = QLabel(self.tab_kalibracja)
        self.label_kal_s4.setObjectName(u"label_kal_s4")
        self.label_kal_s4.setMinimumSize(QSize(250, 50))
        self.label_kal_s4.setMaximumSize(QSize(250, 50))

        self.gridLayout_25.addWidget(self.label_kal_s4, 4, 0, 1, 1)

        self.spinBox_kal_s4 = QSpinBox(self.tab_kalibracja)
        self.spinBox_kal_s4.setObjectName(u"spinBox_kal_s4")
        self.spinBox_kal_s4.setMinimumSize(QSize(50, 50))
        self.spinBox_kal_s4.setMaximumSize(QSize(50, 50))
        self.spinBox_kal_s4.setStyleSheet(u"QSpinBox {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QSpinBox:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSpinBox:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"")
        self.spinBox_kal_s4.setAlignment(Qt.AlignCenter)
        self.spinBox_kal_s4.setMinimum(-5)
        self.spinBox_kal_s4.setMaximum(5)
        self.spinBox_kal_s4.setValue(0)

        self.gridLayout_25.addWidget(self.spinBox_kal_s4, 4, 1, 1, 1)

        self.label_kal_s5 = QLabel(self.tab_kalibracja)
        self.label_kal_s5.setObjectName(u"label_kal_s5")
        self.label_kal_s5.setMinimumSize(QSize(250, 50))
        self.label_kal_s5.setMaximumSize(QSize(250, 50))

        self.gridLayout_25.addWidget(self.label_kal_s5, 5, 0, 1, 1)

        self.spinBox_kal_s5 = QSpinBox(self.tab_kalibracja)
        self.spinBox_kal_s5.setObjectName(u"spinBox_kal_s5")
        self.spinBox_kal_s5.setMinimumSize(QSize(50, 50))
        self.spinBox_kal_s5.setMaximumSize(QSize(50, 50))
        self.spinBox_kal_s5.setStyleSheet(u"QSpinBox {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QSpinBox:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSpinBox:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"")
        self.spinBox_kal_s5.setAlignment(Qt.AlignCenter)
        self.spinBox_kal_s5.setMinimum(-5)
        self.spinBox_kal_s5.setMaximum(5)
        self.spinBox_kal_s5.setValue(0)

        self.gridLayout_25.addWidget(self.spinBox_kal_s5, 5, 1, 1, 1)

        self.label_kal_s6 = QLabel(self.tab_kalibracja)
        self.label_kal_s6.setObjectName(u"label_kal_s6")
        self.label_kal_s6.setMinimumSize(QSize(250, 50))
        self.label_kal_s6.setMaximumSize(QSize(250, 50))

        self.gridLayout_25.addWidget(self.label_kal_s6, 6, 0, 1, 1)

        self.spinBox_kal_s6 = QSpinBox(self.tab_kalibracja)
        self.spinBox_kal_s6.setObjectName(u"spinBox_kal_s6")
        self.spinBox_kal_s6.setMinimumSize(QSize(50, 50))
        self.spinBox_kal_s6.setMaximumSize(QSize(50, 50))
        self.spinBox_kal_s6.setStyleSheet(u"QSpinBox {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QSpinBox:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSpinBox:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"")
        self.spinBox_kal_s6.setAlignment(Qt.AlignCenter)
        self.spinBox_kal_s6.setMinimum(-5)
        self.spinBox_kal_s6.setMaximum(5)
        self.spinBox_kal_s6.setValue(0)

        self.gridLayout_25.addWidget(self.spinBox_kal_s6, 6, 1, 1, 1)

        self.tabWidget_6.addTab(self.tab_kalibracja, "")
        self.tab_kalibracja2 = QWidget()
        self.tab_kalibracja2.setObjectName(u"tab_kalibracja2")
        self.gridLayout_26 = QGridLayout(self.tab_kalibracja2)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.spinBox_kal2_ef = QSpinBox(self.tab_kalibracja2)
        self.spinBox_kal2_ef.setObjectName(u"spinBox_kal2_ef")
        self.spinBox_kal2_ef.setMinimumSize(QSize(100, 50))
        self.spinBox_kal2_ef.setMaximumSize(QSize(100, 50))
        self.spinBox_kal2_ef.setStyleSheet(u"QSpinBox {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QSpinBox:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSpinBox:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"")
        self.spinBox_kal2_ef.setAlignment(Qt.AlignCenter)
        self.spinBox_kal2_ef.setMinimum(0)
        self.spinBox_kal2_ef.setMaximum(200)
        self.spinBox_kal2_ef.setValue(103)

        self.gridLayout_26.addWidget(self.spinBox_kal2_ef, 1, 1, 1, 1)

        self.spinBox_kal2_ef_2 = QSpinBox(self.tab_kalibracja2)
        self.spinBox_kal2_ef_2.setObjectName(u"spinBox_kal2_ef_2")
        self.spinBox_kal2_ef_2.setMinimumSize(QSize(100, 50))
        self.spinBox_kal2_ef_2.setMaximumSize(QSize(100, 50))
        self.spinBox_kal2_ef_2.setStyleSheet(u"QSpinBox {\n"
"    border-radius: 9px;  \n"
"	height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"QSpinBox:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSpinBox:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"")
        self.spinBox_kal2_ef_2.setAlignment(Qt.AlignCenter)
        self.spinBox_kal2_ef_2.setMinimum(0)
        self.spinBox_kal2_ef_2.setMaximum(50)
        self.spinBox_kal2_ef_2.setValue(0)

        self.gridLayout_26.addWidget(self.spinBox_kal2_ef_2, 2, 1, 1, 1)

        self.label_kal2_ef_4 = QLabel(self.tab_kalibracja2)
        self.label_kal2_ef_4.setObjectName(u"label_kal2_ef_4")
        self.label_kal2_ef_4.setMinimumSize(QSize(200, 50))
        self.label_kal2_ef_4.setMaximumSize(QSize(250, 50))

        self.gridLayout_26.addWidget(self.label_kal2_ef_4, 9, 0, 1, 1)

        self.checkBox_kal2_ef = QCheckBox(self.tab_kalibracja2)
        self.checkBox_kal2_ef.setObjectName(u"checkBox_kal2_ef")
        self.checkBox_kal2_ef.setMinimumSize(QSize(350, 50))
        self.checkBox_kal2_ef.setMaximumSize(QSize(350, 50))
        self.checkBox_kal2_ef.setChecked(False)

        self.gridLayout_26.addWidget(self.checkBox_kal2_ef, 0, 0, 1, 2, Qt.AlignTop)

        self.label_kal2_ef = QLabel(self.tab_kalibracja2)
        self.label_kal2_ef.setObjectName(u"label_kal2_ef")
        self.label_kal2_ef.setMinimumSize(QSize(200, 50))
        self.label_kal2_ef.setMaximumSize(QSize(250, 50))

        self.gridLayout_26.addWidget(self.label_kal2_ef, 1, 0, 1, 1)

        self.label_kal2_ef_2 = QLabel(self.tab_kalibracja2)
        self.label_kal2_ef_2.setObjectName(u"label_kal2_ef_2")
        self.label_kal2_ef_2.setMinimumSize(QSize(200, 50))
        self.label_kal2_ef_2.setMaximumSize(QSize(250, 50))

        self.gridLayout_26.addWidget(self.label_kal2_ef_2, 2, 0, 1, 1)

        self.btn_kal2_set_2 = QPushButton(self.tab_kalibracja2)
        self.btn_kal2_set_2.setObjectName(u"btn_kal2_set_2")
        sizePolicy4.setHeightForWidth(self.btn_kal2_set_2.sizePolicy().hasHeightForWidth())
        self.btn_kal2_set_2.setSizePolicy(sizePolicy4)
        self.btn_kal2_set_2.setMinimumSize(QSize(50, 50))
        self.btn_kal2_set_2.setMaximumSize(QSize(50, 50))
        self.btn_kal2_set_2.setFont(font3)
        self.btn_kal2_set_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_kal2_set_2.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(114, 255, 142);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_kal2_set_2.setCheckable(True)
        self.btn_kal2_set_2.setChecked(True)

        self.gridLayout_26.addWidget(self.btn_kal2_set_2, 9, 1, 1, 1)

        self.label_kal2_ef_3 = QLabel(self.tab_kalibracja2)
        self.label_kal2_ef_3.setObjectName(u"label_kal2_ef_3")
        self.label_kal2_ef_3.setMinimumSize(QSize(200, 50))
        self.label_kal2_ef_3.setMaximumSize(QSize(250, 50))

        self.gridLayout_26.addWidget(self.label_kal2_ef_3, 8, 0, 1, 1)

        self.btn_kal2_set_1 = QPushButton(self.tab_kalibracja2)
        self.btn_kal2_set_1.setObjectName(u"btn_kal2_set_1")
        sizePolicy4.setHeightForWidth(self.btn_kal2_set_1.sizePolicy().hasHeightForWidth())
        self.btn_kal2_set_1.setSizePolicy(sizePolicy4)
        self.btn_kal2_set_1.setMinimumSize(QSize(50, 50))
        self.btn_kal2_set_1.setMaximumSize(QSize(50, 50))
        self.btn_kal2_set_1.setFont(font3)
        self.btn_kal2_set_1.setLayoutDirection(Qt.LeftToRight)
        self.btn_kal2_set_1.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(35, 35, 35);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(114, 255, 142);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_kal2_set_1.setCheckable(True)
        self.btn_kal2_set_1.setChecked(True)

        self.gridLayout_26.addWidget(self.btn_kal2_set_1, 8, 1, 1, 1)

        self.label_kal_rys_2 = QLabel(self.tab_kalibracja2)
        self.label_kal_rys_2.setObjectName(u"label_kal_rys_2")
        sizePolicy14.setHeightForWidth(self.label_kal_rys_2.sizePolicy().hasHeightForWidth())
        self.label_kal_rys_2.setSizePolicy(sizePolicy14)
        self.label_kal_rys_2.setMinimumSize(QSize(450, 300))
        self.label_kal_rys_2.setMaximumSize(QSize(900, 600))
        self.label_kal_rys_2.setStyleSheet(u"")
        self.label_kal_rys_2.setPixmap(QPixmap(u":/others/others/vis_calibration3.PNG"))
        self.label_kal_rys_2.setScaledContents(True)
        self.label_kal_rys_2.setAlignment(Qt.AlignCenter)
        self.label_kal_rys_2.setMargin(5)

        self.gridLayout_26.addWidget(self.label_kal_rys_2, 0, 2, 10, 1)

        self.tabWidget_6.addTab(self.tab_kalibracja2, "")

        self.gridLayout_27.addWidget(self.tabWidget_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_settings)

        self.horizontalLayout_9.addWidget(self.stackedWidget)

        self.frame_logo = QFrame(self.frame_stackedWidget)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setMinimumSize(QSize(50, 0))
        self.frame_logo.setMaximumSize(QSize(50, 16777215))
        self.frame_logo.setStyleSheet(u"")
        self.frame_logo.setFrameShape(QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_logo)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 10)
        self.logo = QLabel(self.frame_logo)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(50, 50))
        self.logo.setMaximumSize(QSize(50, 50))
        self.logo.setStyleSheet(u"background-image: url(:/50x50/50x50/icons8-robot-50.png);")
        self.logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.logo)


        self.horizontalLayout_9.addWidget(self.frame_logo, 0, Qt.AlignBottom)


        self.verticalLayout_6.addWidget(self.frame_stackedWidget)

        self.frame_foot = QFrame(self.frame_screens)
        self.frame_foot.setObjectName(u"frame_foot")
        self.frame_foot.setMinimumSize(QSize(0, 30))
        self.frame_foot.setMaximumSize(QSize(16777215, 30))
        self.frame_foot.setStyleSheet(u"background-color: rgb(61, 61, 61);")
        self.frame_foot.setFrameShape(QFrame.NoFrame)
        self.frame_foot.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_foot)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.foot_label_log = QLabel(self.frame_foot)
        self.foot_label_log.setObjectName(u"foot_label_log")
        self.foot_label_log.setMinimumSize(QSize(50, 0))
        self.foot_label_log.setMaximumSize(QSize(50, 16777215))
        self.foot_label_log.setLayoutDirection(Qt.LeftToRight)
        self.foot_label_log.setFrameShadow(QFrame.Raised)
        self.foot_label_log.setLineWidth(0)
        self.foot_label_log.setPixmap(QPixmap(u":/16x16/16x16/icons8-alarms-50.png"))
        self.foot_label_log.setAlignment(Qt.AlignCenter)
        self.foot_label_log.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_3.addWidget(self.foot_label_log)

        self.Log = QTextBrowser(self.frame_foot)
        self.Log.setObjectName(u"Log")
        self.Log.setEnabled(True)
        self.Log.setMaximumSize(QSize(16777215, 20))
        self.Log.setFocusPolicy(Qt.StrongFocus)
        self.Log.setContextMenuPolicy(Qt.NoContextMenu)
        self.Log.setLayoutDirection(Qt.LeftToRight)
        self.Log.setStyleSheet(u"")
        self.Log.setInputMethodHints(Qt.ImhMultiLine)
        self.Log.setFrameShape(QFrame.NoFrame)
        self.Log.setFrameShadow(QFrame.Plain)
        self.Log.setLineWidth(0)
        self.Log.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Log.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Log.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.Log.setAutoFormatting(QTextEdit.AutoAll)
        self.Log.setLineWrapMode(QTextEdit.NoWrap)
        self.Log.setOverwriteMode(False)
        self.Log.setTabStopWidth(0)
        self.Log.setAcceptRichText(True)
        self.Log.setCursorWidth(0)
        self.Log.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.Log.setOpenLinks(False)

        self.horizontalLayout_3.addWidget(self.Log, 0, Qt.AlignVCenter)

        self.foot_label_ver = QLabel(self.frame_foot)
        self.foot_label_ver.setObjectName(u"foot_label_ver")
        self.foot_label_ver.setMinimumSize(QSize(50, 0))
        self.foot_label_ver.setMaximumSize(QSize(50, 16777215))
        self.foot_label_ver.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.foot_label_ver)

        self.frame_grip = QFrame(self.frame_foot)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(25, 25))
        self.frame_grip.setMaximumSize(QSize(25, 16777215))
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 5, 0)
        self.label_foot_grip = QLabel(self.frame_grip)
        self.label_foot_grip.setObjectName(u"label_foot_grip")
        self.label_foot_grip.setMinimumSize(QSize(0, 0))
        self.label_foot_grip.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_foot_grip)


        self.horizontalLayout_3.addWidget(self.frame_grip)


        self.verticalLayout_6.addWidget(self.frame_foot)


        self.horizontalLayout_2.addWidget(self.frame_screens)


        self.verticalLayout.addWidget(self.frame_content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.horizontalSlider_fk_s1.valueChanged.connect(self.lcdNumber_fk_s1.display)
        self.horizontalSlider_fk_s1_2.valueChanged.connect(self.lcdNumber_fk_s2.display)
        self.horizontalSlider_fk_s1_3.valueChanged.connect(self.lcdNumber_fk_s3.display)
        self.horizontalSlider_fk_s1_4.valueChanged.connect(self.lcdNumber_fk_s4.display)
        self.horizontalSlider_fk_s1_5.valueChanged.connect(self.lcdNumber_fk_s5.display)
        self.horizontalSlider_fk_s1_6.valueChanged.connect(self.lcdNumber_fk_s6.display)
        self.horizontalSlider_ik_x.valueChanged.connect(self.lcdNumber_ik_x.display)
        self.horizontalSlider_ik_y.valueChanged.connect(self.lcdNumber_ik_y.display)
        self.horizontalSlider_ik_z.valueChanged.connect(self.lcdNumber_ik_z.display)
        self.verticalSlider.valueChanged.connect(self.lcdNumber_ik_orient.display)
        self.horizontalSlider_j_s1.valueChanged.connect(self.lcdNumber_j_s1.display)
        self.horizontalSlider_j_s2.valueChanged.connect(self.lcdNumber_j_s2.display)
        self.horizontalSlider_j_s3.valueChanged.connect(self.lcdNumber_j_s3.display)
        self.horizontalSlider_j_s4.valueChanged.connect(self.lcdNumber_j_s4.display)
        self.horizontalSlider_j_s5.valueChanged.connect(self.lcdNumber_j_s5.display)
        self.horizontalSlider_j_s6.valueChanged.connect(self.lcdNumber_j_s6.display)
        self.horizontalSlider_manual_x.valueChanged.connect(self.lcdNumber_manual_x.display)
        self.horizontalSlider_manual_y.valueChanged.connect(self.lcdNumber_manual_y.display)
        self.horizontalSlider_manual_z.valueChanged.connect(self.lcdNumber_manual_z.display)
        self.verticalSlider_manual_orient.valueChanged.connect(self.lcdNumber_imanual_orient.display)
        self.horizontalSlider_auto_orient.valueChanged.connect(self.lcdNumber_auto_orient.display)
        self.horizontalSlider_auto_s1.valueChanged.connect(self.lcdNumber_auto_s1.display)
        self.horizontalSlider_auto_s2.valueChanged.connect(self.lcdNumber_auto_s2.display)
        self.horizontalSlider_auto_s3.valueChanged.connect(self.lcdNumber_auto_s3.display)
        self.horizontalSlider_auto_s4.valueChanged.connect(self.lcdNumber_auto_s4.display)
        self.horizontalSlider_auto_s5.valueChanged.connect(self.lcdNumber_auto_s5.display)
        self.horizontalSlider_auto_s6.valueChanged.connect(self.lcdNumber_auto_s6.display)
        self.horizontalSlider_auto_x.valueChanged.connect(self.lcdNumber_auto_x.display)
        self.horizontalSlider_auto_y.valueChanged.connect(self.lcdNumber_auto_y.display)
        self.horizontalSlider_auto_z.valueChanged.connect(self.lcdNumber_auto_z.display)

        self.stackedWidget.setCurrentIndex(5)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(1)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_lista.setText("")
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"ManipulatorApp", None))
#if QT_CONFIG(tooltip)
        self.btn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_min.setText("")
#if QT_CONFIG(tooltip)
        self.btn_max.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_max.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_fk.setText(QCoreApplication.translate("MainWindow", u"FORWARD KINEMATICS", None))
        self.btn_ik.setText(QCoreApplication.translate("MainWindow", u"INVERSE KINEMATICS", None))
        self.btn_manual.setText(QCoreApplication.translate("MainWindow", u"MANUAL MODE", None))
        self.btn_auto.setText(QCoreApplication.translate("MainWindow", u"AUTOMATIC MODE", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.btn_home_manual.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.btn_home_IK.setText(QCoreApplication.translate("MainWindow", u"Inverse kin.", None))
        self.btn_home_FK.setText(QCoreApplication.translate("MainWindow", u"Forward kin.", None))
        self.btn_home_info.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.btn_home_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_home_auto.setText(QCoreApplication.translate("MainWindow", u"Automatic", None))
#if QT_CONFIG(tooltip)
        self.radioButton_home_effector.setToolTip(QCoreApplication.translate("MainWindow", u"Po\u0142\u0105czenie PC <-> Arduino", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_home_effector.setText(QCoreApplication.translate("MainWindow", u"Effector present", None))
#if QT_CONFIG(tooltip)
        self.radioButton_home_comm.setToolTip(QCoreApplication.translate("MainWindow", u"Po\u0142\u0105czenie PC <-> Arduino", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_home_comm.setText(QCoreApplication.translate("MainWindow", u"Communication with board start / exit", None))
        self.label_home_port.setText(QCoreApplication.translate("MainWindow", u"Communication on port COM: 'COM3'", None))
        self.logo_home_effector.setText("")
        self.logo_home_arduino_2.setText("")
        self.logo_home_arduino.setText("")
        self.logo_home_robot.setText("")
        self.label_home_pos.setText(QCoreApplication.translate("MainWindow", u"Actual xyz robot position", None))
        self.label_home_actual_Y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_home_actual_Z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_home_actual_X.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_fk_s1.setText(QCoreApplication.translate("MainWindow", u"S1 - BASE", None))
        self.label_fk_s4.setText(QCoreApplication.translate("MainWindow", u"S3 - LINK 2", None))
        self.label_fk_s2.setText(QCoreApplication.translate("MainWindow", u"S2 - LINK 1", None))
        self.label_fk_s3.setText(QCoreApplication.translate("MainWindow", u"S4 - LINK 3", None))
        self.label_fk_s5.setText(QCoreApplication.translate("MainWindow", u"S5 - EFFECTOR MOVE", None))
        self.label_fk_s6.setText(QCoreApplication.translate("MainWindow", u"S6 - EFFECTOR ACTION", None))
#if QT_CONFIG(tooltip)
        self.btn_fk_reset.setToolTip(QCoreApplication.translate("MainWindow", u"Reset", None))
#endif // QT_CONFIG(tooltip)
        self.btn_fk_reset.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fk_joint), QCoreApplication.translate("MainWindow", u"Joints", None))
        self.label_dh_rys_3.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fk_info), QCoreApplication.translate("MainWindow", u"Info", None))
        self.label_dh_X_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_dh_wynik_2.setText(QCoreApplication.translate("MainWindow", u"Calculated XYZ end effector position", None))
        self.label_dh_Z_2.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_dh_Y_2.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_ik_z.setText(QCoreApplication.translate("MainWindow", u"Z-AXIS", None))
        self.label_ik_y.setText(QCoreApplication.translate("MainWindow", u"Y-AXIS", None))
        self.label_ik_orient.setText(QCoreApplication.translate("MainWindow", u"ORIENTATION", None))
        self.label_ik_x.setText(QCoreApplication.translate("MainWindow", u"X-AXIS", None))
#if QT_CONFIG(tooltip)
        self.btn_ik_reset.setToolTip(QCoreApplication.translate("MainWindow", u"Reset", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ik_reset.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_ik_joint), QCoreApplication.translate("MainWindow", u"XYZ", None))
        self.label_dh_rys_5.setText("")
        self.label_ik_efektor_2.setText("")
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_fk_info_3), QCoreApplication.translate("MainWindow", u"Info", None))
        self.label_s1_ik.setText(QCoreApplication.translate("MainWindow", u"S1 - BASE", None))
        self.label_ik_1.setText(QCoreApplication.translate("MainWindow", u"Calculated joints values - CONFIG. 1", None))
        self.label_s2_ik.setText(QCoreApplication.translate("MainWindow", u"S2 - JOINT 1", None))
        self.label_s3_ik.setText(QCoreApplication.translate("MainWindow", u"S3 - JOINT 2", None))
        self.label_s4_ik.setText(QCoreApplication.translate("MainWindow", u"S4 - JOINT 3", None))
#if QT_CONFIG(tooltip)
        self.btn_ik_reload_1.setToolTip(QCoreApplication.translate("MainWindow", u"Update sim", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ik_reload_1.setText("")
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.config1), QCoreApplication.translate("MainWindow", u"Config1", None))
        self.label_ik_2.setText(QCoreApplication.translate("MainWindow", u"Calculated joints values - CONFIG. 2", None))
        self.label_s1_ik_2.setText(QCoreApplication.translate("MainWindow", u"S1 - BASE", None))
        self.label_s2_ik_2.setText(QCoreApplication.translate("MainWindow", u"S2 - JOINT 1", None))
        self.label_s3_ik_2.setText(QCoreApplication.translate("MainWindow", u"S3 - JOINT 2", None))
        self.label_s4_ik_2.setText(QCoreApplication.translate("MainWindow", u"S4 - JOINT 3", None))
#if QT_CONFIG(tooltip)
        self.btn_ik_reload_2.setToolTip(QCoreApplication.translate("MainWindow", u"Update sim", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ik_reload_2.setText("")
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.config2), QCoreApplication.translate("MainWindow", u"Config2", None))
        self.label_j_s1.setText(QCoreApplication.translate("MainWindow", u"S1 - BASE", None))
        self.label_j_s2.setText(QCoreApplication.translate("MainWindow", u"S2 - LINK 1", None))
        self.label_j_s3.setText(QCoreApplication.translate("MainWindow", u"S3 - LINK 2", None))
        self.label_j_s4.setText(QCoreApplication.translate("MainWindow", u"S4 - LINK 3", None))
        self.label_j_s5.setText(QCoreApplication.translate("MainWindow", u"S5 - EFFECTOR MOVE", None))
        self.label_j_s6.setText(QCoreApplication.translate("MainWindow", u"S6 - EFFECTOR ACTION", None))
#if QT_CONFIG(tooltip)
        self.btn_manual_reset_1.setToolTip(QCoreApplication.translate("MainWindow", u"Reset", None))
#endif // QT_CONFIG(tooltip)
        self.btn_manual_reset_1.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_manual_joints), QCoreApplication.translate("MainWindow", u"Joints", None))
        self.label_manual_x.setText(QCoreApplication.translate("MainWindow", u"X-AXIS", None))
        self.label_manual_y.setText(QCoreApplication.translate("MainWindow", u"Y-AXIS", None))
        self.label_manual_z.setText(QCoreApplication.translate("MainWindow", u"Z-AXIS", None))
        self.label_manual_orient.setText(QCoreApplication.translate("MainWindow", u"ORIENTATION", None))
        self.comboBox_auto_config_2.setItemText(0, QCoreApplication.translate("MainWindow", u"config_1", None))
        self.comboBox_auto_config_2.setItemText(1, QCoreApplication.translate("MainWindow", u"config_2", None))

#if QT_CONFIG(tooltip)
        self.comboBox_auto_config_2.setToolTip(QCoreApplication.translate("MainWindow", u"Robot config", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_manual_reset_2.setToolTip(QCoreApplication.translate("MainWindow", u"Reset", None))
#endif // QT_CONFIG(tooltip)
        self.btn_manual_reset_2.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_manual_xyz), QCoreApplication.translate("MainWindow", u"XYZ", None))
        self.label_manual_actual.setText(QCoreApplication.translate("MainWindow", u"Actual xyz robot position", None))
        self.label_manual_actual_X.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_manual_actual_Y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_manual_actual_Z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
#if QT_CONFIG(tooltip)
        self.btn_auto_add_actual_2.setToolTip(QCoreApplication.translate("MainWindow", u"Set home", None))
#endif // QT_CONFIG(tooltip)
        self.btn_auto_add_actual_2.setText("")
#if QT_CONFIG(tooltip)
        self.btn_auto_add_actual.setToolTip(QCoreApplication.translate("MainWindow", u"Add actual pos", None))
#endif // QT_CONFIG(tooltip)
        self.btn_auto_add_actual.setText("")
        self.label_j_s5_2.setText(QCoreApplication.translate("MainWindow", u"S5 - EFFECTOR MOVE", None))
        self.label_j_s3_2.setText(QCoreApplication.translate("MainWindow", u"S3 - LINK 2", None))
        self.label_autoadd.setText(QCoreApplication.translate("MainWindow", u"ADD POSITION", None))
        self.label_j_s6_2.setText(QCoreApplication.translate("MainWindow", u"S6 - EFFECTOR ACTION", None))
        self.label_j_s4_2.setText(QCoreApplication.translate("MainWindow", u"S4 - LINK 3", None))
        self.label_j_s2_2.setText(QCoreApplication.translate("MainWindow", u"S2 - LINK 1", None))
        self.label_auto_x.setText(QCoreApplication.translate("MainWindow", u"X-AXIS", None))
        self.label_auto_z.setText(QCoreApplication.translate("MainWindow", u"Z-AXIS", None))
        self.label_auto_orient.setText(QCoreApplication.translate("MainWindow", u"ORIENTATION", None))
        self.label_auto_y.setText(QCoreApplication.translate("MainWindow", u"Y-AXIS", None))
        self.label_j_s1_2.setText(QCoreApplication.translate("MainWindow", u"S1 - BASE", None))
        self.label_auto_home.setText(QCoreApplication.translate("MainWindow", u"SET HOME POSITION", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Frame_auto_movement), QCoreApplication.translate("MainWindow", u"Movement", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Command", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"traj.", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"config.", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Z", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ALPHA", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Home", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"home", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"p2p", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"config_1", None));
        ___qtablewidgetitem12 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem13 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem14 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"460", None));
        ___qtablewidgetitem15 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"90", None));
        ___qtablewidgetitem16 = self.tableWidget.item(0, 7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"3.0", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Frame_auto_table), QCoreApplication.translate("MainWindow", u"Table", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Frame_auto_visu), QCoreApplication.translate("MainWindow", u"Visualisation", None))
#if QT_CONFIG(tooltip)
        self.btn_auto_prev.setToolTip(QCoreApplication.translate("MainWindow", u"Prev", None))
#endif // QT_CONFIG(tooltip)
        self.btn_auto_prev.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(tooltip)
        self.btn_auto_start.setToolTip(QCoreApplication.translate("MainWindow", u"START", None))
#endif // QT_CONFIG(tooltip)
        self.btn_auto_start.setText("")
#if QT_CONFIG(tooltip)
        self.btn_auto_next.setToolTip(QCoreApplication.translate("MainWindow", u"Next", None))
#endif // QT_CONFIG(tooltip)
        self.btn_auto_next.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(tooltip)
        self.btn_auto_stop.setToolTip(QCoreApplication.translate("MainWindow", u"STOP", None))
#endif // QT_CONFIG(tooltip)
        self.btn_auto_stop.setText("")
        self.comboBox_auto_sim_servo.setItemText(0, QCoreApplication.translate("MainWindow", u"SIM", None))
        self.comboBox_auto_sim_servo.setItemText(1, QCoreApplication.translate("MainWindow", u"SERVOS", None))

#if QT_CONFIG(tooltip)
        self.comboBox_auto_sim_servo.setToolTip(QCoreApplication.translate("MainWindow", u"Sim / Servos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_auto_Add_path_gen.setToolTip(QCoreApplication.translate("MainWindow", u"Generate path", None))
#endif // QT_CONFIG(tooltip)
        self.btn_auto_Add_path_gen.setText(QCoreApplication.translate("MainWindow", u"Gen.", None))
#if QT_CONFIG(tooltip)
        self.btn_auto_Add_path_read.setToolTip(QCoreApplication.translate("MainWindow", u"Read path from file .txt", None))
#endif // QT_CONFIG(tooltip)
        self.btn_auto_Add_path_read.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.comboBox_auto_command.setItemText(0, QCoreApplication.translate("MainWindow", u"home", None))
        self.comboBox_auto_command.setItemText(1, QCoreApplication.translate("MainWindow", u"move", None))
        self.comboBox_auto_command.setItemText(2, QCoreApplication.translate("MainWindow", u"wait", None))

#if QT_CONFIG(tooltip)
        self.comboBox_auto_command.setToolTip(QCoreApplication.translate("MainWindow", u"Command", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_auto_add_empty.setToolTip(QCoreApplication.translate("MainWindow", u"Add row", None))
#endif // QT_CONFIG(tooltip)
        self.btn_auto_add_empty.setText("")
#if QT_CONFIG(tooltip)
        self.btn_auto_delete.setToolTip(QCoreApplication.translate("MainWindow", u"Delete row", None))
#endif // QT_CONFIG(tooltip)
        self.btn_auto_delete.setText("")
#if QT_CONFIG(tooltip)
        self.spinBox.setToolTip(QCoreApplication.translate("MainWindow", u"Loop", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_auto_traj.setItemText(0, QCoreApplication.translate("MainWindow", u"p2p", None))
        self.comboBox_auto_traj.setItemText(1, QCoreApplication.translate("MainWindow", u"cp_linear", None))

#if QT_CONFIG(tooltip)
        self.comboBox_auto_traj.setToolTip(QCoreApplication.translate("MainWindow", u"Trajectory", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_auto_Add_wait.setToolTip(QCoreApplication.translate("MainWindow", u"Add Wait position", None))
#endif // QT_CONFIG(tooltip)
        self.btn_auto_Add_wait.setText(QCoreApplication.translate("MainWindow", u"WAIT", None))
#if QT_CONFIG(tooltip)
        self.btn_auto_Add_safe.setToolTip(QCoreApplication.translate("MainWindow", u"Add Home position", None))
#endif // QT_CONFIG(tooltip)
        self.btn_auto_Add_safe.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.comboBox_auto_config.setItemText(0, QCoreApplication.translate("MainWindow", u"config_1", None))
        self.comboBox_auto_config.setItemText(1, QCoreApplication.translate("MainWindow", u"config_2", None))

#if QT_CONFIG(tooltip)
        self.comboBox_auto_config.setToolTip(QCoreApplication.translate("MainWindow", u"Robot config", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_auto_add_actual_3.setToolTip(QCoreApplication.translate("MainWindow", u"Dodaj bie\u017c\u0105c\u0105 pozycje", None))
#endif // QT_CONFIG(tooltip)
        self.btn_auto_add_actual_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.info.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Autor: in\u017c. Daniel Sziling</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Technologies used:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Python 3.7 + PySide2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Arduino MEGA 2560</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Dimensions of the manipulator elements:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margi"
                        "n-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Base height: 	118mm</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Link 1 length: 	150mm</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Link 2 length: 	150mm</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Link 3 length: 	  54mm (wrist)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bloc"
                        "k-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Mass of individual elements with servos:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Link 1: 		217g</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Link 2:		141g</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Link 3:		  23g</span></p>\n"
"<p style=\"-qt-paragraph-type:e"
                        "mpty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Servomotors:		Moment:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Base: 		MG996R	13kg/cm</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Link 1: 		DS3218	20kg/cm</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span sty"
                        "le=\" color:#ffffff;\">Link 2: 		MG996R	13kg/cm</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Link 3: 		MG996R	13kg/cm</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Effector movement: 	SG92R	2,5kg/cm</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Effector action: 	SG92R	2,5kg/cm</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_3.setText("")
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_info), QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.radioButton_home_comm_2.setToolTip(QCoreApplication.translate("MainWindow", u"Comm. PC <-> Arduino", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_home_comm_2.setText(QCoreApplication.translate("MainWindow", u"Communication", None))
        self.logo_home_arduino_3.setText("")
        self.label_com_rys.setText("")
        self.label_home_port_2.setText(QCoreApplication.translate("MainWindow", u"Communication on port: 'COM3'", None))
        self.logo_home_arduino_4.setText("")
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_com), QCoreApplication.translate("MainWindow", u"Communication", None))
        self.label_kal_kal.setText(QCoreApplication.translate("MainWindow", u"Robotic Arm Calibration", None))
#if QT_CONFIG(tooltip)
        self.btn_kal_set_0.setToolTip(QCoreApplication.translate("MainWindow", u"Calibrate", None))
#endif // QT_CONFIG(tooltip)
        self.btn_kal_set_0.setText(QCoreApplication.translate("MainWindow", u"SET", None))
        self.label_kal_rys.setText("")
        self.label_kal_s1.setText(QCoreApplication.translate("MainWindow", u"Serwo base", None))
        self.label_kal_s2.setText(QCoreApplication.translate("MainWindow", u"Serwo link 1", None))
        self.label_kal_s3.setText(QCoreApplication.translate("MainWindow", u"Serwo link 2", None))
        self.label_kal_s4.setText(QCoreApplication.translate("MainWindow", u"Serwo link 3", None))
        self.label_kal_s5.setText(QCoreApplication.translate("MainWindow", u"Serwo effector movement", None))
        self.label_kal_s6.setText(QCoreApplication.translate("MainWindow", u"Serwo effector action", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_kalibracja), QCoreApplication.translate("MainWindow", u"Calibration", None))
#if QT_CONFIG(tooltip)
        self.spinBox_kal2_ef_2.setToolTip(QCoreApplication.translate("MainWindow", u"Max 50 mm", None))
#endif // QT_CONFIG(tooltip)
        self.label_kal2_ef_4.setText(QCoreApplication.translate("MainWindow", u"Pen holder", None))
        self.checkBox_kal2_ef.setText(QCoreApplication.translate("MainWindow", u"Has the effector been installed?", None))
        self.label_kal2_ef.setText(QCoreApplication.translate("MainWindow", u"L [mm]", None))
        self.label_kal2_ef_2.setText(QCoreApplication.translate("MainWindow", u"H [mm]", None))
#if QT_CONFIG(tooltip)
        self.btn_kal2_set_2.setToolTip(QCoreApplication.translate("MainWindow", u"Pen holder dimensions", None))
#endif // QT_CONFIG(tooltip)
        self.btn_kal2_set_2.setText(QCoreApplication.translate("MainWindow", u"SET", None))
        self.label_kal2_ef_3.setText(QCoreApplication.translate("MainWindow", u"Gripper", None))
#if QT_CONFIG(tooltip)
        self.btn_kal2_set_1.setToolTip(QCoreApplication.translate("MainWindow", u"Gripper dimensions", None))
#endif // QT_CONFIG(tooltip)
        self.btn_kal2_set_1.setText(QCoreApplication.translate("MainWindow", u"SET", None))
        self.label_kal_rys_2.setText("")
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_kalibracja2), QCoreApplication.translate("MainWindow", u"Effector", None))
        self.logo.setText("")
        self.foot_label_log.setText("")
        self.Log.setDocumentTitle("")
        self.Log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Time | Log</span></p></body></html>", None))
        self.Log.setPlaceholderText("")
        self.foot_label_ver.setText(QCoreApplication.translate("MainWindow", u"ver. 1.0", None))
        self.label_foot_grip.setText(QCoreApplication.translate("MainWindow", u".:", None))
    # retranslateUi

