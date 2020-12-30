## 制作exe
  ```
  pip install pyinstaller
  cd src
  pyinstaller -F --icon=uploader.ico dingding-cookie-uploader.py
  ```

## 常见错误

- The MATPLOTLIBDATA environment variable was deprecated in Matplotlib 3.1 and will be removed in 3.3.   exec(bytecode, module.__dict__)

  ```
  pip install 'matplotlib==3.0.3'
  ```

- ModuleNotFoundError: No module named 'pkg_resources.py2_warn'

  ```
  pip install --upgrade 'setuptools<45.0.0'
  ```

- Processes stuck in loop with PyInstaller-executable

  ```
  You need to use multiprocessing.freeze_support() when you produce a Windows executable with PyInstaller.
  ```

- TypeError: cafile, capath and cadata cannot be all omitted

  ```
  Upgrade websocket to 0.57.0
  ```

## Reference
- https://github.com/pypa/setuptools/issues/1963
- https://stackoverflow.com/questions/57517371/matplotlibdeprecationwarning-with-pyinstaller-exe
- https://stackoverflow.com/questions/54065079/processes-stuck-in-loop-with-pyinstaller-executable