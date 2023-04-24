import cv2  
import numpy as np
import face_recognition

if __name__ == "__main__":
    exitt=cv2.VideoWriter("sierra,india.avi",cv2.VideoWriter_fourcc(*"XVID"),20.0,(640,480))
    camera = cv2.VideoCapture(0)
    _, frame = camera.read()

    frameRGB = cv2.cvtColor ( frame , cv2.COLOR_BGR2RGB )
    boxes = face_recognition.face_locations(frameRGB)

    if boxes:
        box = boxes[0]
        cx = (box[3] + box[1])/2
        cy = (box[0] + box[2])/2
    else:
        cx = 0
        cy = 0
    
    MIN_MOVE = 10
    while True:
        _, frame = camera.read()
        frameRGB = cv2.cvtColor ( frame , cv2.COLOR_BGR2RGB )
        boxes = face_recognition.face_locations(frameRGB)

        if boxes:
            box = boxes[0]
            new_cx = (box[3] + box[1])/2
            new_cy = (box[0] + box[2])/2

            cv2.rectangle ( frame ,(box[3],box[2]) , (box[1],box[0]) , (0,0,255) ,2 )

            if abs(new_cx - cx) > abs(new_cy - cy):
                if new_cx - cx > MIN_MOVE:
                    print("LEFT")
                elif new_cx - cx < -MIN_MOVE:
                    print("RIGHT")
            else:
                if new_cy - cy > MIN_MOVE:
                    print("DOWN")
                elif new_cy - cy < -MIN_MOVE:
                    print("UP")
            cx = new_cx
            cy = new_cy
            
        cv2.imshow ( "si" , frame )
        exitt.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break


camera.release()
exitt.release()
cv2.destroyAllWindows()

            