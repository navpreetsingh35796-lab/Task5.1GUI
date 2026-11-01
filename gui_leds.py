import tkinter as tk
from gpiozero import LED

# Initialize GPIO Pins
led_living = LED(17)
led_bathroom = LED(27)
led_closet = LED(22)

# Function to handle radio button selection
def update_leds():
    selected = room_var.get()
    
    # Reset all LEDs first
    led_living.off()
    led_bathroom.off()
    led_closet.off()
    
    # Turn ON only the selected room's LED
    if selected == "living":
        led_living.on()
    elif selected == "bathroom":
        led_bathroom.on()
    elif selected == "closet":
        led_closet.on()

# Function to cleanly exit the app
def exit_app():
    led_living.off()
    led_bathroom.off()
    led_closet.off()
    window.destroy()

# Main GUI Window Setup
window = tk.Tk()
window.title("Smart Home Light Control")
window.geometry("300x260")

# Header Label
header = tk.Label(window, text="Select Room Light", font=("Arial", 14, "bold"), pady=10)
header.pack()

# Radio Button Variable
room_var = tk.StringVar(value="none")

# Radio Buttons
rb_living = tk.Radiobutton(
    window, text="Living Room", variable=room_var, value="living",
    font=("Arial", 11), command=update_leds, pady=4
)
rb_living.pack(anchor="w", padx=60)

rb_bathroom = tk.Radiobutton(
    window, text="Bathroom", variable=room_var, value="bathroom",
    font=("Arial", 11), command=update_leds, pady=4
)
rb_bathroom.pack(anchor="w", padx=60)

rb_closet = tk.Radiobutton(
    window, text="Closet", variable=room_var, value="closet",
    font=("Arial", 11), command=update_leds, pady=4
)
rb_closet.pack(anchor="w", padx=60)

# Exit Button
btn_exit = tk.Button(
    window, text="Exit", font=("Arial", 11, "bold"),
    bg="#ff4d4d", fg="white", width=12, command=exit_app
)
btn_exit.pack(pady=20)

# Window close event handler (if user clicks the 'X' button on the title bar)
window.protocol("WM_DELETE_WINDOW", exit_app)

# Run the GUI event loop
window.mainloop()
