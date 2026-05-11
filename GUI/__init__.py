# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import tkinter as t

main = t.Tk()
main.title("Cortex")
main.configure(height=200,width=250,bg = "black")
text = t.Text(main,width=50,height=20,bg="black",fg="white")
text.pack()
button = t.Button(main,text="click me")
button.pack()
main.mainloop()