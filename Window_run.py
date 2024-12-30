from Window_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
import torch
import clip
import cv2
import os, sys
import json
from PySide6.QtGui import QPixmap, QImage

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model, preprocess = clip.load("ViT-B/32", device=device)

# Charger le fichier des descriptions
with open('descriptions.json') as jsonfile:
    descriptions = json.load(jsonfile)

class Window_run(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        # Connecter l'événement du bouton de recherche
        self.searchButton.clicked.connect(self.startSearch)
    
    def startSearch(self):
        # Obtenir la saisie de l'utilisateur depuis la barre de recherche
        query = self.lineEdit.text().strip()
        #print(query)
        if not query:
            return

        # Calculer le vecteur de caractéristiques du texte saisi
        text_features = clip.tokenize([query]).to(device)
        with torch.no_grad():
            text_features = model.encode_text(text_features).float()
        
        # Rechercher l'image correspondante
        best_match_path, best_score = self.searchImage(text_features)

        # Si une image correspondante est trouvée, l'afficher dans l'interface
        if best_match_path:
            self.displayImage(best_match_path)

    def searchImage(self, text_features):
        best_match_path = None
        best_score = -float('inf')
    
        for desc in descriptions:
            image_path = os.path.join('images', desc['code'] + '.jpg')
            if not os.path.exists(image_path):
                continue
        
            # Lire l'image et la convertir au format PIL.Image
            from PIL import Image  # Assurer que la bibliothèque PIL est importée
            image = Image.fromarray(cv2.imread(image_path)[:, :, ::-1])  # Convertir numpy en PIL.Image
            image = preprocess(image).unsqueeze(0).to(device)  # Prétraiter et convertir en tenseur

            # Calculer la similarité entre les caractéristiques du texte et de l'image
            with torch.no_grad():
                image_features = model.encode_image(image).float()
            similarity = (text_features @ image_features.T).squeeze().item()
            if similarity > best_score:
                best_match_path = image_path
                best_score = similarity
    
        return best_match_path, best_score

    def displayImage(self, image_path):
        pixmap = QPixmap(image_path)
        label = QLabel()
        label.setPixmap(pixmap.scaled(self.scrollArea.width(), self.scrollArea.height(), Qt.KeepAspectRatio))
        
        layout = QVBoxLayout(self.widget)
        layout.addWidget(label)
        self.widget.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window_run()
    win.show()
    sys.exit(app.exec())