print("Zadanie 3.1")
d5=[]
d3=[]
for x in range (0, 100):
    if x%5==0:
        d5.append(x)
        x=x**3
        d3.append(x)
print(f"Liczby dzielone na 5: {d5}")
print(f"Liczby dzielone na 5 podniesione do potęgi 3: {d3}")

print("Test git")
