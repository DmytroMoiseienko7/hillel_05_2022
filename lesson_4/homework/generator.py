kw = "user"
file_name = "lesson_4/homework/rockyou.txt"
result = []


def collect_kw(filename, kw):
    with open(filename, encoding="utf_8") as txt_file:
        while True:
            line = txt_file.readline()
            if kw in line:
                yield line.replace("\n", "")
            if not line:
                break


rock_you_generator = collect_kw(file_name, kw)

for kw in rock_you_generator:
    print(kw)
    command = input("Do you want to add key word? ")
    if command == "Y":
        result.append(kw)
    elif command == "N":
        pass
    elif command == "F":
        break

print(f" Number of kw :{len(result)}")
print(result)
