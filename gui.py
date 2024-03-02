import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
import easyocr

class ImageReader(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Text Reader")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.image_label = QLabel("Görsel burada görünecek")
        self.layout.addWidget(self.image_label)

        self.load_button = QPushButton("Görsel Yükle")
        self.load_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_button)

        self.text_label = QLabel("Metin burada görünecek")
        self.layout.addWidget(self.text_label)

        self.setLayout(self.layout)

    def load_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Görsel Yükle", "", "Image files (*.jpg *.png *.jpeg *.bmp *.gif)", options=options)
        if file_path:
            self.process_image(file_path)

    def process_image(self, file_path):
        reader = easyocr.Reader(['en']) # Sadece İngilizce metinleri okuyoruz
        results = reader.readtext(file_path)

        text = ""
        for detection in results:
            text += detection[1] + "\n"

        self.text_label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageReader()
    window.show()
    sys.exit(app.exec_())
