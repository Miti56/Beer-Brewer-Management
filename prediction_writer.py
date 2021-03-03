import csv
import json


# open the csv file with the orders data and quantity
def open_doc_orders():
    """
    Open the csf files with the sells data
    :return: the list with the data appended
    """
    with open("Barnabys_sales_fabriacted_data_copy.csv") as file:
        csv_reader = csv.reader(file)
        data_year = list()
        for row in csv_reader:
            # joins data from data an quantity ordered
            data_year.append((row[11]))
        list_data_sells = list(data_year)
        return list_data_sells

def see_total_growth():
    """
    Calculates total growth form different months
    :return: info about growth
    """
    with open("Barnabys_sales_fabriacted_data_copy.csv") as file:
        csv_reader = csv.reader(file)
        data_year = list()
        for row in csv_reader:
            # joins data from data an quantity ordered
            data_year.append((row[11]))
        list_data_sells = list(data_year)
    year_total_growth = list_data_sells
    print("Select to see TOTAL GROWTH")
    print("January--> 1 // December --> 12")
    first_month = year_total_growth[int(input("select current month"))]
    last_month = year_total_growth[int(input("Select the month you want to know about"))]
    year_growth = ((int(last_month) - int(first_month)) / int(first_month)) * 100
    print('The growth for the selected months was:{0}%'.format(str(round(year_growth))))
    print("If the value is positive, the beer is going to sell")
    print("If the value is negative, the beer is not going to sell")

    # Write info into json
    data = {}
    data['total_growth_info'] = []
    data['total_growth_info'].append({'growth': year_growth})
    with open('total_growth_info.txt', 'w') as outfile:
        json.dump(data, outfile)


def see_organic_red_growth():
    """
        Calculates total growth form different months
        :return: info about growth
        """
    with open("Barnabys_sales_fabriacted_data_copy.csv") as file:
        csv_reader = csv.reader(file)
        data_year = list()
        for row in csv_reader:
            # joins data from data an quantity ordered
            data_year.append((row[8]))
        list_data_sells = list(data_year)
    year_organic_growth = list_data_sells
    print("Select the months to calculate ORGANIC BEER growth ")
    print("January--> 1 // December --> 12")
    first_month = year_organic_growth[int(input("select current month"))]
    last_month = year_organic_growth[int(input("Select the month you want to know about"))]
    year_growth = ((int(last_month) - int(first_month)) / int(first_month)) * 100
    print('The red growth for the selected months was:{0}%'.format(str(round(year_growth))))
    print("If the value is positive, the beer is going to sell")
    print("If the value is negative, the beer is not going to sell")
    # write data to  corresponding file
    data = {}
    data['organic_growth_info'] = []
    data['organic_growth_info'].append({'growth': year_growth})
    with open('organic_growth_info.txt', 'w') as outfile:
        json.dump(data, outfile)


def see_pilsner_growth():
    """
        Calculates total growth form different months
        :return: info about growth
        """
    with open("Barnabys_sales_fabriacted_data_copy.csv") as file:
        csv_reader = csv.reader(file)
        data_year = list()
        for row in csv_reader:
            # joins data from data an quantity ordered
            data_year.append((row[9]))
        list_data_sells = list(data_year)
    year_pilsner_growth = list_data_sells
    print("Select the months to calculate PILSNER BEER growth ")
    print("January--> 1 // December --> 12")
    first_month = year_pilsner_growth[int(input("select the current month"))]
    last_month = year_pilsner_growth[int(input("Select last month"))]
    year_growth = ((int(last_month) - int(first_month)) / int(first_month)) * 100
    print('The pilsner growth for the selected months was:{0}%'.format(str(round(year_growth))))
    print("If the value is positive, the beer is going to sell")
    print("If the value is negative, the beer is not going to sell")
    # write data to  corresponding file
    data = {}
    data['pilsner_growth_info'] = []
    data['pilsner_growth_info'].append({'growth': year_growth})
    with open('pilsner_growth_info.txt', 'w') as outfile:
        json.dump(data, outfile)


def see_dunkel_growth():
    """
        Calculates total growth form different months
        :return: info about growth
        """
    with open("Barnabys_sales_fabriacted_data_copy.csv") as file:
        csv_reader = csv.reader(file)
        data_year = list()
        for row in csv_reader:
            # joins data from data an quantity ordered
            data_year.append((row[10]))
        list_data_sells = list(data_year)
    year_dunkel_growth = list_data_sells
    print("Select the months to calculate DUNKEL BEER growth ")
    print("January--> 1 // December --> 12")
    first_month = year_dunkel_growth[int(input("select the current month"))]
    last_month = year_dunkel_growth[int(input("Select the month you want to know about"))]
    year_growth = ((int(last_month) - int(first_month)) / int(first_month)) * 100
    print('The dunker growth for the selected months was:{0}%'.format(str(round(year_growth))))
    print("If the value is positive, the beer is going to sell")
    print("If the value is negative, the beer is not going to sell")
    # write data to  corresponding file
    data = {}
    data['dunkel_growth_info'] = []
    data['dunkel_growth_info'].append({'growth': year_growth})
    with open('dunkel_growth_info.txt', 'w') as outfile:
        json.dump(data, outfile)


see_total_growth()
see_dunkel_growth()
see_organic_red_growth()
see_pilsner_growth()