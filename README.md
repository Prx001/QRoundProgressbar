# QRoundProgressbar
## Custom round progressbar widget implemented in PyQt5 for PyQt5 applications!
[![CodeFactor](https://www.codefactor.io/repository/github/prx001/qroundprogressbar/badge)](https://www.codefactor.io/repository/github/prx001/qroundprogressbar)

### An easy-to-use and modern round progressbar for Qt Python binding PyQt (PyQt5) 📦

## Preview
https://user-images.githubusercontent.com/67240789/147384366-c0f83458-01e0-40c2-8c32-bfb3df69e8e4.mp4

QRoundProgressbar is a custom progressbar widget inherited from 'QWidget' class, and acts as a QProgressBar alternative widget in your PyQt5 application.

## How to use?
### Installation
The package is available on [PyPi](https://pypi.org) so as always use pip for installation:
```
pip install QRoundProgressbar
```

### Usage in your Python application
First of all, as expected, you need to import the package.
Import 'RoundProgressbar' class from the package:
```python
from QRoundProgressbar import RoundProgressbar
```
Now the widget is ready to use!
There are things you can define for the widget, like the progressbar color, background color, size, thickness and some other things.
The package also contains a '__main__' script as shown in the video above so you can test the widget easily:
```
python -m QRoundProgressbar
```
You can use default values for the widget:
```python
round_progressbar = RoundProgressbar(parent)
```
Or define the values yourself. Bellow is an example:
```python
round_progressbar = RoundProgressbar(
	parent=window,
	color=QColor("darkblue"),
	size=120,
	thickness=14,
	value=80,
	maximum=100,
	round_edge=True,
	bg_circle_color=QColor("pink"),
	fill_bg_circle=True
)
```
# Qt Designer integration
Qt Designer is a very extensible tool, even can support your custom widgets! It means you can interact with your custom widget just as you do with Qt widgets, like QPushButton, QCheckBox, you can drag and drop them on your form, change their sizes, set properties and so on.
Qt Designer can load plugins, and you can load your custom widgets through plugins, then your custom widget is available in Qt Designer Widget Box. In C++, using Qt Creator IDE you can create your custom widgets and compile them to a .dll file, then you put the dll file (your plugin) into Qt Designer's relative path for plugins, and that's it you can use your widget in Designer. But, here in python the story is a little different. PyQt supports this plugin developement and can integrate *Python based* Qt custom widgets in Qt Designer. [Learn more about integrating PyQt custom widgets in Qt Designer](https://wiki.python.org/moin/PyQt/Using_Python_Custom_Widgets_in_Qt_Designer) There is the Qt Designer plugin for QRoundProgressbar in package, [QRoundProgressbarplugin.py](https://github.com/Prx001/QRoundProgressbar/blob/main/QRoundProgressbar/QRoundProgressbarplugin.py). You can load it to your Qt Designer.





https://user-images.githubusercontent.com/67240789/147383897-60699224-9c02-4bfa-9c64-a0e33053b510.mp4









