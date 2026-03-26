import cv2
import os
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

# lần cuối phát hiện khuôn mặt của ae nhá
last_seen = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print('Cannot open camera\nPlease check the camera connection and try again')
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        last_seen = time.time()
        print('user present', end = '\r')
    else:
        print('no face detected', end = '\r')

    if time.time() - last_seen > 5: # dòng này ae có thể chỉnh thời gian khi ae rời khỏi máy bao nhiêu seconds thì nó sẽ khóa
                                    # ví dụ ae muốn dưới 5s thì để last_seen > 5:, còn muốn ít hơn thì tùy ae, ví dụ last_seen > 2: là khi ae rời khỏi máy dưới 2s thì sẽ tự động khóa máy
        print('\nLocking System')
        os.system('rundll32.exe user32.dll,LockWorkStation')
        break

    cv2.imshow('smart lock system', frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()