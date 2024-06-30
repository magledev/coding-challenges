import sys
import os


def get_file_size(file_path, cmd_option):
    try:
        if cmd_option == "-c":
            with open(file_path, "rb") as f:
                # Begin at start of file, up until the end i.e. an empty byte
                f.seek(0, 2)
                # Get the current postion, which represents the size
                size = f.tell()
            return size
        else:
            print(f"'{cmd_option}' is not a valid option")
    except FileNotFoundError:
        return f"File not found:"
    except PermissionError:
        return f"Permission denied: {file_path}"
    except Exception as e:
        return f"An error has occured: {e}"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: ccwc.py <option> <file_path>")
    else:
        cmd_option = sys.argv[1]
        file_path = sys.argv[2]
        file_name = os.path.basename(file_path)
        file_size = get_file_size(file_path, cmd_option)
        if file_size is not None:
            print(f"{file_size} {file_name}")
