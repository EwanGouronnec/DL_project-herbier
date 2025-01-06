from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
import PySide6
import sys, os
from Window_ui import SearchEngine  # Remplacez par le bon nom du fichier contenant SearchEngine
import torch
import clip
import cv2
import json
from PySide6.QtGui import QPixmap

# Charger le modèle CLIP
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model, preprocess = clip.load("ViT-B/32", device=device)

# Charger le fichier des descriptions
with open('descriptions.json') as jsonfile:
    descriptions = json.load(jsonfile)

class Window_run(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.search_window = SearchEngine()
        self.setCentralWidget(self.search_window)
        
        self.pixmap = None
        self.zoom_factor = 1.0

        # Connexion du bouton SearchButton à la méthode startSearch
        self.search_window.SearchButton.clicked.connect(self.startSearch)
        
        # Ajouter les boutons Zoom In et Zoom Out
        self.search_window.ZoomIn.clicked.connect(self.zoom_in)
        self.search_window.ZoomOut.clicked.connect(self.zoom_out)
        
    
    def startSearch(self):
        """Effectuer la recherche d'image à partir de la saisie utilisateur."""
        query = self.search_window.SearchEdit.text().strip()
        if not query:
            return

        # Calculer le vecteur de caractéristiques du texte saisi
        text_features = clip.tokenize([query]).to(device)
        with torch.no_grad():
            text_features = model.encode_text(text_features).float()

        # Rechercher l'image correspondante
        best_match_path, best_score = self.searchImage(text_features)

        # Afficher l'image si une correspondance a été trouvée
        if best_match_path:
            self.displayImage(best_match_path)
    
    def searchImage(self, text_features):
        """Rechercher l'image la plus similaire à la requête texte."""
        best_match_path = None
        best_score = -float('inf')

        self.label.clear()
        print("Recherche en cours, veuillez patienter...")

        c = 0

        for desc in descriptions:
            image_path = os.path.join('images', desc['code'] + '.jpg')
            if not os.path.exists(image_path):
                continue

            # Lire l'image et la convertir au format PIL.Image
            from PIL import Image
            image = Image.fromarray(cv2.imread(image_path)[:, :, ::-1])
            image = preprocess(image).unsqueeze(0).to(device)

            # Calculer la similarité
            with torch.no_grad():
                image_features = model.encode_image(image).float()
            similarity = (text_features @ image_features.T).squeeze().item()

            if similarity > best_score:
                best_match_path = image_path
                best_score = similarity

            c += 1
            print(f"Recherche n° {c} | Meilleur score : {best_score}")

        return best_match_path, best_score
    
    def displayImage(self, image_path):
        """Affiche l'image trouvée dans l'interface."""
        self.pixmap = QPixmap(image_path)
        self.update_image()
    
    def update_image(self):
        """Met à jour l'affichage de l'image dans self.Image avec le facteur de zoom."""
        if self.pixmap:
            scaled_pixmap = self.pixmap.scaled(
                self.search_window.Image.size() * self.zoom_factor,  # Adapter à la taille de self.Image
                PySide6.QtCore.Qt.KeepAspectRatio
            )
            self.search_window.Image.setPixmap(scaled_pixmap)
    def zoom_in(self):
        """Zoom avant sur l'image."""
        self.zoom_factor *= 1.1
        self.update_image()

    def zoom_out(self):
        """Zoom arrière sur l'image."""
        self.zoom_factor *= 0.9
        self.update_image()
    
if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication([])
    else:
        app = QApplication.instance()
    window = Window_run()
    window.show()
    sys.exit(app.exec())
