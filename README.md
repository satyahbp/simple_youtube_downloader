# Simple YouTube Downloader
This is a python code that is gonna download 720p YouTube videos.
It has to be run in the command line, or using any python interpreter in your IDE.
<br><br>
This code users a Python package called <b>pytube</b>.<br>
You can get a complete documentation of how pytube works here: https://pytube.io/en/latest/index.html
<br><br>

## Process
First step, download/clone this code. <br><br>

Once downloaded, you need to have python installed in your computer. <br>
You can install python from here: https://www.python.org/ <br>
<br>
Once python is installed, make sure to install <b>pytube</b> package. <br>
You can install the package using the following command in your command line:
```bash
pip install pytube
```
If the above command doesn't work, try the following:
```bash
python -m pip install pytube
```
or
```bash
python3 -m pip install pytube
```

Note: <b>You need to have Python installed to install pytube package.</b>
<br><br>
Great! Once everything is installed, go to the folder where you have this code and copy the link of the youtube videos you want to download, and paste them in a the file named as <b>file.txt</b>
<br><br>
You have to put each link in a new line.
<br><br>
Then next step is to create a folder named <b>downloaded_files</b> in the same folder that carries this code.
<br><br>
Once it is done, you're all set to download.<br><br>
Go to command prompt or terminal, navigate to the folder that carries this code and then type the following command:
```bash
python yt_downloader.py
```
If the above command didn't work (especially if you're in linux), try this command:
```bash
python3 yt_downloader.py
```
And done! <br><br>
If the code didn't show any error, you can find all your files downloaded in the <b>downloaded_files</b> folder.<br>
<br>
I hope you have a good day! Thanks for using this tool. <br><br>
If you want to show support, do leave a star on this github repo!