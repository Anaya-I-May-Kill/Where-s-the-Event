import tkinter as tk

def inch_to_cm():
    
    inch = int(ent_length.get())
    cm = (inch * 2.54)
    lbl_result["text"] = f"{round(cm , 2)} cm"
    
window = tk.Tk()
window.title("Length Converter")
window.resizable(width = False , height = False)

frm_entry = tk.Frame(master = window)
ent_length = tk.Entry(master = frm_entry , width = 10)

lbl_inch = tk.Label(master = frm_entry , text = "inch")

ent_length.grid(row = 0 , column = 0 , sticky = "e")
lbl_inch.grid(row = 0 , column = 1 , sticky = "w")


btn_convert = tk.Button(master = window , text = "-->" , command = inch_to_cm)
lbl_result = tk.Label(master = window , text = "cm")

frm_entry.grid(row = 0 , column = 0 , padx = 10)
btn_convert.grid(row = 0 , column = 1 , pady = 10)
lbl_result.grid(row = 0 , column = 2 , padx = 10)

window.mainloop()