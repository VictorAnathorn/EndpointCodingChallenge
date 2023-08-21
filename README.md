# Directory Management System

A command-line application that allows CRUD operations for virtual directories.

## Features

- **Create Directories**: Easily create hierarchical directories.
- **List Directories**: Display the current structure of created directories.
- **Move Directories**: Move directories from one location to another.
- **Delete Directories**: Remove directories and their sub-directories.

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:VictorAnathorn/EndpointCodingChallenge.git
   ```

2. Navigate to the project directory:
   ```bash
   cd EndpointCodingChallenge
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running in an Isolated Environment

To ensure that dependencies do not conflict, it's recommended to run this project in a virtual environment.

### Prerequisites

Ensure you have `python3` and `pip` installed. If not, you can download and install them from the official [Python website](https://www.python.org/downloads/).

You'll also need `virtualenv`. Install it with:
```bash
pip install virtualenv
```

### Steps to Set Up and Run in a Virtual Environment

1. **Create a virtual environment**:
Navigate to the project root directory in your terminal or command prompt. Then run:
```bash
python3 -m venv venv_name
```
Replace `venv_name` with a name you'd like for your virtual environment. This will create a directory named `venv_name` in your project root.

2. **Activate the virtual environment**:

   - For **Linux/Mac**:
     ```bash
     source venv_name/bin/activate
     ```

   - For **Windows** (Command Prompt):
     ```bash
     venv_name\Scripts\activate.bat
     ```

   - For **Windows** (PowerShell):
     ```bash
     venv_name\Scripts\Activate.ps1
     ```

After activation, your terminal or command prompt should display the name of your virtual environment, confirming its activation.

3. **Install project dependencies**:
With the virtual environment activated, install the required dependencies:
```bash
pip install -r requirements.txt
```

4. **Run the project**:
With the virtual environment still active, you can now run the project:
```bash
python directories.py
```

5. **Deactivate the virtual environment**:
Once you're done, you can deactivate the virtual environment and return to your global Python context:
```bash
deactivate
```

## Testing

To run the unit tests, ensure you have `pytest` installed (from `requirements.txt`) and then run:
```bash
pytest
```

## Commands

- `CREATE [directory-path]`: Creates the specified directory.
- `MOVE [source-path] [destination-path]`: Moves the directory from source to destination.
- `DELETE [directory-path]`: Deletes the specified directory.
- `LIST`: Displays the current structure of directories.

## Example

Input:
```bash
CREATE fruits
CREATE vegetables
LIST
```

Output:
```
CREATE fruits
CREATE vegetables
fruits
vegetables
```

## Providing Input

### Inline Input:

1. Run the script using the command `python directories.py`.
2. Enter your commands one by one or paste them using `CTRL-V`
3. When you are done entering all your commands, enter empty string to signal the end of input and execute the commands.

### Using Default Commands:

You can also run the script with the `--default` flag to automatically use the predefined command list:

```bash
python directories.py --default
```

This will execute the default list of commands using the `verification-input.txt` file and will output the results in `verification-output.txt`.
