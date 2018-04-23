#     Program: CCE Varsity Overbuff
#      Author: Walter Proulx
#        Date: January 14, 2017
#     Version: 1.0
# Description: A program that pulls each players stats and inputs them
#              into a GUI with interpreted stats not normally provided.
# ######################################################################

# importing essentials
from tkinter import *
from tkinter import messagebox
import os
import urllib.parse
import urllib.request
import getpass
import socket
import json

# CONSTANTS
GAMES_PLAYED = 1
HEALING = 0
DEATHS = 2
DAMAGE = 3
ELIMINATIONS = 9


# ######################################################################
# FUNCTION DEFINITIONS
# ######################################################################


#     Pre: player names
#    Post: retrieves information from Blizzard's server
# Purpose: retrieves all the players data from the Varsity Overwatch
#          team
# ######################################################################
def get_data():
    api_url="https://cce-varsity-overwatch-tracker.herokuapp.com/stats/pc/us/" + p1_data_name
    request = urllib.request.Request(api_url)
    response = urllib.request.urlopen(request)
    data = json.load(response)

    p1_games = data["stats"]["game"]["competitive"][GAMES_PLAYED]["value"].replace(",", "")
    p1_elims = data["stats"]["combat"]["competitive"][ELIMINATIONS]["value"].replace(",", "")
    p1_damage = data["stats"]["combat"]["competitive"][DAMAGE]["value"].replace(",", "")
    p1_healing = data["stats"]["assists"]["competitive"][HEALING]["value"].replace(",", "")
    p1_deaths = data["stats"]["combat"]["competitive"][DEATHS]["value"].replace(",", "")

    p1_elims_average = int(p1_elims) / int(p1_games)
    p1_damage_average = int(p1_damage) / int(p1_games)
    p1_healing_average = int(p1_healing) / int(p1_games)
    p1_deaths_average = int(p1_deaths) / int(p1_games)

    p1_elims_average = round(p1_elims_average, 2)
    p1_damage_average = round(p1_damage_average, 2)
    p1_healing_average = round(p1_healing_average, 2)
    p1_deaths_average = round(p1_deaths_average, 2)

    p1_data_elims.set(p1_elims_average)
    p1_data_damage.set(p1_damage_average)
    p1_data_healing.set(p1_healing_average)
    p1_data_deaths.set(p1_deaths_average)

    api_url = "https://cce-varsity-overwatch-tracker.herokuapp.com/stats/pc/us/" + p2_data_name
    request = urllib.request.Request(api_url)
    response = urllib.request.urlopen(request)
    data = json.load(response)

    p2_games = data["stats"]["game"]["competitive"][GAMES_PLAYED]["value"].replace(",", "")
    p2_elims = data["stats"]["combat"]["competitive"][ELIMINATIONS]["value"].replace(",", "")
    p2_damage = data["stats"]["combat"]["competitive"][DAMAGE]["value"].replace(",", "")
    p2_healing = data["stats"]["assists"]["competitive"][HEALING]["value"].replace(",", "")
    p2_deaths = data["stats"]["combat"]["competitive"][DEATHS]["value"].replace(",", "")

    p2_elims_average = int(p2_elims) / int(p2_games)
    p2_damage_average = int(p2_damage) / int(p2_games)
    p2_healing_average = int(p2_healing) / int(p2_games)
    p2_deaths_average = int(p2_deaths) / int(p2_games)

    p2_elims_average = round(p2_elims_average, 2)
    p2_damage_average = round(p2_damage_average, 2)
    p2_healing_average = round(p2_healing_average, 2)
    p2_deaths_average = round(p2_deaths_average, 2)

    p2_data_elims.set(p2_elims_average)
    p2_data_damage.set(p2_damage_average)
    p2_data_healing.set(p2_healing_average)
    p2_data_deaths.set(p2_deaths_average)

    api_url = "https://cce-varsity-overwatch-tracker.herokuapp.com/stats/pc/us/" + p3_data_name
    request = urllib.request.Request(api_url)
    response = urllib.request.urlopen(request)
    data = json.load(response)

    p3_games = data["stats"]["game"]["competitive"][GAMES_PLAYED]["value"].replace(",", "")
    p3_elims = data["stats"]["combat"]["competitive"][ELIMINATIONS]["value"].replace(",", "")
    p3_damage = data["stats"]["combat"]["competitive"][DAMAGE]["value"].replace(",", "")
    p3_healing = data["stats"]["assists"]["competitive"][HEALING]["value"].replace(",", "")
    p3_deaths = data["stats"]["combat"]["competitive"][DEATHS]["value"].replace(",", "")

    p3_elims_average = int(p3_elims) / int(p3_games)
    p3_damage_average = int(p3_damage) / int(p3_games)
    p3_healing_average = int(p3_healing) / int(p3_games)
    p3_deaths_average = int(p3_deaths) / int(p3_games)

    p3_elims_average = round(p3_elims_average, 2)
    p3_damage_average = round(p3_damage_average, 2)
    p3_healing_average = round(p3_healing_average, 2)
    p3_deaths_average = round(p3_deaths_average, 2)

    p3_data_elims.set(p3_elims_average)
    p3_data_damage.set(p3_damage_average)
    p3_data_healing.set(p3_healing_average)
    p3_data_deaths.set(p3_deaths_average)

    api_url = "https://cce-varsity-overwatch-tracker.herokuapp.com/stats/pc/us/" + p4_data_name
    request = urllib.request.Request(api_url)
    response = urllib.request.urlopen(request)
    data = json.load(response)

    p4_games = data["stats"]["game"]["competitive"][GAMES_PLAYED]["value"].replace(",", "")
    p4_elims = data["stats"]["combat"]["competitive"][ELIMINATIONS]["value"].replace(",", "")
    p4_damage = data["stats"]["combat"]["competitive"][DAMAGE]["value"].replace(",", "")
    p4_healing = data["stats"]["assists"]["competitive"][HEALING]["value"].replace(",", "")
    p4_deaths = data["stats"]["combat"]["competitive"][DEATHS]["value"].replace(",", "")

    p4_elims_average = int(p4_elims) / int(p4_games)
    p4_damage_average = int(p4_damage) / int(p4_games)
    p4_healing_average = int(p4_healing) / int(p4_games)
    p4_deaths_average = int(p4_deaths) / int(p4_games)

    p4_elims_average = round(p4_elims_average, 2)
    p4_damage_average = round(p4_damage_average, 2)
    p4_healing_average = round(p4_healing_average, 2)
    p4_deaths_average = round(p4_deaths_average, 2)

    p4_data_elims.set(p4_elims_average)
    p4_data_damage.set(p4_damage_average)
    p4_data_healing.set(p4_healing_average)
    p4_data_deaths.set(p4_deaths_average)

    api_url = "https://cce-varsity-overwatch-tracker.herokuapp.com/stats/pc/us/" + p5_data_name
    request = urllib.request.Request(api_url)
    response = urllib.request.urlopen(request)
    data = json.load(response)

    p5_games = data["stats"]["game"]["competitive"][GAMES_PLAYED]["value"].replace(",", "")
    p5_elims = data["stats"]["combat"]["competitive"][ELIMINATIONS]["value"].replace(",", "")
    p5_damage = data["stats"]["combat"]["competitive"][DAMAGE]["value"].replace(",", "")
    p5_healing = data["stats"]["assists"]["competitive"][HEALING]["value"].replace(",", "")
    p5_deaths = data["stats"]["combat"]["competitive"][DEATHS]["value"].replace(",", "")

    p5_elims_average = int(p5_elims) / int(p5_games)
    p5_damage_average = int(p5_damage) / int(p5_games)
    p5_healing_average = int(p5_healing) / int(p5_games)
    p5_deaths_average = int(p5_deaths) / int(p5_games)

    p5_elims_average = round(p5_elims_average, 2)
    p5_damage_average = round(p5_damage_average, 2)
    p5_healing_average = round(p5_healing_average, 2)
    p5_deaths_average = round(p5_deaths_average, 2)

    p5_data_elims.set(p5_elims_average)
    p5_data_damage.set(p5_damage_average)
    p5_data_healing.set(p5_healing_average)
    p5_data_deaths.set(p5_deaths_average)

    api_url = "https://cce-varsity-overwatch-tracker.herokuapp.com/stats/pc/us/" + p6_data_name
    request = urllib.request.Request(api_url)
    response = urllib.request.urlopen(request)
    data = json.load(response)

    p6_games = data["stats"]["game"]["competitive"][GAMES_PLAYED]["value"].replace(",", "")
    p6_elims = data["stats"]["combat"]["competitive"][ELIMINATIONS]["value"].replace(",", "")
    p6_damage = data["stats"]["combat"]["competitive"][DAMAGE]["value"].replace(",", "")
    p6_healing = data["stats"]["assists"]["competitive"][HEALING]["value"].replace(",", "")
    p6_deaths = data["stats"]["combat"]["competitive"][DEATHS]["value"].replace(",", "")

    p6_elims_average = int(p6_elims) / int(p6_games)
    p6_damage_average = int(p6_damage) / int(p6_games)
    p6_healing_average = int(p6_healing) / int(p6_games)
    p6_deaths_average = int(p6_deaths) / int(p6_games)

    p6_elims_average = round(p6_elims_average, 2)
    p6_damage_average = round(p6_damage_average, 2)
    p6_healing_average = round(p6_healing_average, 2)
    p6_deaths_average = round(p6_deaths_average, 2)

    p6_data_elims.set(p6_elims_average)
    p6_data_damage.set(p6_damage_average)
    p6_data_healing.set(p6_healing_average)
    p6_data_deaths.set(p6_deaths_average)

    api_url = "https://cce-varsity-overwatch-tracker.herokuapp.com/stats/pc/us/" + p7_data_name
    request = urllib.request.Request(api_url)
    response = urllib.request.urlopen(request)
    data = json.load(response)

    p7_games = data["stats"]["game"]["competitive"][GAMES_PLAYED]["value"].replace(",", "")
    p7_elims = data["stats"]["combat"]["competitive"][ELIMINATIONS]["value"].replace(",", "")
    p7_damage = data["stats"]["combat"]["competitive"][DAMAGE]["value"].replace(",", "")
    p7_healing = data["stats"]["assists"]["competitive"][HEALING]["value"].replace(",", "")
    p7_deaths = data["stats"]["combat"]["competitive"][DEATHS]["value"].replace(",", "")

    p7_elims_average = int(p7_elims) / int(p7_games)
    p7_damage_average = int(p7_damage) / int(p7_games)
    p7_healing_average = int(p7_healing) / int(p7_games)
    p7_deaths_average = int(p7_deaths) / int(p7_games)

    p7_elims_average = round(p7_elims_average, 2)
    p7_damage_average = round(p7_damage_average, 2)
    p7_healing_average = round(p7_healing_average, 2)
    p7_deaths_average = round(p7_deaths_average, 2)

    p7_data_elims.set(p7_elims_average)
    p7_data_damage.set(p7_damage_average)
    p7_data_healing.set(p7_healing_average)
    p7_data_deaths.set(p7_deaths_average)

    api_url = "https://cce-varsity-overwatch-tracker.herokuapp.com/stats/pc/us/" + p8_data_name
    request = urllib.request.Request(api_url)
    response = urllib.request.urlopen(request)
    data = json.load(response)

    p8_games = data["stats"]["game"]["competitive"][GAMES_PLAYED]["value"].replace(",", "")
    p8_elims = data["stats"]["combat"]["competitive"][ELIMINATIONS]["value"].replace(",", "")
    p8_damage = data["stats"]["combat"]["competitive"][DAMAGE]["value"].replace(",", "")
    p8_healing = data["stats"]["assists"]["competitive"][HEALING]["value"].replace(",", "")
    p8_deaths = data["stats"]["combat"]["competitive"][DEATHS]["value"].replace(",", "")

    p8_elims_average = int(p8_elims) / int(p8_games)
    p8_damage_average = int(p8_damage) / int(p8_games)
    p8_healing_average = int(p8_healing) / int(p8_games)
    p8_deaths_average = int(p8_deaths) / int(p8_games)

    p8_elims_average = round(p8_elims_average, 2)
    p8_damage_average = round(p8_damage_average, 2)
    p8_healing_average = round(p8_healing_average, 2)
    p8_deaths_average = round(p8_deaths_average, 2)

    p8_data_elims.set(p8_elims_average)
    p8_data_damage.set(p8_damage_average)
    p8_data_healing.set(p8_healing_average)
    p8_data_deaths.set(p8_deaths_average)

    api_url = "https://cce-varsity-overwatch-tracker.herokuapp.com/stats/pc/us/" + p9_data_name
    request = urllib.request.Request(api_url)
    response = urllib.request.urlopen(request)
    data = json.load(response)

    p9_games = data["stats"]["game"]["competitive"][GAMES_PLAYED]["value"].replace(",", "")
    p9_elims = data["stats"]["combat"]["competitive"][ELIMINATIONS]["value"].replace(",", "")
    p9_damage = data["stats"]["combat"]["competitive"][DAMAGE]["value"].replace(",", "")
    p9_healing = data["stats"]["assists"]["competitive"][HEALING]["value"].replace(",", "")
    p9_deaths = data["stats"]["combat"]["competitive"][DEATHS]["value"].replace(",", "")

    p9_elims_average = int(p9_elims) / int(p9_games)
    p9_damage_average = int(p9_damage) / int(p9_games)
    p9_healing_average = int(p9_healing) / int(p9_games)
    p9_deaths_average = int(p9_deaths) / int(p9_games)

    p9_elims_average = round(p9_elims_average, 2)
    p9_damage_average = round(p9_damage_average, 2)
    p9_healing_average = round(p9_healing_average, 2)
    p9_deaths_average = round(p9_deaths_average, 2)

    p9_data_elims.set(p9_elims_average)
    p9_data_damage.set(p9_damage_average)
    p9_data_healing.set(p9_healing_average)
    p9_data_deaths.set(p9_deaths_average)


