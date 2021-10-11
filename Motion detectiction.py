import cv2 
from datetime import datetime

def imageDiff(t0,t1,t2):
    diff1=cv2.absdiff(t2,t1)
    diff2=cv2.absdiff(t1,t0)
    return cv2.bitwise_and(diff1,diff2)

threshold_value=370000


camera=cv2.VideoCapture(0) 
window_name="Motion detecting"
cv2.namedWindow(window_name) 


t_minus=cv2.cvtColor(camera.read()[1],cv2.COLOR_BGR2GRAY)
t=cv2.cvtColor(camera.read()[1],cv2.COLOR_BGR2GRAY)
t_plus=cv2.cvtColor(camera.read()[1],cv2.COLOR_BGR2GRAY)

timeControl=datetime.now()


while True: 

    cv2.imshow(window_name,camera.read()[1])
    

    if cv2.countNonZero(imageDiff(t_minus,t,t_plus))>threshold_value and timeControl !=datetime.now().strftime('%Ss'):
        
        diff_photo=camera.read()[1]
        
        cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f')+'.jpg',diff_photo)
    
    timeControl=datetime.now().strftime('%Ss')
  
    
    t_minus=t
    t=t_plus
    t_plus=cv2.cvtColor(camera.read()[1],cv2.COLOR_BGR2GRAY)
    
   
    key=cv2.waitKey(10)
    if key==27:
        cv2.destroyWindow(window_name)
        camera.release()
        break
    


