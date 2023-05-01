from bulls_and_cows_answer import create_answer
from bulls import bulls
from cow import cow
from input import get_user_input


if __name__ == "__main__":
    answer = create_answer()

    while True:
        user_input = get_user_input()
        bulls_count = bulls(answer, user_input)
        cows_count = cow(answer, user_input)

        print(f"Bulls개수: {bulls_count} Cow개수: {cows_count}")

        if bulls_count == 4:
            print("성공했습니다")
            break
