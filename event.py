import datetime

class Event:
    'Common base class for all events'

    def __init__(self, name, year, month, day, hour, minute):
        self.name = name
        self.date = datetime.datetime(year, month, day, hour, minute)

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.name == other.name and self.date == other.date

    def __gt__(self, other):
        """Override the default behavior"""
        return self.date > other.date

    def __lt__(self, other):
        """Override the default behavior"""
        return self.date < other.date

    def displayEvent(self):
        print("Nazwa wydarzenia: ", self.name, " Data rozpoczęcia: ", self.date)