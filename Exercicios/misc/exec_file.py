import os
import json

type Product = dict["name": str, "price": int]
type Data = list[Product]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CODE = 'utf-8'


def initialize_program():
  filename = os.path.join(BASE_DIR, 'data.json')
  temp_data = []

  print("Welcome to the file reader and writer program!")
  print("This program will read the contents of a file and allow you to write new content to it.")
  print("Please make sure the file exists before running the program.")
  print("Let's get started!")

  try:
    while True:
      print("------------ Menu ------------")
      print("1 - Write text to file")
      print("2 - Read file")
      print("3 - Write to file")
      print("4 - Save file")
      print("5 - List files in directory")
      print("6 - Exit")
      print("------------------------------")
      opt = input("Choose an option: ")
      match opt:
        case "1":
          insert_data(temp_data);
        case "2":
          read_file(filename)
        case "3":
          write_file(filename, temp_data)
        case "4":
          create_file(filename, temp_data)
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

def insert_data(temp_data: list[Product]):
  name = input("Enter product name: ")
  price = int(input("Enter product price: "))
  temp_data.append({"name": name, "price": price})

def read_file(filename):
  if not os.path.exists(filename):
    print("File does not exist.")
  else:
    with open(filename, 'r', encoding=CODE) as file:
      y = json.load(file)
      print("File content:")
      for product in y:
        print(f"Name: {product['name']}, Price: {product['price']}")

def write_file(filename, data: list[Product]):
  if not os.path.exists(filename):
    print("File does not exist. Please create the file first.")
    return
  
  with open(filename, 'w', encoding=CODE) as file:
    json.dump(data, file, indent=4)
    file.close()

def create_file(filename, data: list[Product]):
  with open(filename, 'w', encoding=CODE) as file:
    json.dump(data, file, indent=4)
    file.close()
    print(f"File '{filename}' created successfully.")

def list_files_in_directory(directory: str):
  files = os.listdir(directory)
  if not files:
    print("No files found in the directory.")
  else:
    print("Files in directory:")
    for file in files:
      print(file)

#initialize the program
if __name__ == "__main__":
  initialize_program()