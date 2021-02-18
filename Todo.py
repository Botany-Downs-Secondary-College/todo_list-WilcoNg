#Todo.py
#Wilco Ng 18/06/20
#To do a list
task_list = []
def selection():
    print("1. Add a task")
    print("2. View list")
    print("3. Exit")
    choice = int(input("Please select a number: "))

    if choice == 1:
        print("type 'menu' to go back")
        task_list.append(input("What task would you like to add? "))
        selection()
    elif choice == 2:
        i = 0
        while i < len(task_list):
            print("{}. {}".format(i + 1, task_list[i]))
            i += 1

        print("______________________________")
        selection()
    elif choice == 3:
        print("Good bai")
        exit

selection()
