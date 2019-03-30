from tkinter import *
import urllib.request
import socket
from pythonping import ping


# function that gets the Internal IP address
def internal_IP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    # print(s.getsockname()[0])
    return(s.getsockname()[0])


# function that gets the External IP address
def external_IP():
    external_ip = urllib.request.urlopen('https://canihazip.com/s').read().decode('utf8')
    # print(external_ip)
    return external_ip


# funtion to refresh IPs
def refresh():
    intResult = internal_IP()
    internalResult.config(text=intResult)
    extResult = external_IP()
    externalResult.config(text=extResult)


# ping function
def ping_IP():
    print(ping_txt.get())
    myIP = ping(ping_txt.get(), verbose=True)
    ping_result.insert(END, myIP)


window = Tk()
window.title("IP Checker")
window.geometry('400x400')

# label to show user "external IP"
extlbl = Label(window, text="External IP: ", font=("Arial", 15))
extlbl.grid(column=0, row=0)

# label to show user "internal IP"
intlbl = Label(window, text="Internal IP: ", font=("Arial", 15))
intlbl.grid(column=0, row=1)

# label for ping
ping_lbl = Label(window, text="Ping: ", font=("Arial", 15))
ping_lbl.grid(column=0, row=2)

# ping input field
ping_txt = Entry(window, width=15)
ping_txt.grid(column=1, row=2)

# ping result field
ping_result = Text(window, height=15, width=40)
ping_result.grid(column=0 , row=3, columnspan=2)

# label to print internal IP address to
internalResult = Label(window, text=" ")
internalResult.grid(column=1, row=1)

# label to print external IP address to
externalResult = Label(window, text=" ")
externalResult.grid(column=1, row=0)

# Clicking this button closes the program
Button(window, text='Quit', bg="black", fg="red", command=window.destroy).grid(row=5, column=0, pady=1, padx=1, columnspan=2)

# Button to refresh the IP addresses
Button(window, text="Refresh IPs", bg="blue", fg="white", command=refresh).grid(row=5, column=1, pady=1, padx=1)

# Ping Button
Button(window, text="Ping", bg="orange", fg="black", command=ping_IP).grid(row=5, column=2, pady=1, padx=1)

refresh()
window.mainloop()
