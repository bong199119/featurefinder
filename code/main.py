import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QLabel, QWidget, QHBoxLayout, QCheckBox, QDesktopWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.index = 0
        self.image_paths = []

        # 메뉴바 생성 및 불러오기 액션 추가
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        open_folder_action = QAction('폴더 선택', self)
        open_folder_action.triggered.connect(self.load_images)
        file_menu.addAction(open_folder_action)

        # 이미지를 표시할 QLabel 위젯 생성
        self.image_label = QLabel(self)
        self.image_label.setScaledContents(False)
        # self.image_label.resize(2000, 1200)
        self.image_label.setFixedSize(1000, 800)
        self.image_label.setStyleSheet("color: #FF5733; border-style: solid; border-width: 2px; border-color: #FFC300; border-radius: 10px; ")

        # 이미지 이름을 저장할 체크박스 위젯 생성
        # self.save_checkbox = QCheckBox('이미지 이름 저장', self)

        # 위젯 배치
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.image_label)
        # main_layout.addWidget(self.save_checkbox)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.resize(2000, 1200)
        self.center()

    def center(self):
        # 현재 사용 중인 데스크톱의 정보 가져오기
        desktop = QDesktopWidget().screenGeometry()

        # 윈도우의 위치와 크기 가져오기
        window_size = self.geometry()
        x = (desktop.width() - window_size.width()) / 2
        y = (desktop.height() - window_size.height()) / 2

        # 윈도우 위치 설정
        self.move(x, y)
        

    def load_images(self):
        # 폴더 선택 다이얼로그 실행
        directory = QFileDialog.getExistingDirectory(self, '폴더 선택', '')

        # 선택된 폴더 내의 이미지 파일 경로 가져오기
        image_paths = []
        for filename in os.listdir(directory):
            if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.bmp'):
                image_paths.append(os.path.join(directory, filename))

        # 이미지 파일이 없으면 함수 종료
        if not image_paths:
            return
        self.index = 0
        self.image_paths = image_paths
        self.len_images = len(image_paths)
        # 첫번째 이미지를 QLabel 위젯에 표시
        pixmap = QPixmap(image_paths[self.index])
        pixmap = pixmap.scaledToWidth(1000)
        self.image_label.setPixmap(pixmap)

        

    def load_image(self):        
        # 첫번째 이미지를 QLabel 위젯에 표시
        pixmap = QPixmap(self.image_paths[self.index])
        pixmap = pixmap.scaledToWidth(1000)
        self.image_label.setPixmap(pixmap)

        # # 이미지 이름 저장 체크박스가 체크된 경우, 모든 이미지 이름을 파일에 저장
        # if self.save_checkbox.isChecked():
        #     with open('image_names.txt', 'a') as f:
        #         for path in image_paths:
        #             f.write(path + '\n')

    def keyPressEvent(self, e): #키가 눌러졌을 때 실행됨
        if e.key() == Qt.Key_D:
            if self.index != self.len_images-1:
                self.index += 1
            self.load_image()
            print("esc pressed")
        elif e.key() == Qt.Key_A:
            if self.index != 0:
                self.index -= 1
            self.load_image()
            print("A is pressed)")
        else:
            print((e.key()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
