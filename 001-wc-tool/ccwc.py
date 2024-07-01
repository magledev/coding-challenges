import sys
import os


def wc(file_path, cmd_option):
    try:
        with open(file_path, "rb") as f:
            match cmd_option:
                # Count bytes
                case "-c":
                    # Begin at start of file, up until the end i.e. an empty byte
                    f.seek(0, 2)
                    # Get the current postion in bytes, which represents the file size
                    file_bytes = f.tell()
                    return file_bytes
                # Count lines
                case "-l":
                    file_lines = 0
                    # Loop through the file and count the number of lines
                    for _ in f:
                        file_lines += 1
                    return file_lines
                case _:
                    print(f"'{cmd_option}' is not a valid option")
    except FileNotFoundError:
        return f"File not found:"
    except PermissionError:
        return f"Permission denied:"
    except Exception as e:
        return f"An error has occured: {e}"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            (
                "Usage: ccwc.py [OPTION]... [FILE]..."
                "\nOptions:"
                "\n-c\tprint the byte counts"
                "\n-l\tprint the line counts"
            )
        )
    else:
        cmd_option = sys.argv[1]
        file_path = sys.argv[2]
        file_name = os.path.basename(file_path)
        file_size = wc(file_path, cmd_option)
        if file_size is not None:
            print(f"{file_size} {file_name}")
