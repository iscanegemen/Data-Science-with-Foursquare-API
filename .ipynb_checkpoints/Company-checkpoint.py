#   Author      : Emin Kartci
#   Class       : 3rd Year - EE393.A
#   Department  : Electrical & Electronics Engineering

# To interact with user use ipywidgets library - Generate a simple GUI
import numpy as np
import matplotlib.pyplot as plt
from math import floor
import time

# import pandas and json to handle data
import pandas as pd
import json

################################-- Function Description --#################################

# Purpose:
#       This class represents a company. For other modules we will need its values.
#    Moreover, creating a class makes simple our code.

# PROPERTIES:
#   
#   From constructor:
#   name                -> Name of the company                (String)
#   longitude           -> To represent at the map            (String)
#   latitude            -> To represent at the map            (String)
#   servicesList        -> To compare with others             (List)
#   averagePrice        -> For income statement - Simulation  (Float)
#   averageUnitCost     -> For income statement - Simulation  (Float)
#   salesVolume         -> For income statement - Simulation  (Float)
#   fixedCost           -> For income statement - Simulation  (Float)
#   taxRate             -> For income statement - Simulation  (Float)
#
#   Calculate:
#
#   contributionMargin  -> For income statement - Simulation  (Float)
#   revenue             -> For income statement - Simulation  (Float)
#   costOfGoodSold      -> For income statement - Simulation  (Float)
#   grossMargin         -> For income statement - Simulation  (Float)
#   taxes               -> For income statement - Simulation  (Float)
#   netIncome           -> For income statement - Simulation  (Float)
#   breakEvenPoint      -> For income statement - Simulation  (Float)
#


# BEHAVIOUR:
#   
#   print_company_description -> prints the company inputs to the console
#   print_income_statement    -> prints the income statement to the console

#################################-- END Function Description --##############################


