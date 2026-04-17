import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CODE = 'utf-8'

def initialize_program():
  filename = os.path.join(BASE_DIR, 'data.txt')
  text = ''

  print("Welcome to the file reader and writer program!")
  print("This program will read the contents of a file and allow you to write new content to it.")
  print("Please make sure the file exists before running the program.")
  print("Let's get started!")
  print("------------ Menu ------------")
  print("1 - Write text to file")
  print("2 - Read file")
  print("3 - Write to file")
  print("4 - Save file")
  print("5 - List files in directory")
  print("6 - Exit")
  print("------------------------------")

  try:
    while True:
      opt = input("Choose an option: ")
      match opt:
        case "1":
          text = input("Enter the text you want to write to the file: ")
        case "2":
          read_file(filename)
        case "3":
          write_file(filename, text)
        case "4":
          create_file(filename, text)
        case "5":
          print(f"Listing files in: {BASE_DIR}")
          list_files_in_directory(BASE_DIR)
        case "6":
          print("Exiting program. Goodbye!")
          exit()
        case _:
          print("Invalid option. Please try again.")
  except Exception as e:
    print("An error occurred:", e)

def read_file(filename):
  if not os.path.exists(filename):
    print("File does not exist.")
  else:
    with open(filename, 'r', encoding=CODE) as file:
      data = file.read()
      print("File contents:")
      print(data)
      file.close()
  

def write_file(filename, text):
  with open(filename, 'w', encoding=CODE) as file:
    file.write(text)
    file.close()
  print("Text written to file successfully.")



def create_file(filename, text):
  if os.path.exists(filename):
    print("File already exists. Please choose a different name or delete the existing file.")
    return
  
  with open(filename, 'x', encoding=CODE) as file:
    file.write(text)
    file.close()
  print("File created and text written successfully.")

def list_files_in_directory(directory):
  files = sorted(os.listdir(directory))
  if not files:
    print("No files found in the directory.")
    return
  
  print("Files in directory:")
  for file in files:
    print(file)

#initialize the program
if __name__ == "__main__":
  initialize_program()