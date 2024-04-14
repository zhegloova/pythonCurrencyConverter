from datetime import date
import requests as requests
from tkinter import *

def convert_currency(amount, from_currency, to_currency):
    # Получение актуальных курсов валют
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
    data = response.json()

    # Проверка наличия ошибок в полученных данных
    if "error" not in data:
        # Получение курса обмена между двумя валютами
        exchange_rate = data["rates"][to_currency]
        # Конвертирование валюты
        converted_amount = int(amount) * exchange_rate
        return converted_amount
    else:
        raise Exception("Ошибка при получении курса обмена валют")

# Обработчик кнопки "Конвертировать"
def exchange():
    e_usd.delete(0, END)
    e_eur.delete(0, END)
    e_gbp.delete(0, END)
    e_usd.insert(0, '%.2f' % convert_currency(e_rub.get(), 'RUB', 'USD'))
    e_eur.insert(0, '%.2f' % convert_currency(e_rub.get(), 'RUB', 'EUR'))
    e_gbp.insert(0, '%.2f' % convert_currency(e_rub.get(), 'RUB', 'GBP'))


root = Tk()
root.title('Currency Converter')
root.geometry('400x250+100+100')
root.resizable(width=False, height=False)
root['bg'] = '#020a2e'
# c = CurrencyConverter()
# need_date = date(2013, 3, 21)

header_frame = Frame(root)
header_frame.pack(fill=X)

# Создание сетки
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

# Создание заголовков сетки
h_currency = Label(header_frame, text='Валюта', bg='#020a2e', fg='#c4cfff', font='Times 12 bold')
h_currency.grid(row=0, column=0, sticky=EW)
h_course = Label(header_frame, text='Курс', bg='#020a2e', fg='#c4cfff', font='Times 12 bold')
h_course.grid(row=0, column=1, columnspan=2, sticky=EW)

# USD курс
usd_currency = Label(header_frame, text='USD', font='Times 10')
usd_currency.grid(row=1, column=0, sticky=EW)
usd_one = Label(header_frame, text='1', font='Times 10')
usd_one.grid(row=1, column=1, sticky=EW)
usd_converted = Label(header_frame, text='%.2f' % convert_currency(1, 'USD', 'RUB'), font='Times 10')
usd_converted.grid(row=1, column=2, sticky=EW)

# EUR курс
eur_currency = Label(header_frame, text='EUR', font='Times 10')
eur_currency.grid(row=2, column=0, sticky=EW)
eur_one = Label(header_frame, text='1', font='Times 10')
eur_one.grid(row=2, column=1, sticky=EW)
eur_converted = Label(header_frame, text='%.2f' % convert_currency(1, 'EUR', 'RUB'), font='Times 10')
eur_converted.grid(row=2, column=2, sticky=EW)

# GBP курс
gbp_currency = Label(header_frame, text='GBP', font='Times 10')
gbp_currency.grid(row=3, column=0, sticky=EW)
gbp_one = Label(header_frame, text='1', font='Times 10')
gbp_one.grid(row=3, column=1, sticky=EW)
gbp_converted = Label(header_frame, text='%.2f' % convert_currency(1, 'GBP', 'RUB'), font='Times 10')
gbp_converted.grid(row=3, column=2, sticky=EW)

# Создание фрейма для конвертации валюты
calc_frame = Frame(root, bg='#020a2e')
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)

l_rub = Label(calc_frame, text='Рубли', bg='#020a2e', fg='#c4cfff', font='Times 12 bold')
l_rub.grid(row=0, column=0, padx=10)
e_rub = Entry(calc_frame, justify=CENTER, font='Times 10')
e_rub.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky=EW)

btn_calc = Button(calc_frame, text='Конвертировать', command=exchange)
btn_calc.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)

res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, pady=5)
res_frame.grid_columnconfigure(1, weight=1)

# USD
l_usd = Label(res_frame, text='USD', font='Times 10 bold')
l_usd.grid(row=2, column=0)
e_usd = Entry(res_frame, justify=CENTER, font='Times 10')
e_usd.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)

# EUR
l_eur = Label(res_frame, text='EUR', font='Times 10 bold')
l_eur.grid(row=3, column=0)
e_eur = Entry(res_frame, justify=CENTER, font='Times 10')
e_eur.grid(row=3, column=1, columnspan=2, padx=10, sticky=EW)

# GBP
l_gbp = Label(res_frame, text='GBP', font='Times 10 bold')
l_gbp.grid(row=4, column=0)
e_gbp = Entry(res_frame, justify=CENTER, font='Times 10')
e_gbp.grid(row=4, column=1, columnspan=2, padx=10, sticky=EW)

root.mainloop()