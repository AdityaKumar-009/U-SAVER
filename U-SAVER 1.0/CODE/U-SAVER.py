# ---------------------------------IMPORTANT LIBRARIES------------------------------------------------------ #
from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter import filedialog, messagebox
import urllib.request
import re
import speech_recognition as sr
# ------------------------------------------UI--------------------------------------------------------------- #

# CREATING OBJECT OF TKINTER(WHICH HAS A THEME THE DEFAULT ONE IS UGLY THOUGH)

window = Tk()
window.geometry('595x480')
window.resizable(False, False)
window.title("U-SAVER")

# ------------------ ICON ------------------>
window.iconbitmap("logo_icon.ico")

# ------------- CUSTOM THEMES -------------->
window.call("source", "sun-valley.tcl")

# Set the initial theme
window.call("set_theme", "dark")

# -----------------------------IMAGES---------------------------#

img = Canvas(width=600, height=150, highlightthickness=0)
img.place(x=-2, y=-1)
dark_logo = PhotoImage(file="logo_Dark.png")
img.create_image(1, 1, anchor=NW, image=dark_logo)

img2 = Canvas(width=600, height=150, highlightthickness=0)
light_logo = PhotoImage(file="logo_Light.png")
img2.create_image(1, 1, anchor=NW, image=light_logo)
# canvas2.place(x=-2, y=-1) # I HAVEN'T PLACE THIS IMAGE2 SO IT SHOWS IMAGE 1
mic_logo = PhotoImage(file="mic_logo.png")


def change_theme():
    # NOTE: The theme's real name is sun-valley-<mode>
    if window.call("ttk::style", "theme", "use") == "sun-valley-dark":
        # Set light theme
        window.call("set_theme", "light")
        # Changing switch text and placing image 2
        switch.config(text="Light")
        img2.place(x=-2, y=-1)

    else:
        # Set dark theme
        window.call("set_theme", "dark")
        # Changing switch text and placing image 2 to out of a window to show that it is removed
        switch.config(text="Dark")
        img2.place(x=-2, y=700)


def ui_widgets():
    # label0 = Label(text="U-SAVER",font="TimesRoman 30",fg="red",padx=15,pady=15)
    # label0.place(x=200, y=30) INSTEAD I USE A LOGO

    label1 = Label(text="ENTER URL : ", font="Calibri 12")
    label1.place(x=40, y=168)
    entry_box1 = ttk.Entry(width=45, font="Calibri 13", textvariable=link_string)
    entry_box1.place(x=150, y=160)
    # entry_box1.state(['invalid'])
    label2 = Label(text="OR", fg="teal")
    label2.place(x=340, y=203)

    label3 = Label(text="AI SEARCH : ", font="Calibri 12")
    label3.place(x=42, y=235)
    entry_box2 = ttk.Entry(width=45, font="Calibri 13", textvariable=ai_string)
    entry_box2.place(x=150, y=230)
    # entry_box2.state(['invalid'])

    label4 = Label(text="SAVE TO : ", font="Calibri 12")
    label4.place(x=52, y=296)
    entry_box3 = ttk.Entry(width=34, font="Calibri 13", textvariable=download_path)
    entry_box3.place(x=150, y=290)
    entry_box3.state(['invalid'])
    button1 = ttk.Button(text="Browse", width=10, command=browse)
    button1.place(x=478, y=293)

    button2 = ttk.Button(text="Download", style='Accent.TButton', command=download)
    button2.place(x=200, y=350)
    button3 = ttk.Button(text="AI Download", style='Accent.TButton', command=lambda: download_ai(link_string))
    button3.place(x=350, y=350)

    label5 = Label(text="Use your voice to download any video!", font="Calibri 12", fg="teal")
    label5.place(x=140, y=403)
    button4 = ttk.Button(image=mic_logo, command=lambda: mic_rec(label5, ai_string, link_string))
    # we use lambda because it is
    # calling the function anonymously
    button4.place(x=485, y=395)


