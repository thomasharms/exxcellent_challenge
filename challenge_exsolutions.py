import pandas as pd
import os.path


'''
Task Weather Challenge is solved by class Weather_Data
in order to run it use the predefined instantiation in line 137

Task Football Challenge is solved by class Football_Data
in order to run it use the predefined instantiation in line 139

just run the file to see both solutions printed to stdout
'''

class Weather_Data():

    __data_path = 'src/main/resources/de/exxcellent/challenge/'
    __data_file = 'weather.csv'

    def __init__(self):
        # read csv data into DataFrame self.data
        self.read_weather_data_from_csv()

        # compute min-max temperature distance for each day and assign it
        # into DataFrame column self.data['difference']
        self.compute_min_max_distance()

        # select smallest temperature min-max distance by day
        # assign it to self.min_difference
        self.get_min_temperature_distance_by_day()

    # assigns a DataFrame (matrix) containing the weather data to self.data
    def read_weather_data_from_csv(self):

        # check if file exists at the location in path
        if os.path.isfile(str(self.__data_path)+str(self.__data_file)):
            # assign csv data to pandas DataFrame
            self.data = pd.read_csv(str(self.__data_path)+str(self.__data_file))

        else:
            #TODO might be deleted in deployment
            # in case there is no file... give some hint to user what went wrong
            print("File does not exist. Please check the path and file location. Run program out of folder programming-challenge.")
        
    # assign the distance from min_temperature_value to maxtemperature_value into a column in DataFrame
    # new column is named "difference" and can be referenced in that fashion
    def compute_min_max_distance(self):

        if not self.data.empty:
            self.data['difference'] = abs(self.data['MxT'] - self.data['MnT'])
        else:
            #TODO might be deleted in deployment
            print('No data exists.')

    # select the day with smallest difference in temperature min-max distance by day and
    # assign it to self.min_difference
    def get_min_temperature_distance_by_day(self):
        if not self.data['difference'].empty:
            
            # idxmin() returns index of the row where column 'difference' has the minimum value
            # loc[] returns the row of this index and we need the value in row 'Day'
            try:
                self.min_difference = int(self.data.loc[self.data['difference'].idxmin()]['Day'])
            
            # in case something goes wrong provide an explanation
            #TODO might be deleted in deployment
            except Exception as e:
                print('Could not select minimal temperature difference due to: %s' % (str(e)))
        
        else:
            # in case the column self.data['difference'] does not exists explain...
            #TODO might be deleted in deployment
            print('An error occured while selecting the minimal temperature difference by day')
      

class Football_Data():

    __data_path = 'src/main/resources/de/exxcellent/challenge/'
    __data_file = 'football.csv'

    def __init__(self):
        # read csv data into DataFrame self.data
        self.read_football_data_from_csv()
        
        # compute goal difference and assign it
        # into DataFrame column self.data['difference']
        self.compute_goal_difference()

        # select smallest amount of goal distance by team
        # assign it to self.min_difference
        self.get_min_goal_difference_by_team()


    # assigns a DataFrame (matrix) containing the weather data to self.data
    def read_football_data_from_csv(self):

        # check if file exists at the location in path
        if os.path.isfile(str(self.__data_path)+str(self.__data_file)):
            # assign csv data to pandas DataFrame
            self.data = pd.read_csv(str(self.__data_path)+str(self.__data_file))

        else:
            # in case there is no file... give some hint to user what went wrong
            print("File does not exist. Please check the path and file location. Run program out of folder programming-challenge.")
        
    # assign the goal difference into a column in DataFrame
    # new column is named "difference" and can be referenced in that fashion
    def compute_goal_difference(self):

        if not self.data.empty:
            self.data['difference'] = abs(self.data['Goals'] - self.data['Goals Allowed'])
        else:

            # TODO: provide some hint for debug purposes... might be deleted in deployment
            print('No data exists.')

    # select the team with smallest amount of goal difference and assign it to self.min_difference
    def get_min_goal_difference_by_team(self):
        if not self.data['difference'].empty:
            
            # idxmin() returns index of the row where column 'difference' has the minimum value
            # loc[] returns the row of this index and we need the value in row 'Team'
            try:
                self.min_difference = self.data.loc[self.data['difference'].idxmin()]['Team']
            
            # in case something goes wrong provide an explanation
            #TODO might be deleted in deployment
            except Exception as e:
                print('Could not select team with smallest amount of goal difference due to: %s' % (str(e)))
        
        else:
            # in case the column self.data['difference'] does not exists explain...
            #TODO might be deleted in deployment
            print('An error occured while selecting the smallest goal difference by team')


weather_challenge = Weather_Data()
print(weather_challenge.min_difference)
football_challenge = Football_Data()
print(football_challenge.min_difference)
