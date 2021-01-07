from SimulationLibrary import SimulationEnvironment
from Company import Company
simEnv = SimulationEnvironment()

competitor1 = Company("Competitor1",25,63,["Desert","Salad"]    ,26,11,44533,21333,0.2)
competitor2 = Company("Competitor2",23,63,["Dinner","Salad"]    ,16,13,24533,23633,0.2)
competitor3 = Company("Competitor3",21,65,["Desert","Breakfast"],36,9,64533,23343,0.2)
competitor4 = Company("Competitor4",22,61,["Tea","Dring"]       ,46,26,77533,23233,0.2)

competitorList = []

competitorList.append(competitor1)
competitorList.append(competitor2)
competitorList.append(competitor3)
competitorList.append(competitor4)

simEnv.print_companies()

simEnv.define_competitor_companies(competitorList)

simEnv.print_companies()

simEnv.createCustomers()

simEnv.execute_simulation()

simEnv.calculate_simulation_results()

simEnv.report_simulation_log()

simEnv.report_company_results()

simEnv.report_simulation_summary()

simEnv.plot_price_cost()

competitor3.plot_break_even_point()