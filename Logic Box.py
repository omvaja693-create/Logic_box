while True:
    print("Welcome to the Pattern Generator and Number Analyzer!")
    print()
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    option = int(input("Enter your choice: "))

    if option == 3:
        print("Exiting the program. Goodbye!")
        break

    match option:
        case 1:
            a = int(input("Enter the number of rows for the pattern: "))
            print("\nPattern:")
            
            for i in range(1, a + 1):
                for j in range(1, i + 1):
                    print("*", end=" ")
                print()

        case 2:
            s = int(input("Enter the start range: "))
            e = int(input("Enter the end range: "))

            total_sum = 0

            for i in range(s, e + 1):
                total_sum += i
                if i % 2 == 0:
                    print("Number", i, "is Even")
                else:
                    print("Number", i, "is Odd")

            print("Sum of numbers between", s, "and", e, "is:", total_sum)

        case _:
            print("Invalid option. Please choose 1, 2, or 3.")


