import os
import sys
import cv2

# Asegúrate de que la ruta a drowsiness_processor.main sea correcta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from drowsiness_processor.main import DrowsinessDetectionSystem
from camera import Camera


class VideoStream:
    def __init__(self, cam: Camera, drowsiness_detection_system: DrowsinessDetectionSystem):
        self.camera = cam
        self.drowsiness_detection_system = drowsiness_detection_system

    def run(self):
        while True:
            ret, frame = self.camera.read()
            if ret:
                # Procesar el frame con el sistema de detección de somnolencia
                frame, sketch = self.drowsiness_detection_system.frame_processing(frame)

                # Mostrar el frame procesado y el boceto
                cv2.imshow('Emotion Recognition', frame)
                cv2.imshow('3D sketch image', sketch)

                # Salir si se presiona 'Esc'
                if cv2.waitKey(1) & 0xFF == 27:  # 27 es la tecla 'Esc'
                    break
            else:
                print("No se pudo leer el frame. Asegúrate de que la cámara esté conectada.")

        self.camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # Cambia el índice a 0 para usar la cámara predeterminada
    camera = Camera(0, 1280, 720)  # Para usar la cámara
    # camera = Camera("examples/video_example.mp4", 1280, 720)  # Para video

    # Inicializar el sistema de detección de somnolencia
    emotion_recognition_system = DrowsinessDetectionSystem()
    
    # Crear y ejecutar el flujo de video
    video_stream = VideoStream(camera, emotion_recognition_system)
    video_stream.run()
