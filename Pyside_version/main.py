from PySide6.QtWidgets import QApplication
import sys

from controller import PaintController


app = QApplication(sys.argv)
window = PaintController()
window.view.show()
sys.exit(app.exec())
