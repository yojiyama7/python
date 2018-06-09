### if statement (if文)

- 条件分岐を行う制御文

- 条件によって処理を行うかどうかや、どのような処理を行うかを変えることができる

- 一つのif文に含まれるもの(if, elif, else)のうちの、一つしか実行されない

- 構文
```python
if 条件式:
    条件式がTrueだった時の処理
```

```python
if 条件式:
    条件式がTrueだった時の処理
else:
    条件式がFalseだった時の処理
```

```python
if 条件式1:
    条件式1がTrueだった時の処理
elif 条件式1:
    条件式1がFalseで、
    条件式2がTrueだった時の処理
else:
    条件式1と条件式1が
    両方Falseだった時の処理
```

- 処理
    - 上から条件式を評価していく
    - 条件式がTrueの場合、その部分の処理部分を実行し、それ以降を無視して終了する。
    - 条件式が全てFalseの場合、else部分が実行される(ない場合は何も実行されない)

- 単語
    - 条件式は、TrueまたはFalseを返す式で、`0 <10`や`all([True, False])`などである
    - TrueとFalseについては`tutorial/built_in_type/bool_tutorial.md`を参照
