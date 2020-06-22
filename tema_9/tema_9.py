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


def homework3(file_to_open):
    with open(file_to_open) as page:
        for line in page:
            show = line.split(", ")
            print("- " * len(line))
            print("-" * 2, end=" ")

            for i in range(len(show)):
                print("-" * 2, end=" ")
                print("|| {} ".format(show[i]),  end="")
                print("-" * 2, end=" ")


homework3("testare.txt")
print("\n \n *************** \n")

homework3("saved_pass.txt")




# (activate) C:\Users\Christian\PycharmProjects\week_8\testare_git>py manage.py createsuperuser
# Email address: duluman89@yahoo.com
# First name: DoDo
# Last name: MD
# email: duluman89@yahoo.com - password: 24reMLvFUH
# Superuser created successfully.