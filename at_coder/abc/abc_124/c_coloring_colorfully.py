S = input()

print(
    min(
        sum(
            s==str(i%2) for i, s in enumerate(S)
        ),
        sum(
            s==str((i+1)%2) for i, s in enumerate(S)
        ),
    )
)