# Create a Company class
class Company():

    # Constructor
    def __init__(self, name, longitude, latitude, servicesList, averagePrice, averageUnitCost, salesVolume, fixedCost,
                 taxRate):

        # initialize company properties
        self.name               = name
        self.longitude          = longitude
        self.latitude           = latitude
        self.servicesList       = servicesList

        # initialize customer list
        self.targetCustomers    = []

        self.averagePrice       = averagePrice
        self.averageUnitCost    = averageUnitCost
        self.salesVolume        = salesVolume
        self.fixedCost          = fixedCost
        self.taxRate            = taxRate / 100

        # calculate remain properties
        self.contributionMargin = self.calculate_contribution_margin()
        self.revenue            = self.calculate_revenue()
        self.costOfGoodSold     = self.calculate_COGS()
        self.totalCost          = self.calculate_total_cost()
        self.grossMargin        = self.calculate_gross_margin()
        self.taxes              = self.calculate_taxes()
        self.netIncome          = self.calculate_net_income()
        self.breakEvenPoint     = self.calculate_break_even_point()

        self.priceList          = []
        self.costList           = []

    # returns Contribution Margin = Price - Unit Cost
    def calculate_contribution_margin(self):

        return self.averagePrice - self.averageUnitCost

    # returns revenue = price * sales volume
    def calculate_revenue(self):

        return self.averagePrice * self.salesVolume

    # returns Cost of Goods Sold = Unit Cost * Sales Volume + Direct Fixed Costs
    def calculate_COGS(self):

        return self.salesVolume * self.averageUnitCost

    # returns Gross Margin = revenue - COGS
    def calculate_gross_margin(self):

        return self.revenue - self.costOfGoodSold

    # calculate tax expenses = gross margin * tax rate
    def calculate_taxes(self):

        return self.grossMargin * self.taxRate

    # calculate net income
    def calculate_net_income(self):

        return self.grossMargin - self.taxes

    # returns total costs
    def calculate_total_cost(self):

        return self.costOfGoodSold + self.fixedCost

    # Execute Break-Even Point Analysis
    def calculate_break_even_point(self):

        if self.contributionMargin <= 0:
            print("The contribution margin is not a positive number !!\n Contribution Margin : {}".format(
                self.contributionMargin))
            return 0

        return self.fixedCost / self.contributionMargin

    ########################################################################

    # return a string or print to the console
    def print_company_description(self,willPrint = True):

        companyDescription = """

            Company Name: {}

            Location:
                - Longitude : {}° N
                - Latitude  : {}° E

            Services:
            
            {}
            
            Average Price      : {}
            Average Unit Cost  : {}

            Sales Volume       : {}

            Fixed Cost         : {}

            Tax Rate           : {}


        """.format(self.name, self.longitude, self.latitude, self.set_services_string(), self.averagePrice,
                   self.averageUnitCost, self.salesVolume, self.fixedCost, self.taxRate)

        if willPrint:

            print(companyDescription)

        else:

            return companyDescription

    # set a services string by considering a list
    def set_services_string(self):

        # initialize a string
        serviesString = ""

        # if list is empty
        if len(self.servicesList) == 0:
            # return that
            return "There is no service !!"

        # iterate all elements
        for index,service in enumerate(self.servicesList):
            # create a good string and append it
            serviesString += "{} - {}\n\t\t\t".format(index + 1 , service)

        # return result
        return serviesString

    # create a good income statement String or print it
    def print_income_statement(self,willPrint = True):

        # initialize and assign a new string
        incomeStatementStr = """

                    ==========  {}'s MONTHLY INCOME STATEMENT  ==========
                   +------------------------------------------------------
                   | Unit Price    : {}
                   | Unit Cost     : {}
                   +------------------
                   | Contribution Margin : {}
                   | Sales Volume        : {}
                   | Revenue             : {} (Monthly)
                   +------------------
                   | Cost of Goods Sold  : {} (Monthly)
                   | Total Fixed Cost    : {} (Monthly)
                   | Total Cost          : {}
                   +------------------
                   | Gross Margin        : {}
                   | Taxes               : {}
                   +------------------
                   | NET INCOME          : {}
                   +------------------------------------------------------


        """.format(self.name,
                   self.averagePrice,
                   self.averageUnitCost,
                   self.contributionMargin,
                   self.salesVolume,
                   self.revenue,
                   self.costOfGoodSold,
                   self.fixedCost,
                   self.totalCost,
                   self.grossMargin,
                   self.taxes,
                   self.netIncome)

        if willPrint:

            print(incomeStatementStr)

        else:

            return incomeStatementStr
        
    def plotting_price_cost(self):
        plt.plot(self.price_list, self.cost_list, "o--")
        plt.axhline(y=0, color='r', 
            linewidth=0.5, linestyle='-')
        plt.axvline(x=0, color='r', 
            linewidth=0.5, linestyle='-')
        plt.xlabel("price"); plt.ylabel("cost")
        plt.legend(["corresponding cost"])
        plt.title("price vs. cost")
        plt.grid()
        plt.show()

    # plot the result of break even analysis
    def plot_break_even_point(self):

        # create a numpy array for x line
        sellingRange = np.array(range(floor(self.breakEvenPoint + self.salesVolume * 0.5)))

        # calculate the revenue for each selling
        revenueRange = sellingRange * self.averagePrice

        # calculate COGS for each selling
        costRange = sellingRange * self.averageUnitCost + self.fixedCost

        # calculate the profit according to before steps
        profitRange = revenueRange - costRange

        # create figure object
        fig = plt.figure(figsize=(3, 3), dpi=150,
                         facecolor="lightgrey",
                         edgecolor="red",
                         linewidth=3)

        # add new axis
        ax = fig.add_axes([0, 0, 1, 1])  # axes

        # plot Revenue
        ax.plot(sellingRange, revenueRange, 'g-')
        # plot Cost
        ax.plot(sellingRange, costRange, 'r-.')
        # plot Profit
        ax.plot(sellingRange, profitRange, 'b--')

        # indicate the y line that break-even occurs
        ax.plot([floor(self.breakEvenPoint), floor(self.breakEvenPoint)], [0, revenueRange[-1]], 'ys--')

        # indicate break-even point
        ax.text(floor(self.breakEvenPoint) - len(sellingRange) * 0.3, 0, "Break-Even", fontsize=10,
                fontfamily="Times", color="k")

        # add legends
        ax.legend(labels=('Revenue', 'Cost', 'Profit'), loc='lower right')  # legend placed @lowerright

        # set title and labels
        ax.set_title("Break - Even Point Analysis")
        ax.set_xlabel('Sales')
        ax.set_ylabel('(Euro)')

        # set ticks and paddings
        ax.tick_params(axis='x', pad=5, rotation=30)
        ax.tick_params(axis='y', pad=5, rotation=45,
                       width=2, length=8, direction="inout")

        # add a grid to analyse it easily
        ax.grid(axis="y", color='r', ls=':', lw=0.5)

        # show the plot
        plt.show()

    # Determine the Present value of money
    def calculate_PV(self, futureValue, period, interestRate):
        # use economy formula
        # PV = FV / (1+i)^period
        return futureValue * (1 + interestRate) ** (-period)

    # Determine the futuve value of money
    def calculate_FV(self, presentValue, period, interestRate):
        # use economy formula
        # FV = PV * (1+i)^period
        return presentValue * (1 + interestRate) ** period





