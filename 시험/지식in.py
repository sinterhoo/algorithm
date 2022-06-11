

person = [0,0,0]

n = int(input())

for _ in range(n):
    for i in range(3):
        temp = int(input())
        person[i] = max(person[i], temp)
    print(person)

print(f"Person{person.index(max(person))+1} Win")