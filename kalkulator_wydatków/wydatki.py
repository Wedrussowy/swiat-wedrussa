import os

expenses = []

def save_expenses():
    with open("dane_wydatkow.txt", "w", encoding="utf-8") as file:
        for t in expenses:
            file.write(f"{t['amount']};{t['category']}\n")

def load_data():
    try:
        with open("dane_wydatkow.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(";")

                if len(parts) == 2:
                    try:
                        amount = float(parts[0])
                        category = parts[1]
                        expenses.append({"amount": amount,  "category": category})
                    except ValueError:
                        continue

        print("Wczytano dane z kategoriami.")
    except FileNotFoundError:
        pass
    except (ValueError, IndexError):
        print("Błąd formatu dasnych w pliku. Niektóre wpisy pominięto.")

def show_expenses():
    if not expenses:
        print("Nie ma żadnych wydatków na liście!")
        input("\nNaciśnij Enter, aby wrócić do menu...")
        return False
    else:
        print("Twoje wydatki:")
        for index, expenses_list in enumerate(expenses):
            print(f"{index + 1} - {expenses_list['amount']:.2f} zł | Kategoria: {expenses_list['category']}")

        suma = sum(expenses_list["amount"] for expenses_list in expenses)
        print("-" * 30)
        print(f"SUMA: {suma:.2f} zł")
        return True

def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')

load_data()

while True:
    clear_window()

    print("--- MENU GŁÓWNE ---")

    print("\n1 - Dodaj wwydatek")
    print("2 - Pokaż wszystkie i sumę")
    print("3 - Usuń wydatek z listy")
    print("4 - Wyjdź")

    choice = input("Wybierz opcję: ")

    if choice == "1":
        clear_window()
        print("--- DODAWANIE WYDATKÓW ---")
        user_input = input("Ile kosztował wydatek (Wpisz '0', aby wrócić): ")
        if user_input == "0":
            continue

        try:
            amount = float(user_input)
            category = input("Na co wydałeś?: ")

            new_entry = {"amount": amount, "category": category}
            expenses.append(new_entry)

            save_expenses()
            clear_window()
            print(f"Dodano: {amount:.2f} zł na {category}!")
            input("\nNaciśnij Enter, aby wrócić do menu...")
        except ValueError: 
            clear_window()
            print("Błąd! Podaj liczbę (użyj kropki, np. 15.50)")
            input("\nNaciśnij Enter, aby wrócić do menu...")

    elif choice == "2":
        clear_window()
        print("--- LISTA WYDATKÓW ---")
        show_expenses()
        input("\nNaciśnij Enter, aby wrócić do menu...")

    elif choice == "3":
        clear_window()
        print("--- USUWANIE WYDATKÓW ---")
        if show_expenses():
            user_input = input("Wpisz numer wydatku, który chcesz usunąć z listy (Wpisz '0', aby wrócić): ")
            if user_input == "0":
                continue

            try:
                expense_to_remove = int(user_input)

                if 0 < expense_to_remove <= len(expenses):
                    removed_expense = expenses.pop(expense_to_remove - 1)
                    save_expenses()
                    clear_window()
                    print(f"Wydatek {removed_expense['amount']:.2f} zł. ({removed_expense['category']}) został usunięty z listy wydatków")
                    input("\nNaciśnij Enter, aby wrócić do menu...")

                else:
                    clear_window()
                    print("Wybrałeś niepoprawny numer z listy wydatków.")
                    input("\nNaciśnij Enter, aby wrócić do menu...")
            except ValueError:
                clear_window()
                print("Błąd! Musisz wpisać numer (liczbę całkowitą).")
                input("\nNaciśnij Enter, aby wrócić do menu...")

    elif choice == "4":
        print("Koniec programu.")
        break

    else:
        clear_window()
        print("Niepoprawna opcja.")
        input("\nNaciśnij Enter, aby wrócić do menu...")

