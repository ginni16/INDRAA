from tkinter import *
import tkinter as tk
import requests
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from datetime import datetime
import pytz

She = Tk()
She.geometry("900x500+300+200")
She.title("She Weather App")
She.resizable(False, False)


search_image = PhotoImage(file="Copy of search.png ")
myimage = Label(image=search_image)
myimage.place(x=20, y=20)


textfield = tk.Entry(She, justify="center", width=17, font=(
    "poppins", 25, "bold"), bg='#404040', border=0, fg='white')
textfield.place(x=50, y=40)
textfield.focus()


def getWeather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        # print(result)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
            city+"&appid=06c921750b9a82d8f5d1294e1586276f"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid entry")


search_icon = PhotoImage(file="Copy of search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0,
                      cursor="hand2", bg='#404040', command=getWeather)

myimage_icon.place(x=400, y=34)

logo_image = PhotoImage(file="mylogo2.png")
logo = Label(image=logo_image)
logo.place(x=150, y=100)

frame_image = PhotoImage(file="Copy of box.png")
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

name = Label(She, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(She, font=("Helvetics", 20))
clock.place(x=30, y=130)

label1 = Label(She, text="Wind", font=(
    "Helvetics", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(She, text="Humidity", font=(
    "Helvetics", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(She, text="Description", font=(
    "Helvetics", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(She, text="Pressure", font=(
    "Helvetics", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 20, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

She.mainloop()
