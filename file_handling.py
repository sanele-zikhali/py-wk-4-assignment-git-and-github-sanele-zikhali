def read_and_file():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, 'r') as file:
            content = file.readlines()

        modified_content = [line.upper() for line in content]

        new_filename = "modified_" + filename

        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)

        print(f"Modified content has been saved to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read the file. Please check the file permissions.")

read_and_file()
