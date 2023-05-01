from bulls_and_cows_answer import create_answer
from bulls import bulls
from cow import cow


if __name__ == "__main__":
    answer = create_answer()
    user_input = get_user_input()
    print("정답: ", answer)
    print("사용자 입력: ", user_input)
    print("스트라이크 개수: ", bulls(answer, user_input))
    print("볼 개수: ", cow(answer, user_input))
