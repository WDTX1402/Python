import os

class FileModifier:
    def __init__(self):
        self.filename = ""

    def main(self):
        self.filename = input("Enter a filename: ")

        if not os.path.exists(self.filename):
            print(f"The file {self.filename} does not exist.")
            return

        old_string = input("Enter the old string: ")
        new_string = input("Enter the new string: ")

        if old_string == new_string:
            print("The inputs are the same")
        

        self.replace_string(old_string, new_string)

    def replace_string(self, old_string, new_string):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()

            content = content.replace(old_string, new_string)

            with open(self.filename, 'w') as file:
                file.write(content)
            
            print("Done")

        except FileNotFoundError:
            print(f"Error: The file {self.filename} was not found.")


if __name__ == "__main__":
    file_modifier = FileModifier()
    file_modifier.main()
