# Issues with latest python

When following instructions from [Adafruit RGB Matrix Bonnet for Raspberry Pi: Python Usage](https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/python-usage)

## TL;DR
After receiving the `ModuleNotFoundError: No module named 'distutils'` error...

1. From `rpi-rgb-led-matrix/` folder, run `pip install setuptools`
2. Run the following code in terminal:
```
cd bindings/python
python -m pip install .
```

-----

## Error Message: `ModuleNotFoundError: No module named 'distutils' `*

### Example run
```
(rgbmatrix) username@pi_name:~ $ cd rpi-rgb-led-matrix/
make install-python
make -C ./lib
make[1]: Entering directory '/home/username/rpi-rgb-led-matrix/lib'
make[1]: Leaving directory '/home/username/rpi-rgb-led-matrix/lib'
make -C examples-api-use
make[1]: Entering directory '/home/username/rpi-rgb-led-matrix/examples-api-use'
make -C ../lib
make[2]: Entering directory '/home/username/rpi-rgb-led-matrix/lib'
make[2]: Leaving directory '/home/username/rpi-rgb-led-matrix/lib'
make[1]: Leaving directory '/home/username/rpi-rgb-led-matrix/examples-api-use'
make -C bindings/python build
make[1]: Entering directory '/home/username/rpi-rgb-led-matrix/bindings/python'
make -C ../../lib
make[2]: Entering directory '/home/username/rpi-rgb-led-matrix/lib'
make[2]: Leaving directory '/home/username/rpi-rgb-led-matrix/lib'
make -C rgbmatrix
make[2]: Entering directory '/home/username/rpi-rgb-led-matrix/bindings/python/rgbmatrix'
make[2]: Nothing to be done for 'all'.
make[2]: Leaving directory '/home/username/rpi-rgb-led-matrix/bindings/python/rgbmatrix'
python3 setup.py build --build-lib .
Traceback (most recent call last):
  File "/home/username/rpi-rgb-led-matrix/bindings/python/setup.py", line 6, in <module>
    from distutils.core import setup, Extension
ModuleNotFoundError: No module named 'distutils'
make[1]: *** [Makefile:68: build-python] Error 1
make[1]: Leaving directory '/home/username/rpi-rgb-led-matrix/bindings/python'
make: *** [Makefile:29: build-python] Error 2
```

### The Culprit: `make install-python`
There is a library that cannot be found within `setup.py`

## Solution: `pip install setuptools`
Run it in the terminal, and setuptools has the distutils library built in.
Credit goes to [Solved: How to Fix the ‘No module named distutils.util’ Error in Python](https://sqlpey.com/python/fix-the-no-module-named-distutils-util-error-in-python/)

## Error Message: `SetuptoolsDeprecationWarning: setup.py install is deprecated.`
### Example run
```
(rgbmatrix) username@pi_name:~/rpi-rgb-led-matrix $ make install-python
make -C ./lib
make[1]: Entering directory '/home/username/rpi-rgb-led-matrix/lib'
make[1]: Leaving directory '/home/username/rpi-rgb-led-matrix/lib'
make -C examples-api-use
make[1]: Entering directory '/home/username/rpi-rgb-led-matrix/examples-api-use'
make -C ../lib
make[2]: Entering directory '/home/username/rpi-rgb-led-matrix/lib'
make[2]: Leaving directory '/home/username/rpi-rgb-led-matrix/lib'
make[1]: Leaving directory '/home/username/rpi-rgb-led-matrix/examples-api-use'
make -C bindings/python build
make[1]: Entering directory '/home/username/rpi-rgb-led-matrix/bindings/python'
make -C ../../lib
make[2]: Entering directory '/home/username/rpi-rgb-led-matrix/lib'
make[2]: Leaving directory '/home/username/rpi-rgb-led-matrix/lib'
make -C rgbmatrix
make[2]: Entering directory '/home/username/rpi-rgb-led-matrix/bindings/python/rgbmatrix'
make[2]: Nothing to be done for 'all'.
make[2]: Leaving directory '/home/username/rpi-rgb-led-matrix/bindings/python/rgbmatrix'
python3 setup.py build --build-lib .
make[1]: Leaving directory '/home/username/rpi-rgb-led-matrix/bindings/python'
make -C bindings/python install
make[1]: Entering directory '/home/username/rpi-rgb-led-matrix/bindings/python'
python3 setup.py install
/home/username/rgbmatrix/lib/python3.13/site-packages/setuptools/_distutils/cmd.py:90: SetuptoolsDeprecationWarning: setup.py install is deprecated.
!!

        ********************************************************************************
        Please avoid running ``setup.py`` directly.
        Instead, use pypa/build, pypa/installer or other
        standards-based tools.

        This deprecation is overdue, please update your project and remove deprecated
        calls to avoid build errors in the future.

        See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
        ********************************************************************************

!!
  self.initialize_options()
make[1]: Leaving directory '/home/username/rpi-rgb-led-matrix/bindings/python'
```

### The Culprit [Why you shouldn't invoke setup.py directly](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)

### The solution
Assumes you are in the `~/rpi-rgb-led-matrix/` folder.
<!-- Container for code block + button -->
<div style="position: relative;">
  <!-- Copy button -->
  <button 
    style="position: absolute; top: 5px; right: 5px; z-index: 1;"
    onclick="navigator.clipboard.writeText(document.getElementById('my-code-snippet').textContent).then(() => this.textContent = 'Copied!').then(() => setTimeout(() => this.textContent = 'Copy', 2000))"
  >
    Copy
  </button>
 
  <!-- Code snippet (with id for targeting) -->
  <pre><code id="my-code-snippet">
cd bindings/python
python -m pip install .
  </code></pre>
</div>