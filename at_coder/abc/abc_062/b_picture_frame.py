h, w = map(int, input().split(" "))
a = [input() for i in range(h)]

print("\n".join(["#" + line + "#" for line in ["#"*w] + a + ["#"*w]]))