import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import tkinter.font as font


def binary_fraction(num ,n):
    binary =[]
    temporary_num = num
    while num != 1.0 and n != 0:
        num = num * 2
        output2.insert("insert",f" {temporary_num} * 2 ={num}\n")

        if num == 1.0:
            binary.append(1)
            output2.insert("end", "take 1 and finish:\n")
            output2.insert("end",binary)
            output2.insert("end","\n")
            return binary

        if num  < 1:
            binary.append(0)
            if n-1 == 0:
                output2.insert('insert','Done we got to your precision\n')
                return binary
            output2.insert("insert", f"Take 0 then multiply ({num}) with 2\n")
            n -= 1
            temporary_num = num

        if num  > 1:
            binary.append(1)
            num = str(num)
            num = float("." + num.split(".")[1])
            temporary_num = num
            if n-1 == 0:
                output2.insert('insert','Done we got to your precision\n')
                return binary
            output2.insert("insert",f"Take 1 then multiply fraction({num}) part with 2\n")
            n -= 1


    return binary

def Integral_part(number):
    binary = []
    if number == 0:
        binary.append(0)
        output2.insert("end", binary)
        output2.insert("insert", "\n")
        output2.insert("insert", "================\n")
        return binary

    while number != 0:
        rem = int(number % 2)
        output2.insert("insert",f"{int(number)}/2 =>")
        output2.insert("insert",f"remainder:{rem}")
        output2.insert("insert", "\n")
        binary.append(rem)
        Quotient = number // 2
        output2.insert("insert", f"Quotient:{int(Quotient)}\n")
        number = Quotient

        if Quotient == 0:
            output2.insert("end", "now just writing remainder from bottom to top\n")
            binary.reverse()
            output2.insert("end", binary)
            output2.insert("insert", "\n")
            output2.insert("insert", "================\n")

            return binary

    output1.insert("end", binary)

def add_one(li):
    if li[-1] == 0:
        li[-1] = 1
        return li
    else:
        li[-1] = 0
        for i in range(2, len(li)+1):
            if li[-i] == 1:
                li[-i] = 0

            else:
                li[-i] = 1
                return li
        return [1] + li

def not_list(n):
    for i in range(0,len(n)):
        if n[i] == 0:
            n[i] = 1
        else:
            n[i] = 0
    return n




def main():
    #get user input
    number = entry1.get()
    n = entry2.get()
    try:
        number = float(number)
        # Show a message box if the users input was invalid
    except:
        clear_field()
        messagebox.askretrycancel('Error', " Invalid Input,just numbers!")


    #this is where the user input is integer
    if number - int(number) == 0.0 and number > 0 :
        binary = Integral_part(number)
        output1.insert("insert",binary)

    if number == 0:
        binary = Integral_part(number)
        output1.insert("insert", binary)

    #this is where the input is not integer
    if number - int(number) != 0.0 :

        if n != "":
            try:
                n = int(n)
            except:
                messagebox.askretrycancel('Error', " Invalid Input,just numbers!")
                return
        else:
            #default precision
            n = 10
        fpart = int(number)
        output2.insert("insert" , f"         < Integral part = {fpart}>\n ")
        string_num = str(number)
        separt = float("." + string_num.split(".")[1])
        #binary of first part
        f_part = Integral_part(fpart)
        output2.insert("insert", f"          <Fraction part = {separt}>\n")
        #binary of second part
        se_part = binary_fraction(separt,n)
        binary = f_part +["."] + se_part
        output2.insert("end" , f"Now concatinate {f_part} + {se_part} =\n")
        output2.insert("insert", binary)
        output1.insert("insert", binary)

    if number < 0.0 :
        output2.insert("insert",f"First calculate Binary of {-(int(number))} : \n")
        binary_num = Integral_part(-number)
        output2.insert("end", f"\nComplement_1 for {binary_num} ==>")
        complement = not_list(binary_num)
        output2.insert("end", complement)
        output2.insert("end",f"\n\ncomplement 2 = complement_1 + 1 ==>")
        result = add_one(complement)
        output2.insert("end",result)
        result = [1] + result
        output2.insert("end","\nresult:")
        output2.insert("end", "\n")
        output2.insert("end",result)

        output1.insert("end", result)




#Functions to exit the program
def exit_program():
    root.destroy()

#Function to clear_fields
def clear_field():
    entry1.delete(0,"end")
    entry2.delete(0, "end")
    output2.delete(1.0,"end")
    output1.delete(1.0, "end")


root = tk.Tk()
root.geometry("1200x500")
root.title("Decimal to Binary Converter")
#root.resizable(False, False)



frame = tk.Frame(root)
frame.pack(fill='none' ,side='top')


output1_frame = tk.Frame(root)
output1_frame.pack(side = 'left')



main_frame = tk.Frame(root)
main_frame.pack(fill='both' , expand=1,side='right')

my_canvas = tk.Canvas(main_frame)
my_canvas.pack(side='right',fill='both', expand = 1)
second_frame = tk.Frame(my_canvas)

#button frame
button_frame =tk.Frame(root)
button_frame.pack(side='bottom')



label1 = tk.Label(frame,text = "Type a number you want to convert :")
label1.pack(side='top',expand=1)

#entry field
entry1 = tk.Entry(frame)
entry1.pack(side='top',expand=1)
#entry label
label_entry2 = tk.Label(frame , text ="If it's float ,type a precision for floating point(default=10):")
label_entry2.pack(side='top')
#entry field
entry2 = tk.Entry(frame)
entry2.pack(side= 'top')

myfont = font.Font(family='couriel',size='10',weight='bold')

#button convert
button_convert = tk.Button(frame,text="Convert",command=main,bg='black',fg='white')
button_convert.pack(side='bottom')
button_convert['font'] = myfont


#exit and clear button
btn_exit = tk.Button(button_frame,text = "Exit" , command=exit_program,bg='black',fg='red')
btn_exit.pack(side='right',fill='none')
btn_exit['font'] = myfont
btn_clear = tk.Button(button_frame,text="Clear" ,command = clear_field,bg='black',fg='red')
btn_clear['font'] = myfont
btn_clear.pack(side='right',fill='none')

#result label
label2 = tk.Label(output1_frame , text ="Result=>  ")
label2.pack(side='left')

#result field
output1 = tk.Text(output1_frame,width = 50, height = 100)
output1.pack(side='right',expand=1,fill='both')





#procedure field
label3 = tk.Label(main_frame , text ="Procedures ==>")
label3.pack(side='left',expand=1)
my_canvas.create_window((0,0), window=second_frame,anchor="nw")
output2 = tk.Text(second_frame , width = 50 , height = 100)
output2.pack(fill='both',expand=1,side='right')
scrollb = ttk.Scrollbar(main_frame, orient='vertical',command = my_canvas.yview)
output2.configure(yscrollcommand =scrollb.set)
scrollb.pack(side='right',fill='y')
scrollb1 = ttk.Scrollbar(main_frame, orient='horizontal',command = my_canvas.xview)
scrollb1.pack(side='bottom',fill='y')

my_canvas.configure(yscrollcommand=scrollb.set)
my_canvas.configure(xscrollcommand=scrollb1.set)
output2.bind('<Configure>',lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))




root.mainloop()
