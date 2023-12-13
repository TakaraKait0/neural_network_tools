import csv
import tkinter
import datetime as dt
from datetime import datetime
import re

    
#クリックイベントの作成
def btn_click():
    inputs = txt_input.get()
    output = txt_output.get()
    stride = txt_stride.get()
    kernel = txt_kernel.get()
    if inputs == '' and output == '' and stride == '' and kernel == '':
        pass
    else:
        padding = ((int(output) - 1) * int(stride) - int(inputs) + int(kernel)) / 2
        txt_padding.insert(0, padding)
        

def btn_click_delete():
    txt_input.delete(0, tkinter.END)
    txt_output.delete(0, tkinter.END)
    txt_stride.delete(0, tkinter.END)
    txt_kernel.delete(0, tkinter.END)
    txt_padding.delete(0, tkinter.END)


#GUIの作成
root = tkinter.Tk()
root.geometry('1800x900')
root.title('畳み込み計算機')
labeltitle = tkinter.Label(text='input "input data size, output data size, stride, kernel"', font=("Times", 30))
labeltitle.place(x=200, y=50)
label_input = tkinter.Label(text='input data size', font=("Times", 30))
label_input.place(x=200, y=200)
label_output = tkinter.Label(text='output data size', font=("Times", 30))
label_output.place(x=200, y=250)
label_stride = tkinter.Label(text='stride', font=("Times", 30))
label_stride.place(x=200, y=300)
label_kernel = tkinter.Label(text='kernel', font=("Times", 30))
label_kernel.place(x=200, y=350)
label_padding = tkinter.Label(text='padding', font=("Times", 30))
label_padding.place(x=200, y=400)




txt_input = tkinter.Entry(width=15,  font=("Times", 30))
txt_input.place(x=500, y=200)
txt_output = tkinter.Entry(width=15,  font=("Times", 30))
txt_output.place(x=500, y=250)
txt_stride = tkinter.Entry(width=15,  font=("Times", 30))
txt_stride.place(x=500, y=300)
txt_kernel = tkinter.Entry(width=15,  font=("Times", 30))
txt_kernel.place(x=500, y=350)
txt_padding = tkinter.Entry(width=15,  font=("Times", 30))
txt_padding.place(x=500, y=400)


btn = tkinter.Button(root, text='calculate', command=btn_click, font=("Times", 20), bg="orange", width=10)
btn.place(x=750, y=750)
btn2 = tkinter.Button(root, text='reset', command=btn_click_delete, font=("Times", 20), bg="orange", width=10)
btn2.place(x=950, y=750)
        
root.mainloop()
