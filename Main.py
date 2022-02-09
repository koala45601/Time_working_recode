from tkinter import *
from command import *

#operator
main_windows = Tk()
frame_main = LabelFrame(main_windows)
frame_main.pack(padx=5, pady=5,fill='both',expand=True)

header = LabelFrame(frame_main)
center = LabelFrame(frame_main)

header.pack(padx=5, pady=5,fill='both',expand=False)
center.pack(padx=5, pady=5,fill='both',expand=True)

#popup
def pop_1():
    #Create a Toplevel window
    top= Toplevel(main_windows)
    top.geometry("150x95")
    top.title("Inuput User")

    L_name = Label(top,text='Input Account Name').pack(padx=5, pady=5)
    text_user = Entry(top,bg='blue')
    
    btn_save = Button(top,text='Submit',command=top.destroy)
    btn_save.pack(padx=5, pady=5,side='bottom')
    text_user.pack(padx=5, pady=5,side='bottom')
    
    if btn_save == btn_save:
        pass
        

#manu bar
start_time = Button(header, text = 'START TIME',command='',height=5,width=20)
break_time = Button(header, text = 'BREAK TIME',command='',height=5,width=20)
end_time = Button(header, text = 'END TIME',command='',height=5,width=20)
input_user = Button(header, text = 'Input - User',command=pop_1,height=5,width=20)

#All Pack header
start_time.pack(padx=5, pady=5,side='left')
break_time.pack(padx=5, pady=5,side='left')
end_time.pack(padx=5, pady=5,side='left')
input_user.pack(padx=5, pady=5,side='left')

#Label
h_acct = Label(header,text='Account :',font=('Arial',35))
h_inputacct = Label(header,text='54845',font=('Arial',35))

#Pack
h_inputacct.pack(padx=5, pady=5,side='right')
h_acct.pack(padx=5, pady=5,side='right')


Time_cen = Label(center,text='00:00:00',font=('Arial',200))
#Time_cen.config(text=command_1.test(1))

Time_cen.pack(padx=5, pady=5,)

main_windows.title('Time Working Record')
main_windows.geometry('1100x300')
main_windows.mainloop()