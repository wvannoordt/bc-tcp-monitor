import sys
import hub
import W_hub
import tkinter as tk
import hub_support

root = tk.Tk()
top = hub.TcpMonitorHub (root)
bindings = W_hub.W_TcpMonitorHub(top, root)
hub_support.init(root, top)
root.mainloop()
sys.exit()
