
#  ================================================  VER 2.0  ==============================================  #

# ---------------------------------IMPORTANT LIBRARIES------------------------------------------------------ #
from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter import filedialog, messagebox
import urllib.request
import re
import speech_recognition as sr
import os
import threading
from PIL import Image, ImageTk
from io import BytesIO

# import pafy
Directory = "U-SAVER"
Dir_Name = "C:/"
path = os.path.join(Dir_Name, Directory)
try:
    os.mkdir(path)
except OSError as error:
    pass

# ------------------------------------------UI--------------------------------------------------------------- #
# CREATING OBJECT OF THEMED TKINTER(WHICH HAS A THEME THE DEFAULT ONE WAS UGLY YIKES)

window = Tk()
window.geometry('595x510')
window.resizable(False, False)
window.title("U-SAVER")
window.iconbitmap("logo_icon.ico")

# CUSTOM THEME
window.call("source", "sv.tcl")
# Set the initial theme
window.call("set_svtheme", "svdark")

img1 = PhotoImage(file="logo_Dark.png")
img2 = PhotoImage(file="logo_Light.png")
img3 = PhotoImage(file="az_dark.png")
img4 = PhotoImage(file="az_light.png")
img5 = PhotoImage(file="f_dark.png")
mic_logo = PhotoImage(file="mic_2.png")


def ui_widgets():
    global pbar, button2, button3, button4, label5, label6, res, canvas, canvas2, canvas3
    # IMAGES
    canvas = Canvas(window, width=600, height=150, highlightthickness=0)
    canvas.place(x=-2, y=-1)
    canvas.create_image(1, 1, anchor=NW, image=img1)

    canvas2 = Canvas(window, width=600, height=150, highlightthickness=0)
    canvas2.create_image(1, 1, anchor=NW, image=img2)
    # canvas2.place(x=-2, y=-1) # I HAVEN'T PLACE THIS IMAGE2 SO IT SHOWS IMAGE 1

    canvas3 = Canvas(width=220, height=130, bg="grey", highlightthickness=0)

    label1 = Label(window, text="ENTER URL : ", font="Calibri 12")
    label1.place(x=40, y=168)
    entry_box1 = ttk.Entry(window, width=45, font="Calibri 13", textvariable=link_string)
    entry_box1.place(x=150, y=160)

    label2 = Label(window, text="OR", fg="teal")
    label2.place(x=340, y=203)

    label3 = Label(window, text="AI SEARCH : ", font="Calibri 12")
    label3.place(x=42, y=235)
    entry_box2 = ttk.Entry(window, width=45, font="Calibri 13", textvariable=keyword_string)
    entry_box2.place(x=150, y=230)
    entry_box2.config(width=40)
    entry_box2.focus_set()

    label4 = Label(window, text="SAVE TO : ", font="Calibri 12")
    label4.place(x=52, y=296)
    entry_box3 = ttk.Entry(window, width=34, font="Calibri 13", textvariable=download_Path)
    entry_box3.place(x=150, y=290)
    entry_box3.state(['invalid'])  # This custom theme supports invalid states

    button1 = ttk.Button(window, text="Browse", width=10, command=browse)
    button1.place(x=478, y=293)

    button2 = ttk.Button(window, text="Download", style='Accent.TButton',
                         command=lambda: threading.Thread(target=download).start())
    # Used lambda here since calling a Thread function

    button2.place(x=200, y=350)
    button3 = ttk.Button(window, text="AI Download", style='Accent.TButton',
                         command=lambda: threading.Thread(target=lambda: download_ai(link_string)).start())
    # Since it has arguments in parenthesis() so I called it anonymously using lambda in the "target="
    button3.place(x=350, y=350)

    label5 = Label(window, text="Tip: Use your voice to download any video.", font="Calibri 12", fg="teal")
    label5.place(x=160, y=403)

    button4 = ttk.Button(window, image=mic_logo,
                         command=lambda: threading.Thread(target=lambda: mic_rec(keyword_string, link_string)).start())
    button4.place(x=532, y=230)

    pbar = ttk.Progressbar(orient="horizontal", length=400)

    label6 = Label(text="", font="TimesRoman 10", fg="teal")
    label6.place(x=455, y=442)

    theme = StringVar()
    theme.set("Sun-valley dark")
    label7 = Label(text="Theme: ", font="Calibri 12")
    label7.place(x=2, y=478)
    theme_menu = ttk.OptionMenu(window, theme, "", "Sun-valley dark", "Sun-valley light", "Azure dark", "Azure light",
                                "Forest dark", "Forest light", command=themer)
    theme_menu.place(x=55, y=475)

    label8 = Label(text="Resolution : ", font="Calibri 12")
    label8.place(x=445, y=478)
    res = StringVar()
    drop_menu = ttk.OptionMenu(window, res, "SELECT RESOLUTION", "144p", "360p", "720p", " mp3")
    drop_menu.place(x=528, y=475)
    res.set("720p")


