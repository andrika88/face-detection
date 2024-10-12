import cv2

frontalface = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

camera = cv2.VideoCapture(0)

def face_detect(frame):
    optimized_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    face = frontalface.detectMultiScale(optimized_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return face

def draweer_box(frame):
    for (x, y, w, h) in face_detect(frame):
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    pass

def close_camera():
    camera.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        _, frame = camera.read()
        
        draweer_box(frame)

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            close_camera()

if __name__ == "__main__":
    main()