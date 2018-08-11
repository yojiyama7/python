### 01 ###

musicians = ["米津玄師", "GYARI"]

### 02 ###

# 適当
visiteds = [(0, 0), (1, 1), (2, 2)]

### 03 ###

me = {"name": "yayo256", "age": 15}

### 04 ###

input_text = input()
if input_text in me:
	print(me[input_text])
else:
	print("該当するキーがありません")

### 05 ###

musicians = {
	"米津玄師": ["LOSER", "アイネクライネ"],
	"GYARI": ["なんでもいうことをきいてくれるアカネちゃん", "ボーカロイドたちがただ叫ぶだけ"]
}

### 06 ###

# set は 集合
# 集合和 や 集合積 を求めることができる
# 数学的な集合(またその機能)を扱いたい時に使う