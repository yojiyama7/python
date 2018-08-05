def sign(n):
    if 0 <= n:
        return 0
    return -1

sx, sy, tx, ty = map(int, input().split(" "))

w, h = tx-sx, ty-sy

text = ""
text += "UD"[sign(h)] * abs(h)
text += "RL"[sign(w)] * abs(w)
text += "DU"[sign(h)] * abs(h)
text += "LR"[sign(w)] * (abs(w)+1)
text += "UD"[sign(h)] * (abs(h)+1)
text += "RL"[sign(w)] * (abs(w)+1)
text += "DU"[sign(h)]
text += "RL"[sign(w)]
text += "DU"[sign(h)] * (abs(h)+1)
text += "LR"[sign(w)] * (abs(w)+1)
text += "UD"[sign(h)]
print(text)