#     Pre: form information
#    Post: resets form
# Purpose: reset the form if the user does not wish to use the current
#          information set in the form
# ######################################################################
def new_window():
    # code taken from: https://stackoverflow.com/questions/41655618/restart-program-tkinter
    python = sys.executable
    os.execl(python, python, * sys.argv)


#     Pre: root
#    Post: exits program
# Purpose: allows user to exit program
# ######################################################################
def quit_program():
    root.destroy()


#     Pre: none
#    Post: print text
# Purpose: show program description
# ######################################################################
def show_about():
    messagebox.showinfo("About", "Description:\n"
                                   "A program that show the Varsity\n"
                                 "Overwatch Team's competitive stats.\n"
                                 "\n"
                                 "Author: Walter Proulx\n"
                                 "Version: 1.0")


# ######################################################################
# MAIN METHOD
# ######################################################################
root = Tk()

root.title("CCE Overbuff")
root.iconbitmap('CCE Icon.ico')

root.columnconfigure(0, minsize=100)
root.columnconfigure(1, minsize=100)
root.columnconfigure(2, minsize=100)
root.columnconfigure(3, minsize=100)
root.columnconfigure(4, minsize=100)
root.columnconfigure(5, minsize=100)
root.columnconfigure(6, minsize=100)
root.columnconfigure(7, minsize=100)
root.columnconfigure(8, minsize=100)

