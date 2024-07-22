from tkinter import *
import instaloader
from urllib.request import urlopen
from PIL import Image, ImageTk
import io

def get_profile_info():
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username.get())
    open_url = urlopen(profile.get_profile_pic_url())
    data = open_url.read()
    open_url.close()
    image = Image.open(io.BytesIO(data))
    pic = ImageTk.PhotoImage(image)
    label_image.config(image=pic)
    label_image.image = pic
    label_followers.config(text=f"Followers: {profile.followers}")
    label_following.config(text=f"Following: {profile.followees}")

program = Tk()

program.title('Instagram Profile Downloader')
program.geometry('500x500')
program.resizable(False, False)

Label(program, text='Instagram Profile Downloader', fg="red").pack()
username = Entry(program, width=30)
username.pack()

button = Button(program, text='Click For Download', command=get_profile_info)
button.pack()

label_image = Label(program)
label_image.pack()

label_followers = Label(program, text="Followers: ")
label_followers.pack()

label_following = Label(program, text="Following: ")
label_following.pack()

program.mainloop()

































































# window = Tk()
# window.maxsize(600,700)
# window.minsize(600,700)
# window.geometry('500x610')
# window.title("Instagram Profile Downloader")
#
# # label
# label = Label(window, text= 'Hello To You ',fg="blue")
# label.pack()
# # button
#
# def hello():
#     label.config(text=input.get())
#     button.config(text="Loading For You....")
#
#
#
# button = Button(window,text="Click Here to Download",fg="yellow",bg="green",command=hello)
# button.place(x=225,y=80)
#
# # Inputs
# input = Entry(window)
# input.pack()
#
#
#
# window.mainloop()



