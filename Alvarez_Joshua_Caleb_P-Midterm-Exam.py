# ==================================================
# ALVAREZ, JOSHUA CALEB P.
# MIDTERM EXAM IN OOP
# ==================================================


# ==================================================
# QUESTION 1
# Temperature Conversion
# ==================================================

def question1():

    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * 5 / 9

    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15

    tempInCelsius = float(input("Enter the temperature in Celsius: "))

    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")

    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")

    tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    convert = FahrenheitToCelsius(tempInFahrenheit)
    print(str(convert.conversion()) + " Celsius")

    tempInKelvin = float(input("Enter the temperature in Kelvin: "))
    convert = KelvinToCelsius(tempInKelvin)
    print(str(convert.conversion()) + " Celsius")


# ==================================================
# QUESTION 2
# Change Background Color
# ==================================================

def question2():

    import tkinter as tk

    def change_color():
        window.config(bg="yellow")

    window = tk.Tk()
    window.title("Special Midterm Exam in OOP")
    window.geometry("315x250")

    button = tk.Button(
        window,
        text="Click to Change Color",
        command=change_color
    )

    button.place(x=108, y=135)

    window.mainloop()


# ==================================================
# QUESTION 3
# Display Fullname
# ==================================================

def question3():

    import tkinter as tk

    def display_fullname():
        fullname = entry1.get()
        entry2.delete(0, tk.END)
        entry2.insert(0, fullname)

    window = tk.Tk()
    window.title("Midterm in OOP")
    window.geometry("360x250")

    label = tk.Label(
        window,
        text="Enter your fullname:",
        fg="red"
    )
    label.place(x=45, y=80)

    entry1 = tk.Entry(window, width=20)
    entry1.place(x=195, y=78)

    button = tk.Button(
        window,
        text="Click to display your Fullname",
        command=display_fullname
    )
    button.place(x=45, y=110)

    entry2 = tk.Entry(window, width=20)
    entry2.place(x=195, y=110)

    window.mainloop()


# ==================================================
# RUN THE QUESTION YOU WANT TO TEST
# ==================================================

question1()