# # setting menu
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
helpMenu = Menu(menu)

menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="quit", command=quit_program)

menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="about", command=show_about)

# # setting buttons
refresh_button = Button(root, text="Refresh", command=get_data)

# # setting logo and labels and fields
photo_logo = PhotoImage(file="CCE_banner_small.gif")
label_logo = Label(root, image=photo_logo)
label_logo.pack()

col_label_name = Label(root, text="Name")
col_label_elims = Label(root, text="Elims/Game")
col_label_damage = Label(root, text="Damage/Game")
col_label_healing = Label(root, text="Healing/Game")
col_label_deaths = Label(root, text="Deaths/Game")

p1_data_name = "roussin-1506"
p1_data_elims = StringVar()
p1_data_damage = StringVar()
p1_data_healing = StringVar()
p1_data_deaths = StringVar()

p1_label_name = Label(root, text=p1_data_name)
p1_label_elims = Label(root, textvariable=p1_data_elims)
p1_label_damage = Label(root, textvariable=p1_data_damage)
p1_label_healing = Label(root, textvariable=p1_data_healing)
p1_label_deaths = Label(root, textvariable=p1_data_deaths)

p2_data_name = "Nexima-1781"
p2_data_elims = StringVar()
p2_data_damage = StringVar()
p2_data_healing = StringVar()
p2_data_deaths = StringVar()

