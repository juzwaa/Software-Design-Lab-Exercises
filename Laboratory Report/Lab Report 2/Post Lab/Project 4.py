from breezypythongui import EasyFrame
from bank import Bank, createBank
# Code for the ATM class goes here (in atm.py)
def main(fileName = None):
 
    if not fileName:
        bank = createBank(5)
    else:
        bank = Bank(fileName)
    print(bank) # For testing only
    atm = ATM(bank)
    atm.mainloop()
 # Could save the bank to a file here.
if __name__ == "__main__":
 main()


class ATM(EasyFrame):

 def __init__(self, bank):
    EasyFrame.__init__(self, title = "ATM")
    self.unsuccessfulLoginCount = 0
    
def login(self):
    name = self.nameField.getText()
    pin = self.pinField.getText()
    self.account = self.bank.get(name, pin)
    if self.account:
        self.unsuccessfulLoginCount = 0
        self.statusField.setText("Hello, " + name + "!")
        self.balanceButton["state"] = "normal"
        self.depositButton["state"] = "normal"
        self.withdrawButton["state"] = "normal"
        self.loginButton["text"] = "Logout"
        self.loginButton["command"] = self.logout
    else:
        self.unsuccessfulLoginCount += 1
        if self.unsuccessfulLoginCount > 2:
            self.messageBox(title = "Attention", \
                        message = "Police is on the way")
            self.loginButton["state"] = "disabled"       
        else:
            self.messageBox(title = "Attention", \
                        message = "Police will be called after " + \
                        str (3 - self.unsuccessfulLoginCount) + " more consecutive login fails!")   
        self.statusField.setText("Name and pin not found!")