
from PyQt4 import QtGui,QtCore
from face_recognition import recognize_student


class AttendanceWindow(QtGui.QMainWindow):
    #Attendance Window
    def __init__(self):
        super(AttendanceWindow, self).__init__()
        self.setGeometry(300,50,800,600)
        self.setWindowTitle("Record Attendance")
        self.setWindowIcon(QtGui.QIcon('images/DUET.png'))

        #Heading
        h=QtGui.QLabel(self)
        h.setAlignment(QtCore.Qt.AlignCenter)
        h.setGeometry(QtCore.QRect(200,20,400,50))
        h.setStyleSheet("QLabel { background-color : blue;color :white ; }")
        font=QtGui.QFont("Times",20,QtGui.QFont.Bold)
        h.setFont(font)
        h.setText("ATTENDANCE")

        #Taking Student's Name
        l1=QtGui.QLabel(self)
        l1.setAlignment(QtCore.Qt.AlignCenter)
        l1.setGeometry(QtCore.QRect(150,100,130,30))
        l1.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        font=QtGui.QFont("Times",14,QtGui.QFont.Bold)
        l1.setFont(font)
        l1.setText("Teacher ID.")

        self.e1=QtGui.QLineEdit(self)
        self.e1.setGeometry(290,100,300,30)
        self.e1.setAlignment(QtCore.Qt.AlignCenter)
        font1=QtGui.QFont("Arial",14)
        self.e1.setFont(font1)

        #Taking Student's Registration Number
        l2=QtGui.QLabel(self)
        l2.setAlignment(QtCore.Qt.AlignCenter)
        l2.setGeometry(QtCore.QRect(150,175,130,30))
        l2.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        l2.setFont(font)
        l2.setText("Course ID.")

        self.e2=QtGui.QLineEdit(self)
        self.e2.setGeometry(290,175,300,30)
        self.e2.setAlignment(QtCore.Qt.AlignCenter)
        self.e2.setFont(font1)

        #Taking Student's Year of Study
        l3=QtGui.QLabel(self)
        l3.setAlignment(QtCore.Qt.AlignCenter)
        l3.setGeometry(QtCore.QRect(150,250,130,30))
        l3.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        l3.setFont(font)
        l3.setText("YEAR")
      
        self.e3=QtGui.QLineEdit(self)
        self.e3.setGeometry(290,250,300,30)
        self.e3.setAlignment(QtCore.Qt.AlignCenter)
        self.e3.setFont(font1)

        #Label for displaying message
        self.l5=QtGui.QLabel(self)
        self.l5.setAlignment(QtCore.Qt.AlignCenter)
        self.l5.setStyleSheet("QLabel {  color:green ; }")
        self.l5.setFont(QtGui.QFont('Times',13))

        #Recording Button
        b1=QtGui.QPushButton(self)
        b1.setText("RECORD ATTENDANCE")
        b1.setStyleSheet("QPushButton { background-color : gray;color : black ; }")
        b1.setFont(font)
        b1.setGeometry(250,300,300,50)
        b1.clicked.connect(self.record_attendance)


        #Button for displaying Main page 
        b3=QtGui.QPushButton(self)
        b3.setText("Home")
        b3.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        b3.setGeometry(560,500,100,30)
        b3.setStyleSheet("QPushButton { background-color : green;color : white ; }")
        b3.clicked.connect(self.create_main_window)
        
    def create_main_window(self):
        #Function for opening Registration window
        from Home_Page import MainWindow
        self._main_window = MainWindow()
        self._main_window.show()
        self.close()


    def record_attendance(self):
        result = recognize_student(self.e1.text(), self.e2.text(), self.e3.text())
        self.l5.setGeometry(QtCore.QRect(40,400,500,30))
        self.l5.setText("Present Students: " + result)



        
        
            
if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = AttendanceWindow()
    gui.show()
    app.exec_()
