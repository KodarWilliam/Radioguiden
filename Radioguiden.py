from tkinter import *
import requests

def channel(channelid):
    URL = "http://api.sr.se/api/v2/scheduledepisodes/rightnow"

    PARAMS = {
        "channelid": channelid,
        "format": "JSON"
    }

    response = requests.get(url=URL, params=PARAMS).json()

    channel_info = response.get("channel", {})
    previous_schedule_episode = channel_info.get("previousscheduledepisode", {})
    current_schedule_episode = channel_info.get("currentscheduledepisode", {})
    next_schedule_episode = channel_info.get("nextscheduledepisode", {})

    new_window = Tk()
    new_window.title("P1")
    new_window.geometry('800x600')

    title_label = Label(new_window, text="Radio Schedule", font=("Helvetica", 16, "bold"))
    title_label.grid(row=0, column=0, pady=10)

    # Previous Episode
    Label(new_window, text="Previous Episode:", font=("Helvetica", 12, "bold")).grid(row=1, column=0, sticky="w", pady=5)
    Label(new_window, text=f"Title: {previous_schedule_episode.get('title', 'N/A')}", wraplength=700, justify="left").grid(row=2, column=0, sticky="w")
    Label(new_window, text=f"Description: {previous_schedule_episode.get('description', 'N/A')}", wraplength=700, justify="left").grid(row=3, column=0, sticky="w")

    # Add space
    Label(new_window).grid(row=4, column=0)

    # Current Episode
    Label(new_window, text="Current Episode:", font=("Helvetica", 12, "bold")).grid(row=5, column=0, sticky="w", pady=5)
    Label(new_window, text=f"Title: {current_schedule_episode.get('title', 'N/A')}", wraplength=700, justify="left").grid(row=6, column=0, sticky="w")
    Label(new_window, text=f"Description: {current_schedule_episode.get('description', 'N/A')}", wraplength=700, justify="left").grid(row=7, column=0, sticky="w")

    # Add space
    Label(new_window).grid(row=8, column=0)

    # Next Episode
    Label(new_window, text="Next Episode:", font=("Helvetica", 12, "bold")).grid(row=9, column=0, sticky="w", pady=5)
    Label(new_window, text=f"Title: {next_schedule_episode.get('title', 'N/A')}", wraplength=700, justify="left").grid(row=10, column=0, sticky="w")
    Label(new_window, text=f"Description: {next_schedule_episode.get('description', 'N/A')}", wraplength=700, justify="left").grid(row=11, column=0, sticky="w")

    new_window.mainloop()

window = Tk()
window.title("Radioguiden")
window.geometry('800x600')

Label(window, text="MENU", font=("Helvetica", 14)).pack(pady=10)
Label(window, text="Choose a radio station to retrieve information about previous, current and next episode:", font=("Helvetica", 14)).pack(pady=10)

button_frame = Frame(window)
button_frame.pack()

Button(button_frame, text="P1", command=lambda: channel(132), height=2, width=10).grid(row=0, column=0, padx=5)
Button(button_frame, text="P2", command=lambda: channel(163), height=2, width=10).grid(row=0, column=1, padx=5)
Button(button_frame, text="P3", command=lambda: channel(164), height=2, width=10).grid(row=0, column=2, padx=5)
Button(button_frame, text="P4 Blekinge", command=lambda: channel(213), height=2, width=10).grid(row=0, column=3, padx=5)
Button(button_frame, text="P4 Dalarna", command=lambda: channel(223), height=2, width=10).grid(row=0, column=4, padx=5)

window.mainloop()
