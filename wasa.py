import cv2

# Clase Camera
class Camera:
    def __init__(self, index: int, width: int, height: int):
        self.cap = cv2.VideoCapture(index)
        self.cap.set(3, width)  # Ancho
        self.cap.set(4, height)  # Alto

    def read(self):
        ret, frame = self.cap.read()
        return ret, frame

    def release(self):
        self.cap.release()


if __name__ == "__main__":
    # Cambia el índice a 0 para usar la cámara predeterminada
    camera = Camera(0, 1280, 720)  # Cambia 0 por la ruta de un video si es necesario

    while True:
        ret, frame = camera.read()
        if not ret:
            print("No se pudo leer el frame. Asegúrate de que la cámara esté conectada.")
            break
        
        # Mostrar el frame en una ventana
        cv2.imshow("Video Stream", frame)

        # Salir si se presiona 'Esc'
        if cv2.waitKey(1) & 0xFF == 27:  # 27 es la tecla 'Esc'
            break

    camera.release()
    cv2.destroyAllWindows()
