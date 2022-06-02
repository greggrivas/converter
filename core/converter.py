import os

class Converter:
    """
    The Converter class which will perform the necessary conversions
    """
    def __int__(self):
        """
        the constructor of the Converter class for the initialization of the required variables
        """
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.degs = 0.0
        self.temp = 0
        self.temp2 = 0

    @staticmethod
    def hours_to_degs(hours, mins, secs):
        degs = float((hours + mins / 60 + secs / 3600) * 15)
        return degs

    @staticmethod
    def degs_to_hours(degs: float):
        hours = int(degs / 15)
        temp = degs / 15
        mins = int(60 * (temp - hours))
        temp2 = 60 * (temp - hours)
        secs = int(round(60 * (temp2 - int(mins)),1))
        return hours, mins, secs

#test = Converter()
#print(test.degs_to_hours(30.5))
