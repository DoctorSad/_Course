def main():
    user_list = []

    while True:
        name = input("name: ")
        surname = input("surname: ")
        age = input("age: ")

        user_list.append([name, surname, age])

        if input("Continue? ([y]/n)") == "n":
            break

    print(user_list)

    for user in user_list:
        print(user[0])


if __name__ == "__main__":
    main()
