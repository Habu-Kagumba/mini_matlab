Mini Matlab REPL Clone
===============================

Installing and running
----------------------

You can install through pip straight from my github repo. *Preferably do this in a virtual environment*.

```bash
pip install -e git+https://github.com/Habu-Kagumba/mini_matlab#egg=mini_matlab
```

or alternatively you can clone this repo and install from the root directory.

```bash
git clone https://github.com/Habu-Kagumba/mini_matlab

# Recommended - do this in an environment.

python setup.py develop
```

Running is as easy as;

```bash
mini_matlab
```

Features
--------

- **Array and Matrix creation through variables.**

```python
  a = [1, 2, 3]

  b = [1 2 3; 4 5 10]

  c = [10 30 50; 100 20 80]

  d = [1 3 5; 2 5 1; 3 5 2]
```

- **Basic Matrix operations.**
  * Transpose
  
    ```bash
    b'
    ```
    
  * Inverse
  
    ```bash
    inv(d)
    ```
    
  * Multiplication
  
    ```bash
    c * d
    ```
  
  * Addition / Subtraction
  
    ```
    b + c
    ```

- **Ability to save workspace on exit and automatically loaded during the next session.**

```bash
  Do you want to save your workspace? (yes|no) yes
  Successfully saved your workspace. Goodbye.
```

- **Autocomplete features with mouse capability.**


Requirements
------------

- Tested with Python 2.7
