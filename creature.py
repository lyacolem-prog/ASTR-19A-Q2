def Creature(length_of_arms, length_of_legs, number_of_eyes, tail, furry):

    print("Arm Length: ", length_of_arms)
    print("Leg Length: ", length_of_legs)
    print("Number of Eyes: ", number_of_eyes)
    print("Does it Have a tail?: ", tail)
    print("Is it furry?: ", furry)


def main():
    
   Creature(length_of_arms = 2.0, length_of_legs = 5.0, number_of_eyes = 2, tail = True, furry = True)

if __name__=='__main__': # Calls Main functions
    main()