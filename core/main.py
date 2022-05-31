import os
import sys
import logging

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from converter import Converter


class UI_Converter(QtWidgets.QApplication):

    def __init__(self, parent=None):
        super(UI_Converter, self).__init__(parent)
        self.logger = logging.getLogger(__name__)  # Create the logger for the file
        self.h = ''
        # Load resource file
        resource_object = QtCore.QResource()
        resource_file = resource_object.registerResource(os.path.abspath("resources.rcc"))
        if resource_file.bit_length() == 0:
            self.logger.error("Resources file could not be loaded. Program is exiting.")

        self.main_window = QtWidgets.QMainWindow() # Create the main GUI window or any other windows
        self.main_widget = self.ui_loader(':/ui/ConverterUI', self.main_window) # Loading the respective UI files
        self.setup_ui()

    def setup_ui(self):
        # the input for the first box
        self.main_window.hour_line_in.text()
        self.main_window.mins_line_in.text()
        self.main_window.secs_line_in.text()
        self.main_window.calc_degs.clicked.connect(self.clicked1)
        # the input for the second box
        self.main_window.degs_line_in.text()
        self.main_window.calc_hours.clicked.connect(self.clicked2)


    def clicked1(self):
        h = Converter.hours_to_degs(int(self.main_window.hour_line_in.text()),
                                    int(self.main_window.mins_line_in.text()),
                                    int(self.main_window.secs_line_in.text()))
        self.main_window.degs_line_out.setText(str(h))

    def clicked2(self):
        h2 = Converter.degs_to_hours(float(self.main_window.degs_line_in.text()))
        self.main_window.hour_line_out.setText(str(h2[0]))
        self.main_window.mins_line_out.setText(str(h2[1]))
        self.main_window.secs_line_out.setText(str(h2[2]))

    def show_app(self):
        self.main_widget.show()

    @staticmethod
    def ui_loader(ui_resource, base=None):
        ui_file = QtCore.QFile(ui_resource)
        ui_file.open(QtCore.QFile.ReadOnly)
        try:
            parsed_ui = uic.loadUi(ui_file, base)
            return parsed_ui
        finally:
            ui_file.close()


app = UI_Converter(sys.argv)
app.show_app()
sys.exit(app.exec())

# /home/ggrivas/PycharmProject/Converter/core/resources.rcc
