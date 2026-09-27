def main():
    try:
        a = int(input("hey, Enter a number: "))
        print(a)
        return

    except Exception as e:  
        print(e)  
        return

    finally:
        print("I am inside finally")     # Agar try statement and except satatement koi bhi run ho and besk return krde but finally to chelaga hi chelaga 

main()