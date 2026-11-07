def create_file():
    file_name=input("enter file name : ")
    try:
        open(f"{file_name}.tawfiq", "x")
    except FileExistsError:
        print("the file is exists")
    else:
        print("done")

def write_file():
    file_name=input("enter file name : ")

    try:
        open(f"{file_name}.tawfiq", "r+")
    except FileNotFoundError:
        print("the file not found")


while True:
    command=input(" enter command >> ")
    if command=="create_file":
        create_file()
    elif command=="write_file":
        write_file()
    elif command=="exit":
        break
    else: 
        print("CommandErorr: the command is not exists")


 