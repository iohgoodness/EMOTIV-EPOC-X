
# Filename: Input.py
# Timestamp: 07/30/2021 14:07:55
# Author: @iohgoodness
# Description: For reading inputs from the eeg device


# Headset has a 9 hour battery life
# The input will be 14 different sensors
# When thinking about how these sensors are to be trained to perform certain actions,
# It is important to remember that slight things may effect these waves
# To ensure that the waves are as well seperated as possible,
# Big motions will be tested first, such as physical motions.

# The sensors include the following
# AF3, F7, F3, FC5, T7, P7, O1, O2, P8, T8, FC6, F4, F8, AF4

# We will want to track the patterns in the sensors as certain body motions are made

Sensors = []

class Input:

    # Init class with the eeg values as floats
    def __init__(self):
        self.AF3    = 0.0
        self.F7     = 0.0
        self.F3     = 0.0
        self.FC5    = 0.0
        self.T7     = 0.0
        self.P7     = 0.0
        self['01']  = 0.0
        self['02']  = 0.0
        self.P8     = 0.0
        self.T8     = 0.0
        self.FC6    = 0.0
        self.F4     = 0.0
        self.F8     = 0.0
        self.AF4    = 0.0

    # Save the sensor waves to a file to be read later
    def saveSensorWaves(self, fileName='output.csv'):
        pass
    # Reading the sensor waves for detecing patterns
    def readSensorWaves(self, fileName='output.csv'):
        pass

    # As far as recording the waves go, the idea is that they will be recorded
    # every 0.1 seconds, for around 2 seconds
    # This will ensure the human can make enough of the "test movement"
    # and that the waves and measurements can be recorded
    # They will be recorded as float values (to whatever signifigant figure is reasonable)
    def startRecordingWaves(self, increment=0.1, duration=2):
        pass
    def stopRecordingWaves(self, ):
        pass



