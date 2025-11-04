import tkinter as tk
import tkinter.font as font

def click(button_text):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + button_text)
def clear():
    display.delete(0, tk.END)
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
root = tk.Tk()
root.title("Calculator")
bold_font = font.Font(weight="bold", size=14)
display = tk.Entry(root, width=35, borderwidth=10, font=("Arial", 24))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = [('7',1,0),('8',1,1),('9',1,2),('/',1,3),('4',2,0),('5',2,1),('6',2,2),('*',2,3),
           ('1',3,0),('2',3,1),('3',3,2),('-',3,3),('0',4,0),('.',4,1),('C',4,2),('+',4,3),
           ('=',5,0,4)]
for (text, row, col, cs) in [(b[0], b[1], b[2], 1) if len(b)==3 else b for b in buttons]:
    if text == 'C':
        action = clear
    elif text == '=':
        action = calculate
    else:
        action = lambda x=text: click(x)
    if text in ['+', '-', '*', '/']:
        bg_color = 'crimson'
        fg_color = 'white'
    elif text == '=':
        bg_color = 'seagreen'
        fg_color = 'white'
    else:
        bg_color = 'steelblue'
        fg_color = 'white'
    button = tk.Button(root, text=text, width=13 if cs==1 else 38, height=3,command=action, bg=bg_color, fg=fg_color, font=bold_font)
    button.grid(row=row, column=col, columnspan=cs)
root.mainloop()
