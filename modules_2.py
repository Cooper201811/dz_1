answers = {
"Привет": "Привет!",
"Как дела?": "Отлично, а у тебя?",
"Пока": "Еще увидимся!"
}

def get_answer(answer, answers):
    return answers.get(answer)


def ask_user(answers):
    while True:
        user_input = input("Скажи что-нибудь: ")
        answer = get_answer(user_input, answers)
        print(answer)

        if user_input == 'Пока':
            break


if __name__ == "__main__":
    ask_user(answers)