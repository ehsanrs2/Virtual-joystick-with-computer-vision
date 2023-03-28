# Virtual joystick with computer vision (OpenCV)
## Overview
This open-source project uses computer vision to simulate a joystick by tracking hand and finger movements, allowing users to play racing games.


![ezgif-4-4e00d29e37](https://user-images.githubusercontent.com/15442079/177322315-df07a035-e9ab-4db5-a7fc-ff8299622c0d.gif)  

## Getting Started  
1. Clone the project:
```bash
git clone https://github.com/ehsanrs2/Virtual-joystick-with-computer-vision.git
```
2. Install the required Python libraries:
```bash
pip install -r requirements.txt
```
3. Navigate to the `Virtual_joystick_with_computer_vision` directory and run the following command:
```bash
python Hand_Tracking.py
```
![xbox_360_controller](https://user-images.githubusercontent.com/15442079/177328365-389c0f20-fa66-4604-b7f4-067f831ae36e.png)

## Controls

- Right thumb: Acts as the 9 key, with a range of 0 to 255 (by opening and closing).
- Left thumb: Acts as the 6 key.
- Rotating hands: Moves axis 1 (key number 3 in the image) left and right, with a range of -32767 to 32767.

The variable `threshold = 50` in line 94 of `Hand_Tracking.py` limits the rotation to ±50 degrees for the maximum point (±32767). You can adjust this value if desired.
