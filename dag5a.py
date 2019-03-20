#!python3

def ongeveergelijk(letter1, letter2):
    if letter1 == letter2:
        return 0

    if letter1.lower() == letter2.lower():
        return (letter1.isupper() and letter2.islower()) or (letter1.islower() and letter2.isupper())

regels = open('input.dag5').read().splitlines()

solution = regels[0]
teller = 0
while teller < (len(solution)-1):
    if ongeveergelijk(solution[teller], solution[teller+1]):
        print(solution[teller], solution[teller+1])
        solution = solution[:teller] + solution[teller+2:]
        teller -= 1
    else:
        teller += 1

print(len(solution))
