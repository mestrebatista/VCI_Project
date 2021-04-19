import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

out = cv.VideoWriter("TestCaptureVideo.avi",cv.VideoWriter_fourcc(*"MJPG"), 30,(640,480))

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.flip(frame, 1)

    # write the flipped frame
    out.write(frame)

    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
out.release()
cv.destroyAllWindows()

