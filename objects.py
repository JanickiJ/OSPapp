#raczej nie bd potrzebne

from myfirebase import MyFirebase
class OSP():
    def __init__(self,firebase :MyFirebase):
        self.db = firebase
        self.password = None
        self.email = self.db.get_email()
        self.name = self.db.get_name()
        self.crew_members = [FireFighter(details) for details in self.db.get_crew_members()]
        self.address = self.db.get_address()
        self.reports = []


class FireFighter():
    def __init__(self, details):
        self.name = details[0]
        self.is_action_commander = details[1]
        self.is_driver = details[2]
        self.is_section_commander = details[3]

class Report():
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None
        self.number = None
        self.action_commander = None
        self.arrival_time = None