def themer(theme):
    if theme == "Sun-valley dark":
        canvas.create_image(1, 1, anchor=NW, image=img1)
        try:
            window.call("source", "theme/svdark.tcl")
            window.call("set_svtheme", "svdark")
        except:
            window.call("set_svtheme", "svdark")
        canvas2.place(x=-2, y=700)
    if theme == "Sun-valley light":
        canvas2.create_image(1, 1, anchor=NW, image=img2)
        if window.call("ttk::style", "theme", "use") == "sv-dark" or "f-dark" or "azure dark":
            try:
                window.call("source", "theme/svlight.tcl")
                window.call("set_svtheme", "svlight")
            except:
                window.call("set_svtheme", "svlight")
        canvas2.place(x=-2, y=-1)

    if theme == "Azure dark":
        canvas.create_image(1, 1, anchor=NW, image=img3)
        try:
            window.call("source", "Azure-ttk-theme-main/azure.tcl")
            window.call("set_theme", "dark")
        except:
            window.call("set_theme", "dark")
        canvas2.place(x=-2, y=700)
    if theme == "Azure light":
        canvas2.create_image(1, 1, anchor=NW, image=img4)
        try:
            window.call("source", "Azure-ttk-theme-main/azure.tcl")
            window.call("set_theme", "light")
        except:
            window.call("set_theme", "light")
        canvas2.place(x=-2, y=-1)

    if theme == "Forest dark":
        canvas.create_image(1, 1, anchor=NW, image=img5)
        try:
            window.call("source", "Forest/forest.tcl")
            window.call("set_ftheme", "fdark")
        except:
            window.call("set_ftheme", "fdark")
        canvas2.place(x=-2, y=700)

    if theme == "Forest light":
        canvas2.create_image(1, 1, anchor=NW, image=img4)
        try:
            window.call("source", "Forest/forest.tcl")
            window.call("set_ftheme", "flight")
        except:
            window.call("set_ftheme", "flight")
        canvas2.place(x=-2, y=-1)


# ------------------------- Buttons Functions --------------------------------------------------------------- #


def mic_rec(keyword, url_link):
    button4["state"] = "disabled"
    pbar.place(x=50, y=450)
    pbar.config(mode="indeterminate")
    pbar.start(10)
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say Something")
        label5.config(text="Listening....")
        audio = r.listen(source, timeout=10)
        print("Time's up, Thanks !!")
        label5.config(text="Time's up, Thanks!!")

    try:
        print("Text: " + r.recognize_google(audio))
        label5.config(text="Converting Speech to Text from the server....")
    except:
        print("unable to understand !!")
        label5.config(text="Unable to understand Please try again !!")
        button4["state"] = "normal"
        pbar.stop()
        pbar.place(x=1110, y=1460)
    pass

    mic_text = r.recognize_google(audio)
    keyword.set(mic_text)
    label5.config(text="Getting link....")
    ai_search = mic_text
    ai_search = ai_search.replace(" ", "+")
    search_keyword = ai_search
    try:
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        print("https://www.youtube.com/watch?v=" + video_ids[0])
        youtube_link = "https://www.youtube.com/watch?v=" + video_ids[0]  # link of the first video using the keyword
        url_link.set(youtube_link)
        download_folder = download_Path.get()
        if download_folder == "":
            messagebox.showinfo("ERROR", "Select the save location first!!")
            button4["state"] = "normal"
        else:
            get_video = YouTube(youtube_link)
            # u = urllib.request.urlopen(get_video.thumbnail_url).read()
            # global image1
            # im = Image.open(BytesIO(u))
            # resize = im.resize((220, 130), Image.ANTIALIAS)
            # image1 = ImageTk.PhotoImage(resize)
            # canvas3.create_image(0, 0, image=image1, anchor=NW)
            # canvas3.place(x=190, y=10)
            threading.Thread(target=lambda: dnwld(get_video, download_folder)).start()

    except:
        messagebox.showerror("Error", "Error Raised Due To! \n>Your Internet Connectivity")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    inc = int(percentage_of_completion)
    bd = bytes_downloaded / (1024 * 1024)
    s = total_size / (1024 * 1024)
    pbar["value"] = inc
    label5.config(text="Downloading - " + f"{inc}%")
    label6.config(text=f"{round(bd, 2)} MB / {round(s, 2)} MB")


