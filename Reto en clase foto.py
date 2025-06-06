import cv2

# Cargar el clasificador preentrenado (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detectar_persona():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        
        if len(faces) > 0:
            print("✅ Persona detectada")
        else:
            print("❌ No hay persona")

        
        # Dibujar rectángulos (opcional)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.imshow('Detector de Rostros - Haar Cascade', frame)
        
        if cv2.waitKey(1) == 27:  # Presiona ESC para salir
            break
    
    cap.release()
    cv2.destroyAllWindows()

detectar_persona()