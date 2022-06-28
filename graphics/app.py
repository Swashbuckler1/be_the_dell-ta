import tkinter
import customtkinter
from PIL import Image, ImageTk
import os

from matplotlib import projections
from filtering_data import *

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
        label = customtkinter.CTkLabel(project_window, text="Discover Interns by Business Unit")
        label.place(relx=0.5, rely=0.06, anchor=tkinter.CENTER)

        csg = customtkinter.CTkButton(project_window,
                                      width=200,
                                      height=100,
                                      corner_radius=6,
                                      text="CSG",
                                      command=self.project_search, )
        csg.place(relx=0.35, rely=0.25, anchor=tkinter.CENTER)

        isg = customtkinter.CTkButton(project_window,
                                      width=200,
                                      height=100,
                                      corner_radius=6,
                                      text="ISG",
                                      command=self.isg_search, )
        isg.place(relx=0.65, rely=0.25, anchor=tkinter.CENTER)

        cto = customtkinter.CTkButton(project_window,
                                      width=200,
                                      height=100,
                                      corner_radius=6,
                                      text="CTO",
                                      command=self.project_search, )
        cto.place(relx=0.35, rely=0.5, anchor=tkinter.CENTER)

        cso = customtkinter.CTkButton(project_window,
                                      width=200,
                                      height=100,
                                      corner_radius=6,
                                      text="CSO",
                                      command=self.project_search, )
        cso.place(relx=0.65, rely=0.5, anchor=tkinter.CENTER)

        go = customtkinter.CTkButton(project_window,
                                     width=200,
                                     height=100,
                                     corner_radius=6,
                                     text="GO",
                                     command=self.project_search, )
        go.place(relx=0.35, rely=0.75, anchor=tkinter.CENTER)

        telecom = customtkinter.CTkButton(project_window,
                                          width=200,
                                          height=100,
                                          corner_radius=6,
                                          text="TELECOM",
                                          command=self.project_search, )
        telecom.place(relx=0.65, rely=0.75, anchor=tkinter.CENTER)

    def isg_search(self):
        isg_search = customtkinter.CTkToplevel(self)
        isg_search.geometry("800x450")
        isg_search.title("Discover Interns by Business Unit: ISG")

        label = customtkinter.CTkLabel(isg_search, text="Discover Interns by Business Unit: ISG")
        label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

        proj1 = customtkinter.CTkButton(isg_search,
                                        width=300,
                                        height=50,
                                        corner_radius=6,
                                        text="Data Management",
                                        command=self.data_mang, )
        proj1.pack()

        proj2 = customtkinter.CTkButton(isg_search,
                                        width=300,
                                        height=50,
                                        corner_radius=6,
                                        text="Sonic Partner Ecosystem Framework", )

        proj3 = customtkinter.CTkButton(isg_search,
                                        width=300,
                                        height=50,
                                        corner_radius=6,
                                        text="Process Optimization \n Customer requirements", )
        proj4 = customtkinter.CTkButton(isg_search,
                                        width=300,
                                        height=50,
                                        corner_radius=6,
                                        text="NextGen Infrastructure Engineering", )
        proj5 = customtkinter.CTkButton(isg_search,
                                        width=300,
                                        height=50,
                                        corner_radius=6,
                                        text="Incubation Engineering", )
        proj6 = customtkinter.CTkButton(isg_search,
                                        width=300,
                                        height=50,
                                        corner_radius=6,
                                        text="Acceleration Engineering", )

        proj7 = customtkinter.CTkButton(isg_search,
                                        width=300,
                                        height=50,
                                        corner_radius=6,
                                        text="Acceleration Engineering", )
        proj8 = customtkinter.CTkButton(isg_search,
                                        width=300,
                                        height=50,
                                        corner_radius=6,
                                        text="Acceleration Engineering", )
        proj9 = customtkinter.CTkButton(isg_search,
                                        width=300,
                                        height=50,
                                        corner_radius=6,
                                        text="Acceleration Engineering", )
        proj10 = customtkinter.CTkButton(isg_search,
                                         width=300,
                                         height=50,
                                         corner_radius=6,
                                         text="Acceleration Engineering", )
        proj11 = customtkinter.CTkButton(isg_search,
                                         width=300,
                                         height=50,
                                         corner_radius=6,
                                         text="Acceleration Engineering", )
        proj12 = customtkinter.CTkButton(isg_search,
                                         width=300,
                                         height=50,
                                         corner_radius=6,
                                         text="Acceleration Engineering", )
        proj13 = customtkinter.CTkButton(isg_search,
                                         width=300,
                                         height=50,
                                         corner_radius=6,
                                         text="Acceleration Engineering", )

        proj1.place(relx=0.3, rely=0.15, anchor=tkinter.CENTER)
        proj2.place(relx=0.3, rely=0.30, anchor=tkinter.CENTER)
        proj3.place(relx=0.3, rely=0.45, anchor=tkinter.CENTER)
        proj4.place(relx=0.3, rely=0.60, anchor=tkinter.CENTER)
        proj5.place(relx=0.3, rely=0.75, anchor=tkinter.CENTER)
        proj6.place(relx=0.3, rely=0.90, anchor=tkinter.CENTER)

        proj7.place(relx=0.72, rely=0.15, anchor=tkinter.CENTER)
        proj8.place(relx=0.72, rely=0.30, anchor=tkinter.CENTER)
        proj9.place(relx=0.72, rely=0.45, anchor=tkinter.CENTER)
        proj10.place(relx=0.72, rely=0.60, anchor=tkinter.CENTER)
        proj11.place(relx=0.72, rely=0.75, anchor=tkinter.CENTER)
        proj12.place(relx=0.72, rely=0.90, anchor=tkinter.CENTER)

    def data_mang(self):
        data_mang = customtkinter.CTkToplevel(self)
        data_mang.geometry("800x450")
        data_mang.title("Discover Interns by Business Unit: ISG")

        label = customtkinter.CTkLabel(data_mang, text="Data Management")
        label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

        back = customtkinter.CTkButton(data_mang,
                                       width=30,
                                       corner_radius=6,
                                       text="<—",
                                       command=data_mang.destroy, )
        back.place(relx=0, anchor="nw")

        proj_desc = customtkinter.CTkLabel(data_mang,
                                           height=20,
                                           width=30,
                                           bg="#616161",
                                           text="Project Description")
        proj_desc.place(relx=0.2, rely=0.2, anchor="n")

    def filter_search(self):
        filter_window = customtkinter.CTkToplevel(self)
        filter_window.geometry("800x450")
        filter_window.title("Discover Interns by Filter")

        # ============ create two frames ============

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(filter_window,
                                                 width=250,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(filter_window)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

        # ============ frame_left ============

        # configure grid layout (1x11)
        for i in range(30):
            self.frame_left.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.frame_left.grid_columnconfigure(i, weight=1)

        # add labels, buttons, and other components for filtration

        self.label_2 = customtkinter.CTkLabel(self.frame_left,
                                              text="gender")
        self.label_2.grid(row=1, column=0, columnspan=2, sticky="ew")

        female = customtkinter.CTkCheckBox(master=self.frame_left, text="female")
        female.grid(row=3, column=1, padx=10)

        male = customtkinter.CTkCheckBox(master=self.frame_left, text="male")
        male.grid(row=3, column=0, padx=10)

        self.label_3 = customtkinter.CTkLabel(self.frame_left,
                                              text="university")
        self.label_3.grid(row=5, column=0, columnspan=2, sticky="ew")

        university = customtkinter.CTkComboBox(self.frame_left,
                                               values=universities)
        university.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.label_4 = customtkinter.CTkLabel(self.frame_left,
                                              text="degree")
        self.label_4.grid(row=9, column=0)

        self.label_5 = customtkinter.CTkLabel(self.frame_left,
                                              text="year")
        self.label_5.grid(row=9, column=1)

        for i in range(len(years)):  # 11 + 2 + 2 + 2 = 17
            obj = customtkinter.CTkCheckBox(master=self.frame_left, text=years[i])
            obj.grid(row=11 + 2 * i, column=1, pady=2, padx=10, sticky="w")

        for i in range(len(degrees)):
            obj = customtkinter.CTkCheckBox(master=self.frame_left, text=degrees[i])
            obj.grid(row=11 + 2 * i, column=0, pady=2, padx=10, sticky="w")

        self.label_8 = customtkinter.CTkLabel(self.frame_left,
                                              text="major")
        self.label_8.grid(row=19, column=0, columnspan=3, sticky="ew")

        major = customtkinter.CTkComboBox(self.frame_left, values=majors)
        major.grid(row=21, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.label_7 = customtkinter.CTkLabel(self.frame_left,
                                              text="business unit")
        self.label_7.grid(row=23, column=0, pady=10, sticky="e")

        businessunits = customtkinter.CTkOptionMenu(self.frame_left,
                                                    values=business_units)
        businessunits.grid(row=23, column=1, padx=10, pady=10, sticky="w")

        self.label_6 = customtkinter.CTkLabel(self.frame_left,
                                              text="returning intern?")
        self.label_6.grid(row=25, column=0, pady=10, sticky="e")

        yes_no = customtkinter.CTkOptionMenu(self.frame_left,
                                             values=["yes", "no"])
        yes_no.grid(row=25, column=1, padx=10, pady=10)

        self.search = customtkinter.CTkButton(self.frame_left, text="search", command=self.onclick_search)
        self.search.grid(row=26, column=0, columnspan=2, padx=75, sticky="ew")

    def onclick_search(self):
        self.frame_right.columnconfigure(0, weight=1)
        self.frame_right.columnconfigure(1, weight=5)
        textarray = [
            "Anisha Mukherjee\nBachelor's at Rice University, Computer Science '25\nPart of ISG, working with PowerFlex and the cloud\nInterested in dance and calligraphy",
            "Camila Kahneman\nBachelor's at Rice University, Computer Science '25\nPart of ISG, working with API integration with customers\nInterested in football",
            "Christy Lefteri\nBachelor's at Rice University, Computer Science '25\nPart of ISG, working with ML and server storage\nInterested in crocheting and hockey"]
        for i in range(3):
            self.frame_right.rowconfigure(i, weight=1)
            curr = customtkinter.CTkLabel(self.frame_right,
                                          text=textarray[i],
                                          height=100,
                                          fg_color=("white", "gray38"),  # <- custom tuple-color
                                          justify=tkinter.LEFT)
            curr.grid(column=1, row=i, sticky="nwe", padx=5, pady=10)
            image = Image.open(PATH + "/images/bg_gradient.jpeg").resize((75, 75))
            img = ImageTk.PhotoImage(image)
            label = tkinter.Label(master=self.frame_right, image=img)
            label.grid(row=i, column=0, padx=5, pady=10, sticky="ew")


app = ExampleApp()
app.mainloop()