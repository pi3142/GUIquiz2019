# Anti-Food Waste Quiz 2019
This is the repo of the anti-food waste quiz writted in Python 3 that can be run on a Raspberry Pi (Raspberry Pi 1B+ and 3B+ tested).

This code is a project to teach pupils not to waste food.

### Setup
1. Install the ThorPy and pygame libraries with:

<code> pip3 install thorpy </code>

<code> pip3 install pygame </code>

2. Run the GUI.py code with:

<code> python3 GUI.py </code>

#### Make sure that the terminal has access to a X session. If you are on a remote terminal connection (eg ssh), run:

<code> export DISPLAY=:0 </code>

##### (The Raspberry Pi that you are remotely connected to must have a X session running at address 0, if not change the address accordingly)

### How to test your code on a Linux / Mac environment

If you are not going to run the code on a Raspberry Pi, change the varable on the first few lines <code> COMPUTER = False </code> to <code> COMPUTER = True </code>
