class Phone():
    """ This is a phone class that can be used for inheritance """
    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color

    def __str__(self):
        return f"This phone belongs to {self.phone_number}"
    
    def call(self, other_number):
        print(f"Calling number: {other_number}")

    def text(self, other_number, message):
        print(f"Sending text to {other_number}")
        print(message)

    def open_app(self, app_name):
        print(f"Opening: {app_name}")

class Android(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50

    def __str__(self):
        return f"Android phone that belongs to number {self.phone_number}"

    def set_passcode(self, passcode):
        self.passcode = passcode

    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print("Phone unlocked")
        else:
            print("Passcode Incorrect. Try Again")
        

    def view_battery_life(self):
        print(f"Battery Life: {self.battery}")

    def charge_phone(self, charging_amount):
        self.battery += charging_amount
        if self.battery > 100:
            self.battery = 100

    def view_phone_number(self):
        print(f"Phone number: {self.phone_number}")

class Iphone(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50

    def __str__(self):
        return f"iPhone phone that belongs to number {self.phone_number}"

    def set_passcode(self, passcode):
        self.passcode = passcode
        print("Passcode set")

    def change_passcode(self, current_passcode, new_passcode):
        if self.passcode == None:
            print("Please set passcode")
        else:
            if current_passcode == self.passcode:
                self.passcode = new_passcode
                print("New passcode set")
            else:
                print("Current passcode incorrect")


    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print("Phone unlocked")
        else:
            print("Passcode Incorrect. Try Again")
        

    def view_battery_life(self):
        print(f"Battery Life: {self.battery}")

    def charge_phone(self, charging_amount):
        self.battery += charging_amount
        if self.battery > 100:
            self.battery = 100

    def view_phone_number(self):
        print(f"Phone number: {self.phone_number}")

tuhoa_phone = Iphone('617-561-1111', 'black')

tuhoa_phone.view_battery_life()
tuhoa_phone.charge_phone(40)
tuhoa_phone.view_battery_life()
tuhoa_phone.view_phone_number()
tuhoa_phone.call("617-561-0711")
tuhoa_phone.set_passcode(4444)
tuhoa_phone.change_passcode(0000, 0000)
tuhoa_phone.change_passcode(4444, 0000)
tuhoa_phone.unlock_phone(0000)
tuhoa_phone.unlock_phone(4444)