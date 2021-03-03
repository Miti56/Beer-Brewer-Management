Thanks for using this program to handle the brewing process of your company!

------------
I. File list
------------
brewing_program.py
prediction_writer.py
albert_info.txt
brigadiers_info.txt
camilla_info.txt
dylon_info.txt
emily_info.txt
florence_info.txt
gertrude_info.txt
harry_info.txt
hot_brew_info.txt
new_fermented_info.txt
total_info.txt
warnings.txt
test.log
pilsner_growth.txt
dunkel_growth.txt
total_growth.txt
organic_growth.txt
README.TXT      (duh)

--------------
II. HOW TO USE
--------------
                                                     ---------------
                                                     -PREDICTION_WRITER.PY-
                                                     ---------------
This program is CMD based, so it's locally accessible and no internet is required.
How to use:
    -Open your favorite IDE and load the file "Barnabys_sales_fabriacted_data_copy.csv" in the same folder as "prediction_writer.py"
    -Make sure the extension csv, queue and threading are installed.
    -Once running, select one of the option with the number pad.
    -Each month has is own corresponding number.
    -Select the current month, and the month you want to know about.
    -A prediction of the sale growth will be displayed in %, but will also be displayed in brewing_program.py
    -If it's negative, DON'T BREW THE BEER, it will not sell.
    -If it's positive, go for it!! The beer will most likely sell.

                                                    --------------------
                                                    -BREWING_PROGRAM.PY-
                                                    --------------------

Let's star with running the program:
    -Open the IDE of your choice and make sure that all the necessary extensions are downloaded (json, flask, logging)
    -Run the program named "Brewing_Program.py"
    -DO NOT USE THE GIVEN URL OR IT WILL CRASH instead use this one:
    http://127.0.0.1:5000/?hotbrew=0&cleardata3=on&name=0&cleardata=on&fermented=0&cleardata2=on
    -That's it! Easy right?

Now let's see how to use the program:
    1) In the top of the page you have a calendar and a clock to help track time
    2) Then we have the "Hot Brew Stage", where you can input the quantity of ingredients to brew.

    !!Only use numbers, if not, the program will crash!!
    Tip: you can always clear the data by selecting "Clear Data" and putting "0" as input.
    Tip: Select in all submit boxes and check "Clear Data" in all checkboxes to start again

    3) Then we have the "Ferment Beer" section, where you can assign the brewed ingredients into different tanks
    4) You have the total of free space in total, and in each tank to help running the brewery smoothly
    5) In the Fermentation Process Section you have access to the amount of fermented beer available, you can easily select
        where and assign precisely where to put the fermented beer
    6) Of course, there is real time information of the capacity of each tank
    7) In the "Bottling Process" you can see the amount of beer that need to be bottled and also the time it will take.
    8) Finally, you have an option to see all the data of all tanks and the growths previously selected,
        if the values are positive, the beer is going to most likely sell.


-------------------------
Design Decisions & Issues
-------------------------
This program is not perfect, the prediction program had to be modified manually, as panda stopped working hours before the deadline. All operations made
with it became unusable, so I had to rely on modifying manually the csv file instead.
In the other hand we have the "brewing_program.py", which is far from perfect. My knowledge was limited, and so many things couldn't be done as I wanted.
    -There is no schedule function, so everything must be done by hand.
    -Also there is no different types of beer, as following the way I did the program it could be easily another 500 lines of code
All of those problems could have been solved, but due to having such a short deadline this is what I did
The biggest problem wa


----------
DISCLAIMER
----------

This submission is supplied without any WARRANTY (EXPRESSED or IMPLIED)
and is intended in good faith to provide the Barnaby's team with a
way to test new functions in their company.

THIS PROGRAM IS IN NO WAY INTENDED FOR ANY BARNABY'S USER OR
ADMINISTRATOR TO IMPORT OR IN ANY WAY ADD INTO ANY OTHER SYSTEM. IT IS
PROVIDED FOR THE SOLE PURPOSE OF TESTING.


