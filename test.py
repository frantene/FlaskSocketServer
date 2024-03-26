import pprint

class Test:
    def __init__(self):
        self.main = [True]
        self.other = "String is inherited"
        self.room = {}

    def create_room(self, room_code):
        self.room[room_code] = {
            "Inheritance Data": self.Inheritance(room=self.room, main=self.main)
        }

    class Inheritance:
        def __init__(self, room=None, main='Temporary'):
            self.main = main
            self.main.append('Hi')
            self.current = room

        def add_data(self, number):
            self.main.append(number)

        def set_room(self, code):
            self.current = code

    def data(self):
        return {'Main': self.main,
                'other': self.other,
                'Inheritance': self.room}

# Create an instance of the Test class
test_instance = Test()

# Call the create_room method
test_instance.create_room('Among Us')

# Access the data using the data() method
pprint.pprint(test_instance.data(), indent=2)

# Accessing and running a function in the Inheritance class
test_instance.room['Among Us']["Inheritance Data"].add_data("New data")
print(test_instance.room['Among Us']["Inheritance Data"].main)
