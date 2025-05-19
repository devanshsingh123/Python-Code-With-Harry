def func1():
    try:
        l=[2,6,9,13]
        i = int(input("Enter the number: "))
        print(l[i])
        return 0
    except:
        print("Some error occured!")
        return 1
    finally:
        print("I am always executed!")
    # finally:

val = func1()
    