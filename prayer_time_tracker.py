import tkinter as tk
from tkinter import messagebox
import time, json, api
from tkinter import ttk

# import ttkbootstrap as ttk
# import sv_ttk

try:
    times = json.load(open("prayer_times.json"))
except FileNotFoundError:
    api.main()
    times = json.load(open("prayer_times.json"))


# root = ttk.Window(themename="darkly")
def main_window():
    pady_val = 10
    root = tk.Tk()
    window_width = 250
    window_height = 150
    left = (root.winfo_screenwidth() // 2) - (window_width // 2)
    top = (root.winfo_screenheight() // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{left}+{top}")
    root.bind("<Escape>", lambda e: root.destroy())
    root.title("Prayer Timer")

    time_label = ttk.Label(root, text="Chose which time to dispay", font=("segoe ui", 14))
    time_label.pack(pady=pady_val)

    combo_var = tk.StringVar(value="Please select an option")
    combo = ttk.OptionMenu(root, combo_var, "Please select an option", *times[list(times.keys())[0]]["times"].keys())
    combo.pack(pady=pady_val)

    ok_button = ttk.Button(root, text="OK", command=lambda: ok_button_command(root, combo_var))
    ok_button.pack(pady=pady_val)

    # sv_ttk.use_dark_theme()
    root.mainloop()


def ok_button_command(root, combo_var):
    if combo_var.get() == "Please select an option":
        messagebox.showerror("Error", "Please select a time to display")
        return
    root.destroy()
    time_window(combo_var.get())


def time_window(combo_var):
    pady_val = 0
    root = tk.Tk()

    root.attributes("-topmost", True)
    root.overrideredirect(True)
    root.attributes("-alpha", 0.75)
    root.configure(bg="#000000")

    window_width = 250
    window_height = 150
    gap = 10
    left = root.winfo_screenwidth() - window_width - gap
    top = gap
    root.geometry(f"{window_width}x{window_height}+{left}+{top}")
    root.bind("<Escape>", lambda e: root.destroy())
    root.title("Prayer Timer")

    prayer_name_label = tk.Label(root, text=combo_var.title(), font=("segoe ui", 12), background="black", foreground="white")
    prayer_name_label.pack(pady=pady_val)

    prayer_label = tk.Label(root, text=f"{times[time.strftime('%d')]['times'][combo_var]['hour']}:{times[time.strftime('%d')]['times'][combo_var]['minute']}", font=("segoe ui", 20), background="black", foreground="white")
    prayer_label.pack(pady=pady_val)

    time_frame = tk.Frame(root, background="black")
    time_frame.columnconfigure(0, weight=1)
    time_frame.columnconfigure(1, weight=1)
    time_frame.rowconfigure(0, weight=1)
    time_frame.rowconfigure(1, weight=1)
    time_frame.pack(pady=pady_val)

    time_name_label = tk.Label(time_frame, text="Current", font=("segoe ui", 12), background="black", foreground="white")
    time_name_label.grid(row=0, column=0, pady=pady_val)

    prayer_remaining_name_label = tk.Label(time_frame, text="Remaining", font=("segoe ui", 12), background="black", foreground="white")
    prayer_remaining_name_label.grid(row=0, column=1, pady=pady_val)

    time_label = tk.Label(time_frame, text="", font=("segoe ui", 16), background="black", foreground="white")
    time_label.grid(row=1, column=0, pady=pady_val)

    prayer_remaining_label = tk.Label(time_frame, text="", font=("segoe ui", 16), background="black", foreground="white")
    prayer_remaining_label.grid(row=1, column=1, pady=pady_val)

    def update_time():
        t_now = time.localtime()
        prayer_time = time.struct_time((t_now.tm_year, t_now.tm_mon, t_now.tm_mday, times[time.strftime("%d")]["times"][combo_var]["hour"], times[time.strftime("%d")]["times"][combo_var]["minute"], 0, 0, 0, 0))
        diff = time.mktime(prayer_time) - time.mktime(t_now)
        hours, remainder = divmod(diff, 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours < 0:
            prayer_remaining_label.config(text="--:--:--")
        else:
            prayer_remaining_label.config(text=f"{'{:02d}'.format(int(hours))}:{'{:02d}'.format(int(minutes))}:{'{:02d}'.format(int(seconds))}")
        current_time = time.strftime("%H:%M:%S")
        time_label.config(text=current_time)
        root.after(1000, update_time)
        if hours == 0 and minutes == 0 and seconds == 0:
            root.destroy()
            messagebox.showinfo(f"{combo_var.title()} Time", f"{combo_var.title()} time has arrived")

    update_time()
    root.mainloop()


times = json.load(open("prayer_times.json"))
if __name__ == "__main__":
    try:
        special_case = open("special_case.txt").read()
        if special_case not in times[time.strftime("%d")]["times"].keys():
            special_case = None
    except FileNotFoundError:
        special_case = None
    if special_case is None:
        main_window()
    elif abs(times[time.strftime("%d")]["times"][special_case]["hour"] - int(time.strftime("%H"))) <= 1:
        time_window(special_case)
    else:
        main_window()
