## Python - Input/Output
A file is a container in computer systems that stores information

Files can have different forms: data files, text files, binary, etc
- These files are processed in bits of 0s and 1s

Files contain 3 main parts:
- **header**: contains information about the file: `filename`, `type`, `size`
- **data**: the file's content
- **end of file**: marks the end of a file

### Reading and Writing to Files
The built-in function `open()` opens a file and returns a file object
`f = open('filename', 'r')`
- `filename` refers to the path of the file we want to open
- `r`: access mode to the file(read), others are: `w` for write, `a`: append
- `f`: the file object returned, can be used to access the content of the file

### Close a file
It is important to close a file after processing is done, to free up resources and avoud corruption of the data, or unwanted data loss

Can be done by calling the `close` method on the file object

`f.close()`

### Key Concepts
- Opening a file
- Writing text to a file
- Read the full content of a file
- How to move the cursor in a file
- How to ensure a file is closed after using it
- How to use the `with` statement
- What is `JSON`, serialization and deserialization
- Converting a Python data structure to a JSON string and vice versa
