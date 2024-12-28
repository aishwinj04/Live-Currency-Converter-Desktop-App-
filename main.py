from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
from bs4 import BeautifulSoup
import requests 


# VERSION3 ADVANCED LAYOUT


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

# children of main_layout is layout1 and label vertical stacked
main_layout = QVBoxLayout()

# layout1 children is layout2 and layout3 horizontal aligned
layout1 = QHBoxLayout()
main_layout.addLayout(layout1)

output_label = QLabel('')
main_layout.addWidget(output_label)

# layout2 children is 2 combobox vertical stacked
layout2 = QVBoxLayout()
layout1.addLayout(layout2)

# layout3 children is the input field and button vertical stacked
layout3 = QVBoxLayout()
layout1.addLayout(layout3)



# input currency dropdown 
in_combo = QComboBox()
currencies = ['USD', 'EUR', 'INR', 'CAD', 'GBP', 'AUD', 'JPY', 'CNY']
in_combo.addItems(currencies)
main_layout.addWidget(in_combo)


# output currency dropdown
to_combo = QComboBox()
to_combo.addItems(currencies)
main_layout.addWidget(to_combo)


# amount entry 
text = QLineEdit()
main_layout.addWidget(text)


# validate button 
btn = QPushButton('Convert')
main_layout.addWidget(btn)
btn.clicked.connect(show_conversion)


# output
window.setLayout(main_layout)
window.show()
app.exec()
