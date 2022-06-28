import tkinter
import customtkinter
from PIL import Image, ImageTk
import os

from matplotlib import projections

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))

class ExampleApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x450")
        self.title("Dell Intern Connect")

        # image = Image.open(PATH + "/images/bg_gradient.jpeg").resize((800, 450))
        # self.bg_image = ImageTk.PhotoImage(image)

        # self.image_label = tkinter.Label(master=self, image=self.bg_image)
        # self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


        self.username = customtkinter.CTkEntry(self,
                               corner_radius=6,
                               width=200,
                               placeholder_text="username")
        self.username.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.password = customtkinter.CTkEntry(self,
                               corner_radius=6,
                               width=200,
                               show="*",
                               placeholder_text="password")
        self.password.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        
        self.signin = customtkinter.CTkButton(self, text="sign in", command=self.view_dashboard)
        self.signin.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        self.createacct = customtkinter.CTkButton(self, text="create an account", command=self.create_account)
        self.createacct.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    # TODO: Create survey page for intern entry point into web app
    def create_account(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("800x450")

        label = customtkinter.CTkLabel(window, text="Create an Account")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)
    
    def view_dashboard(self):
        dashboard_window = customtkinter.CTkToplevel(self)
        dashboard_window.geometry("800x450")
        dashboard_window.title("Discover Interns")
        
        label = customtkinter.CTkLabel(dashboard_window, text="discover interns")
        label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        projects = customtkinter.CTkButton(dashboard_window,
                                 width=200,
                                 corner_radius=6,
                                 text="search by projects",
                                 command=self.project_search)
        projects.place(relx=0.35, rely=0.5, anchor=tkinter.CENTER)

        filters = customtkinter.CTkButton(dashboard_window, 
                                 width=200,
                                 corner_radius=6,
                                 text="search by filter",
                                 command=self.filter_search)
        filters.place(relx=0.65, rely=0.5, anchor=tkinter.CENTER)


    def project_search(self):
        project_window = customtkinter.CTkToplevel(self)
        project_window.geometry("800x450")
        project_window.title("Discover Interns by Projects")


    def filter_search(self):
        filter_window = customtkinter.CTkToplevel(self)
        filter_window.geometry("800x450")
        filter_window.title("Discover Interns by Filter")
        
        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(filter_window,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(filter_window)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(self.frame_left, 
                                              text="Filters"
                                             )
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton()
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton()
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="CTkButton",
                                                command=self.button_event)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="CTkLabel: Lorem ipsum dolor sit,\n" +
                                                        "amet consetetur sadipscing elitr,\n" +
                                                        "sed diam nonumy eirmod tempor" ,
                                                   height=100,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)


app = ExampleApp()
app.mainloop()