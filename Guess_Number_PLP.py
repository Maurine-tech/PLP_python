
def main ():
    n = int(input("Enter the number I am guessing, between 1 to 9."))
    if n == 6:
        print("Well guessed!")
        
    elif n <= 9 and n != 6:
            print ("Good guess, but not yet there. Try again.")
            main()
    else:
        main()
main ()        
