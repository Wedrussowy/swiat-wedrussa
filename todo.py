tasks = []

def save_tasks():
    with open("zadania.txt", "w", encoding="utf-8") as file:
            for t in tasks:
                file.write(t + "\n")

def load_tasks():
    # Próbujemy wczytać zadania
    try:
        with open("zadania.txt", "r", encoding="utf-8") as file:
            for line in file:
                tasks.append(line.strip()) # strip() usuwa Entery z końca linii
        print("Wczytano zapisane zadania.")
    except FileNotFoundError:
        pass

def show_tasks():
    if not tasks:
        print("Nic tu nie ma!")
        return False
    else:
        for index, task in enumerate(tasks):
            print(index + 1, "-", task)
        return True


load_tasks()

while True:
    print("\n1 - Pokaż zadania")
    print("2 - Dodaj zadanie")
    print("3 - Wyjdź")
    print("4 - Usuń zadanie")
    print("5 - Edytuj zadanie")

    choice = input("Wybierz opcję: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        new_task = input("Podaj treść zadania: ")
        tasks.append(new_task)
        save_tasks()
        print("Dodano!")

    elif choice == "3":
        print("Koniec programu.")
        break

    elif choice == "4":
        if show_tasks():
            task_index = int(input("Wpisz numer zadania, które ma zostać usunięte: "))
            if 0 < task_index <= len(tasks):
                removed_task = tasks.pop(task_index - 1)
                save_tasks()
                print("Zadanie {removed_task} zostało usunięte")
            else:
                print("Nie ma takiego zadania.")

    elif choice == "5":
        if show_tasks():
            task_index = int(input("Wpisz numer zadania do zmiany: "))   
            if 0 < task_index <= len(tasks):
                new_text = input("Wpisz nową treść zadania:: ")
                tasks[task_index - 1] =new_text
                save_tasks()
                print("Zadanie zaktualizowane!")
            else:
                print("Nie ma takiego zadania.")
            
    else:
        print("Niepoprawna opcja.")