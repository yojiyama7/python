import pyxel
import random

WINDOW_WIDTH, WINDOW_HEIGHT = 240, 145
WINDOW_TITLE = "title"
# PYXEL_FILE_NAME             = "file_name.pyxel"

small_chars = "abcdefghijklmnopqrstuvwxyz"
kana_list = []
for s in ["", *"kstnhmr"]:
    for c in "aiueo":
        kana_list.append(s+c)
kana_list += ["ya", "yu", "yo", "wa", "wo", "xn"]
en_words = []
with open("en_words.txt", "r", encoding="utf-8") as f:
    l = f.read().split("\n")
    en_words = [line.split(",")[0] for line in l]
    jp_words = [line.split(",")[1] for line in l]

questions = []
# questions += en_words
# random.shuffle(questions)

def solve_pos(xp, yp):
    y = 14*yp
    x = [0, 4, 10][yp] + 14*xp
    return (x, y)

class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, caption=WINDOW_TITLE)
        # pyxel.load(PYXEL_FILE_NAME)
        pyxel.mouse(True)

        self.score = 0
        self.score_before = 0
        with open('score.txt', 'r', encoding="utf-8") as f:
            self.score = int(f.read())

        self.keys_pos = (40, 80)
        self.keys = []
        for yp, l in enumerate(["qwertyuiop", "asdfghjkl", "zxcvbnm"]):
            for xp, char in enumerate(l):
                self.keys.append([char, solve_pos(xp, yp)])
        self.keys.sort()
        self.key_flags = [0]*26

        # self.question_number = 0
        self.question = ""
        self.question_i = 0
        self.set_question()

        self.rect_effects = []

        pyxel.run(self.update, self.draw)
    
    def set_question(self):
        self.question_i = 0
        # self.question_number += 1
        # self.question = questions[self.question_number]
        # self.question = "".join([random.choice(kana_list) for _ in range(random.randint(2, 6))])
        # self.question = random.choice(kana_list)
        self.question = random.choice(en_words)
        # x = random.randint(0, len(en_words)-1)
        # self.question = en_words[x]
        # print(f"{en_words[x]: >16}: {jp_words[x]}")

    def check_question(self):
        if pyxel.btnp(ord(self.question[self.question_i])-97 + 18):
            self.question_i += 1
        if self.question_i >= len(self.question):
            self.next_question()
    
    def next_question(self):
        for i in range(32):
            if (self.score>>i)&1:
                x, y = 230-4*i, 135
                self.rect_effects.append((x, y))

        self.score += 1
        self.set_question()

        self.rect_effects = [(x, y-3) for x, y in self.rect_effects]
        self.rect_effects = [(x, y) for x, y in self.rect_effects if y >= 0]
        

    def update(self):
        self.key_flags = [pyxel.btn(i+18) for i, (char, *_) in enumerate(self.keys)]
        
        with open('score.txt', 'w', encoding="utf-8") as f:
            f.write(str(self.score))

        self.check_question()

    def draw(self):
        pyxel.cls(0)
        # pyxel.rect(230, 135, 2, 2, 13)
        for i in range(32):
            if (self.score>>i)&1:
                x, y = 230-4*i, 135
                pyxel.rect(x, y, 2, 2, 11)
        for rx, ry in self.rect_effects:
            pyxel.rect(rx, ry, 2, 2, 1)

        kx, ky = self.keys_pos
        for i, key in enumerate(self.keys):
            flag = self.key_flags[i]
            char, (x, y) = key
            pyxel.rectb(kx+x, ky+y, 12, 12, [13, 5][flag])
            pyxel.text(kx+2+x, ky+2+y, str.upper(char), [0, 6][flag])
        pyxel.text(20, 20, f"score: {self.score}", 7)
        pyxel.text(80, 40, ":", 7)
        t = str.capitalize(self.question)
        pyxel.text(80+4, 40, (f"{t[:self.question_i]}"), 1)
        pyxel.text(80+4+4*self.question_i, 40, (f"{t[self.question_i:]}"), 12)

        self.score_before = self.score

if __name__ == "__main__":
    app = App()