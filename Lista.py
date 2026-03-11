owoce = ["jabłko", "banan", "wiśnia"]

with open("test.txt", "w", encoding="utf-8") as file:
    for lista in owoce:
        file.write(lista + "\n") # Dodajemy \n, żeby każde zadanie było w nowej linii

print("Program skończył pracę. Sprawdź lewy panel w VS Code!")