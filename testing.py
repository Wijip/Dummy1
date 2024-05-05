import tkinter as tk

# Function to convert temperature based on selected unit
def convert_temperature():
  try:
    # Get user input and convert to float
    value = float(entry_value.get())

    # Get selected unit from radio buttons
    selected_unit = unit_var.get()

    # Conversion logic based on selected unit
    if selected_unit == "celsius":
      result = (value * 9/5) + 32
      result_unit = "Fahrenheit"
    elif selected_unit == "fahrenheit":
      result = (value - 32) * 5/9
      result_unit = "Celsius"
    else:
      # Handle potential errors (e.g., invalid unit)
      return

    # Update result label with converted value and unit
    label_result.config(text=f"Converted value: {result:.2f} {result_unit}")
  except ValueError:
    # Handle invalid input (e.g., non-numeric characters)
    label_result.config(text="Invalid Input. Please enter a number.")

# Main program window
window = tk.Tk()
window.title("Temperature Converter")

# Unit selection variables
unit_var = tk.StringVar()
unit_var.set("celsius")  # Set default unit

# Label for temperature value entry
label_value = tk.Label(window, text="Enter temperature value:")
label_value.grid(row=0, column=0, padx=5, pady=5)

# Entry field for temperature value
entry_value = tk.Entry(window, width=10)
entry_value.grid(row=0, column=1, padx=5, pady=5)

# Radio buttons for unit selection
celsius_radio = tk.Radiobutton(window, text="Celsius", variable=unit_var, value="celsius")
celsius_radio.grid(row=1, column=0, padx=5, pady=5)

fahrenheit_radio = tk.Radiobutton(window, text="Fahrenheit", variable=unit_var, value="fahrenheit")
fahrenheit_radio.grid(row=1, column=1, padx=5, pady=5)

# Button to trigger conversion
button_convert = tk.Button(window, text="Convert", command=convert_temperature)
button_convert.grid(row=2, columnspan=2, padx=5, pady=5)

# Label to display conversion result
label_result = tk.Label(window, text="")
label_result.grid(row=3, columnspan=2, padx=5, pady=5)

# Run the main event loop
window.mainloop()
