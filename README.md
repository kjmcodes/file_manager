# Python File Organizer

Jump to:
  - [Description](#description)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Contributing](#contributing)
## Description
This project is an automated script written in Python that organizes files into folders by format.

It uses the `os` and `shutil` modules to access the OS and shell utilities respectively.

These three lines of code:
```
root_folder = os.path.dirname(os.path.realpath(__file__))
root_folder = root_folder.replace("\\","/")
downloaded_items = os.listdir (root_folder)
```
are responsible for the following functions respectively:

1. Getting the path of the script and saving that as in a varible named `root_folder`
2. Changing the back slash signs returned from the previous line into a forward slash to prevent the program from searching for non-existent escape sequences
3. Accessing each item in `root_folder`

The next part of the script uses the `splitext` function, specifically designed to split the extension type from the file name. This way, you'd get `.md` from README.md, for instance.


`type = f"{type[1:].upper()}s"` would give you "MDs" by:

1. Eliminating the period at index 0
2. Capitlizing every remaining character
3. Adding "s" to the end of the string to pruralize it

If/when the script creates a new folder for each file type, it uses the value from this step to name it using `new_folder = f"{root_folder}/{type}"`

The remaining lines of code:

1. Check for existing folders for each file type the script discovers using `if os.path.exists (new_folder)`
2. Creates and names a folder if it doesn't find one using `os.makedirs (new_folder)`
3. Moves the files into the approproate locations using `shutil.move(f"{root_folder}/{item}", f"{new_folder}/{item}")`

## Setup
You only need to save and move the script into <i>any</i> folder you want to organize. The original version of this project was built to handle only the User/Downloads folder but the current version is more versatile.

For stability and best results, I recommend having Python 3.8 or later. Download the latest version from the official [Python website](https://www.python.org/downloads/).

## Usage
Running the script via command line or IDE should get it to automatically perform the tasks as required.

Just in case you're new to running .py scripts, you can go through the most popular methods in the video below:

[![How to run Python scripts](https://img.youtube.com/vi/1DtlzSDdk4s/0.jpg)](https://www.youtube.com/watch?v=1DtlzSDdk4s "How to run .py scripts")

## Contributing
Please feel free to add to the code! I'm certain there are ways to improve it that I'm yet to find; my previous iterations of this very script prove this.

If you're up to it, check out [a blog post I wrote](https://medium.com/@kevinteaches/how-i-test-my-students-b75f01c751d0) about the last version of this script to see the improvements I've made since.
