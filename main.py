from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
from bs4 import BeautifulSoup
import requests 


# VERSION2 SUPPORT FOR ANY CURRENCY 


# beautifulsoup to get live exchange rate 
def get_exchange(input_curr, output_curr):
    url = f"https://www.x-rates.com/calculator/?from={input_curr}&to={output_curr}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4]) # exlcude code

    return rate

# slot function
def show_conversion():
    input_text = float(text.text())
    input_curr = in_combo.currentText()
    output_curr = to_combo.currentText()
   # print(input_curr, output_curr)
    rate = get_exchange(input_curr, output_curr)
    result = input_text*rate
    rounded_rate = round(result,2)
    message = f"{input_text} {input_curr} is {rounded_rate} {output_curr}"
    output_label.setText(message)


app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency App")
window.resize(300, 300)

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
