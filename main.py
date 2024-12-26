from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit


app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency App")
window.resize(300, 400)

layout = QVBoxLayout()

# select input currency


# select output currency



# amount entry 


# validate button 
















window.setLayout(layout)
window.show()
app.exec()
