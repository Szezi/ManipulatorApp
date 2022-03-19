from ManipulatorApp.main import MainWindow
from ManipulatorApp.main import *


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
        self.ui.horizontalSlider_fk_s1.setValue(0)
        self.ui.horizontalSlider_fk_s1_2.setValue(90)
        self.ui.horizontalSlider_fk_s1_3.setValue(0)
        self.ui.horizontalSlider_fk_s1_4.setValue(0)
        self.ui.horizontalSlider_fk_s1_5.setValue(0)
        self.ui.horizontalSlider_fk_s1_6.setValue(0)

    def page_ik_reset(self):
        self.ui.horizontalSlider_ik_x.setValue(0)
        self.ui.horizontalSlider_ik_y.setValue(0)
        self.ui.horizontalSlider_ik_z.setValue(472)
        self.ui.verticalSlider.setValue(90)

    def page_manual_reset(self):
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
