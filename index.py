def write_to_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write("This is line 1\n")
            f.write("12345\n")
            f.write("Another line with some text\n")
        print("File 'my_file.txt' created and written successfully.")
    except FileNotFoundError:
        print("Error: File not found or path is incorrect.")
    except PermissionError:
        print("Error: Permission denied to write the file.")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Writing process completed.\n")

def read_and_display(filename):
    try:
        with open(filename, 'r') as f:
            print("Contents of 'my_file.txt':")
            for line in f:
                print(line.strip())
        print("\nFile read and displayed successfully.")
    except FileNotFoundError:
        print("Error: File not found or path is incorrect.")
    except PermissionError:
        print("Error: Permission denied to read the file.")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Reading process completed.\n")

def append_to_file(filename):
    try:
        with open(filename, 'a') as f:
            f.write("Appending line 1\n")
            f.write("Appending line 2\n")
            f.write("Appending line 3\n")
        print("Additional lines appended to 'my_file.txt' successfully.")
    except FileNotFoundError:
        print("Error: File not found or path is incorrect.")
    except PermissionError:
        print("Error: Permission denied to write the file.")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Appending process completed.\n")

def main():
    filename = "my_file.txt"
    write_to_file(filename)
    read_and_display(filename)
    append_to_file(filename)

if __name__ == "__main__":
    main()
