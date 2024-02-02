# Setup
```
make environment python
pip install PyQt5 pyinstaller
```
Or use this
```
pip install -r requirements.txt
```

o) make .py file for desktop app \
o) run this code for compile into .exe: 

```
# with console
pyinstaller --onefile 'file name'.py

# without console
pyinstaller --onefile --noconsole 'file name'.py 
```