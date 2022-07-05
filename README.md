# Virtual joystick with computer vision
## Overview
Virtual joystick with computer vision is an open-source project that simulates a joystick by moving a hand and it can be used to play racing games. 


![ezgif-4-4e00d29e37](https://user-images.githubusercontent.com/15442079/177322315-df07a035-e9ab-4db5-a7fc-ff8299622c0d.gif)  

## Getting Started  
First, clone the project 
```
git clone https://github.com/ehsanrs2/Virtual-joystick-with-computer-vision.git
```

The `requirements.txt` file should list all Python libraries that your notebooks
depend on, and they will be installed using:
```
pip install -r requirements.txt
```
Go to `Virtual_joystick_with_computer_vision` directory and in Cmd or PowerShell run this code:
```
C:\Virtual-joystick-with-computer-vision> python Hand_Tracking.py
```

![xbox_360_controller](https://user-images.githubusercontent.com/15442079/177328365-389c0f20-fa66-4604-b7f4-067f831ae36e.png)

The right thumb is used as the 9 key, and it ranges from 0 to 255 by opening and closing, left tumb is used as the key 6.  
by rotating your hands, axis 1 (the key number 3 in pic) moves left and right and it is variable between -32767 and 32767 and
by the variable `threshold = 50`  in line 94 in `Hand_Tracking.py` it is limited to +-50 degrees to the maximum point (+-32767) and you can change it if you like.
