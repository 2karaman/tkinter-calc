import tkinter as tk

def close():
    root.destroy()

def click(event):
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "MC":
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Memory Cleared")
        entry.delete(0, tk.END)
    elif button_text == "OFF":
        close()
    elif button_text == "Minimise":
        root.iconify()
    elif button_text == "Maximise":
        root.attributes("-fullscreen", True)
    elif button_text == "Restore":
        root.attributes("-fullscreen", False)
        root.geometry("600x500")
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)


BG_COLOR = "#b6b9a6"
BTN_COLOR = "#FFFFFF"
BTN_HOVER = "#B4B4B4"
TEXT_COLOR = "#000000"
FONT = ("Arial", 18)


root = tk.Tk()
root.title("My Calculator")
root.configure(bg=BG_COLOR)
# root.geometry("350x450")
root.resizable(True, True)
root.attributes('-fullscreen', False)

root.iconbitmap("image.ico")

root.geometry("600x500")

entry = tk.Entry(root, font=("Segoe UI", 24), bg=BTN_COLOR, fg=TEXT_COLOR, border=0, justify="right")
entry.pack(fill="both", padx=20, pady=20, ipady=10)

frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(expand=True, fill="both")

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["MC", "Minimise", "Maximise", "OFF", "Restore"]
]

def on_enter(e): e.widget["bg"] = BTN_HOVER
def on_leave(e): e.widget["bg"] = BTN_COLOR


def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def end_fullscreen(event=None):
    root.attributes("-fullscreen", False)

def restore(event=None):
    root.attributes("-fullscreen", False)
    root.geometry("500x500")

root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", end_fullscreen)
root.bind("<F5>", restore)

for row in buttons:
    row_frame = tk.Frame(frame, bg=BG_COLOR)
    row_frame.pack(expand=True, fill="both")
    for b in row:
        btn = tk.Button(row_frame, text=b, font=FONT, bg=BTN_COLOR, fg=TEXT_COLOR, activebackground=BTN_HOVER,
                        activeforeground=TEXT_COLOR, relief="flat", borderwidth=0)
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        btn.bind("<Button-1>", click)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

root.mainloop()


