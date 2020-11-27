import tkinter as tk
window = tk.Tk()

window.title("Network Scanner")
window.geometry("500x480")

frame_header = tk.Frame(window, borderwidth=2, pady=2)
middle_frame = tk.Frame(window, borderwidth=2, pady=5)
bottom_frame = tk.Frame(window, borderwidth=2, pady=5)

frame_header.grid(row=0, column=0)
middle_frame.grid(row=1, column=0)
bottom_frame.grid(row=2, column=0)

header = tk.Label(frame_header,
                  text = "Network Scanner",
                  bg='grey', fg='black', height='1', width='70')
header.grid(row=0, column=0)

#networks scan part
frame_scan = tk.Frame(middle_frame, borderwidth=2, relief='sunken')
network_label = tk.Label(middle_frame,
                         text = "Networks",
                         anchor='w',
                         justify='left')
network_text = tk.Text(frame_scan, width=55, height=10)
button_scan = tk.Button(frame_scan,
                       text="Scan",
                       bg='dark green',
                       fg='white',
                       relief='raised',
                       width=10)

network_label.pack()
frame_scan.pack(fill='x', pady=2)
network_text.pack(padx=5)
button_scan.pack()

#info about one network
frame_hack = tk.Frame(bottom_frame, borderwidth=2, relief='sunken')
info_label = tk.Label(bottom_frame, text = "Network Information")
hack_text = tk.Text(frame_hack, width=55, height=10)

info_label.pack()
frame_hack.pack(fill='x', pady=2)
hack_text.pack(padx=5)
