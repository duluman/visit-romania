print("\n *************** \n")


def homework():
    with open("testare.txt") as page:
        for line in page:
            show = line.split(", ")

            for letter in show:
                if letter not in ",":
                    print(letter, end=" ")


homework()
print("\n \n*************** \n")


def homework2():
    with open("testare.txt") as page:
        for line in page:
            for letter in line:
                if letter != ",":
                    print(letter, end="")


homework2()
print("\n \n*************** \n")


def homework3():
    with open("testare.txt") as page:
        for line in page:
            show = line.split(", ")
            print("- " * len(line))
            print("-" * 2, end=" ")

            for i in range(len(show)):
                print("-" * 2, end=" ")
                print("|| {} ".format(show[i]),  end="")
                print("-" * 2, end=" ")


homework3()
print("\n \n *************** \n")