def dnwld(video, download_location):
    print("Initializing Info...")
    title = video.title
    author = video.author
    views = video.views
    Length = video.length
    global length
    if 60 < Length < 3600:
        minute = Length // 60
        second = Length % 60
        length = f"Length: {minute} minutes {second} seconds"

    elif Length >= 3600:
        hour = (Length // 60) // 60
        minute = (Length // 60) % 60
        second = Length % 60
        length = f"Length: {hour} hour {minute} minutes {second} seconds"

    elif Length < 60:
        length = f"Length: {Length} seconds"

    if res.get() != " mp3":
        label5.config(text="Processing the video.....")
        file = video.streams.filter(res=res.get()).first()
        size = file.filesize
        fs = size / (1024 * 1024)
        label6["text"] = f"0 MB / {round(fs, 2)} MB"
        pbar.stop()
        pbar.config(mode="determinate", value=0)
        pbar.place(x=50, y=450)
        a = messagebox.askyesno("Do You Want To Download?",
                                "||-------------------  VIDEO INFORMATION  ------------------||\n"
                                + f"\n> TITLE: {title}"
                                + f"\n> AUTHOR: {author}"
                                + "\n> VIEWS: {:,}\n> ".format(views) + length
                                + f"\n> File Size: {round(fs, 2)} MB")

        if a:
            video.register_on_progress_callback(on_progress)
            try:
                print("Initializing Download...")
                file.download(download_location)
                label5.config(text="Video downloaded!!")
                messagebox.showinfo("SUCCESS", "DOWNLOADED AND SAVED IN\n" + download_location)
            except:
                messagebox.showerror("Error", "Error Raised Due To!\n"
                                              ">Your Internet Connectivity \n>Or selected resolution not Available")
                label5.config(text="Error!!")

            if not a:
                label5.config(text="Downloading cancelled!!")

    else:
        label5.config(text="Processing the audio file.....")
        mp3 = video.streams.filter(only_audio=True).first()
        size = mp3.filesize
        fs = size / (1024 * 1024)
        get = messagebox.askyesno("Do You Want To Download", f"File Size: {round(fs, 2)} MB")
        if get:
            try:
                print("Initializing Download...")
                video.register_on_progress_callback(on_progress)
                audio = mp3.download(download_location)
                base, ext = os.path.splitext(audio)
                converted = base + '.mp3'
                os.rename(audio, converted)
                label5.config(text="Audio downloaded!!")
            except:
                messagebox.showerror("Error ", "Error Raised Due To!\n>Your Internet Connectivity")

        if not get:
            label5.config(text="Downloading cancelled!!")

    button2["state"] = "normal"
    button3["state"] = "normal"
    button4["state"] = "normal"
    label6["text"] = ""
    pbar.stop()
    pbar.place(x=1110, y=1460)
    canvas3.place(x=1190, y=1110)


def browse():
    download_directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")

    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_directory)


def download_ai(x):
    ai_search = keyword_string.get()

    download_folder = download_Path.get()
    if download_folder == "":
        messagebox.showinfo("ERROR", "Select the save location first!!")
    elif ai_search == "":
        messagebox.showinfo("ERROR", "Specify the KEYWORD first!!")
    else:
        button3["state"] = "disabled"
        pbar.place(x=50, y=450)
        pbar.config(mode="indeterminate")
        pbar.start(10)
        label5.config(text="Getting link....")

        ai_search = ai_search.replace(" ", "+")
        try:
            search_keyword = ai_search
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            print("https://www.youtube.com/watch?v=" + video_ids[0])
            youtube_link = "https://www.youtube.com/watch?v=" + video_ids[0]
            x.set(youtube_link)
            # Creating object of YouTube()
            print("Getting YouTube Video...")
            get_video = YouTube(youtube_link)
            u = urllib.request.urlopen(get_video.thumbnail_url).read()
            global image1
            im = Image.open(BytesIO(u))
            resize = im.resize((220, 130))
            image1 = ImageTk.PhotoImage(resize)
            canvas3.create_image(0, 0, image=image1, anchor=NW)
            canvas3.place(x=190, y=10)
            threading.Thread(target=lambda: dnwld(get_video, download_folder)).start()
        except E as e:
            print(e)
            messagebox.showerror("Error", "Error Raised Due To!\n>Your Internet Connectivity")


def download():
    # getting user-input Youtube Link

    youtube_link = link_string.get()

    download_folder = download_Path.get()
    if download_folder == "":
        messagebox.showwarning("ERROR", "Select the save location first!!")
    elif youtube_link == "":
        messagebox.showwarning("ERROR", "Specify the video URL first!!")
    else:
        button2["state"] = "disabled"
        pbar.place(x=50, y=450)
        pbar.config(mode="indeterminate")
        pbar.start(10)
        try:
            # Creating object of YouTube()
            get_video = YouTube(youtube_link)
            u = urllib.request.urlopen(get_video.thumbnail_url).read()
            global image1
            im = Image.open(BytesIO(u))
            resize = im.resize((220, 130))
            image1 = ImageTk.PhotoImage(resize)
            canvas3.create_image(0, 0, image=image1, anchor=NW)
            canvas3.place(x=190, y=10)
            threading.Thread(target=lambda: dnwld(get_video, download_folder)).start()
        except:
            messagebox.showerror("Error", "Error Raised Due To!\n>URL is wrong  \n>Your Internet Connectivity ")
        button2["state"] = "normal"
        pbar.stop()
        pbar.place(x=1110, y=1460)


# ALL STRINGS ---------------------------------------
link_string = StringVar()
keyword_string = StringVar()
download_Path = StringVar()
download_Path.set("C:/U-SAVER")

# Calling UI function -------------------------------
ui_widgets()

# Creating loop to show the UI continuously ---------
window.mainloop()
