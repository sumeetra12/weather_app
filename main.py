from tkinter import *
import tkinter as tk
from tkinter.messagebox import showerror

from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

window = Tk()
window.title("Weather app")
window.geometry("900x500+300+200")
window.resizable(False, False)


def getWeather(event):
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)


        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT TIME")

        # weather

        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=226b4914318c75c00ef8139d88c8844d"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition, "|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except EXCEPTION as e:
        showerror("Weather App", "Invalid Entry!!!", e)



# search box
search_image = PhotoImage(file='img/search.png')
myimage = Label(image=search_image)
myimage.place(x=200, y=20)

textfield = tk.Entry(window, justify="center", width=17, font=("poppins", 25, "bold"), fg="white", bg="#404040", border=0)
textfield.place(x=250, y=40)
textfield.focus()

textfield.bind("<Return>", getWeather)

search_icon = PhotoImage(file='img/search_icon.png')
myimage_icon = Button(image=search_icon, command=getWeather, cursor="hand2", bg="#404040", relief="flat", activeforeground="#404040", activebackground="#404040")
myimage_icon.place(x=570, y=31)


# logo
logo_image =PhotoImage(file='img/logo.png')
logo = Label(image=logo_image)
logo.place(x=300, y=100)


# Bottom box
frame_image = PhotoImage(file='img/box.png')
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(window, font=("arial", 15, "bold"))
name.place(x=120, y=110)
clock = Label(window, font=("Helvetica", 20))
clock.place(x=120, y=140)

# label
label1 = Label(window, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(window, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(window, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(window, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"))
t.place(x=600, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=600, y=250)

w = Label(text="---", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="---", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="---", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)
p = Label(text="---", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)


window.mainloop()
