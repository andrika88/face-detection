import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

video_capture = cv2.VideoCapture(0)

def detect_faces(frame):
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(grayscale_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

def draw_faces(frame):
    for (x, y, w, h) in detect_faces(frame):
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    pass

def close_camera():
    video_capture.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        _, frame = video_capture.read()
        
        draw_faces(frame)

        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            close_camera()

if __name__ == "__main__":
    main()
