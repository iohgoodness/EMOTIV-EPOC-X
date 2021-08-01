
# Filename: Query.py
# Timestamp: 07/30/2021 14:08:07
# Author: @iohgoodness
# Description: For making queries using the eeg device


# In theory, we will be able to make google searches (and other possible queries) using just eeg brain waves
# For this test, we will have some simple python web searching examples

class Query:
    def __init__(self):
        # Search string will be for putting together letters adn then searching something on google
        # result will then be returned VIA earpiece
        self.SearchString = ''

    # Check between two numbers
    def inRange(self, minValue, maxValue, value):
        if value >= minValue and value <= maxValue:
            return True
        return False
    
    def getWeather(self):
        pass

