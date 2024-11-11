# How to run the project

Follow the given instruction to run the project, and write the commands in your shell (command prompt for windows).

## Clone the project repository
first of all clone the github repository 
```
git clone https://github.com/Khushboo-Dar/Digital-signal-generator.git
```

now change your directory to the project directory using `cd Digital-signal-generator`

## Setup Virtual environment

### For Linux
now we will create a virtual environment to install packages
```
virtualenv venv
```

now activate the virtaul environment and install required packages
```
source venv/bin/activate
```

### For Windows
create a virtaul environment
```
python -m venv venv
```

activate the virtual environment
```
venv\Scripts\activate
```

## Install the packages required

```
pip3 install numpy matplotlib
```

## Run the project
TO run the project we will run the follwing command
```
python3 main.py
```

