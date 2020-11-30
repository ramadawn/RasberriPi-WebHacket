import tkinter as tk
window = tk.Tk()
from PortScan import findOpenPorts as findport
import LocalIP
import ImprovedScanner
import ssh_brute_force
import login_brute_force

window.title("Network Scanner")
window.geometry("478x650")

network_value = ""

#function to grab text from network_input
def retrieve_network():
    network = network_input.get()
    if network == "":
        network = None

    port = network_port_input.get()
    if port == "":
        return

    network_list.delete(0, tk.END)

    open_ip_list, available_ip_list, vendors = ImprovedScanner.ImprovedScanner(int(port), network=network)

    if len(open_ip_list) == 0:
        network_list.insert(0, "No open ports found on any IP address.")

    for idx, ip in enumerate(open_ip_list):
        output = f"IP: {ip}      Vendor: {vendors.get(ip)}"
        network_list.insert(idx, output)

#function to grab text from the 4 entries in login hacker
def retrieve_hacking():
    result_text.delete('1.0', tk.END)

    if brute_force_options.get() == "HTTP/HTTPS":
        url = url_input.get()
        username_format = username_input.get()
        password_format = password_input.get()

        if url == "" or username_format == "" or password_format == "":
            result_text.insert(tk.END, "empty")
            return

        result = login_brute_force.brute_force_login(url, username_format, password_format)

        if result == None:
            return
    else:
        url = url_input.get()
        port = port_input.get()
        try:
            if url == "" or port == "":
                result_text.insert(tk.END, "empty")
                return

            result = ssh_brute_force.brute_force(url, int(port))
        except:
            result = f"Could not connect to port {port} on {url}."





    result_text.insert(tk.END, result)

#attempt to make call the function in portscan
#def findOpenPorts(network_value, scanRange = 255,network =None)

#attempt to inport the values into network_list
"""for ip in Avail_IP_List:
    network_list.insert(0, ip)"""

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
network_port_label = tk.Label(frame_network, text = "Port:")
network_port_input = tk.Entry(frame_network)
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
network_port_label.grid(row=1, column=0, padx=2)
network_port_input.grid(row=1, column=1, padx=2)
network_button.grid(row=0, column=2, padx=2)

network_list.pack(pady=5, padx=5)

#inputing info to hack login site
OptionList = [
"HTTP/HTTPS",
"SSH"
]
frame_hack = tk.Frame(bottom_frame, borderwidth=2, relief='sunken')
info_label = tk.Label(frame_hack, text = "Login Hacker",font=(None, 12))
hack_input = tk.Frame(frame_hack, borderwidth=2)
url_label = tk.Label(hack_input, text = "URL Address:", anchor='e')
url_input = tk.Entry(hack_input)
port_label = tk.Label(hack_input, text = "Port Number:")
port_input = tk.Entry(hack_input)
username_label = tk.Label(hack_input, text = "Username Format:")
username_input = tk.Entry(hack_input)
password_label = tk.Label(hack_input, text = "Password Format:")
password_input = tk.Entry(hack_input)

#configure dropdown
brute_force_options = tk.StringVar(window)
brute_force_options.set(OptionList[0])
opt = tk.OptionMenu(frame_hack, brute_force_options, *OptionList)
opt.grid(row=2, column=1, padx=2, pady=2)
opt.pack()

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
button_scan.grid(row=2, column=2, padx=2, pady=2)

frame_result.pack(fill='x', padx=2, pady=5)
result_label.pack(pady=2, padx=5)
result_text.pack(pady=5, padx=5)

window.mainloop()