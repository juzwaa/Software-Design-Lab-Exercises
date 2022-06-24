from breezypythongui import EasyFrame
class LabelDemo(EasyFrame):
 
 def __init__(self):

    EasyFrame.__init__(self)
    self.addLabel(text = "Jozhua Lenard Huertas", row = 0, column = 0)
    self.addLabel(text = "July 01, 2002", row = 0, column = 10)
    
def main():

 LabelDemo().mainloop()
if __name__ == "__main__":
 main()
 