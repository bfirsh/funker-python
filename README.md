# Funker for Python

A Python implementation of [Funker](https://github.com/bfirsh/funker).

## Installation

Add `funker` to your `requirements.txt` or install with Pip:

    $ pip install funker

## Usage

Defining functions:

```python
import funker

def handler(x, y):
    return x + y

if __name__ == '__main__':
    funker.handle(handler)
```

Calling functions:

```python
>>> import funker
>>> funker.call("add", x=1, y=2)
3
```
