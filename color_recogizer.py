import numpy as np,cv2
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    img = cv2.cvtColor(frame,1)
    color = np.average(np.average(img, axis=0), axis=0)
    c=max(color)
    if c-color[0]<10 and c-color[1]<10 and c-color[2]<10 and c>65.0:
          print("White Color Detected")
    elif c-color[0]<10 and c-color[1]<10 and c-color[2]<10:
          print("Black Color Detected")
    elif c==color[0]:
        print("Blue Color Detected")
    elif c==color[1] :
        print ("Green Color Detected")
    else:
        print ("Red Color Detected")
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

