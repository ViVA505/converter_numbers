import tkinter as tk

class NumberConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Конвертер чисел")
        root.geometry("600x400")
        root.resizable(False, False)

        self.label = tk.Label(root, text="Введите десятичное число:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.conversion_option = tk.StringVar()
        self.conversion_option.set("binary")

        self.binary_radio = tk.Radiobutton(root, text="Двоичная", variable=self.conversion_option, value="binary")
        self.binary_radio.pack()

        self.octal_radio = tk.Radiobutton(root, text="Восьмеричная", variable=self.conversion_option, value="octal")
        self.octal_radio.pack()

        self.hexadecimal_radio = tk.Radiobutton(root, text="Шестнадцатеричная", variable=self.conversion_option, value="hexadecimal")
        self.hexadecimal_radio.pack()

        self.convert_button = tk.Button(root, text="Конвертировать", command=self.convert)
        self.convert_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def convert(self):
        decimal_number = self.entry.get()
        conversion_option = self.conversion_option.get()

        if not decimal_number:
            self.result_label.config(text="Введите пожалуйста число")
            return

        if conversion_option == "binary":
            # Конвертация в двоичную систему
            result = bin(int(decimal_number))[2:]
        elif conversion_option == "octal":
            # Конвертация в восьмеричную систему
            result = oct(int(decimal_number))[2:]
        elif conversion_option == "hexadecimal":
            # Выполните конвертацию в шестнадцатеричную систему
            result = hex(int(decimal_number))[2:].upper()
        else:
            result = "Выбран неверный вариант конвертации"

        self.result_label.config(text=result)

