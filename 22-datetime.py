from datetime import date
from datetime import datetime
import pytz

data = date(2025, 2, 20)
print(data)
print(date.today())

print("________________________")


data_hora = datetime(2025, 2, 20)
print(data_hora)
print(datetime.today())

print("________________________")

data_hora_atual = datetime.now()
data_hora_str = "2023-2-20 21:40"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))


data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))

# Trabalhando com timezone

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)