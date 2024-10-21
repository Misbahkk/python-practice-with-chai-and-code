import json


file_name = 'youtube.txt'
def load_vedios():
    try:
        with open(file_name,'r') as file:
           return json.load(file)
    except FileNotFoundError:
        return "You not add Vedio Now"
    

def save_helper(vedios):
    with open(file_name,'w') as file:
        json.dump(vedios,file)


def list_all_vedios(vedios):
    print("\n")
    print("*"*50)
    print("-"*50)
    print("*"*50)
    print("\n")
    for index,vedio in enumerate(vedios,start=1):
        print(f"{index}. {vedio['name']}, douration: {vedio['time']}")
    print("\n")
    print("*"*50)
    print("-"*50)
    print("*"*50)
    print("\n")


def add_vedios(vedios):
    print("\n")
    name = input("Enter Vedio Name: ")
    time = input("Enter Vedio Time: ")
    vedios.append({'name':name,"time":time})
    save_helper(vedios)
    print("\n****** Vedio Add Successfully ******")
    print("\n")


def update_vediso(vedios):
    list_all_vedios(vedios)
    index = int(input("Enter vedio Number: "))
    if 1<= index <= len(vedios):
        name = input("Enter a Vedio Name: ")
        time = input("Enter a vedio duration Time: ")
        vedios[index-1]=({'name':name,"time":time})
        save_helper(vedios)
        print("\n**** Your Vedio is Update Now ****\n")
    else:
        print("Invalid Input")

def delete_vedios(vedios):
    list_all_vedios(vedios)
    index = int(input("Enetr a vedio Number that You Want To delete: "))
    if 1 <= index <=len(vedios):
        del vedios[index-1]
        save_helper(vedios)
        print("\n**** Your Vedio is Deleted Succesfully ****\n")
    else:
        print("Invalid Input")
    


def main():

    while True:
        vedios = load_vedios()
        print("\n****** Youtube Manger App *******")
        print("1. List all Youtube vedios..")
        print("2. Add Youtube vedios..")
        print("3. Update Youtube vedios..")
        print("4. Delete Youtube vedios..")
        print("5. Exit the app..")
        print("*"*30)
        choice = input("Enter a Choice: ")
        match choice:
            case "1":
                list_all_vedios(vedios)
            case "2":
                add_vedios(vedios)
            case "3":
                update_vediso(vedios)
            case "4":
                delete_vedios(vedios)
            case "5":
                exit()
            case _:
                print("Invalid choice. Please choose a valid option.")



if __name__ == "__main__":
    main()