from random import randrange

def ticketGenerator():
    numList = []
    num = -1
    #Generate the 6 first numbers
    for x in range(6):
        while num == -1 or num in numList:
            num = '{:02}'.format(randrange(1, 71))
        else: 
            numList.append(num)
    #Generate the Yotta ball number 
    numList.append('{:02}'.format(randrange(1, 64)))
    return numList

def main():
    print("==============================================")
    print("Starting Yotta Savings Lotto Numbers Generator")
    print("==============================================") 
    ticketCount = int(input("Enter number of tickets to generate: "))
    print("\n")

    ticketList = []
    for x in range(ticketCount):
        ticketList.append(ticketGenerator())

    for ticket in ticketList:
        print(*ticket, sep = ' ') 

    print("\nGood luck!") 

if __name__ == "__main__":
    main()
    k = input("press close to exit") 