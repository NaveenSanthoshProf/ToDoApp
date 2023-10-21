import customtkinter
import tkinter
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class ApplicationUI(customtkinter.CTk):
    def __init__(self,sqlCon):
        super().__init__()

        self.geometry ("1000X2000")
        self.title("To-Do Application")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=4)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=75, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Daily Tasks" , command=lambda: self.dailytask())
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Work ToDo" , command=lambda: self.WorkTodo())
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Week Planner" , command=lambda: self.weeklyplan())
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Habit Tracker" , command=lambda: self.habittrack())
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Side Hustle" , command=lambda: self.sidehustle())
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
        self.dailytask_frame = customtkinter.CTkFrame(self, width=700, corner_radius=0)
        self.dailytask_frame.grid(row=0, column=1, rowspan=4, columnspan = 3 ,padx=(10, 0), sticky="nsew")
        self.dailytask_frame.grid_rowconfigure(4, weight=1)
        self.entry = customtkinter.CTkEntry(self.dailytask_frame, placeholder_text="Add Task", width=500)
        self.entry.grid(row=1, column=2, columnspan=4, padx=(20, 0),pady=(20, 20), sticky="nsew")
        self.main_button_1 = customtkinter.CTkButton(master=self.dailytask_frame,text="Add", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=1, column=7, padx=(20, 20), pady=(20, 20), sticky="nsew")
        try:
            self.journal_frame.destroy()
            self.WorkTodo_frame.destroy()
            self.weeklyplan_frame.destroy()
            self.habittrack_frame.destroy()
            self.sidehustle_frame.destroy()
        except:
            print("Log?")

    def journal(self):
        self.journal_frame = customtkinter.CTkFrame(self, width=700, corner_radius=0)
        self.journal_frame.grid(row=0, column=1, rowspan=4, columnspan = 3 ,padx=(10, 0), sticky="nsew")
        self.journal_frame.grid_rowconfigure(4, weight=1)
        self.textbox = customtkinter.CTkTextbox(self.journal_frame, width=750, height=750)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        try:
            self.dailytask_frame.destroy()
            self.WorkTodo_frame.destroy()
            self.weeklyplan_frame.destroy()
            self.habittrack_frame.destroy()
            self.sidehustle_frame.destroy()
        except:
            print("Log?")
    
    def WorkTodo(self):
        self.WorkTodo_frame = customtkinter.CTkFrame(self, width=700, corner_radius=0)
        self.WorkTodo_frame.grid(row=0, column=1, rowspan=4, columnspan = 3 ,padx=(10, 0), sticky="nsew")
        self.WorkTodo_frame.grid_rowconfigure(4, weight=1)
        try:
            self.journal_frame.destroy()
            self.dailytask_frame.destroy()
            self.weeklyplan_frame.destroy()
            self.habittrack_frame.destroy()
            self.sidehustle_frame.destroy()
        except:
            print("Log?")        

    def weeklyplan(self):
        self.weeklyplan_frame = customtkinter.CTkFrame(self, width=700, corner_radius=0)
        self.weeklyplan_frame.grid(row=0, column=1, rowspan=4, columnspan = 3 ,padx=(10, 0), sticky="nsew")
        self.weeklyplan_frame.grid_rowconfigure(4, weight=1)
        try:
            self.journal_frame.destroy()
            self.dailytask_frame.destroy()
            self.WorkTodo_frame.destroy()
            self.habittrack_frame.destroy()
            self.sidehustle_frame.destroy()
        except:
            print("Log?")        

    def habittrack(self):
        self.habittrack_frame = customtkinter.CTkFrame(self, width=700, corner_radius=0)
        self.habittrack_frame.grid(row=0, column=1, rowspan=4, columnspan = 3 ,padx=(10, 0), sticky="nsew")
        self.habittrack_frame.grid_rowconfigure(100, weight=1)
        habits = ["habit a", "habit b", "habit c", "habit d", "habit a", "habit b", "habit c", "habit d" ,"habit a", "habit b", "habit c", "habit d" ]
        for i in range(len(habits)) :
            self.habit_label = customtkinter.CTkLabel(self.habittrack_frame, text=habits[i], font=customtkinter.CTkFont(size=20, weight="bold"))
            self.habit_label.grid(row=i, column=0, pady=(10, 10))
            self.progressbar_1 = customtkinter.CTkProgressBar(self.habittrack_frame)
            self.progressbar_1.grid(row=i, column=2, padx=(20, 10), pady=(10, 10), sticky="nsew")
            self.habit_label = customtkinter.CTkLabel(self.habittrack_frame, text="num/100", font=customtkinter.CTkFont(size=7))
            self.habit_label.grid(row=i, column=3, pady=(10, 10))
            #self.progressbar_1.set(0.2)
        
        #self.progressbar_2 = customtkinter.CTkProgressBar(self.habittrack_frame)
        #self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        try:
            self.journal_frame.destroy()
            self.dailytask_frame.destroy()
            self.WorkTodo_frame.destroy()
            self.weeklyplan_frame.destroy()
            self.sidehustle_frame.destroy()
        except:
            print("Log?")        

    def sidehustle(self):
        self.sidehustle_frame = customtkinter.CTkFrame(self, width=700, corner_radius=0)
        self.sidehustle_frame.grid(row=0, column=1, rowspan=4, columnspan = 3 ,padx=(10, 0), sticky="nsew")
        self.sidehustle_frame.grid_rowconfigure(4, weight=1)
        try:
            self.journal_frame.destroy()
            self.dailytask_frame.destroy()
            self.WorkTodo_frame.destroy()
            self.weeklyplan_frame.destroy()
            self.habittrack_frame.destroy()
        except:
            print("Log?")        
        
