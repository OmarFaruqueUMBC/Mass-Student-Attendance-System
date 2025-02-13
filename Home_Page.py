from PyQt4 import QtGui,QtCore
from Add_Student import AddStudentData
from face_training import train
from Record_Attendance import AttendanceWindow

class MainWindow(QtGui.QMainWindow):
    #Main Window of Interface
    def __init__(self):
        super(MainWindow, self).__init__()
        self._registration_window = None
        self._attendance_window = None
        self.setGeometry(300,50,800,600)
        self.setWindowTitle("Attendance System")
        self.setWindowIcon(QtGui.QIcon('images/DUET.png'))

        #Heading
        h=QtGui.QLabel(self)
        h.setAlignment(QtCore.Qt.AlignCenter)
        h.setGeometry(QtCore.QRect(100,30,600,60))
        h.setStyleSheet("QLabel { background-color : blue;color :white ; }")
        font=QtGui.QFont("Times",20,QtGui.QFont.Bold)
        h.setFont(font)
        h.setText("ATTENDANCE SYSTEM")

        #Registration Button for opening registration window
        b1=QtGui.QPushButton(self)
        b1.setText("ADD STUDENT")
        font1=QtGui.QFont("Times",16,QtGui.QFont.Bold)
        b1.setFont(font1)
        b1.setGeometry(450,200,200,50)
        b1.setStyleSheet("QPushButton { background-color : gray;color :black ; }")
        b1.clicked.connect(self.create_registration_window)

        #Registration Button for opening registration window
        b3=QtGui.QPushButton(self)
        b3.setText("TRAIN MODEL")
        font1=QtGui.QFont("Times",16,QtGui.QFont.Bold)
        b3.setFont(font1)
        b3.setGeometry(450,300,200,50)
        b3.setStyleSheet("QPushButton { background-color : gray;color :black ; }")
        b3.clicked.connect(self.train_model)

        #Attendance Button for opening attendance window
        b2=QtGui.QPushButton(self)
        b2.setText("ATTENDANCE")
        b2.setFont(font1)
        b2.setGeometry(450,400,200,50)
        b2.setStyleSheet("QPushButton { background-color : gray;color :black ; }")
        b2.clicked.connect(self.create_attendance_window)    

        #Label for displaying message
        self.l5=QtGui.QLabel(self)
        self.l5.setAlignment(QtCore.Qt.AlignCenter)
        self.l5.setStyleSheet("QLabel {  color:red ; }")
        self.l5.setFont(QtGui.QFont('Times',13))

        #Adding Logo of college 
        pic =QtGui.QLabel(self)
        pic.setGeometry(150,150,300,350)
        pic.setPixmap(QtGui.QPixmap("images/DUET.png"))

    def create_registration_window(self):
        #Function for opening Registration window
        self._registration_window = AddStudentData()
        self._registration_window.show()
        self.close()
        
    def create_attendance_window(self):
        #Function for opening Attendance window
        self._attendance_window = AttendanceWindow()
        self._attendance_window.show()
        self.close()

    def train_model(self):
        train()
        self.l5.setGeometry(QtCore.QRect(450,360,200,30))
        self.l5.setText("Model training completed.")


if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = MainWindow()
    gui.show()
    app.exec_()
