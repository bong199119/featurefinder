import sys
from PyQt5.QtGui import QPixmap, QPainter, QPolygonF
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsPolygonItem

class MainWindow(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        pixmap = QPixmap(r"D:\project\featurefinder\data\2021.05.25.8828782.F.84.GC.Lap.STG.D1.B2-frame.edit_00004712.png")
        self.imageItem = self.scene.addPixmap(pixmap)
        self.setScene(self.scene)
        self.polygonItem = None
        self.polygonPoints = []

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            point = self.mapToScene(event.pos())
            self.polygonPoints.append(point)
            if len(self.polygonPoints) == 1:
                self.polygonItem = self.scene.addLine(point.x(), point.y(), point.x(), point.y(), pen=Qt.red)
            else:
                lastPoint = self.polygonPoints[-2]
                self.scene.removeItem(self.polygonItem)
                polygon = QPolygonF([lastPoint, point])
                self.polygonItem = QGraphicsPolygonItem(polygon)
                self.polygonItem.setPen(Qt.red)
                self.scene.addItem(self.polygonItem)

    def mouseMoveEvent(self, event):
        if self.polygonItem is not None:
            point = self.mapToScene(event.pos())
            lastPoint = self.polygonPoints[-1]
            polygon = QPolygonF([lastPoint, point])
            self.scene.removeItem(self.polygonItem)
            self.polygonItem = QGraphicsPolygonItem(polygon)
            self.polygonItem.setPen(Qt.red)
            self.scene.addItem(self.polygonItem)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            point = self.mapToScene(event.pos())
            self.polygonPoints.append(point)
            lastPoint = self.polygonPoints[-2]
            polygon = QPolygonF([lastPoint, point])
            self.scene.removeItem(self.polygonItem)
            self.polygonItem = QGraphicsPolygonItem(polygon)
            self.polygonItem.setPen(Qt.red)
            self.scene.addItem(self.polygonItem)
            self.polygonItem = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
