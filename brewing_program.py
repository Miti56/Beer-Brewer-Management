from flask import Flask, render_template
from flask import request
import json
import logging
app = Flask(__name__)

# IMPORTANT NOTICE:
# Enter link: http://127.0.0.1:5000/?hotbrew=0&cleardata3=on&name=0&cleardata=on&fermented=0&cleardata2=on
# If the program is opened without any input it gives a fatal error :/

def clear_data():
    """
    :return: nothing, just clears data in all json when called
    """
    # adding logging capabilities
    logging.basicConfig(filename='test.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    # Clears data florence data
    with open('florence_info.txt') as json_file:
        data_info = json.load(json_file)
    data = {'info_beer': []}
    data['info_beer'].append({
        'name': 'florence', 'quantity': '0'})
    with open('florence_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in Florence has been cleaned")


    # Clears data in emily info
    with open('emily_info.txt') as json_file:
        data_info = json.load(json_file)
    data = {'info_beer': []}
    data['info_beer'].append({
        'name': 'emily', 'quantity': '0'})
    with open('emily_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in Emily has been cleaned")

    # Clears data in total info
    with open('total_info.txt') as json_file:
        data = json.load(json_file)
    # reset json file
    data = {'info_beer': []}
    data['info_beer'].append({'name': 'total','quantity': "0"})
    with open('total_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in Total has been cleaned")

    # Clears data in albert info
    with open('albert_info.txt') as json_file:
        data_info = json.load(json_file)
    data = {'info_beer': []}
    data['info_beer'].append({'name': 'albert', 'quantity': '0'})
    with open('albert_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in Albert has been cleaned")

    # Clears data in brigadiers info
    with open('brigadiers_info.txt') as json_file:
        data_info = json.load(json_file)
    data = {'info_beer': []}
    data['info_beer'].append({'name': 'dunkers', 'quantity': '0'})
    with open('brigadiers_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in Brigadiers has been cleaned")

    # Clears data in camilla info
    with open('camilla_info.txt') as json_file:
        data_info = json.load(json_file)
    data = {'info_beer': []}
    data['info_beer'].append({'name': 'camilla', 'quantity': '0'})
    with open('camilla_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in Camilla has been cleaned")

    # Clears data in dylon info
    with open('dylon_info.txt') as json_file:
        data_info = json.load(json_file)
    data = {'info_beer': []}
    data['info_beer'].append({'name': 'dylon', 'quantity': '0'})
    with open('dylon_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in Dylon has been cleaned")





def clear_data2():
    """
    Clears data of second part when needed
    :return: nothing, just clears the txt files
    """
    # adding logging capabilities
    logging.basicConfig(filename='test.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    # Clears data in harry info
    with open('harry_info.txt') as json_file:
        data_info = json.load(json_file)
    data = {'info_beer': []}
    data['info_beer'].append({
        'name': 'harry', 'quantity': '0'})
    with open('harry_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in Harry has been cleaned")

    # Clears data in gertrude info
    with open('gertrude_info.txt') as json_file:
        data_info = json.load(json_file)
    data = {'info_beer': []}
    data['info_beer'].append({
        'name': 'gertrude', 'quantity': '0'})
    with open('gertrude_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in Harry has been cleaned")

def clear_data3():
    """
    Same as the others function, but only for hot brew
    :return: still nothing
    """
    # adding logging capabilities
    logging.basicConfig(filename='test.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    # Clears data in hot brew info
    with open('hot_brew_info.txt') as json_file:
        data_info = json.load(json_file)
    data = {'info_beer': []}
    data['info_beer'].append({'name': 'hot brew', 'quantity': '0'})
    with open('hot_brew_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in Hot brew has been cleaned")

def clear_data4():
    """
    Same as the other function but for the growth data
    :return: nothing...
    """
    # adding logging capabilities
    logging.basicConfig(filename='test.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    # clears data in total
    with open('total_growth_info.txt') as json_file:
        data_info = json.load(json_file)
    data = {'total_growth_info': []}
    data['total_growth_info'].append({'growth': '0'})
    with open('gertrude_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in Total growth has been cleaned")

    # clears data in dunkel
    with open('dunkel_growth_info.txt') as json_file:
        data_info = json.load(json_file)
    data = {'dunkel_growth_info': []}
    data['dunkel_growth_info'].append({'growth': '0'})
    with open('dunkel_growth_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in dunkel growth has been cleaned")

    # clears data in pilsner
    with open('pilsner_growth_info.txt') as json_file:
        data_info = json.load(json_file)
    data = {'pilsner_growth_info': []}
    data['pilsner_growth_info'].append({'growth': '0'})
    with open('pilsner_growth_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in pilsner growth has been cleaned")

    # clears data in organic
    with open('organic_growth_info.txt') as json_file:
        data_info = json.load(json_file)
    data = {'organic_growth_info': []}
    data['organic_growth_info'].append({'growth': '0'})
    with open('organic_growth_info.txt', 'w') as outfile:
        json.dump(data, outfile)
    logging.debug("Data in organic growth has been cleaned")


@app.route('/', methods=['POST', 'GET'])
def brew_state_tank_1():
    """
    Function takes care of info about each tank
    :return: Return info storage remaining and state of each tank
    """
    # adding logging capabilities
    logging.basicConfig(filename='test.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    #get infgo about hot brew
    with open('hot_brew_info.txt') as json_file:
        data = json.load(json_file)
        list_hot_brew = []
        # append info a obout tank in json file
        for p in data['info_beer']:
            tanks = p['quantity']
            list_hot_brew.append(tanks)
        # add values to each tank
        hot_brew_volume = (list_hot_brew[0])
        logging.debug("tank1 volume: ", hot_brew_volume)
        # Ask for beer quantity
    ask_quantity_hot_brew = request.args.get("hotbrew")
    logging.debug("quantity asked for hot brew is: ", ask_quantity_hot_brew)
    new_hot_brew = ask_quantity_hot_brew
    logging.debug("quantity after calc :", new_hot_brew)
    # append hot brew info to file
    data = {}
    data['info_beer'] = []
    data['info_beer'].append({'name': 'hot brew', 'quantity': new_hot_brew})
    with open('hot_brew_info.txt', 'w') as outfile:
        json.dump(data, outfile)

    # clear data if needed--------------------------------------------
    if request.args.get("cleardata3"):
        logging.debug("Clearing Data of Hot Brew")
        clear_data3()
    else:
        logging.debug("No need to clear Data in Hot Brew")

    # get the info from all tanks
    with open('total_info.txt') as json_file:
        data = json.load(json_file)
        list_tanks = []
        # append info a obout tank in json file
        for p in data['info_beer']:
            tanks = p['quantity']
            list_tanks.append(tanks)
        # add values to each tank
        tank1_volume = (list_tanks[0])
        logging.debug("tank1 volume: ", tank1_volume)
        # Ask for beer quantity
    ask_quantity = request.args.get("name")
    logging.debug("quanntity asked for Fermentation: ", ask_quantity)
    # add info about tank to new variable
    new_tank_volume = int(tank1_volume) + int(ask_quantity)
    logging.debug("New tank volume for fermentation: ", new_tank_volume)

    # append volume to json file--------------------------------------
    data = {}
    data['info_beer'] = []
    data['info_beer'].append({'name': 'total', 'quantity': new_tank_volume})
    with open('total_info.txt', 'w') as outfile:
        json.dump(data, outfile)

    # clear data if needed--------------------------------------------
    if request.args.get("cleardata"):
        logging.debug("Clearing Data for fermentation")
        clear_data()
    else:
        logging.debug("No need to clear Data in fermentation")

    # show warning if limit reached----------------------------------
    if new_tank_volume > 5400:
        logging.debug("No more space in fermentation tanks, remove load")
        # add new value to tank
        new_tank_volume = "5400"
        # add the info to webpage
        data = {}
        data['warnings'] = []
        data['warnings'].append({'name': 'There is no space'})
        with open('warnings.txt', 'w') as outfile:
            json.dump(data, outfile)
        # open the file
        with open('warnings.txt') as json_file:
            data_warnings = json.load(json_file)
            warnings = []
            for p in data_warnings['warnings']:
                warnings = p['name']
                logging.debug("Warning shown are",warnings)
    else:
        # add info to json file
        remaining_storage = "You still have:", int("5400") - int(new_tank_volume), "L of free space"
        data = {}
        data['warnings'] = []
        data['warnings'].append({'name': remaining_storage})
        with open('warnings.txt', 'w') as outfile:
            json.dump(data, outfile)
        # open the file
        with open('warnings.txt') as json_file:
            data_warnings = json.load(json_file)
            warnings = []
            for p in data_warnings['warnings']:
                warnings = p['name']
                logging.debug("Warning shown are:", warnings)

    # Append data into corresponding files--------------------------------------------
    # open corresponding file
    with open('florence_info.txt') as json_file:
        data_info = json.load(json_file)
        volume_tank_florence = []
    with open('emily_info.txt') as json_file:
        data_info = json.load(json_file)
        volume_tank_emily = []
    with open('albert_info.txt') as json_file:
        data_info = json.load(json_file)
        volume_tank_albert = []
    with open('brigadiers_info.txt') as json_file:
        data_info = json.load(json_file)
        volume_tank_brigadiers = []
    with open('camilla_info.txt') as json_file:
        data_info = json.load(json_file)
        volume_tank_camilla = []
    with open('dylon_info.txt') as json_file:
        data_info = json.load(json_file)
        volume_tank_dylon = []

        # second option checkbox ---> brigadiers
        if request.args.get("checkbox2"):
            logging.debug("brigadiers: Selected", int(ask_quantity))
            with open('brigadiers_info.txt') as json_file:
                data_info_brigadiers = json.load(json_file)
                volume_tank_brigadiers = []
                for p in data_info_brigadiers['info_beer']:
                    tank_used = p['quantity']
                    volume_tank_brigadiers.append(tank_used)
                volume_tank_brigadiers = int(volume_tank_brigadiers[0]) + int(ask_quantity)
                logging.debug("The volume of beer in brigadiers: ", volume_tank_brigadiers)

                # Write info into json
                data = {}
                data['info_beer'] = []
                data['info_beer'].append({
                    'name': 'dunkers', 'quantity': volume_tank_brigadiers})
                with open('brigadiers_info.txt', 'w') as outfile:
                    json.dump(data, outfile)


        # third option checkbox --> camilla
        elif request.args.get("checkbox3"):
            logging.debug("Camilla: Selected", int(ask_quantity))
            with open('camilla_info.txt') as json_file:
                data_info_camilla = json.load(json_file)
                volume_tank_camilla = []
                for p in data_info_camilla['info_beer']:
                    tank_used = p['quantity']
                    volume_tank_camilla.append(tank_used)
                volume_tank_camilla = int(volume_tank_camilla[0]) + int(ask_quantity)
                logging.debug("The volume of beer in camilla: ", volume_tank_camilla)
                # Write info into json
                data = {}
                data['info_beer'] = []
                data['info_beer'].append({
                    'name': 'camilla', 'quantity': volume_tank_camilla})
                with open('camilla_info.txt', 'w') as outfile:
                    json.dump(data, outfile)



        # first option checkbox --> albert
        elif request.args.get("checkbox1"):
            logging.debug("Albert: Selected", int(ask_quantity))
            with open('albert_info.txt') as json_file:
                data_info_albert = json.load(json_file)
                volume_tank_albert = []
                for p in data_info_albert['info_beer']:
                    tank_used = p['quantity']
                    volume_tank_albert.append(tank_used)
                volume_tank_albert = int(volume_tank_albert[0]) + int(ask_quantity)
                logging.debug("The volume of beer in albert: ", volume_tank_albert)

                # Write info into json
                data = {}
                data['info_beer'] = []
                data['info_beer'].append({
                    'name': 'albert', 'quantity': volume_tank_albert})
                with open('albert_info.txt', 'w') as outfile:
                    json.dump(data, outfile)

        # forth option checkbox --> dylon
        elif request.args.get("checkbox4"):
            logging.debug("Dylon: Selected", int(ask_quantity))
            with open('dylon_info.txt') as json_file:
                data_info_dylon = json.load(json_file)
                volume_tank_dylon = []
                for p in data_info_dylon['info_beer']:
                    tank_used = p['quantity']
                    volume_tank_dylon.append(tank_used)
                volume_tank_dylon = int(volume_tank_dylon[0]) + int(ask_quantity)
                logging.debug("The volume of beer in dylon: ", volume_tank_dylon)

                # Write info into json
                data = {}
                data['info_beer'] = []
                data['info_beer'].append({
                    'name': 'dylon', 'quantity': volume_tank_dylon})
                with open('dylon_info.txt', 'w') as outfile:
                    json.dump(data, outfile)


        # fith option checkbox --> emily
        elif request.args.get("checkbox5"):
            logging.debug("Emily: Selected", int(ask_quantity))
            with open('emily_info.txt') as json_file:
                data_info_emily = json.load(json_file)
                volume_tank_emily = []
                for p in data_info_emily['info_beer']:
                    tank_used = p['quantity']
                    volume_tank_emily.append(tank_used)
                volume_tank_emily = int(volume_tank_emily[0]) + int(ask_quantity)
                logging.debug("The volume of beer in emily: ", volume_tank_emily)

                # Write info into json
                data = {}
                data['info_beer'] = []
                data['info_beer'].append({
                    'name': 'dylon', 'quantity': volume_tank_emily})
                with open('emily_info.txt', 'w') as outfile:
                    json.dump(data, outfile)


        # sixth option checkbox --> florence
        elif request.args.get("checkbox6"):
            logging.debug("Florence: Selected", int(ask_quantity))
            with open('florence_info.txt') as json_file:
                data_info_florence = json.load(json_file)
                volume_tank_florence = []
                for p in data_info_florence['info_beer']:
                    tank_used = p['quantity']
                    volume_tank_florence.append(tank_used)
                volume_tank_florence = int(volume_tank_florence[0]) + int(ask_quantity)
                logging.debug("The volume of beer in Florence: ", volume_tank_florence)

                # Write info into json
                data = {}
                data['info_beer'] = []
                data['info_beer'].append({
                    'name': 'florence', 'quantity': volume_tank_florence})
                with open('florence_info.txt', 'w') as outfile:
                    json.dump(data, outfile)
        else:
            pass

    # making variable easier to handle
    brigadiers = volume_tank_brigadiers
    camilla = volume_tank_camilla
    albert = volume_tank_albert
    dylon = volume_tank_dylon
    emily = volume_tank_emily
    florence = volume_tank_florence

    # --------------------------------------SECOND STAGE-----------------------------------------

    # clear data if needed
    if request.args.get("cleardata2"):
        logging.debug("Clearing Data Second Stage")
        clear_data2()

    else:
        logging.debug("No need to clear Data of Second stage")

    # get value from form
    ask_quantity_fermented = request.args.get("fermented")
    # open info.txt and send it to webpage
    with open('total_info.txt') as json_file:
        data = json.load(json_file)
        for p in data['info_beer']:
            fermented = p['quantity']
    # Add values to gertrude or harry
    with open('harry_info.txt') as json_file:
        data_info = json.load(json_file)
        volume_tank_harry = []
    with open('gertrude_info.txt') as json_file:
        data_info = json.load(json_file)
        volume_tank_gertrude = []
    logging.debug("First fermented", fermented)
    # different choices with checkbox

    # Choice gertrude
    if request.args.get("gertrude"):
        logging.debug("gertrude: Selected", int(ask_quantity_fermented))
        with open('gertrude_info.txt') as json_file:
            data_info_gertrude = json.load(json_file)
            volume_tank_gertrude = []
            for p in data_info_gertrude['info_beer']:
                tank_used_fermented = p['quantity']
                volume_tank_gertrude.append(tank_used_fermented)
            volume_tank_gertrude = int(volume_tank_gertrude[0]) + int(ask_quantity_fermented)

            # Write info into json
            data = {}
            data['info_beer'] = []
            data['info_beer'].append({
                'name': 'gertrude', 'quantity': volume_tank_gertrude})
            with open('gertrude_info.txt', 'w') as outfile:
                json.dump(data, outfile)




    # Choice harry
    elif request.args.get("harry"):
        logging.debug("harry: Selected", int(ask_quantity_fermented))
        with open('harry_info.txt') as json_file:
            data_info_harry = json.load(json_file)
            volume_tank_harry = []
            for p in data_info_harry['info_beer']:
                tank_used_fermented = p['quantity']
                volume_tank_harry.append(tank_used_fermented)
            volume_tank_harry = int(volume_tank_harry[0]) + int(ask_quantity_fermented)

            # Write info into json
            data = {}
            data['info_beer'] = []
            data['info_beer'].append({
                'name': 'harry', 'quantity': volume_tank_harry})
            with open('harry_info.txt', 'w') as outfile:
                json.dump(data, outfile)
    else:
        pass

    # we get last fermented stage
    new_fermented = int(fermented) - int(ask_quantity_fermented)
    # Write that info into respective file
    data = {}
    data['info_beer'] = []
    data['info_beer'].append({
        'name': 'total', 'quantity': new_fermented})
    with open('total_info.txt', 'w') as outfile:
        json.dump(data, outfile)




    # make varialbes easier to handle
    logging.debug("new fermented", new_fermented)
    gertrude = volume_tank_gertrude
    logging.debug("volume gertrude", gertrude)
    harry = volume_tank_harry
    logging.debug("volume harry ", harry)

    # Bottling information
    with open('harry_info.txt') as json_file:
        data_info_harry = json.load(json_file)
        for p in data_info_harry['info_beer']:
            harry_quantity = p['quantity']
    with open('gertrude_info.txt') as json_file:
        data_info_harry = json.load(json_file)
        for p in data_info_harry['info_beer']:
            gertrude_quantity = p['quantity']
    # sum two tanks get whole beer quantity
    bottling_number = int(gertrude_quantity) + int(harry_quantity)

    # get time for bottling knowing that each bottle take 2s to fill
    if bottling_number > 0:
        time_remaining = ((int(bottling_number)*2)/0.5)/3600
    else:
        time_remaining = ("Waiting for bottles to brew")
    # returns time in hour

    return render_template("brew_info.html", tank1_volume=new_tank_volume, warnings=warnings,
                           info_beer_brigadiers=brigadiers, info_beer_albert=albert,
                           info_beer_camilla=camilla, info_beer_dylon=dylon, info_beer_emily=emily,
                           info_beer_florence=florence, fermented=fermented, fermented_gertrude=gertrude,
                           fermented_harry=harry, info_hot_brew = new_hot_brew, bottling_number = bottling_number,
                           time_remaining = time_remaining)

@app.route('/data', methods=['POST', 'GET'])
def view_all_data():

    # adding logging capabilities
    logging.basicConfig(filename='test.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    with open('total_info.txt') as json_file:
        data_info_total = json.load(json_file)
        print(data_info_total)
    with open('albert_info.txt') as json_file:
        data_info_albert = json.load(json_file)
        print(data_info_albert)
    with open('brigadiers_info.txt') as json_file:
        data_info_brigadiers = json.load(json_file)
        print(data_info_brigadiers)
    with open('camilla_info.txt') as json_file:
        data_info_camilla = json.load(json_file)
        print(data_info_camilla)
    with open('dylon_info.txt') as json_file:
        data_info_dylon = json.load(json_file)
        print(data_info_dylon)
    with open('emily_info.txt') as json_file:
        data_info_emily = json.load(json_file)
        print(data_info_emily)
    with open('florence_info.txt') as json_file:
        data_info_florence = json.load(json_file)
        print(data_info_florence)
    with open('gertrude_info.txt') as json_file:
        data_info_gertrude = json.load(json_file)
        print(data_info_gertrude)
    with open('harry_info.txt') as json_file:
        data_info_harry = json.load(json_file)
        print(data_info_harry)

    # add growth data
    with open('total_growth_info.txt') as json_file:
        data_info_total_growth = json.load(json_file)
        print(data_info_total_growth)
    with open('organic_growth_info.txt') as json_file:
        data_info_organic = json.load(json_file)
        print(data_info_organic)
    with open('pilsner_growth_info.txt') as json_file:
        data_info_pilsner = json.load(json_file)
        print(data_info_pilsner)
    with open('dunkel_growth_info.txt') as json_file:
        data_info_dunkel = json.load(json_file)
        print(data_info_dunkel)



    return render_template("data.html", data_info_florence = data_info_florence, data_info_brigadiers = data_info_brigadiers,
                           data_info_total = data_info_total,
                           data_info_harry = data_info_harry, data_info_albert = data_info_albert,
                           data_info_dylon = data_info_dylon, data_info_camilla = data_info_camilla,
                           data_info_gertrude = data_info_gertrude, data_info_emily= data_info_emily,
                           total_year_growth = data_info_total_growth, organic_year_growth = data_info_organic,
                           pilsner_year_growth = data_info_pilsner, dunkel_year_growth = data_info_dunkel)

if __name__ == "__main__":
    app.run(debug=True)
