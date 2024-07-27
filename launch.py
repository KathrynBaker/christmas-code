import subprocess
from PIL import Image, ImageTk
import PIL
import keyboard
import tkinter
import time

print("Using PIL Image ID %s" % Image.ID)
print("Using ImageTk ffi %s" % ImageTk.BitmapImage)
print("Using PIL %s" % PIL.version)
print("Using keyboard modifiers %s" % keyboard.all_modifiers)
print("Using tkinter S %s" % tkinter.S)
print("Using time timezone %s" % time.timezone)

subprocess.call(["python","christmas_code.py"])
