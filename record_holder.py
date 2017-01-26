class Record_Holder:
    def __init__(self, name, country, number_of_catches):
        self.name = name
        self.country = country
        self.number_of_catches = number_of_catches


    def set_country(self, country):
        self.country = country

    def set_number_of_catches(self, number_of_catches):
        self.number_of_catches = number_of_catches

    def __str_(self):
        template = 'Name: {} Country: {} Number Of Catches: {}'
        return template.format(self.name, self.country, self.number_of_catches)
