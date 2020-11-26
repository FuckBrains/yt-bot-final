import os
import sys
from PyQt5.QtGui import QPalette, QColor

#currentPath = os.path.dirname(os.path.realpath(__file__))
#sys.path.append(currentPath.replace("\manualreview", ""))



import rawscriptsmenu
from PyQt5 import QtWidgets
import client
import sys
import atexit
import datetime
import configparser
import settings
import pandas as pd
from datetime import timedelta
currentPath = os.path.dirname(os.path.realpath(__file__))



def loadVideoScripts():
    pass

class App():
    def __init__(self):
        application = QtWidgets.QApplication(sys.argv)
        application.processEvents()
        loginWindow = client.LoginWindow()
        if settings.darkMode:
            application.setStyle("Fusion")
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
            palette.setColor(QPalette.Base, QColor(25, 25, 25))
            palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
            palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
            palette.setColor(QPalette.Text, QColor(255, 255, 255))
            palette.setColor(QPalette.Button, QColor(53, 53, 53))
            palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
            palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
            palette.setColor(QPalette.Link, QColor(42, 130, 218))
            palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
            application.setPalette(palette)
        loginWindow.show()


        #new = rawscriptsmenu.ScriptsMenu()
        #new.show()
        sys.exit(application.exec_())
        client.safeDisconnect()


sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    print("nice exit")
    sys.exit(1)

sys.excepthook = exception_hook

def init():

    os.chdir(currentPath)

    if not os.path.exists(settings.thumbnailpath):
        os.mkdir(settings.thumbnailpath)

    if not os.path.exists(settings.scriptsaves):
        os.mkdir(settings.scriptsaves)

    app = App()

def exit_handler():
    print("Safe Exit")
    client.sock.close()



if __name__ == "__main__":
    #data = pd.read_csv("bannedwords.csv")
    #print(data)
    atexit.register(exit_handler)
    settings.generateConfigFile()
    init()


# import os
# import sys

# try:
#     curr_dir = os.path.realpath(os.path.dirname(__file__))
#     sys.path.append(curr_dir + "/../common")
#     import logging 
#     import config
#     logger.init_logger(logger.get_logger_args())
#     config.read_config(curr_dir + "/config.ini")
# except Exception as e:
#     print("Missing required libraries at ../common")
#     print(e)
#     sys.exit()


# import rawscriptsmenu
# from PyQt5 import QtWidgets
# import client
# import sys
# import atexit
# import datetime
# import configparser
# import settings
# from datetime import timedelta
# import videoscriptcore

# currentPath = os.path.dirname(os.path.realpath(__file__))


# def loadVideoScripts():
#     pass

# class App():
#     def __init__(self):
#         application = QtWidgets.QApplication(sys.argv)
#         application.processEvents()
#         loginWindow = client.LoginWindow()
#         loginWindow.show()
#         sys.exit(application.exec_())
#         client.safeDisconnect()



# sys._excepthook = sys.excepthook
# def exception_hook(exctype, value, traceback):
#     sys._excepthook(exctype, value, traceback)
#     logger.critical("Uncaught Exception Occured! Exiting...")
#     sys.exit(1)
# sys.excepthook = exception_hook

# def init():
#     os.chdir(currentPath)
#     app = App()


# def exit_handler():
#     logger.info("Safe Exit")
#     client.sock.close()

# if __name__ == "__main__":
#     atexit.register(exit_handler)
#     settings.generateConfigFile()
#     init()

