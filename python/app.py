file_name = "names.txt"

while True:
    name = input("Enter a name (or type 'exit' to stop): ")

    if name.lower() == 'exit':
        break

    with open(file_name, "a") as f:
        f.write(name + "\n")

    print("\nNames entered so far:")
    with open(file_name, "r") as f:
        print(f.read())
    print("-" * 20)