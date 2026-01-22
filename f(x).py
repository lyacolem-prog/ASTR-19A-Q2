


def F(x): # F of X function
    result = x**3 + 8
    return(result)

def main(): # Main Function - it feels very strange to see "f(x)" with a Captial "F"
    print(F(9))
    if F(9) > 27: 
        print("YAY!")
    
if __name__=='__main__': # Calls Main functions
    main()