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





