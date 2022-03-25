import io

try:
    file = open("files.csv", "r")
    print(file.read())
    file.close()
except FileNotFoundError as e:
    print("Error: ", e)

    """ Output: Error:  [Errno 2] No such file or directory: 'files.txt'"""
    """
    In a production system, ensure the file to be read from already exist before attempting to open.
    This can be done by either manually creating the file or programmatically creating the file in write mode.
    """

try:
    file1 = open("file.txt", "w")
    print(file1.readlines())
    file1.close()
except io.UnsupportedOperation as e:
    print("Error: ", e)

    """Output: Error:  not readable"""
    """
    In production system, ensure you open files in the correct mode.
    r mode to read file only. w mode to write file only. w+ or r+ to read and write to.
    a to append to already existing file.
    """
try:
    file2 = open("file.txt", "r")
    print(next(file2))
    print(next(file2))
    file2.close()
except StopIteration:
    print("Error: File does not have enough content to iterate through")

    """Output: Error: File does not have enough content to iterate through. """
    """
    In production, always check if the file has content in the next line before 
    iterating through. Other failsafe approaches might be to use a loop going though the content
    line by line or reading all the content at once.
    """
