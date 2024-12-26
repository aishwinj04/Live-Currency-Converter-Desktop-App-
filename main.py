from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from bs4 import BeautifulSoup
import requests 


# VERSION1 SUPPORT ONLY FOR CAD->USD EXCHANGE RATE


# beautifulsoup to get live exchange rate 
def get_exchange(amount, input_curr='CAD', output_curr='USD'):
    url = f"https://www.x-rates.com/calculator/?from={input_curr}&to={output_curr}&amount={amount}" # static amount of 1, multiply user amount later
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4]) # exlcude code

    return rate
    

# slot function
def show_conversion():
    amount = float(text.text())
    rate = get_exchange(amount)
    rounded_rate = round(rate,2)
    output_label.setText(str(rounded_rate))


app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency App")
window.resize(300, 400)

layout = QVBoxLayout()

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
