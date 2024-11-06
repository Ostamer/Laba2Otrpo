import cv2
import sys
import os

# Используем универсальный путь для каскада Хаара
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def detect_faces(image_path):
    # Проверка наличия файла каскада
    if not os.path.exists(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'):
        print("Cascade file not found.")
        return

    # Загружаем изображение и преобразуем в оттенки серого
    image = cv2.imread(image_path)
    if image is None:
        print(f"Could not open or find the image: {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    print(f"Found {len(faces)} face(s) in the image.")
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Сохраняем результат с обнаруженными лицами
    result_path = os.path.join(os.path.dirname(image_path), 'result_with_faces.jpg')
    cv2.imwrite(result_path, image)
    print(f"Result saved as {result_path}")


if __name__ == "__main__":
    # Берем изображение из текущей директории по умолчанию, если путь не передан
    image_path = sys.argv[1] if len(sys.argv) == 2 else os.path.join(os.getcwd(), 'image.jpg')

    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
    else:
        detect_faces(image_path)