p2_label_name = Label(root, text=p2_data_name)
p2_label_elims = Label(root, textvariable=p2_data_elims)
p2_label_damage = Label(root, textvariable=p2_data_damage)
p2_label_healing = Label(root, textvariable=p2_data_healing)
p2_label_deaths = Label(root, textvariable=p2_data_deaths)

p3_data_name = "Sixel-1774"
p3_data_elims = StringVar()
p3_data_damage = StringVar()
p3_data_healing = StringVar()
p3_data_deaths = StringVar()

p3_label_name = Label(root, text=p3_data_name)
p3_label_elims = Label(root, textvariable=p3_data_elims)
p3_label_damage = Label(root, textvariable=p3_data_damage)
p3_label_healing = Label(root, textvariable=p3_data_healing)
p3_label_deaths = Label(root, textvariable=p3_data_deaths)

p4_data_name = "Squiddy-11860"
p4_data_elims = StringVar()
p4_data_damage = StringVar()
p4_data_healing = StringVar()
p4_data_deaths = StringVar()

p4_label_name = Label(root, text=p4_data_name)
p4_label_elims = Label(root, textvariable=p4_data_elims)
p4_label_damage = Label(root, textvariable=p4_data_damage)
p4_label_healing = Label(root, textvariable=p4_data_healing)
p4_label_deaths = Label(root, textvariable=p4_data_deaths)

