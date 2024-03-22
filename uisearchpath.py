# import tkinter as tk
# import configparser
# from tkinter import filedialog

# class PathSelectorApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("Path Selector")

#         self.path_entry = tk.Entry(master, width=50)
#         self.path_entry.grid(row=0, column=0, padx=10, pady=10)

#         self.browse_button = tk.Button(master, text="Browse", command=self.browse_path)
#         self.browse_button.grid(row=0, column=1, padx=5, pady=10)

#         self.ok_button = tk.Button(master, text="OK", command=self.on_ok)
#         self.ok_button.grid(row=1, column=0, columnspan=2, pady=10)

#     def browse_path(self):
#         filename = filedialog.askdirectory()
#         if filename:
#             self.path_entry.delete(0, tk.END)
#             self.path_entry.insert(0, filename)

#     def on_ok(self):
#        selected_path = self.path_entry.get()
#        if selected_path:
#            print("Selected Path:", selected_path)
#            # Membaca file config.conf
#            config = configparser.ConfigParser()
#            config.read("config.conf")
#            # Memperbarui nilai PATH dalam file config.conf
#            config["USER"]["path"] = selected_path
#            # Menyimpan kembali perubahan ke dalam file config.conf
#            with open("config.conf", "w") as configfile:
#                config.write(configfile)
#            print("Path saved to config.conf")
#            # Menyembunyikan tampilan UI
#            self.master.withdraw()


import tkinter as tk
from tkinter import filedialog
import configparser

class PathSelectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Path Selector")

        self.path_entry = tk.Entry(master, width=50)
        self.path_entry.grid(row=0, column=0, padx=10, pady=10)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_path)
        self.browse_button.grid(row=0, column=1, padx=5, pady=10)

        self.ok_button = tk.Button(master, text="OK", command=self.on_ok)
        self.ok_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Membaca file config.conf
        self.config = configparser.ConfigParser()
        self.config.read("config.conf")

        # Mendapatkan nilai dari bagian [ID] dalam file config.conf
        self.id_values = list(self.config["ID"].values())

        # Dropdown button untuk ID
        self.id_dropdown = tk.StringVar(master)
        self.id_dropdown.set(self.id_values[0])  # Mengatur nilai default
        self.id_dropdown_menu = tk.OptionMenu(master, self.id_dropdown, *self.id_values)
        self.id_dropdown_menu.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def browse_path(self):
        filename = filedialog.askdirectory()
        if filename:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, filename)

    def on_ok(self):
        selected_path = self.path_entry.get()
        if selected_path:
            print("Selected Path:", selected_path)
            # Memperbarui nilai PATH dalam file config.conf
            self.config["USER"]["path"] = selected_path
            # Menyimpan kembali perubahan ke dalam file config.conf
            with open("config.conf", "w") as configfile:
                self.config.write(configfile)
            print("Path saved to config.conf")
            # Menyembunyikan tampilan UI
            # self.master.withdraw()

# def main():
#     root = tk.Tk()
#     app = PathSelectorApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()
