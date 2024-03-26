import pprint
class Test:
    def __init__(self):
        self.main = [True]
        self.other = "String is inherited"
        self.inheritance = self.Inheritance(self.main)

    class Inheritance:
        def __init__(self, main):
            self.main = main
            self.main.append('Hi')

        def add_data(self, number):
            self.main.append(number)

    def data(self):
        return {'Main': self.main,
                'Inherited': self.other}

# Create an instance of the Test class
test_instance = Test()

# Call the add_data method
test_instance.inheritance.add_data(5)

# Access the data using the data() method
pprint.pp(test_instance.data(), indent=2)

