#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 22, 2020 01:24:02 PM GMT  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import hub_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = TcpMonitorHub (root)
    hub_support.init(root, top)
    root.mainloop()

w = None
def create_TcpMonitorHub(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = TcpMonitorHub (w)
    hub_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_TcpMonitorHub():
    global w
    w.destroy()
    w = None

class TcpMonitorHub:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("403x496+2919+428")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(0, 0)
        top.title("TCP Monitor")
        top.configure(background="#212121")
        top.configure(highlightcolor="black")

        self.monitor_list_box = tk.Listbox(top)
        self.monitor_list_box.place(relx=0.025, rely=0.081, relheight=0.778
                , relwidth=0.804)
        self.monitor_list_box.configure(background="#191919")
        self.monitor_list_box.configure(borderwidth="0")
        self.monitor_list_box.configure(font="-family {Courier} -size 10")
        self.monitor_list_box.configure(foreground="#dddddd")
        self.monitor_list_box.configure(highlightbackground="#191919")
        self.monitor_list_box.configure(selectbackground="#0068dd")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=-0.047, rely=0.022, height=26, width=149)
        self.Label1.configure(activebackground="#212121")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(activeforeground="#dddddd")
        self.Label1.configure(background="#212121")
        self.Label1.configure(font="-family {Courier} -size 14")
        self.Label1.configure(foreground="#dddddd")
        self.Label1.configure(justify='left')
        self.Label1.configure(text='''Monitors''')

        self.open_connection_button = tk.Button(top)
        self.open_connection_button.place(relx=0.764, rely=0.02, height=26
                , width=26)
        self.open_connection_button.configure(activebackground="#0068dd")
        self.open_connection_button.configure(activeforeground="white")
        self.open_connection_button.configure(background="#191919")
        self.open_connection_button.configure(highlightbackground="#191919")
        self.open_connection_button.configure(relief="flat")

        self.ip_addr_label = tk.Label(top)
        self.ip_addr_label.place(relx=0.022, rely=0.869, height=21, width=319)
        self.ip_addr_label.configure(activebackground="#f9f9f9")
        self.ip_addr_label.configure(anchor='w')
        self.ip_addr_label.configure(background="#212121")
        self.ip_addr_label.configure(font="-family {Courier} -size 14")
        self.ip_addr_label.configure(foreground="#dddddd")
        self.ip_addr_label.configure(justify='left')
        self.ip_addr_label.configure(text='''IP:''')

        self.port_label = tk.Label(top)
        self.port_label.place(relx=0.025, rely=0.907, height=21, width=319)
        self.port_label.configure(activebackground="#f9f9f9")
        self.port_label.configure(anchor='w')
        self.port_label.configure(background="#212121")
        self.port_label.configure(font="-family {Courier} -size 14")
        self.port_label.configure(foreground="#dddddd")
        self.port_label.configure(justify='left')
        self.port_label.configure(text='''Port:''')

        self.transfer_rate_label = tk.Label(top)
        self.transfer_rate_label.place(relx=0.025, rely=0.944, height=21
                , width=319)
        self.transfer_rate_label.configure(activebackground="#f9f9f9")
        self.transfer_rate_label.configure(anchor='w')
        self.transfer_rate_label.configure(background="#212121")
        self.transfer_rate_label.configure(font="-family {Courier} -size 14")
        self.transfer_rate_label.configure(foreground="#dddddd")
        self.transfer_rate_label.configure(justify='left')
        self.transfer_rate_label.configure(text='''Transfer rate:''')

        self.monitor_time_history_button = tk.Button(top)
        self.monitor_time_history_button.place(relx=0.844, rely=0.02, height=56
                , width=56)
        self.monitor_time_history_button.configure(activebackground="#0068dd")
        self.monitor_time_history_button.configure(activeforeground="white")
        self.monitor_time_history_button.configure(background="#191919")
        self.monitor_time_history_button.configure(highlightbackground="#191919")
        self.monitor_time_history_button.configure(relief="flat")

        self.monitor_profile_button = tk.Button(top)
        self.monitor_profile_button.place(relx=0.844, rely=0.141, height=56
                , width=56)
        self.monitor_profile_button.configure(activebackground="#0068dd")
        self.monitor_profile_button.configure(activeforeground="white")
        self.monitor_profile_button.configure(background="#191919")
        self.monitor_profile_button.configure(highlightbackground="#191919")
        self.monitor_profile_button.configure(relief="flat")

if __name__ == '__main__':
    vp_start_gui()