p5_data_name = "Grendel-12934"
p5_data_elims = StringVar()
p5_data_damage = StringVar()
p5_data_healing = StringVar()
p5_data_deaths = StringVar()

p5_label_name = Label(root, text=p5_data_name)
p5_label_elims = Label(root, textvariable=p5_data_elims)
p5_label_damage = Label(root, textvariable=p5_data_damage)
p5_label_healing = Label(root, textvariable=p5_data_healing)
p5_label_deaths = Label(root, textvariable=p5_data_deaths)

p6_data_name = "ShadowDragon-133959"
p6_data_elims = StringVar()
p6_data_damage = StringVar()
p6_data_healing = StringVar()
p6_data_deaths = StringVar()

p6_label_name = Label(root, text=p6_data_name)
p6_label_elims = Label(root, textvariable=p6_data_elims)
p6_label_damage = Label(root, textvariable=p6_data_damage)
p6_label_healing = Label(root, textvariable=p6_data_healing)
p6_label_deaths = Label(root, textvariable=p6_data_deaths)

p7_data_name = "UltiG-11198"
p7_data_elims = StringVar()
p7_data_damage = StringVar()
p7_data_healing = StringVar()
p7_data_deaths = StringVar()

p7_label_name = Label(root, text=p7_data_name)
p7_label_elims = Label(root, textvariable=p7_data_elims)
p7_label_damage = Label(root, textvariable=p7_data_damage)
p7_label_healing = Label(root, textvariable=p7_data_healing)
p7_label_deaths = Label(root, textvariable=p7_data_deaths)

p8_data_name = "Hawk-13845"
p8_data_elims = StringVar()
p8_data_damage = StringVar()
p8_data_healing = StringVar()
p8_data_deaths = StringVar()

p8_label_name = Label(root, text=p8_data_name)
p8_label_elims = Label(root, textvariable=p8_data_elims)
p8_label_damage = Label(root, textvariable=p8_data_damage)
p8_label_healing = Label(root, textvariable=p8_data_healing)
p8_label_deaths = Label(root, textvariable=p8_data_deaths)

p9_data_name = "Woltyii-1290"
p9_data_elims = StringVar()
p9_data_damage = StringVar()
p9_data_healing = StringVar()
p9_data_deaths = StringVar()

p9_label_name = Label(root, text=p9_data_name)
p9_label_elims = Label(root, textvariable=p9_data_elims)
p9_label_damage = Label(root, textvariable=p9_data_damage)
p9_label_healing = Label(root, textvariable=p9_data_healing)
p9_label_deaths = Label(root, textvariable=p9_data_deaths)

