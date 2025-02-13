import cv2
import numpy as np
import os 
import sqlite3
from datetime import datetime

def recognize_student(teacher_id, course_id, year):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "Cascades/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX

    conn=sqlite3.connect('Attendance.db')
    c=conn.cursor()

    #iniciate id counter
    id = 0
    present = []

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:
        ret, img =cam.read()
        img = cv2.flip(img, 1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                
            # If confidence is less them 100 ==> "0" : perfect match 
            if (confidence < 100):
                #id = names[id]
                if not (id in present):
                    present.append(id)
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
        
            cv2.putText(
                        img, 
                        str(id), 
                        (x+5,y-5), 
                        font, 
                        1, 
                        (255,255,255), 
                        2
                    )
            cv2.putText(
                        img, 
                        str(confidence), 
                        (x+5,y+h-5), 
                        font, 
                        1, 
                        (255,255,0), 
                        1
                    )  
    
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break  # Do a bit of cleanup

    query='SELECT * FROM students where year ={};'.format(year)
    c.execute(query)
    rolls = []
    for row in c.fetchall():
        rolls.append(row[0])

    print(present)

    temp = ""
    cur_date = datetime.now().strftime("%Y-%m-%d")
    for r in rolls:
        if (r in present):
            temp = temp + str(r) + ", "
            values = (cur_date, course_id, teacher_id, year,r,'P')
        else:
            values = (cur_date, course_id, teacher_id, year,r,'A')
        query='''INSERT INTO attendance (Date,course,teacher,year,id,status) VALUES (?,?,?,?,?,?)'''
        print (query, ','.join([ str(i) for i in values]) )
        c.execute(query, values)


    conn.commit()
    c.close()
    conn.close()

    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
    return temp