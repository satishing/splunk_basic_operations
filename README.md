# SPLUNK SDK BASIC OPERATIONS

### Prerequisite:
- Python 3.x

### Project prerequisitels
Set following splunk environment variables
```cmd
set SPLUNK_HOST=<splunk hostname>     # Default is locaalhost
set SPLUNK_PORT=<splunk port>         # Default is 8089
set SPLUNK_USER<splunk username>      # Default is admin
set SPLUNK_PASSWORD<splunk password>
```

### Environment Setup
Clone this project
```cmd
git clone https://github.com/satishing/splunk_basic_operations.git
```
Move to project directory 
```cmd
python3 --version 

virtualenv venv -p python3
source .\venv\bin\activate.cmd
pip install -r requirements.txt

set PYTHONPATH=.\venv\lib\python3.8\site-packages

python3 run.py
```

