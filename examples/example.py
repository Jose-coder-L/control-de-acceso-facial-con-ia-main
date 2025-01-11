import os
import sys
from tkinter import *
import logging as log

log.basicConfig(level=log.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Add project root to path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from process.main import GraphicalUserInterface

app = GraphicalUserInterface(Tk())
app.frame.mainloop()