def pon():
    while True:
        user_input = input("1: グー, 2: チョキ, 3: パー を入力してください: ")
        if user_input in ['1', '2', '3']:
            return int(user_input)
        else:
            print("無効な入力です。再度入力してください。")