switch = ttk.Checkbutton(text="Dark", style='Switch.TCheckbutton', command=change_theme)
switch.place(x=510, y=450)
# ------------------------- Buttons Functions --------------------------------------------------------------- #


def mic_rec(l5, e2, e1):
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say Something")
        audio = r.listen(source, timeout=10)
        print("Time's up, Thanks !!")
    try:
        print("Text: " + r.recognize_google(audio))
    except:
        print("unable to understand !!")
        l5.config(text="Unable to understand Please try again !!")
        pass

    mictext = r.recognize_google(audio)
    e2.set(mictext)
    l5.config(text="Mic text:  " + mictext)
    ai_srch = mictext
    ai_srch = ai_srch.replace(" ", "+")

    search_keyword = ai_srch
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print("VIDEO LINK: https://www.youtube.com/watch?v=" + video_ids[0])
    youtube_link = "https://www.youtube.com/watch?v=" + video_ids[0]
    e1.set(youtube_link)

    # select the optimal location for
    # saving file's
    download_folder = download_path.get()
    if download_folder == "":
        messagebox.showwarning("WARNING", "Select the save location first!!")
    else:
        # Creating object of YouTube()
        get_video = YouTube(youtube_link)

        # Getting all the available streams of the
        # YouTube video and selecting the highest one
        videostream = get_video.streams.get_highest_resolution()

        # Downloading the video to destination
        # directory
        videostream.download(download_folder)

        # Displaying the message
        messagebox.showinfo("SUCCESS",
                            "DOWNLOADED AND SAVED IN\n"
                            + download_folder)


def browse():
    # Presenting user with a pop-up for
    # directory selection. Initial directory
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_directory = filedialog.askdirectory(title="Save Video")

    # Displaying the directory in the directory
    # textbox
    download_path.set(download_directory)


def download_ai(url_link):
    ai_search = ai_string.get()
    # select the optimal location for
    # saving file's
    download_folder = download_path.get()
    if download_folder == "":
        messagebox.showwarning("ERROR", "Select the save location first!!")
    elif ai_search == "":
        messagebox.showwarning("ERROR", "Specify the KEYWORD first!!")
    else:
        ai_search = ai_search.replace(" ", "+")
        search_keyword = ai_search
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        print("https://www.youtube.com/watch?v=" + video_ids[0])
        youtube_link = "https://www.youtube.com/watch?v=" + video_ids[0]
        url_link.set(youtube_link)

        # Creating object of YouTube()
        get_video = YouTube(youtube_link)

        # Getting all the available streams of the
        # YouTube video and selecting the highest resolution one
        videostream = get_video.streams.get_highest_resolution()

    # Downloading the video to destination
    # directory
        videostream.download(download_folder)

    # Displaying the message
        messagebox.showinfo("SUCCESS", "DOWNLOADED AND SAVED IN\n" + download_folder)


# Defining Download() to download the video
def download():
    # getting user-input Youtube Link

    youtube_link = link_string.get()

    # select the optimal location for
    # saving file's
    download_folder = download_path.get()
    if download_folder == "":
        messagebox.showwarning("WARNING", "Select the save location first!!")
    elif youtube_link == "":
        messagebox.showwarning("WARNING", "Specify the video URL first!!")
    else:
        # Creating object of YouTube()
        get_video = YouTube(youtube_link)

        # Getting all the available streams of the
        # YouTube video and selecting the highest one
        videostream = get_video.streams.get_highest_resolution()

        # Downloading the video to destination
        # directory
        videostream.download(download_folder)

        # Displaying the message
        messagebox.showinfo("SUCCESS", "DOWNLOADED AND SAVED IN\n" + download_folder)


# ALL STRINGS ---------------------------------------
link_string = StringVar()
ai_string = StringVar()
download_path = StringVar()

# Calling UI function -------------------------------
ui_widgets()

# Creating loop to show the UI continuously ---------
window.mainloop()

# CREATED BY ADITYA ----- DISRUPTIVE TECHNOLOGY PROJECT (SEMESTER-1) -----
# DATE OF STARTING THIS IDEA OF THE PROJECT -- 12 NOVEMBER 2021 --
