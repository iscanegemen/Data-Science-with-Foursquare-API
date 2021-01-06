#   Author      : Emin Kartci
#   Class       : 3rd Year - EE393.A
#   Department  : Electrical & Electronics Engineering

# This module is to represent customers

# get random library to execute a stochastic simulation
# do not get all library I only need randint method
from random import randint

# define a class
class Customer:

    # Constructor
    def __init__(self,id,minPrice = 0,maxPrice= 100,centerLocation = [0,0]):

        # set initial parameters
        self.id = id

        # decide customer's budget
        self.setRandomCash(minPrice,maxPrice)

        # give a location to the customer
        self.setRandomRange(maxDistance=10000)
        self.setRandomLocation(centerLocation)

    # sets a random location around the center
    def setRandomLocation(self,centerLocation):

        # set a location that arounds the center
        self.longitude  = centerLocation[0] + randint(1,10)
        self.latitude   = centerLocation[1] + randint(1,10)

    # sets a random budget by considering the prices
    def setRandomCash(self,minPrice,maxPrice):

        self.cash = randint(minPrice,maxPrice)

    # the customer can visit this range
    def setRandomRange(self,maxDistance = 14000):

        self.maxRestaurantRange =randint(0,maxDistance)

    # returns a string or prints to the console
    def print_customer(self,willPrint = True):

        customerString = "\n\n---CUSTOMER---\nID: {}\nLon: {}\nLat: {}\nCash: {}\nMax Restaurant Range: {}".format(self.id,
                                                                                                    self.longitude,
                                                                                                    self.latitude,
                                                                                                    self.cash,
                                                                                                    self.maxRestaurantRange)
        if willPrint:
            print(customerString)
        else:
            return customerString
