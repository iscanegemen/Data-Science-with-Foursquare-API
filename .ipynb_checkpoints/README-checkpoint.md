# Data-Science-with-Foursquare-API-
Project for EE393 Python for Engineers

In this project we have tried to demonstrate our data analysis skills with Python. In order to achieve this task, we obtained coffee shop data from the Foursquare Places API. Then we created various hypotethical scenarios to create some business problems and solve them.

We shall now briefly explain how each and every one of the files in the project repository function, one by one.

Company.py => In this class, we describe all the functionalities of a real company like its name, location, sales volume etc. Then, we implemented all the necessary functions to prepare an income statement of the company. Also, we can determine its break-even point, present value and future value with additional functions we have implemented. Overall, one can understand what would it take establish a company from scratch with high-precision statistics and information.

Customer.py => In this class, we define all the attributes and functionalities of a real customer. We give an ID to represent each distinct customer, then we set their location, cash and range to the relevant company on a random basis.

datacollection_api.ipynb => Using the Foursquare Places API, we have come up with a large dataset which we can analyze and synthesize. We chose New York as our target city to work on. Then, we got the venues in New York in JSON format, parsed them and come up with a very large DataFrame. As a result, we have turned this DataFrame to a CSV file to use it in other classes.

EE393_Semester_Project_Map_SimpleGUI_CompanyObject_Version2.ipynb => This class is actually a graphical user interface which contains the attributes and a general report of a company. It displays everything in the Company.py in a GUI.

GetClosestCompanies.py => This class uses Distance.ipynb which we implemented in a seperate file. In this class, we get a set of inputs from the user as latitude and longitude. Once we get them, according to the set of input, we come up with the nearest companies to that specific latitude and longitude and print their name, latitude, longitude and the calculated distance to the set of latitude and longitude the user entered.

Map.py => It represents the visualization of the found possible "rival" companies.

Near_Class.ipynb => It prints all the necessary information about the possible "rival" companies like their tip count, their photo count on the Web, their ratings, their likes etc.

SimulationExecution.py => It executes the simulation based on default competitors. From that, it calculates and prints the companies, creates the customers in a random manner, and plots the break-even point to guide the user whether to establish such a company in these circumstances or not.

SimulationLibrary.py => It contains all the necessary implementations of the simulation environment such as defining the competitors, creating the customers, calculating the distances between "rival" companies, creating the customer choices etc.

newyorkcoffeewithdetails.csv => It contains the CSV as a result of datacollection_api.ipynb.

