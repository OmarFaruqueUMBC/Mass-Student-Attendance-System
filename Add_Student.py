import cv2
import sqlite3
from PyQt4 import QtGui,QtCore



class AddStudentData(QtGui.QMainWindow):
    #Registration window for adding student information
    
    def __init__(self):
        super(AddStudentData, self).__init__()
        
        #Creating Registration Window 
        self._main_window = None
        self.setGeometry(300,50,800,660)
        self.setWindowTitle("Add Student")
        self.setWindowIcon(QtGui.QIcon('images/DUET.png'))

        self.count = 0

        #Heading
        h=QtGui.QLabel(self)
        h.setAlignment(QtCore.Qt.AlignCenter)
        h.setGeometry(QtCore.QRect(100,30,600,60))
        h.setStyleSheet("QLabel { background-color : blue;color :white ; }")
        font=QtGui.QFont("Times",20,QtGui.QFont.Bold)
        h.setFont(font)
        h.setText("Student Information")

        #Pseudo photo ID to be replaced by Student's Photo
        self.pic=QtGui.QLabel(self)
        self.pic.setGeometry(50,120,320,320)
        self.pic.setPixmap(QtGui.QPixmap("images/default.png"))

        #Button for opening Webcam and take photo 
        b=QtGui.QPushButton(self)
        b.setText("Take Picture")
        b.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        b.setGeometry(100,420,100,30)
        b.clicked.connect(self.take_photo)

        #SET OF ENTRIES
        #Taking Student's Name
        l1=QtGui.QLabel(self)
        l1.setAlignment(QtCore.Qt.AlignCenter)
        l1.setGeometry(QtCore.QRect(310,150,130,30))
        l1.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        font=QtGui.QFont("Times",14,QtGui.QFont.Bold)
        l1.setFont(font)
        l1.setText("NAME")

        self.e1=QtGui.QLineEdit(self)
        self.e1.setGeometry(450,150,300,30)
        self.e1.setAlignment(QtCore.Qt.AlignCenter)
        font1=QtGui.QFont("Arial",14)
        self.e1.setFont(font1)

        #Taking Student's Registration Number
        l2=QtGui.QLabel(self)
        l2.setAlignment(QtCore.Qt.AlignCenter)
        l2.setGeometry(QtCore.QRect(310,250,130,30))
        l2.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        l2.setFont(font)
        l2.setText("Std ID.")

        self.e2=QtGui.QLineEdit(self)
        self.e2.setGeometry(450,250,300,30)
        self.e2.setAlignment(QtCore.Qt.AlignCenter)
        self.e2.setFont(font1)

        #Taking Student's Year of Study
        l3=QtGui.QLabel(self)
        l3.setAlignment(QtCore.Qt.AlignCenter)
        l3.setGeometry(QtCore.QRect(310,350,130,30))
        l3.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        l3.setFont(font)
        l3.setText("YEAR")
      
        self.e3=QtGui.QLineEdit(self)
        self.e3.setGeometry(450,350,300,30)
        self.e3.setAlignment(QtCore.Qt.AlignCenter)
        self.e3.setFont(font1)

        #Display Student Picture Count
        self.l4=QtGui.QLabel(self)
        self.l4.setAlignment(QtCore.Qt.AlignCenter)
        self.l4.setGeometry(QtCore.QRect(310,450,180,30))
        self.l4.setStyleSheet("QLabel { background-color : gray;color :black ; }")
        self.l4.setFont(font)
        self.l4.setText('Picture Count : ' +  str(self.count) )
      
        #Display Message to close Video
        self.l6=QtGui.QLabel(self)
        self.l6.setAlignment(QtCore.Qt.AlignCenter)
        self.l6.setGeometry(QtCore.QRect(40,600,400,30))
        self.l6.setStyleSheet("QLabel { background-color : yellow;color :red ; }")
        self.l6.setFont(font)
        self.l6.setText('To close Video press ESC button twice!!' )

        #Button for clearing fields 
        b2=QtGui.QPushButton(self)
        b2.setText("RESET")
        b2.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        b2.setGeometry(650,550,100,30)
        b2.setStyleSheet("QPushButton { background-color : red ;color : white ; }")
        self.entries=[self.e1,self.e2,self.e3]
        b2.clicked.connect(self.erase)

        #Label for displaying message
        self.l5=QtGui.QLabel(self)
        self.l5.setAlignment(QtCore.Qt.AlignCenter)
        self.l5.setStyleSheet("QLabel {  color:green ; }")
        self.l5.setFont(QtGui.QFont('Times',13))
        
        #Button for submission of data and storing in database 
        b1=QtGui.QPushButton(self)
        b1.setText("SAVE")
        b1.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        b1.setGeometry(520,550,100,30)
        b1.setStyleSheet("QPushButton { background-color : green;color : white ; }")
        b1.clicked.connect(self.store_in_database)

        #Button for displaying Main page 
        b1=QtGui.QPushButton(self)
        b1.setText("Home")
        b1.setFont(QtGui.QFont("Times",12,QtGui.QFont.Bold))
        b1.setGeometry(520,600,100,30)
        b1.setStyleSheet("QPushButton { background-color : green;color : white ; }")
        b1.clicked.connect(self.create_main_window)
            
    def create_main_window(self):
        #Function for opening Registration window
        from Home_Page import MainWindow
        self._main_window = MainWindow()
        self._main_window.show()
        self.close()
    
    def erase(self):
        #function for clearing fields and changing to default
        for entry in self.entries:
            entry.clear()
        self.count = 1
        self.pic.setPixmap(QtGui.QPixmap("other_images/default.png"))
        self.l4.setText("")
        self.l4.setText('Picture Count : ' +  str(self.count) )
        self.l5.setText("")
    
    def take_photo(self):
        #Function for clicking,displaying and storing photo
        check_value = self.check()
        if (check_value == 1):
            self.l5.setGeometry(QtCore.QRect(40,500,250,30))
            self.l5.setText("Invalid Name")
        elif (check_value == 2):
            self.l5.setGeometry(QtCore.QRect(40,500,250,30))
            self.l5.setText("Invalid Roll / Out of Range")
        elif (check_value == 3):
            self.l5.setGeometry(QtCore.QRect(40,500,250,30))
            self.l5.setText("Year should be between 1 to 4")
        elif (self.count == 30):
            self.l5.setGeometry(QtCore.QRect(40,500,250,30))
            self.l5.setText("Maximim 30 pictures per student")
        else:
            cam = cv2.VideoCapture(0)
            cam.set(3, 640) # set video width
            cam.set(4, 480) # set video height
            face_detector = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
            self.count += 1
            while(True):
                ret, img = cam.read()
                img = cv2.flip(img, 1) # flip video image vertically
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_detector.detectMultiScale(
                    gray,
                    scaleFactor=1.3,
                    minNeighbors=5
                )
                for (x,y,w,h) in faces:
                    print("x: " + str(x) +" y: "+ str(y) + " w: "+ str(w) +" h: " + str(h) )
                    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                    cv2.imshow('video',img)
                    wait1 = cv2.waitKey(10) & 0xff  
                    # Save the captured image into the datasets folder
                    std_image=gray[y:y+h,x:x+w]
                    cv2.imwrite("dataset/User." + str(self.e2.text()) + '.' +  str(self.count) + ".jpg", std_image)
                    print("x: " + str(x) +" y: "+ str(y) + " x+w: "+ str(x+w) +" y+h: " + str(y+h) )
                    #cv2.imshow('image', img)
                k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
                if k == 27:
                    break


            cam.release()
            cv2.destroyAllWindows()
            self.pic.setPixmap(QtGui.QPixmap(str(r'dataset/User.' + str(self.e2.text()) + '.' +  str(self.count) +'.jpg')))
            self.l4.setText('Picture Count : ' +  str(self.count) )

    def store_in_database(self):
        #Function for storing information in database
        check_value = self.check()
        print ('>>', check_value)
        if (check_value == 0):
            conn=sqlite3.connect('Attendance.db')
            c=conn.cursor()
            (id,name,year)=(int(self.e2.text()),self.e1.text(),int(self.e3.text()))
            c.execute('INSERT INTO STUDENTS (id, name, year) VALUES(?,?,?)',(id,name,year))
            conn.commit()
            c.close()
            conn.close()
            #Displaying message after successful submission 
            self.l5.setGeometry(QtCore.QRect(40,500,250,30))
            self.l5.setText("Successfully Saved..")
            self.erase()
        elif (check_value == 1):
            self.l5.setGeometry(QtCore.QRect(40,500,250,30))
            self.l5.setText("Invalid Name")
        elif (check_value == 2):
            self.l5.setGeometry(QtCore.QRect(40,500,250,30))
            self.l5.setText("Roll - Out of Range")
        elif (check_value == 3):
            self.l5.setGeometry(QtCore.QRect(40,500,250,30))
            self.l5.setText("Year should be between 1 to 4")
        elif (check_value == 4):
            self.l5.setGeometry(QtCore.QRect(40,500,250,30))
            self.l5.setText("Click again please.")
            

    def check(self):
        name = self.e1.text()
        if (len(name) == 0):
            return 1
        
        for i in range(10):
            if (str(i) in name):
                return 1
        
        try:
            roll = int(self.e2.text())
            print("\n [INFO] roll is : " + self.e2.text())
            r_len = len(self.e2.text())
            if (r_len < 6 ):
                return 2
            if (roll < 10000):
                return 2
        except:
            return 2
        
        try:
            year = int(self.e3.text())
            if (year < 1 or year > 4):
                return 3
        except:
            return 3
        
        return 0
    

if __name__ == '__main__':  
    app = QtGui.QApplication([])
    gui = AddStudentData()
    gui.show()
    app.exec_()
