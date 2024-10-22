import sqlite3



conn = sqlite3.connect("youtube_vedios.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE  IF NOT EXISTS vedio(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEX NOT NULL
               )
""")

def list_all_vedios():
    print("="*30)
    cursor.execute("SELECT * FROM vedio")
    for list in cursor.fetchall():
            print(f"{list[0]}. {list[1]} , Duration : {list[2]}")
    print("="*30)

        

def add_vedios(name,time):
    cursor.execute("INSERT  INTO vedio (name,time) VALUES (?,?)",(name,time))
    conn.commit()
    print("\n **** Add Successfull!! ****")

def update_vediso(name,time,id_key):
    

    cursor.execute("UPDATE vedio SET name = ? , time  = ? WHERE id = ?",(name,time,id_key))
    conn.commit()
    print("\n **** Update Successfull!! ****")

def delete_vedios(id_key):
    

    cursor.execute("DELETE FROM vedio WHERE id =?",(id_key,))
    conn.commit()
    print("\n **** Delete Successfull!! ****")
def main():
    while True:
        print("\n****** Youtube Manger App DB *******")
        print("1. List all Youtube vedios..")
        print("2. Add Youtube vedios..")
        print("3. Update Youtube vedios..")
        print("4. Delete Youtube vedios..")
        print("5. Exit the app..")
        print("*"*30)
        choice = input("Enter a Choice: ")
        match choice:
            case "1":
                list_all_vedios()
            case "2":
                name =  input("Enter a vedio Nmae: ")
                time =  input("Enter a vedio Duration Time : ")
                add_vedios(name,time)
            case "3":
                list_all_vedios()
                id_key =  int(input("Enter a Id that you  want to update: "))
                name =  input("Enter a vedio Nmae: ")
                time =  input("Enter a vedio Duration Time : ")
                update_vediso(name,time,id_key)
            case "4":
                list_all_vedios()
                id_key =  int(input("Enter a Id that you  want to delete: "))
                delete_vedios(id_key)
            case "5":
                break
            case _:
                print("Invalid choice. Please choose a valid option.")
    
    
    conn.close()



if __name__ == "__main__":
    main()
