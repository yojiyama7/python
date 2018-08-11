### 01 ###

with open("charange_8.py", "r", encoding="utf-8") as f:
    print(f.read())

### 02 ### 

input_text = input("なまえは？: ")
with open("charange_8_player_name.txt", "r", encoding="utf-8") as f:
    player_name = f.read()
with open("charange_8_player_name.txt", "w", encoding="utf-8") as f:
    f.write(player_name + "\n" + input_text)

### 03 ###

l = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day", "Man on Fire", "Flight"]
]
with open("charange_8.csv", "w", encoding="utf-8") as f:
    f.write("\n".join([",".join(line) for line in l]))

### 04 ###

l = [
    ["トップ ガン", "危険なビジネス", "マイノリティー レポート"],
    ["タイタニック", "亡霊", "開始"],
    ["訓練日", "消防士", "フライト"]
]
with open("charange_8_jp.csv", "w", encoding="utf-8") as f:
    f.write("\n".join([",".join(line) for line in l]))