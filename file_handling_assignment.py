def write_to_file():
    try:
        # Create a new text file in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write three lines of text to the file
            file.write("This is the fifth plp week 1\n")
            file.write("21, 05, 2024 \n")
            file.write("2024 is the year we make some changes\n")
        print("File created and initial content written successfully.")
    except IOError as e:
        print("Error: Unable to write to file.", e)
    finally:
        file.close()


def read_and_display():
    try:
        # Open the file in read mode
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied to access the file.")


def append_to_file():
    try:
        # Open the file in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
        print("Three lines appended to the file successfully.")
    except IOError as e:
        print("Error: Unable to append to file.", e)
    finally:
        file.close()


if __name__ == "__main__":
    # Write to file
    write_to_file()

    # Read and display file contents
    read_and_display()

    # Append to file
    append_to_file()
