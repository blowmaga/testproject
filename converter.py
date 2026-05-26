FILENAME = "rates.txt"

def load_rates():
    rates = {}
    
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                line = line.strip()  
                if not line:         
                    continue 

                parts = line.split()
                
                if len(parts) == 2:
                    currency = parts[0].upper()
                    rate = float(parts[1])
                    rates[currency] = rate  

    except FileNotFoundError:
        print(f"Файл {FILENAME} не найден. Создаем новый с базовыми курсами.")
        rates = {"USD": 75.5, "EUR": 85.2, "RUB": 1.0}
        save_rates(rates)  
        
    return rates


def save_rates(rates):
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            for currency, rate in rates.items():
                f.write(f"{currency} {rate}\n")
    except IOError:
        print("Ошибка: не удалось сохранить данные в файл.")


def convert_currency(amount, from_cur, to_cur, rates):
    if from_cur not in rates:
        return f"Ошибка: валюта {from_cur} не найдена в базе."
    if to_cur not in rates:
        return f"Ошибка: валюта {to_cur} не найдена в базе."
        
    amount_in_rubles = amount * rates[from_cur]
    
    result = amount_in_rubles / rates[to_cur]
    
    return round(result, 2)