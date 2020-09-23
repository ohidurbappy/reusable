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
random_string() : return a random string of specified length and character set
print_table() : prints a data table provided as list
print_time_taken [decorator] : prints the time of execution of a parameter
groupby_count() : groups a given list according the number of times it appears


