# Always specify encoding explicitly when opening files
with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.readlines()  # Note: readlines() not readlines
    for line in content:
        print(line.strip())