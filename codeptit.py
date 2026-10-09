import customtkinter as ctk

app = ctk.CTk()
app.title("Kiểm tra Custom")
app.geometry("300x150")

label = ctk.CTkLabel(app, text="Cài đặt thành công!", font=("Arial", 16))
label.pack(pady=40)

app.mainloop()
