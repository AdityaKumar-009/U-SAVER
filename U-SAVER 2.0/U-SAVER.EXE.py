# ---------------------------------IMPORTANT LIBRARIES------------------------------------------------------ #
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from pytube import YouTube
from tkinter import filedialog, messagebox
import urllib.request
import re
import speech_recognition as sr

# ------------------------------------------UI--------------------------------------------------------------- #

window = ThemedTk(theme='yaru')
window.geometry('595x480')
window.resizable(False, False)
# window.config(bg="#FF1616")
window.title("U-SAVER")


def ui_widgets():
    label = Label(window, text="U-SAVER", font="Calibri 50", fg="red")
    label.place(x=200, y=30)

    label1 = Label(window, text="ENTER URL : ", font="Calibri 12")
    label1.place(x=40, y=162)
    entrybox1 = ttk.Entry(window, width=45, font="Calibri 13", textvariable=link_string)
    entrybox1.place(x=150, y=160)

    label2 = Label(window, text="OR", fg="teal")
    label2.place(x=340, y=203)

    label3 = Label(window, text="AI SEARCH : ", font="Calibri 12")
    label3.place(x=42, y=232)
    entrybox2 = ttk.Entry(window, width=45, font="Calibri 13", textvariable=ai_string)
    entrybox2.place(x=150, y=230)

    label4 = Label(window, text="SAVE TO : ", font="Calibri 12")
    label4.place(x=52, y=292)
    entrybox3 = ttk.Entry(window, width=34, font="Calibri 13", textvariable=download_Path)
    entrybox3.place(x=150, y=290)
    button1 = ttk.Button(window, text="Browse", width=10, command=browse)
    button1.place(x=478, y=290)

    button2 = ttk.Button(window, text="Download", style='Accent.TButton', command=download)
    button2.place(x=200, y=350)
    button3 = ttk.Button(window, text="AI Download", style='Accent.TButton', command=lambda: download_ai(link_string))
    button3.place(x=350, y=350)

    label5 = Label(window, text="Use your MAGICAL Voice to download any video :)", font="Calibri 12", fg="teal")
    label5.place(x=140, y=400)
    button4 = ttk.Button(window, text='MIC', command=lambda: mic_rec(label5, ai_string, link_string))
    # we use lambda because it is
    # calling the function anonymously
    button4.place(x=485, y=398)
# ------------------------- Buttons Functions --------------------------------------------------------------- #


def mic_rec(m, n, o):
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
        m.config(text="Unable to understand Please try again !!")
        pass

    mictext = r.recognize_google(audio)
    n.set(mictext)
    m.config(text="Mic text:  " + mictext)
    ai_srch = mictext
    ai_srch = ai_srch.replace(" ", "+")

    search_keyword = ai_srch
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print("https://www.youtube.com/watch?v=" + video_ids[0])
    Youtube_link = "https://www.youtube.com/watch?v=" + video_ids[0]
    o.set(Youtube_link)
    # lnktxt = Youtube_link
    # print(Youtube_link)

    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()
    if download_Folder == "":
        messagebox.showinfo("ERROR", "Select the save location first!!")
    else:
        # Creating object of YouTube()
        getVideo = YouTube(Youtube_link)

        # Getting all the available streams of the
        # youtube video and selecting the highest
        # from the
        videoStream = getVideo.streams.get_highest_resolution()

        # Downloading the video to destination
        # directory
        videoStream.download(download_Folder)

        # Displaying the message
        messagebox.showinfo("SUCCESS",
                            "DOWNLOADED AND SAVED IN\n"
                            + download_Folder)


def browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")

    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)


def download_ai(x):
    ai_srch = ai_string.get()
    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()
    if download_Folder == "":
        messagebox.showinfo("ERROR", "Select the save location first!!")
    elif ai_srch == "":
        messagebox.showinfo("ERROR", "Specify the KEYWORD first!!")
    else:
        ai_srch = ai_srch.replace(" ", "+")
        search_keyword = ai_srch
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        print("https://www.youtube.com/watch?v=" + video_ids[0])
        Youtube_link = "https://www.youtube.com/watch?v=" + video_ids[0]
        x.set(Youtube_link)

        # Creating object of YouTube()
        getVideo = YouTube(Youtube_link)

        # Getting all the available streams of the
        # youtube video and selecting the first
        # from the
        videoStream = getVideo.streams.get_highest_resolution()

        # Downloading the video to destination
        # directory
        videoStream.download(download_Folder)

        # Displaying the message
        messagebox.showinfo("SUCCESS",
                            "DOWNLOADED AND SAVED IN\n"
                            + download_Folder)


# Defining Download() to download the video
def download():
    # getting user-input Youtube Link

    Youtube_link = link_string.get()

    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()
    if download_Folder == "":
        messagebox.showinfo("ERROR", "Select the save location first!!")
    elif Youtube_link=="":
        messagebox.showinfo("ERROR", "Specify the video URL first!!")
    else:
        # Creating object of YouTube()
        getVideo = YouTube(Youtube_link)

        # Getting all the available streams of the
        # youtube video and selecting the first
        # from the
        videoStream = getVideo.streams.get_highest_resolution()

        # Downloading the video to destination
        # directory
        videoStream.download(download_Folder)

        # Displaying the message
        messagebox.showinfo("SUCCESS",
                            "DOWNLOADED AND SAVED IN\n"
                            + download_Folder)


# ALL STRINGS ---------------------------------------
link_string = StringVar()
ai_string = StringVar()
download_Path = StringVar()

# Calling UI function -------------------------------
ui_widgets()

# Creating loop to show the UI continuously ---------
window.mainloop()
