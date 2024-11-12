from player import pon as human_pon
from computer import pon as cpu_pon
from janken_judge import judge

def janken_main():
    player_wins = 0
    computer_wins = 0

    for _ in range(3):
        player_hand = human_pon()
        computer_hand = cpu_pon()
        result = judge(player_hand, computer_hand)
        print(f"プレイヤーの手: {player_hand}, コンピュータの手: {computer_hand}")
        print(f"結果: {result}")

        if result == "プレイヤーの勝ち":
            player_wins += 1
        elif result == "コンピュータの勝ち":
            computer_wins += 1

    print(f"最終結果: プレイヤーの勝ち数: {player_wins}, コンピュータの勝ち数: {computer_wins}")

if __name__ == "__main__":
    janken_main()
