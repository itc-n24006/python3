class Person:
    def __init__(self,
            name = '',
            nationality = '',
            birth = '',
            addres = ''):
        
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.addres = address

    def show_attributes(self):
        print("名前", self.name)
        print("国籍", self.nationality)
        print("生まれ年", self.birth)
        print("住んでいる所", self.address)

