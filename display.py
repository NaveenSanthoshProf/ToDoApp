import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class ApplicationUI(customtkinter.CTk):
    def __init__(self,sqlCon):
        super().__init__()

        self.geometry ("600x400")
        self.title("To-Do Application")
        self.button = customtkinter.CTkButton(master = self, text ="Button",  command=lambda: self.buttonFn(sqlCon) )
        self.button.place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER) 
        self.button_Data = customtkinter.CTkButton(master = self, text ="Seedata",  command=lambda: self.fetchdata(sqlCon) )
        self.button_Data.place(relx=0.8,rely=0.8,anchor=customtkinter.CENTER) 
        self.mainloop()

    def buttonFn (self,sqlCon):
        print("Button clicked")
        cursor = sqlCon.cursor()
        habit_name = "firstentry"
        insert = f"INSERT INTO Habit (habitname) VALUES ('{habit_name}');"
        cursor.execute(insert) 
        print("updated sql")
  
    def fetchdata(self,sqlCon):
        cursor = sqlCon.cursor()
        read = "SELECT * FROM Habit"
        cursor.execute(read)
        updatedRow = cursor.fetchall()
        for column in updatedRow:
            print(column)      
