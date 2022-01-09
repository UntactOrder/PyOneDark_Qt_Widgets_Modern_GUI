# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from src.main.gui.core.functions import set_svg_icon
from src.main.gui.core.functions import set_svg_image

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from src.main.qt_core import Qt
from src.main.qt_core import QGraphicsDropShadowEffect
from src.main.qt_core import QCoreApplication
from src.main.qt_core import QGraphicsOpacityEffect
from src.main.qt_core import QColor
from src.main.qt_core import QPoint
from src.main.qt_core import QIcon
from src.main.qt_core import QSvgWidget
from src.main.qt_core import QPropertyAnimation
from src.main.qt_core import QEasingCurve

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from src.main.gui.core.json_settings import Settings

# IMPORT MAIN WINDOW PAGES / AND SIDE BOXES FOR APP
# ///////////////////////////////////////////////////////////////
from src.main.gui.uis.pages.ui_splash_screen import UiSplashScreen


# SPLASH WINDOW
class UiSplashWindow(object):
    def __init__(self):
        self.ui = UiSplashScreen()
        self.ui.setup_ui(self)

        self.login_button_clicked = False

        # UI ==> INTERFACE CODES
        # ///////////////////////////////////////////////////////////////
        self.logo_svg = QSvgWidget(set_svg_image("logo_home.svg"))
        self.ui.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)
        self.lock_icon_svg = QSvgWidget(set_svg_icon("icon_lock.svg"))
        self.ui.lock_icon_layout.addWidget(self.lock_icon_svg, Qt.AlignCenter, Qt.AlignCenter)
        self.ui.close_button.setIcon(QIcon(set_svg_icon("icon_close.svg")))
        self.ui.close_button.clicked.connect(self.on_close_button_clicked)
        self.ui.login_button.clicked.connect(lambda: self.on_login_button_clicked(self))

        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # DROP SHADOW EFFECT
        self.construct_shadow()

    @staticmethod
    def on_close_button_clicked(self):
        pass

    @staticmethod
    def adjust_window_position(window):
        pos = window.mapToGlobal(QPoint(0, 0))
        window.move(pos.x(), pos.y() + 100)

    @staticmethod
    def show_login_panel(window):
        # Expand Widget
        pos = window.mapToGlobal(QPoint(0, 0))
        window.ani = QPropertyAnimation(window, b"pos")
        window.ani.setDuration(800)
        window.ani.setEasingCurve(QEasingCurve.InOutBack)
        window.ani.setEndValue(QPoint(pos.x(), pos.y() - 80))

        window.login_ani = QPropertyAnimation(window.ui.login_panel, b"pos")
        window.login_ani.setDuration(1200)
        window.login_ani.setStartValue(QPoint(40, 100))
        window.login_ani.setEndValue(QPoint(40, 270))
        window.login_ani.setEasingCurve(QEasingCurve.InOutBack)
        window.login_ani.finished.connect(window.construct_shadow)

        # Move Objects
        window.small_title_ani = QPropertyAnimation(window.ui.label_small_title, b"pos")
        window.small_title_ani.setDuration(800)
        window.small_title_ani.setStartValue(QPoint(44, 0))
        window.small_title_ani.setEndValue(QPoint(44, 36))
        window.small_title_ani.setEasingCurve(QEasingCurve.Linear)

        def fade_animation():
            nonlocal window
            effect = QGraphicsOpacityEffect(window.ui.lock_icon, opacity=0.0)
            window.ui.lock_icon.setGraphicsEffect(effect)
            window.lock_icon_fade_in = QPropertyAnimation(effect, b"opacity")
            window.lock_icon_fade_in.setDuration(1000)
            window.lock_icon_fade_in.setStartValue(0.0)
            window.lock_icon_fade_in.setEndValue(1.0)
            window.ui.lock_icon.setVisible(True)
            window.lock_icon_fade_in.finished.connect(lambda: window.ui.lock_icon.setGraphicsEffect(None))
            window.lock_icon_fade_in.start()

            effect = QGraphicsOpacityEffect(window.ui.user_name, opacity=0.0)
            window.ui.user_name.setGraphicsEffect(effect)
            window.user_name_fade_in = QPropertyAnimation(effect, b"opacity")
            window.user_name_fade_in.setDuration(1000)
            window.user_name_fade_in.setStartValue(0.0)
            window.user_name_fade_in.setEndValue(1.0)
            window.ui.user_name.setVisible(True)
            window.user_name_fade_in.finished.connect(lambda: window.ui.user_name.setGraphicsEffect(None))
            window.user_name_fade_in.start()

            effect = QGraphicsOpacityEffect(window.ui.user_name_description, opacity=0.0)
            window.ui.user_name_description.setGraphicsEffect(effect)
            window.user_name_description_fade_in = QPropertyAnimation(effect, b"opacity")
            window.user_name_description_fade_in.setDuration(1000)
            window.user_name_description_fade_in.setStartValue(0.0)
            window.user_name_description_fade_in.setEndValue(1.0)
            window.ui.user_name_description.setVisible(True)
            window.user_name_description_fade_in.finished.connect(lambda: window.ui.user_name_description.setGraphicsEffect(None))
            window.user_name_description_fade_in.start()

            effect = QGraphicsOpacityEffect(window.ui.login_button, opacity=0.0)
            window.ui.login_button.setGraphicsEffect(effect)
            window.login_button_fade_in = QPropertyAnimation(effect, b"opacity")
            window.login_button_fade_in.setDuration(1000)
            window.login_button_fade_in.setStartValue(0.0)
            window.login_button_fade_in.setEndValue(1.0)
            window.ui.login_button.setVisible(True)
            window.login_button_fade_in.finished.connect(lambda: window.ui.login_button.setGraphicsEffect(None))
            window.login_button_fade_in.start()

        window.login_ani.finished.connect(lambda: fade_animation() or window.login_ani.finished.disconnect())

        # Start Animations
        window.ani.start()
        window.ui.login_panel.setVisible(True)
        window.login_ani.start()
        window.ui.label_small_title.setVisible(True)
        window.small_title_ani.start()

    @staticmethod
    def hide_login_panel(window, callback):
        try:
            effect = QGraphicsOpacityEffect(window.ui.login_button, opacity=1.0)
            window.ui.login_button.setGraphicsEffect(effect)
            window.login_button_fade_in = QPropertyAnimation(effect, b"opacity")
            window.login_button_fade_in.setDuration(400)
            window.login_button_fade_in.setStartValue(1.0)
            window.login_button_fade_in.setEndValue(0.0)
            window.login_button_fade_in.finished.connect(
                lambda: window.ui.login_button.setVisible(False)
                        or window.construct_shadow()
                        or window.ui.login_button.setGraphicsEffect(None))
            window.login_button_fade_in.start()

            window.login_ani.setDirection(QPropertyAnimation.Backward)
            window.login_ani.finished.connect(lambda: callback() or window.login_ani.finished.disconnect())
            pos = window.mapToGlobal(QPoint(0, 0))
            window.ani = QPropertyAnimation(window, b"pos")
            window.ani.setDuration(800)
            window.ani.setEasingCurve(QEasingCurve.InOutBack)
            window.ani.setEndValue(QPoint(pos.x(), pos.y() + 80))
            window.ani.start()
            window.login_ani.start()
        except Exception as e:
            print(e)  # show_login_panel 메서드 실행 이후에만 제대로 동작함

    def construct_shadow(self):
        self.ui.dropShadowBackFrame.setGraphicsEffect(None)
        self.drop_shadow = QGraphicsDropShadowEffect(self.ui.dropShadowBackFrame)
        self.drop_shadow.setBlurRadius(20)
        self.drop_shadow.setXOffset(0)
        self.drop_shadow.setYOffset(0)
        self.drop_shadow.setColor(QColor(0, 0, 0, 160))
        self.ui.dropShadowBackFrame.setGraphicsEffect(self.drop_shadow)

        self.ui.login_panel_back.setGraphicsEffect(None)
        self.login_shadow = QGraphicsDropShadowEffect(self.ui.login_panel_back)
        self.login_shadow.setBlurRadius(20)
        self.login_shadow.setXOffset(0)
        self.login_shadow.setYOffset(0)
        self.login_shadow.setColor(QColor(0, 0, 0, 160))
        self.ui.login_panel_back.setGraphicsEffect(self.login_shadow)

    def fade_objects(self, callback):
        # Fade out Objects
        effect = QGraphicsOpacityEffect(self.ui.label_title, opacity=1.0)
        self.ui.label_title.setGraphicsEffect(effect)
        self.title_fade_out = QPropertyAnimation(effect, b"opacity")
        self.title_fade_out.setDuration(200)
        self.title_fade_out.setEndValue(0.0)
        self.title_fade_out.finished.connect(lambda: self.ui.label_title.setVisible(False) or callback())

        effect = QGraphicsOpacityEffect(self.ui.label_description, opacity=1.0)
        self.ui.label_description.setGraphicsEffect(effect)
        self.description_fade_out = QPropertyAnimation(effect, b"opacity")
        self.description_fade_out.setDuration(200)
        self.description_fade_out.setEndValue(0.0)
        self.description_fade_out.finished.connect(lambda: self.ui.label_description.setVisible(False))

        effect = QGraphicsOpacityEffect(self.ui.progressBar, opacity=1.0)
        self.ui.progressBar.setGraphicsEffect(effect)
        self.progress_fade_out = QPropertyAnimation(effect, b"opacity")
        self.progress_fade_out.setDuration(200)
        self.progress_fade_out.setEndValue(0.0)
        self.progress_fade_out.finished.connect(lambda: self.ui.progressBar.setVisible(False))

        effect = QGraphicsOpacityEffect(self.ui.label_loading, opacity=1.0)
        self.ui.label_loading.setGraphicsEffect(effect)
        self.loading_fade_out = QPropertyAnimation(effect, b"opacity")
        self.loading_fade_out.setDuration(200)
        self.loading_fade_out.setEndValue(0.0)
        self.loading_fade_out.finished.connect(lambda: self.ui.label_loading.setVisible(False))

        effect = QGraphicsOpacityEffect(self.ui.logo, opacity=0.0)
        self.ui.logo.setGraphicsEffect(effect)
        self.logo_fade_in = QPropertyAnimation(effect, b"opacity")
        self.logo_fade_in.setDuration(1200)
        self.logo_fade_in.setStartValue(0.0)
        self.logo_fade_in.setEndValue(1.0)
        self.logo_fade_in.finished.connect(self.construct_shadow)

        effect = QGraphicsOpacityEffect(self.ui.close_button, opacity=0.0)
        self.ui.logo.setGraphicsEffect(effect)
        self.close_button_fade_in = QPropertyAnimation(effect, b"opacity")
        self.close_button_fade_in.setDuration(1000)
        self.close_button_fade_in.setStartValue(0.0)
        self.close_button_fade_in.setEndValue(1.0)

        # Start Animations
        self.title_fade_out.start()
        self.description_fade_out.start()
        self.progress_fade_out.start()
        self.loading_fade_out.start()
        self.logo_fade_in.start()
        self.ui.logo.setVisible(True)
        self.close_button_fade_in.start()
        self.ui.close_button.setVisible(True)
        self.ui.dropShadowBackFrame.setGraphicsEffect(None)

    def set_progress(self, value):
        self.ui.progressBar.setValue(value)

    @staticmethod
    def on_login_button_clicked(window):
        # SHOW/HIDE PASSWORD INPUT LAYOUT
        if window.login_button_clicked:
            window.__hide_password_input_layout(window)
            window.login_button_clicked = False
            window.ui.login_button.setText(QCoreApplication.translate("SplashScreen", u"LOGIN", None))
        else:
            window.login_button_clicked = True
            window.ui.login_button.setText(QCoreApplication.translate("SplashScreen", u"CANCEL", None))
            if window.check_if_encrypted(window):
                window.__show_password_input_layout(window)
            else:
                window.set_login_success_flag(window)
                window.on_close_button_clicked()

    @staticmethod
    def on_password_inputted(window):
        if window.try_decrypt():
            window.set_login_success_flag()
            window.on_close_button_clicked()

    @staticmethod
    def __show_password_input_layout(window):
        pass

    @staticmethod
    def __hide_password_input_layout(window):
        try:
            pass
        except Exception as e:
            print(e)

    @staticmethod
    def check_if_encrypted(window):
        return False

    @staticmethod
    def try_decrypt(window):
        return True

    @staticmethod
    def set_login_success_flag(window):
        try:
            window.args['login_success'] = True
        except Exception as e:
            print(e)
            print("Failed to set login success flag; could not find 'args' variable")
