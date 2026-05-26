from converter import load_rates, save_rates, convert_currency

def show_help():
    print("\n--- Доступные команды ---")
    print("1. Конвертация: [Сумма] [Из валюты] [В валюту] (например: 100 USD RUB)")
    print("2. Обновление: update [Валюта] [Новый курс] (например: update EUR 90.5)")
    print("3. Просмотр: list (показать все курсы)")
    print("4. Выход: exit")
    print("-------------------------")

def main():
    print("КОНВЕРТЕР ВАЛЮТ USD,EUR,RUB")
    rates = load_rates()
    show_help()

    while True:
        user_input = input("\nВведи команду: ").strip()
        if not user_input:
            continue
            
        words = user_input.split()
        
        command = words[0].lower()

        if command == "exit":
            print("Программа завершена.")
            break

        elif command == "list":
            print("\nСписок всех доступных валют (курс к рублю):")
            for currency, rate in rates.items():
                print(f"{currency}: {rate}")

        elif command == "update":
            if len(words) != 3:
                print("update [Валюта] [Курс]")
                continue
            
            currency = words[1].upper()
            
            try:
                new_rate = float(words[2])
                rates[currency] = new_rate
                save_rates(rates)
                print(f"Курс {currency} обновлен до {new_rate}")
                
            except ValueError:
                print("Курс должен быть числом (например, 75.5).")

        else:
            if len(words) != 3:
                print("Неизвестная команда.")
                show_help()
                continue
            
            try:
                amount = float(words[0])
                from_cur = words[1].upper() 
                to_cur = words[2].upper()   
                result = convert_currency(amount, from_cur, to_cur, rates)

                if isinstance(result, str):
                    print(result)
                else:
                    print(f"Результат: {amount} {from_cur} = {result} {to_cur}")
                    
            except ValueError:
                print("Ошибка! Сумма должна быть числом (например: 100 USD RUB).")





if __name__ == "__main__":
    main()