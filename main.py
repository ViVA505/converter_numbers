import tkinter as tk
from Num_convert.number_convert import NumberConverterApp


if __name__ == "__main__":
    app = tk.Tk()
    converter_app = NumberConverterApp(app)
    app.mainloop()