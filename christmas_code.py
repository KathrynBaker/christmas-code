from PIL import Image, ImageTk
import PIL
import keyboard
import tkinter
import time
from pathlib import Path


def ex_cb():
    print("Suppressing something")


# The image to show
pilImage = PIL.Image.open("pic.png")

# Commands
please_exit = "GADAEL"
use_tries = "CYFRI"
stop_using_tries = "DIDDIWEDD"
reset_tries = "AILOSOD"
use_timeout = "AMSER"
stop_using_timeout = "BYTH"

#Variables
keep_looping = True
keyboard.add_hotkey('alt+tab', ex_cb, suppress=True)
keyboard.add_hotkey('win', ex_cb, suppress=True)
keyboard.add_hotkey('ctrl+alt+up', ex_cb, suppress=True)
root_row = 1
root_col = 0
font_name = "Courier"
font_size = 44
max_tries = 3
current_tries = 0
using_tries = False
warning_message = "Incorrect Code, try again"
no_tries_left = False
no_tries_left_message = "No tries left"
global next_action_test
next_action_test = 0
using_timeout = False
timeout = 6


def show_entry_fields_outer():
    next_action = 0
    under_test = e1.get()
    if under_test == please_exit:
        next_action = 1
    if under_test == show_image:
        if no_tries_left:
            next_action = 0
        else:
            next_action = 2
    if under_test == use_tries:
        next_action = 3
    if under_test == reset_tries:
        next_action = 4
    if under_test == stop_using_tries:
        next_action = 5
    if under_test == use_timeout:
        next_action = 6
    if under_test == stop_using_timeout:
        next_action = 7
    master.quit()
    global next_action_test
    next_action_test = next_action


display_message = False
create_screen = True

#Get password
show_image = "TEST" # This is the password!
show_image = Path('code.txt').read_text()

while keep_looping:

    if create_screen:
        create_screen = False
        master = tkinter.Tk()

        master.overrideredirect(True)
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))

        master.enter_code = tkinter.Frame(master)
        master.enter_code.place(relx=.5, rely=.5, anchor="c")

        extra_message_var = tkinter.StringVar()
        extra_label = tkinter.Label(master.enter_code, textvariable=extra_message_var, font=(font_name, font_size))

        extra_label.grid(row=root_row, column=root_col, columnspan=2)

        code_label = tkinter.Label(master.enter_code, text="Enter the code:  ", font=(font_name, font_size))

        code_label.grid(row=root_row+1, column = root_col)

        def caps(event):
            v.set(v.get().upper())

        v = tkinter.StringVar()
        e1 = tkinter.Entry(master.enter_code, font=(font_name, font_size), textvariable = v)
        e1.bind("<KeyRelease>", caps)

        e1.grid(row=root_row+1, column=root_col+1)
        e1.focus()

        try_code = tkinter.Button(master.enter_code, text='Try Code', command=show_entry_fields_outer,
                              font=(font_name, font_size))

        try_code.grid(row=root_row+2, column=root_col+1, sticky=tkinter.W, pady=4)

        #keyboard.add_hotkey('return', show_entry_fields_outer)

        master.mainloop()
    else:
        extra_message_var.set(extra_message)
        e1.focus()
        #keyboard.add_hotkey('return', show_entry_fields_outer)
        master.mainloop()

    if next_action_test == 1:
        master.destroy()
        keep_looping = False
        break
    elif next_action_test == 2:
        display_message = False
        #show_pil(pilImage)
        root = tkinter.Toplevel()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.overrideredirect(1)
        root.geometry("%dx%d+0+0" % (w, h))
        root.focus_set()
        root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
        canvas = tkinter.Canvas(root, width=w, height=h)
        canvas.pack()
        canvas.configure(background='black')
        img_width, img_height = pilImage.size
        if img_width > w or img_height > h:
            ratio = min(w / img_width, h / img_height)
            img_width = int(img_width * ratio)
            img_height = int(img_height * ratio)
            pilImage = pilImage.resize((img_width, img_height), PIL.Image.ANTIALIAS)
        image = PIL.ImageTk.PhotoImage(pilImage)
        imagesprite = canvas.create_image(w / 2, h / 2, image=image)
        root.mainloop()
        root.destroy()
        master.destroy()
        create_screen = True
        extra_message = ""
        no_tries_left = False
        current_tries = 0
    elif next_action_test == 3:
        using_tries = True
        extra_message = "Tries Set"
        current_tries = 0
        no_tries_left = False
    elif next_action_test == 4:
        extra_message = "Tries Reset"
        current_tries = 0
        no_tries_left = False
    elif next_action_test == 5:
        extra_message = "Never Ending"
        using_tries = False
        no_tries_left = False
    elif next_action_test == 6:
        extra_message = "Using Timeout"
        using_timeout = True
    elif next_action_test == 7:
        extra_message = "End of Timeout"
        using_timeout = False
    else:
        if using_timeout:
            def countdown(count):
                # change text in label
                timer_label['text'] = "Continue in %i" % count

                if count > 0:
                    # call countdown again after 1000ms (1s)
                    timer.after(1000, countdown, count - 1)
                if count <= 0:
                    timer.quit()

            deadline = time.time() + timeout
            timer_message = tkinter.StringVar()
            timer = tkinter.Toplevel()
            w, h = timer.winfo_screenwidth(), timer.winfo_screenheight()
            timer.overrideredirect(1)
            timer.geometry("%dx%d+0+0" % (w, h))
            timer.focus_set()

            timer_label = tkinter.Label(timer, font=(font_name, font_size))
            timer_label.pack()
            timer_label.place(relx=.5, rely=.5, anchor="c")
            timer_label.focus()

            countdown(timeout)

            timer.mainloop()
            timer.destroy()
            #timer_message.set("Timer Timer")
            #while time.time() < deadline:
                #time.sleep(1)
                #print("Running this bit!")
                #extra_message_var.set(int(deadline - time.time()))

        if current_tries >= max_tries:
            extra_message = no_tries_left_message
            no_tries_left = True
        else:
            if using_tries:
                extra_message = "You have " + str(max_tries - current_tries) + " tries"
            else:
               extra_message = warning_message
        if using_tries:
            current_tries = current_tries + 1
