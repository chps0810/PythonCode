print("Type integers, each followed by Enter; or just Enter to finish")

total = 0
count = 0

while True:
    line = input("integer: ")
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print("Fuck you.")
            continue
        total += number
        count += 1
    else:
        break
if count:
    print("count =", count, "total =", total, total / count)
