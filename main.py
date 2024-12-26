from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit


# function to get converted rate
def get_conversion():
    return 0


app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency App")
window.resize(300, 400)

layout = QVBoxLayout()

# select input currency


# select output currency



# amount entry 


# validate button 
btn = QPushButton('Calculate')
layout.addWidget(btn)
btn.clicked.connect(get_conversion)


# output value
output_label = QLabel('')
layout.addWidget(output_label)




# output
window.setLayout(layout)
window.show()
app.exec()
