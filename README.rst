===============================
Mini Matlab REPL Clone
===============================

.. .. image:: https://badge.fury.io/py/mini_matlab.png
..     :target: http://badge.fury.io/py/mini_matlab

.. .. image:: https://travis-ci.org/Habu-Kagumba/mini_matlab.png?branch=master
..         :target: https://travis-ci.org/Habu-Kagumba/mini_matlab

.. .. image:: https://pypip.in/d/mini_matlab/badge.png
..         :target: https://crate.io/packages/mini_matlab?version=latest


Mini Matlab clone (REPL)

Installing and running
----------------------

You can install through pip straight from my github repo.

.. code-block:: bash
   pip install -e git+https://github.com/Habu-Kagumba/mini_matlab#egg=mini_matlab


Running is as easy as;

.. highlight:: bash
   mini_matrix

Features
--------

- Array and Matrix creation through variables

.. code-block:: python
  a = [1, 2, 3]

  b = [1 2 3; 4 5 10]

  c = [10 30 50; 100 20 80]

  d = [1 3 5; 2 5 1; 3 5 2]

- Basic Matrix operations
  * Transpose
.. code-block:: bash
    b'

  * Inverse
.. code-block:: bash
   inv(d)

  * Multiplication
.. code-block:: bash
    c * d
    ```
  * Addition / Subtraction
.. code-block:: bash
    b + c

- Ability to save workspace on exit.

.. code-block:: bash
  Do you want to save your workspace? (yes|no) yes
  Successfully saved your workspace. Goodbye.

- Autocomplete features with mouse capability.


Requirements
------------

- Tested with Python 2.7
