import tkinter as tk
window = tk.Tk()
from PortScan import findOpenPorts as findport

window.title("Network Scanner")
window.geometry("478x586")

#function to grab text from network_input
def retrieve_network():
    put_in = network_input.get()
    if network_input.get() == "":
        network_list.insert(0, "default network")
    else:
       network_list.insert(0, put_in)

#function to grab text from the 4 entries in login hacker
def retrieve_hacking():
    network_ip = network_list.get(network_list.curselection())
    if network_ip != "":
        result_text.insert(tk.END, network_ip)
    if url_input.get() == "" or port_input.get() == "" or username_input.get == "" or password_input.get() == "":
        result_text.insert(tk.END, "nothing inputted\n")
    else:
        result_text.insert(tk.END, "works")

#function to grab values from hacking importion?
#def hacking_results():

#main frames
frame_header = tk.Frame(window, borderwidth=2, pady=2)
middle_frame = tk.Frame(window, borderwidth=2, pady=5)
bottom_frame = tk.Frame(window, borderwidth=2, pady=2)

frame_header.grid(row=0, column=0)
middle_frame.grid(row=1, column=0)
bottom_frame.grid(row=2, column=0)

#header for program
header = tk.Label(frame_header,
                  text = "Network Scanner",
                  font=(None, 15),
                  bg='grey', fg='black', height='1', width='42')
header.grid(row=0, column=0)

#networks scanning part
frame_scan = tk.Frame(middle_frame, borderwidth=2, relief='sunken')
network_label = tk.Label(frame_scan, text = "Networks",font=(None, 12))

frame_network = tk.Frame(frame_scan, borderwidth=2)
network_address = tk.Label(frame_network, text = "Network Address:")
network_input = tk.Entry(frame_network)
network_button = tk.Button(frame_network,
                           text="Scan Networks",
                           bg='dark green',
                           fg='white',
                           relief='raised',
                           command = retrieve_network)

network_list = tk.Listbox(frame_scan, selectmode='single', width=74)

frame_scan.pack(fill='x', pady=2)
network_label.pack()

frame_network.pack(pady=2)
network_address.grid(row=0, column=0, padx=2)
network_input.grid(row=0, column=1, padx=2)
network_button.grid(row=0, column=2, padx=2)

network_list.pack(pady=5, padx=5)

#inputing info to hack login site
frame_hack = tk.Frame(bottom_frame, borderwidth=2, relief='sunken')
info_label = tk.Label(frame_hack, text = "Login Hacker",font=(None, 12))

hack_input = tk.Frame(frame_hack, borderwidth=2)
url_label = tk.Label(hack_input, text = "URL Address:", anchor='e')
url_input = tk.Entry(hack_input)
port_label = tk.Label(hack_input, text = "Port Number:")
port_input = tk.Entry(hack_input)
username_label = tk.Label(hack_input, text = "Username:")
username_input = tk.Entry(hack_input)
password_label = tk.Label(hack_input, text = "Password:")
password_input = tk.Entry(hack_input)

button_scan = tk.Button(hack_input,
                        text="Scan",
                        bg='dark green',
                        fg='white',
                        relief='raised',
                        width=10,
                        command = retrieve_hacking)

frame_result = tk.Frame(bottom_frame, borderwidth=2, relief='groove')
result_label = tk.Label(frame_result, text = "Results",font=(None, 12))
result_text = tk.Text(frame_result, width=55, height=7)

#packing the hacking section
frame_hack.pack(fill='x')
info_label.pack()

hack_input.pack(pady=2)
url_label.grid(row=0, column=0, padx=2, pady=2)
url_input.grid(row=0, column=1, padx=2, pady=2)
port_label.grid(row=0, column=2, padx=2, pady=2)
port_input.grid(row=0, column=3, padx=2, pady=2)

username_label.grid(row=1, column=0, padx=2, pady=2)
username_input.grid(row=1, column=1, padx=2, pady=2)
password_label.grid(row=1, column=2, padx=2, pady=2)
password_input.grid(row=1, column=3, padx=2, pady=2)

button_scan.grid(row=2, column=0, padx=2, pady=2)

frame_result.pack(fill='x', padx=2, pady=5)
result_label.pack(pady=2, padx=5)
result_text.pack(pady=5, padx=5)
