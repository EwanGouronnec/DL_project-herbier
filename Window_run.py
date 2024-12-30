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

# 加载描述文件
with open('descriptions.json') as jsonfile:
    descriptions = json.load(jsonfile)

class Window_run(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        # 为搜索按钮绑定事件
        self.searchButton.clicked.connect(self.startSearch)
    
    def startSearch(self):
        # 从搜索框中获取用户输入
        query = self.lineEdit.text().strip()
        print(query)
        if not query:
            return

        # 计算输入文本的特征向量
        text_features = clip.tokenize([query]).to(device)
        with torch.no_grad():
            text_features = model.encode_text(text_features).float()
        
        # 搜索图片
        best_match_path, best_score = self.searchImage(text_features)

        # 如果找到匹配的图片，则在界面中显示
        if best_match_path:
            self.displayImage(best_match_path)

    def searchImage(self, text_features):
        best_match_path = None
        best_score = -float('inf')
    
        for desc in descriptions:
            image_path = os.path.join('images', desc['code'] + '.jpg')
            if not os.path.exists(image_path):
                continue
        
            # 读取图片并转换为 PIL.Image 格式
            from PIL import Image  # 确保导入 PIL 库
            image = Image.fromarray(cv2.imread(image_path)[:, :, ::-1])  # 将 numpy 转换为 PIL.Image
            image = preprocess(image).unsqueeze(0).to(device)  # 预处理并转换为张量

            # 计算文本与图片特征之间的相似性
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