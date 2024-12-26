from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
from bs4 import BeautifulSoup
import requests 


# VERSION2 SUPPORT FOR ANY CURRENCY 


# beautifulsoup to get live exchange rate 
def get_exchange(input_curr='EUR', output_curr='CAD'):
    url = f"https://www.x-rates.com/calculator/?from={input_curr}&to={output_curr}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4]) # exlcude code

    return rate
    

# slot function
def show_conversion():
    amount = float(text.text())
    rate = get_exchange()
    result = amount*rate
    rounded_rate = round(result,2)
    output_label.setText(str(rounded_rate))


app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency App")
window.resize(300, 400)

layout = QVBoxLayout()

# input currency dropdown 
in_combo = QComboBox()
currencies = ['USD', 'EUR', 'INR', 'CAD', 'GBP', 'AUD', 'JPY', 'CNY']
in_combo.addItems(currencies)
layout.addWidget(in_combo)


# output currency dropdown
to_combo = QComboBox()
to_combo.addItems(currencies)
layout.addWidget(to_combo)




# amount entry 
text = QLineEdit()
layout.addWidget(text)


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
