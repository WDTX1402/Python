import pickle
import os 

class Phonebook:
    def __init__(self):
        self.contacts = {}
        self.filename = None
        self.bad = ['nahee', 'tianmensquare', 'visis']
    def main(self):
        while True:
            inpus = input("Enter your command: ")

            if inpus == "+":
                new_contact = input("Enter name: ")
                num = int(input("Enter a number: "))
                self.contacts[new_contact] = num

            elif inpus == "-":
                contact = input("Enter name: ")
                if contact in self.contacts:
                    self.contacts.pop(contact)
                else:
                    print("No contact found")
            
            elif inpus == "f":
                contact = input("Enter name: ")
                print(self.contacts.get(contact, "No contact found"))

            elif inpus == "p":
                print(self.contacts)
            
            elif inpus == "s":
                self.filename = input("Enter filename (with .pkl extension): ")
                for i in self.bad:
                    if i == self.filename:
                        raise NameError("Offensive name is not allowed ( ｡ •̀ ᴖ •́ ｡)")  
                    else:
                        self.save_data_as()
            
            elif inpus == "l":
                self.filename = input("Enter filename (with .pkl extension): ")
                self.load_data()

            elif inpus == "q":
                break 

    def save_data_as(self):
        if os.path.exists(self.filename):
            print("This file already exists")
        elif self.filename:
            with open(self.filename, 'wb') as f:
                pickle.dump(self.contacts, f)
            print(f"Data saved to {self.filename}.")
        else:
            print("No filename specified.")

    def load_data(self):
        if self.filename:
            try:
                with open(self.filename, 'rb') as f:
                    self.contacts = pickle.load(f)
                print(f"Data loaded from {self.filename}.")
            except (FileNotFoundError, EOFError, pickle.UnpicklingError) as e:
                print(f"Error loading data: {e}")
        else:
            print("No filename specified.")

if __name__ == "__main__":
    pb = Phonebook()
    pb.main()
