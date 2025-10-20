
'''
This program creates a GUI for calculating traffic flow based on user input for traffic light timings and arrival flow.
'''
import tkinter as tk

root = tk.Tk()
root.title("Traffic Flow Calculator")
root.geometry("650x650")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Green (s):").grid(row=0, column=0, sticky="w", padx=4, pady=4)
green_entry = tk.Entry(frame, width=16)
green_entry.grid(row=0, column=1, padx=4, pady=4)
green_entry.insert(0, "3")
green_entry.focus()



tk.Label(frame, text="Yellow (s):").grid(row=1, column=0, sticky="w", padx=4, pady=4)
yellow_entry = tk.Entry(frame, width=16)
yellow_entry.grid(row=1, column=1, padx=4, pady=4)
yellow_entry.insert(0, "1")
yellow_entry.focus()



tk.Label(frame, text="Red(s):").grid(row=2, column=0, sticky="w", padx=4, pady=4)
red_entry = tk.Entry(frame, width=16)
red_entry.grid(row=2, column=1, padx=4, pady=4)
red_entry.insert(0, "3")
red_entry.focus()




tk.Label(frame, text="arrival flow (veh/min):").grid(row=3, column=0, sticky="w", padx=4, pady=4)
arrive_entry = tk.Entry(frame, width=16)
arrive_entry.grid(row=3, column=1, padx=4, pady=4)
arrive_entry.insert(0, "20")
arrive_entry.focus()


result_var = tk.StringVar()
result_var.set("Enter values and click Calculate.")
result_label = tk.Label(root, textvariable=result_var, justify="left", anchor="w")
result_label.pack(fill="x", padx=10, pady=10)







def convert_cycle_time():
    try:
        green = float(green_entry.get().strip())
        yellow = float(yellow_entry.get().strip())
        red = float(red_entry.get().strip())
        arrival = float(arrive_entry.get().strip())
        if green <= 0 or yellow <= 0 or red <= 0 or arrival <= 0:
            raise ArithmeticError
    except:
        result_var.set("Please enter a valid number (seconds, veh/min).")
        return
    final = green + yellow + red
    expected_per_min = arrival * (green / final) # since we only care about the green
    expected_per_hour = expected_per_min * 60
    res = (
        f"Total Cycle Time: {final:.2f} s\n"
        f"Expected Flow per Minute: {expected_per_min:.2f} veh/min\n"
        f"Expected Flow per Hour: {expected_per_hour:.2f} veh/hr"
    )
    result_var.set(res)

def clear():
    green_entry.delete(0, "end")
    green_entry.insert(0, "3")
    yellow_entry.delete(0, "end")
    yellow_entry.insert(0, "1")
    red_entry.delete(0, "end")
    red_entry.insert(0, "3")
    arrive_entry.delete(0, "end")
    arrive_entry.insert(0, "20")
    result_var.set("Enter values and click Calculate.")
    green_entry.focus()
    yellow_entry.focus()
    red_entry.focus()
    arrive_entry.focus()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=(0, 10))

calculate_btn = tk.Button(btn_frame, text="Calculate", width=15, command=convert_cycle_time)
calculate_btn.pack(side="left", padx=8)





root.mainloop()
