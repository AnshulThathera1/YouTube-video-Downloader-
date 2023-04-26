# importing the necessary modules
from tkinter import *  # importing all widgets and modules from tkinter
from tkinter import messagebox as mb  # importing the messagebox module from tkinter
from tkinter import filedialog as fd  # importing the filedialog module from tkinter
from pytube import YouTube  # importing the YouTube class from pytube
from PIL import Image, ImageTk  # importing Image and ImageTk module from PIL


# ------------------------- defining functions -------------------------

# function to browse the folder
def browse_folder():
    # using the askdirectory() method of the filedialog module to select the directory
    download_path = fd.askdirectory(initialdir="D:\Downloads", title="Select the folder to save the video")
    # using the set() method to set the directory path in the entry field
    download_dir.set(download_path)


# function to download the video to the designated path
def download_video():
    # using the get() method to retrieve the string from the entry fields
    youtube_url = video_url.get()
    download_folder = download_dir.get()

    # checking if the entry fields are not entry
    if (youtube_url != "" and download_folder != ""):
        # creating an object of the YouTube class for the request URL
        video = YouTube(youtube_url)

        # selecting the stream with file extension = 'mp4', progressive = 'True',
        # and itag = '22' in order to download the video of 720p resolution
        video_stream = video.streams.filter(file_extension="mp4", progressive=True, res="720p",
                                            type="video").get_by_itag(22)

        # selecting the download folder
        video_stream.download(download_folder)

        # displaying a message indicating the successful download
        mb.showinfo("Download Complete", "Selected Video is downloaded\nand saved successfully in " + download_folder)

        # else statement
    else:
        # displaying an error message indicating empty fields
        mb.showerror("Empty Fields", "Fields are empty!")

    # function to reset the entries


def reset():
    # using the set() method to set the values
    # of the entry fields to empty string
    video_url.set("")
    download_dir.set("")

    # using the focus_set() method to set the
    # cursor focus to first entry field
    url_field.focus_set()


# function to close the application
def exit():
    # using the destroy() method to close the application
    gui_root.destroy()


# ------------------------- main function -------------------------

if __name__ == "__main__":
    # creating an object of the Tk() class
    gui_root = Tk()

    # setting the title of the window
    gui_root.title("YouTube Downloader - JAVATPOINT")

    # setting the size and position of the window
    gui_root.geometry("580x220+700+250")

    # disabling the resizable option for better UI
    gui_root.resizable(0, 0)

    # configuring the background color of the window
    gui_root.config(bg="#FEE4E3")

    # configuring the icon of the window


    # adding frames to the window using the Frame() widget
    header_frame = Frame(gui_root, bg="#FEE4E3")
    entry_frame = Frame(gui_root, bg="#FEE4E3")
    button_frame = Frame(gui_root, bg="#FEE4E3")

    # using the pack() method to set the positions of the frames
    header_frame.pack()
    entry_frame.pack()
    button_frame.pack()

    # ------------------------- the header_frame frame -------------------------

    # importing the Tkinter-compatible bitmap image
    the_image = ImageTk.PhotoImage(Image.open("youtubelogo.png").resize((50, 35), Image.ANTIALIAS))

    # adding the labels to the header_frame frame using the Label() widget
    image_label = Label(
        header_frame,
        image=the_image,
        bg="#FEE4E3",
        fg="#FE0700",
        anchor=SE
    )
    header_label = Label(
        header_frame,
        text="YouTube Video Downloader",
        font=("verdana", "14", "bold"),
        bg="#FEE4E3",
        anchor=SE
    )

    # using the grid() method to set the position of the labels in the grid format
    image_label.grid(row=0, column=0, padx=10, pady=10)
    header_label.grid(row=0, column=1, padx=10, pady=10)

    # ------------------------- the entry_frame frame -------------------------

    # adding the labels to the entry_frame frame using the Label() widget
    url_label = Label(
        entry_frame,
        text="Video URL:",
        font=("verdana", "10"),
        bg="#FEE4E3",
        fg="#000000",
        anchor=SE
    )
    des_label = Label(
        entry_frame,
        text="Destination:",
        font=("verdana", "10"),
        bg="#FEE4E3",
        fg="#000000",
        anchor=SE
    )

    # using the grid() method to set the position of the labels in the grid format
    url_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)
    des_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    # creating the objects of the StringVar() class
    video_url = StringVar()
    download_dir = StringVar()

    # adding the entry fields to the entry_frame frame using the Entry() widget
    url_field = Entry(
        entry_frame,
        textvariable=video_url,
        width=35,
        font=("verdana", "10"),
        bg="#FFFFFF",
        fg="#000000",
        relief=GROOVE
    )
    des_field = Entry(
        entry_frame,
        textvariable=download_dir,
        width=26,
        font=("verdana", "10"),
        bg="#FFFFFF",
        fg="#000000",
        relief=GROOVE
    )

    # using the grid() method to set the position of the entry fields in the grid format
    url_field.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
    des_field.grid(row=1, column=1, padx=5, pady=5)

    # adding a button to the entry_frame frame using the Button() widget
    browse_button = Button(
        entry_frame,
        text="Browse",
        width=7,
        font=("verdana", "10"),
        bg="#FF9200",
        fg="#FFFFFF",
        activebackground="#FFE0B7",
        activeforeground="#000000",
        relief=GROOVE,
        command=browse_folder
    )

    # using the grid() method to set the position of the button in the grid format
    browse_button.grid(row=1, column=2, padx=5, pady=5)

    # ------------------------- the button_frame frame -------------------------

    # adding the buttons to the button_frame frame using the Button() widget
    download_button = Button(
        button_frame,
        text="Download",
        width=12,
        font=("verdana", "10"),
        bg="#15EF5F",
        fg="#FFFFFF",
        activebackground="#97F9B8",
        activeforeground="#000000",
        relief=GROOVE,
        command=download_video
    )
    reset_button = Button(
        button_frame,
        text="Clear",
        width=12,
        font=("verdana", "10"),
        bg="#23B1E6",
        fg="#FFFFFF",
        activebackground="#C3E6EF",
        activeforeground="#000000",
        relief=GROOVE,
        command=reset
    )
    close_button = Button(
        button_frame,
        text="Exit",
        width=12,
        font=("verdana", "10"),
        bg="#F64247",
        fg="#FFFFFF",
        activebackground="#F7A2A5",
        activeforeground="#000000",
        relief=GROOVE,
        command=exit
    )

    # using the grid() method to set the position of the buttons in the grid format
    download_button.grid(row=0, column=0, padx=5, pady=10)
    reset_button.grid(row=0, column=1, padx=5, pady=10)
    close_button.grid(row=0, column=2, padx=5, pady=10)

    # using the mainloop() method to run the application
    gui_root.mainloop()