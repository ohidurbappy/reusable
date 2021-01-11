# reusable
Python reusable code, utility functions and time saver.

## Overview
Python `reusable` library contains a handful of reusable functions and utility class

### Install

```bash
pip install -U reusable
```

## Usage
### Loading Configuration files as class attributes

```python
from reusable import AppConfig
config=AppConfig('config.json')
mykey=config.my_key
```
### Load config file accessible via class methods

```python
from reusable import Config
config=Config('config.json')
mykey=config.get('my_key')
```

## Available functions
- **random_string()** : return a random string of specified length and character set
- **print_table()** : prints a data table provided as list
- **print_time_taken** [decorator] : prints the time of execution of a parameter
- **groupby_count()** : groups a given list according the number of times it appears
- **generate_all_datetime_regex** : generate the regex for all possible datetime
- **download_file** : download a file from the given url
- **is_python3()** : check if the interpreter is python v3
- **is_python_above_or_equal()** : check if the interpreter is above or equal to the given version
- **check_modules_installed()** : check if the given modules are installed
- **random_useragent()** : return a random useragent
- **is_valid_json()** : checks if given string is valid json
- **headline()** : return a formatted string in headline style
- **splash()** : return a string with splash style
- **multiline_input()** : takes multiline user input
- **get_datadir()** : returns the app data folder
- **get_windows_appdata_dir()** : similar to get_datadir() but windows only
