import os
import sys


def get_file_bytes(file_name, cmd_option):
    try:
        if cmd_option == "-c":
            return f"{os.stat(file_name).st_size} {file_name}"
        else:
            print(f"'{cmd_option}' is not a valid command line option")
    except FileNotFoundError:
        return f"File {file_name} not found"
    except PermissionError:
        return f"Permission denied: '{file_name}'"
    except Exception as e:
        return f"An error occured: {e}"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: ccwc.py <option> <file_name>")
        print(f"Options: -c (bytes)")
    else:
        cmd_option = sys.argv[1]
        file_name = sys.argv[2]
        result = get_file_bytes(file_name, cmd_option)
        if result is not None:
            print(result)
