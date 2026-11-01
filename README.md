# SIT210 - Task 5.1P: Smart Home Lighting GUI

This project is a Raspberry Pi-based graphical user interface (GUI) designed to control room lights (LEDs) for a smart home system. It allows a user to toggle between different room lights using radio buttons, ensuring only one light remains on at a time.

---

## Features
- **Graphical User Interface (GUI):** Built using Python and Tkinter for simple, interactive control.
- **Exclusive Light Selection:** Radio buttons for Living Room, Bathroom, and Closet ensure only the selected room LED is illuminated while the others turn off.
- **Clean Exit:** An Exit button safely closes the interface and shuts off all active GPIO pins.

---

## Hardware Setup
- **Microcontroller:** Raspberry Pi 4 Model B
- **Components:**
  - 3x LEDs (Living Room, Bathroom, Closet)
  - 3x 220Ω Resistors
  - 1x Solderless Breadboard
  - Jumper Wires (Female-to-Male and Male-to-Male)

### Circuit Connections
| Component | Function / Pin | Raspberry Pi Pin |
| :--- | :--- | :--- |
| **Living Room LED** | Anode (+) via 220Ω Resistor | GPIO 17 (Physical Pin 11) |
| **Bathroom LED** | Anode (+) via 220Ω Resistor | GPIO 27 (Physical Pin 13) |
| **Closet LED** | Anode (+) via 220Ω Resistor | GPIO 22 (Physical Pin 15) |
| **Ground (All LEDs)** | Cathode (-) common rail | Ground (Physical Pin 6) |
