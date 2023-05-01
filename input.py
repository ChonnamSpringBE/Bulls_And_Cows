import bulls
import bulls_and_cows_answer
import cow

randomNum = bulls_and_cows_answer.create_answer()

while True:
    guessNum = list(input("Guess your number": ))

    bullsCount = bulls.bulls()
    cowsCount = cow.cow()

    print(f'bulls: {bullsCount} cows: {cowsCount}')

    if bullsCount == 4:
        print("성공했습니다")
        break


