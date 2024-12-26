from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from bs4 import BeautifulSoup
import requests 

# beautifulsoup to get live exchange rate 
def get_exchange(input_curr='CAD', output_curr='USD'):
    url = f"https://www.x-rates.com/calculator/?from={input_curr}&to={output_curr}&amount={amount}"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt")
    rate = float(rate[:-4]) # exlcude code

    return rate
    


# slot function
def show_conversion():
    input_amount = amount.text()






app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency App")
window.resize(300, 400)

layout = QVBoxLayout()

# select input currency


# select output currency



# amount entry 
amount = QLineEdit()
layout.addWidget(amount)


# validate button 
btn = QPushButton('Convert')
layout.addWidget(btn)
btn.clicked.connect(show_conversion)


# output value
output_label = QLabel('')
layout.addWidget(output_label)




# output
window.setLayout(layout)
window.show()
app.exec()
