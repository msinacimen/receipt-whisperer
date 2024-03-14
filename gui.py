import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QComboBox
from tensorflow import keras
from tensorflow.keras.models import load_model
import easyocr
import pytesseract
from google.cloud import vision
from google.oauth2 import service_account
import io

credentials = service_account.Credentials.from_service_account_file('key.json')

client = vision.ImageAnnotatorClient(credentials=credentials)

# model = load_model("model.h5")

class ImageReader(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Text Reader")
        self.setGeometry(100, 100, 400, 250)

        self.layout = QVBoxLayout()

        self.image_label = QLabel("Görsel burada görünecek")
        self.layout.addWidget(self.image_label)

        self.load_button = QPushButton("Görsel Yükle")
        self.load_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_button)

        self.ocr_selector = QComboBox()
        self.ocr_selector.addItems(["EasyOCR", "Tesseract OCR", "Google Vision API"])
        self.layout.addWidget(self.ocr_selector)

        self.text_label = QLabel("Metin burada görünecek")
        self.layout.addWidget(self.text_label)

        self.setLayout(self.layout)

    def load_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Görsel Yükle", "", "Image files (*.jpg *.png *.jpeg *.bmp *.gif)", options=options)
        if file_path:
            self.process_image(file_path)

    def process_image(self, file_path):
        ocr_method = self.ocr_selector.currentText()

        if ocr_method == "EasyOCR":
            reader = easyocr.Reader(["tr"])
            result = reader.readtext(file_path)
            text = " ".join([x[1] for x in result])
            self.text_label.setText(text)
        elif ocr_method == "Tesseract OCR":  # Tesseract OCR
            text = pytesseract.image_to_string(file_path, lang="tur")
            self.text_label.setText(text)
        else:  # Google Cloud Vision
            with io.open(file_path, 'rb') as image_file:
                content = image_file.read()

            image = vision.Image(content=content)

            response = client.text_detection(image=image)
            texts = response.text_annotations

            if texts:
                text = texts[0].description
                print(text)
                # prediction = model.predict(text)

                self.text_label.setText(text)
            else:
                print("Metin tespit edilemedi.")

            print(text)
            self.text_label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageReader()
    window.show()
    sys.exit(app.exec_())
