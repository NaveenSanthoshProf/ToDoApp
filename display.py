import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class ApplicationUI(customtkinter.CTk):
    def __init__(self,sqlCon):
        super().__init__()

        self.geometry ("1000X2000")
        self.title("To-Do Application")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=75, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Daily Tasks" , command=lambda: self.dailytask())
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Deloitte ToDo" , command=lambda: self.buttonFn(sqlCon))
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Week Planner" , command=lambda: self.buttonFn(sqlCon))
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Habit Tracker" , command=lambda: self.buttonFn(sqlCon))
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Side Hustle" , command=lambda: self.buttonFn(sqlCon))
        self.sidebar_button_3.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Journal " , command=lambda: self.journal())
        self.sidebar_button_3.grid(row=5, column=0, padx=20, pady=10)

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

       
        


        #self.button = customtkinter.CTkButton(master = self, text ="Button",  command=lambda: self.buttonFn(sqlCon) )
        #self.button.place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER) 
        #self.button_Data = customtkinter.CTkButton(master = self, text ="Seedata",  command=lambda: self.fetchdata(sqlCon) )
        #self.button_Data.place(relx=0.8,rely=0.8,anchor=customtkinter.CENTER) 
        self.mainloop()

    def buttonFn (self,sqlCon):
        print("Button clicked")

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        
    def dailytask(self):
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Add Task")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(master=self,text="Add", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.textbox.destroy()

    def journal(self):
        self.entry.destroy()
        self.main_button_1.destroy()
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
