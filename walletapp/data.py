class Account:
    def __init__(self,account_name,opening_balance):
        self.account_name = account_name
        self.balance = opening_balance
    #Constructor

    def display(self):
        # Balance Inquiry
        return self.account_name + ' ' + f"{self.balance:,.2f}"

    def setAccountName(self, new_name):
        self.account_name = new_name

class Character:
    def __init__(self, character_name, vision, MyWeapon):
        self.__character_name = character_name
        self.__vision = vision
        self.__weapon = MyWeapon


    def display(self):
        self.__weapon.display()
        print(self.__character_name + ' ' + self.__vision)

    def setCharacterName(self, new_name):
        self.__character_name = new_name


class Weapon:
    def __init__(self, weapon_name, weapon_type):
        self.__weapon_name = weapon_name
        self.__weapon_type = weapon_type
        self.__level = 1

    def display(self):
        print(self.__weapon_name + ' ' + self.__weapon_type + ' ' + str(self.__level))


def run():
    dull_blade = Weapon('Dull Blade','Sword')
    #dull_blade.display()

    raiden_character = Character('Raiden Shogun', 'Electro', dull_blade)
    raiden_character.display()  # Display "Raiden Shogun Electro" on the screen

    # raiden_character.character_name = 'Yae Miko'
    # raiden_character.display()