# # setting up grid
label_logo.grid(columnspan=9, padx=35, pady=20)

col_label_name.grid(row=1, sticky=E, pady=2)
col_label_elims.grid(row=2, sticky=E, pady=2)
col_label_damage.grid(row=3, sticky=E, pady=2)
col_label_healing.grid(row=4, sticky=E, pady=2)
col_label_deaths.grid(row=5, sticky=E, pady=2)

p1_label_name.grid(row=1, column=1, sticky=W+E, pady=2)
p1_label_elims.grid(row=2, column=1, sticky=W+E, pady=2)
p1_label_damage.grid(row=3, column=1, sticky=W+E, pady=2)
p1_label_healing.grid(row=4, column=1, sticky=W+E, pady=2)
p1_label_deaths.grid(row=5, column=1, sticky=W+E, pady=2)

p2_label_name.grid(row=1, column=2, sticky=W+E, pady=2)
p2_label_elims.grid(row=2, column=2, sticky=W+E, pady=2)
p2_label_damage.grid(row=3, column=2, sticky=W+E, pady=2)
p2_label_healing.grid(row=4, column=2, sticky=W+E, pady=2)
p2_label_deaths.grid(row=5, column=2, sticky=W+E, pady=2)

p3_label_name.grid(row=1, column=3, sticky=W+E, pady=2)
p3_label_elims.grid(row=2, column=3, sticky=W+E, pady=2)
p3_label_damage.grid(row=3, column=3, sticky=W+E, pady=2)
p3_label_healing.grid(row=4, column=3, sticky=W+E, pady=2)
p3_label_deaths.grid(row=5, column=3, sticky=W+E, pady=2)

p4_label_name.grid(row=1, column=4, sticky=W+E, pady=2)
p4_label_elims.grid(row=2, column=4, sticky=W+E, pady=2)
p4_label_damage.grid(row=3, column=4, sticky=W+E, pady=2)
p4_label_healing.grid(row=4, column=4, sticky=W+E, pady=2)
p4_label_deaths.grid(row=5, column=4, sticky=W+E, pady=2)

p5_label_name.grid(row=1, column=5, sticky=W+E, pady=2)
p5_label_elims.grid(row=2, column=5, sticky=W+E, pady=2)
p5_label_damage.grid(row=3, column=5, sticky=W+E, pady=2)
p5_label_healing.grid(row=4, column=5, sticky=W+E, pady=2)
p5_label_deaths.grid(row=5, column=5, sticky=W+E, pady=2)

p6_label_name.grid(row=1, column=6, sticky=W+E, pady=2)
p6_label_elims.grid(row=2, column=6, sticky=W+E, pady=2)
p6_label_damage.grid(row=3, column=6, sticky=W+E, pady=2)
p6_label_healing.grid(row=4, column=6, sticky=W+E, pady=2)
p6_label_deaths.grid(row=5, column=6, sticky=W+E, pady=2)

p7_label_name.grid(row=1, column=7, sticky=W+E, pady=2)
p7_label_elims.grid(row=2, column=7, sticky=W+E, pady=2)
p7_label_damage.grid(row=3, column=7, sticky=W+E, pady=2)
p7_label_healing.grid(row=4, column=7, sticky=W+E, pady=2)
p7_label_deaths.grid(row=5, column=7, sticky=W+E, pady=2)

p8_label_name.grid(row=1, column=8, sticky=W+E, pady=2)
p8_label_elims.grid(row=2, column=8, sticky=W+E, pady=2)
p8_label_damage.grid(row=3, column=8, sticky=W+E, pady=2)
p8_label_healing.grid(row=4, column=8, sticky=W+E, pady=2)
p8_label_deaths.grid(row=5, column=8, sticky=W+E, pady=2)

p9_label_name.grid(row=1, column=9, sticky=W+E, pady=2)
p9_label_elims.grid(row=2, column=9, sticky=W+E, pady=2)
p9_label_damage.grid(row=3, column=9, sticky=W+E, pady=2)
p9_label_healing.grid(row=4, column=9, sticky=W+E, pady=2)
p9_label_deaths.grid(row=5, column=9, sticky=W+E, pady=2)

refresh_button.grid(row=6, column=0, sticky=E, pady=10)



root.mainloop()
