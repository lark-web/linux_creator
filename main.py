import sys
import os
#from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
#import main_window
from linux_creator import Ui_MainWindow

class ExampleApp(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(ExampleApp,self).__init__(parent)
        #super().__init__()
        self.setupUi(self)
        www = self.centralwidget.getContentsMargins()
        print(www)
        self.setWindowTitle('Linux FIT creator')
        self.work_directory = '/home/lark/ebaz_dma'
        self.lineEdit_Work_Directory.setText(self.work_directory)
        self.pushButton_Select_Work_Directory.setFlat(False)
        self.pushButton_Select_Work_Directory.clicked.connect(self.action_push)
        self.pushButton_Select_Work_Directory.setToolTip("Select Work Directory")
        self.pushButton_Create_Work_Space.clicked.connect(self.action_create_workspace)
        self.statusbar.showMessage("Message")
        #self.label_Work_Directory.setText("Заголовок-1")
    def action_create_workspace(self):
        res = False
        #QMessageBox.information(self,'LARK','test')
        # create some files and subdirectories in work directory :
        #file_br_config = open(work_directory/ "br-config","w+")
        path = self.work_directory + '/br-config'
        print(path)
        print(self.work_directory)
        if os.path.isfile(path):
            print('file br-config already exist')
            self.statusbar.showMessage("file br-config already exist")
        else:
            with open(os.path.join(self.work_directory,"br-config"), 'w') as fp:
                fp.write("#!/bin/sh \n")
                fp.write("make -C /home/lark/buildroot \n")
                fp.write("ARCH = arm \n")
                fp.write("BR2_EXTERNAL = $PWD/apps \n ")
                #fp.write("#!BR2_JLEVEL = "$(($(nproc) -2)) \n"" )
                fp.close()

        # creating some  dir..es
        path = self.work_directory + '/apps'
        if os.path.exists(path):
            print('dir already exist')
        else:
            os.mkdir(path)

        path = self.work_directory + '/buildroot'
        if os.path.exists(path):
            print('dir already exist')
        else:
            os.mkdir(path)

        path = self.work_directory + '/kernel'
        if os.path.exists(path):
            print('dir already exist')
        else:
            os.mkdir(path)

        path = self.work_directory + '/u-boot'
        if os.path.exists(path):
            print('dir already exist')
        else:
            os.mkdir(path)

        res = True    #debug
        if res == True:
            QMessageBox.information(self, 'LARK', 'Workspace Sucssesfully created')
    def action_push(self):
        a=10
        #print('action push')
        #result = QMessageBox.question(self,'Disk Full ','LARK information')
        #result = QInputDialog.getText(self,'','Ну',text='введите')
        #result = QFileDialog.getOpenFileName(self,'','d:/SHARE/dt/','image File (*.jpg)')
        self.work_directory = QFileDialog.getExistingDirectory(self,'select directory','/home/lark')
        #print(type(work_directory))
        self.pushButton_Select_Work_Directory.setFlat(True)
        self.lineEdit_Work_Directory.setText(self.work_directory)
def main():
        app=QApplication(sys.argv)
        window = ExampleApp()
        window.show()
        app.exec_()
if __name__ =='__main__':
    main()