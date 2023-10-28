import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QAction, QMenu, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, Qt

class SystemTrayApplet(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create a floating widget
        self.floating_widget = QWidget()
        self.floating_widget.setWindowFlags(Qt.ToolTip)
        self.floating_widget.setWindowFlag(Qt.FramelessWindowHint)
        self.floating_widget.setGeometry(0, 0, 200, 150)
        self.floating_widget.hide()

        # Create labels in the floating widget
        layout = QVBoxLayout(self.floating_widget)
        for text in ["Label 1", "Label 2", "Label 3", "Label 4", "Label 5"]:
            label = QLabel(text, self.floating_widget)
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

        # Create the system tray icon
        self.tray_icon = QSystemTrayIcon(QIcon("icon.png"), self)
        self.tray_icon.activated.connect(self.show_hide_floating_widget)

        # Create the context menu
        self.context_menu = QMenu()
        self.context_menu.addAction("Open")
        self.context_menu.addAction("Save")
        self.context_menu.addAction("Refresh")
        self.context_menu.addAction("Settings")
        self.context_menu.addSeparator()
        self.context_menu.addAction("Quit")
        self.context_menu.triggered.connect(self.menu_item_clicked)
        self.tray_icon.setContextMenu(self.context_menu)

        self.tray_icon.show()

    def show_hide_floating_widget(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.floating_widget.isVisible():
                self.floating_widget.hide()
            else:
                self.floating_widget.show()

    def menu_item_clicked(self, action):
        if action.text() == "Quit":
            QApplication.quit()
        elif action.text() == "Settings":
            self.show_settings_dialog()

    def show_settings_dialog(self):
        # Add code to display the settings dialog here
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    applet = SystemTrayApplet()
    sys.exit(app.exec_())

