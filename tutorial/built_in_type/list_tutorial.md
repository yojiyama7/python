
### list(変更可能)の操作

#### 作成

    x = []
    x = [要素1, 要素2, 要素3, .....]

#### 取得

    スライス
    len(s)
    min(s)
    max(s)
    s.index(x)
    s.count(x)

#### 演算

    x in s
    x not in s
    s + t
    s * n, n * s

### 変更

    s[i] = x
    s[i:j] = x
    del s[i:j]
    s.append(x)
    s.clear()
    s.extend(t)
    s += t
    s.insert(i, x) == s[i:i] = [x]
    s.pop(i)
    s.remove(x)
    s.reverse()
    s.sort()