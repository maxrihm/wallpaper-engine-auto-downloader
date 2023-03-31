## Wallpaper Engine Auto Downloader
This is a Python-based software that automates the process of downloading wallpapers from Wallpaper Engine, a popular wallpaper software for Windows. With this program, you can download new wallpapers automatically on a daily basis and have them added to a new playlist in Wallpaper Engine.

### How it Works
This program uses the following Python libraries to detect and interact with images on the screen:

* OpenCV
* PyAutoGUI
* Pillow

The program checks the popular tab and recommended tab of Wallpaper Engine for new wallpapers that you don't already have, and downloads them automatically. It also creates a new playlist in Wallpaper Engine and adds all the downloaded wallpapers to it.

### How to Use
To use this program, you will need to have Python 3 installed on your computer. Once you have Python 3 installed, you can install the necessary libraries using pip. Here are the steps to get started:

1. Clone this repository to your local machine
2. Open a terminal window in the root directory of the repository
3. Install the required libraries using pip: `pip install -r requirements.txt`
4. Run the program: `python main.py`

The program will start running and will automatically download new wallpapers on a daily basis.

### Disclaimer
This program is not affiliated with Wallpaper Engine or any of its creators. Use at your own risk.
