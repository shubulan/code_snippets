import random, time
from datetime import datetime

# 定义扑克牌的列表，包括普通牌和大小王

colors = ["红桃", "黑桃", "梅花", "方块"]
points = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]

orders = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2", "d", "D"]

cards = []

for c in colors:
    for pts in points:
        cards.append([c, pts])
cards.append(["小", "d"])
cards.append(["大", "D"])

def printCards(cards, color=False):
    for c in cards:
        print(c, end=' ')
    print("")

# 从列表中随机选择17张牌
selected_cards = random.sample(cards, 17)

# 输出选中的牌
print("随机选出的17张扑克牌：")

selected_cards = [ p for c, p in selected_cards]

selected_cards = sorted(selected_cards, key = lambda card: orders.index(card))

# test
# selected_cards = "3 3 3 4 5 5 8 9 9 10 J J Q K 2 2 d".split()

printCards(selected_cards)
start_time = datetime.now()

ok = input("are you ok?")

# time.sleep(10)
end_time1 = datetime.now()

time_diff1 = end_time1 - start_time

for _ in range(50):
    print()
ans = input("发挥你的记忆力吧，输入空格隔开的牌张:\n").split()
# test
# ans = "3 3 3 4 5 5 8 9 10 J Q K A 2 2 D".split()
end_time2 = datetime.now()

time_diff2 = end_time2 - end_time1

try:
    ans = sorted(ans, key = lambda card: orders.index(card))
except Exception as e: 
    print("发生异常 ", e)

print("请看答案吧")
printCards(selected_cards)
printCards(ans)

print("记忆用时：", time_diff1)
print("重现用时：", time_diff2)
def stat(ori, ans):
    idx = 0
    res = []
    for card in ori:
        if idx == len(ans):
            res.append(('miss', card))
            continue

        if card == ans[idx]:
            idx += 1
            continue

        if orders.index(card) < orders.index(ans[idx]):
            res.append(('miss', card))
            continue

        while idx < len(ans) and orders.index(ans[idx]) < orders.index(card):
            res.append(('xtra', ans[idx]))
            idx += 1
        if idx < len(ans) and ans[idx] == card:
            idx += 1

    while idx < len(ans):
        res.append(('xtra', ans[idx]))
        idx += 1
    return res

res = stat(selected_cards, ans)
for type, card in res:
    print(type, card)

print("正确率", (1 - len(res) / 17) * 100 , "%")


