import time
import tkinter
from tkinter import ttk

import db

global top
top = tkinter.Tk()

global label1text
tab1_label2text = tkinter.StringVar()

global tabControl
tabControl = ttk.Notebook(top)

global tab1
tab1 = ttk.Frame(tabControl)

global tab2
tab2 = ttk.Frame(tabControl)

global tab1_tree
tab1_tree = ttk.Treeview(tab1, show='headings')


def gui_set():

    top.title('设备节点后台系统')
    # top.iconbitmap('img/kklyz.ico')
    top.iconphoto(False, tkinter.PhotoImage(file='img/kklyz.png'))
    top.geometry('640x380')

    # 标签
    tabControl.add(tab1, text='数据统计')
    tabControl.add(tab2, text='数据库显示')
    tabControl.pack(expand=1, fill='both')

    # 表格
    tab1_tree['columns'] = ('UUID', '位置', '电源状态', '电压', '电流', '有功功率', '有功电能',
                            '功率因数')
    tab1_tree.column('UUID', width=50, anchor='center')
    tab1_tree.column('位置', width=50, anchor='center')
    tab1_tree.column('电源状态', width=80, anchor='center')
    tab1_tree.column('电压', width=80, anchor='center')
    tab1_tree.column('电流', width=80, anchor='center')
    tab1_tree.column('有功功率', width=80, anchor='center')
    tab1_tree.column('有功电能', width=80, anchor='center')
    tab1_tree.column('功率因数', width=80, anchor='center')
    tab1_tree.heading('UUID', text='UUID')
    tab1_tree.heading('位置', text='位置')
    tab1_tree.heading('电源状态', text='电源状态')
    tab1_tree.heading('电压', text='电压')
    tab1_tree.heading('电流', text='电流')
    tab1_tree.heading('有功功率', text='有功功率')
    tab1_tree.heading('有功电能', text='有功电能')
    tab1_tree.heading('功率因数', text='功率因数')
    tab1_tree.pack(side='left', fill='both')

    # 标签1
    # tab1_label1 = ttk.Label(tab1,
    #                         text='UUID\t位置\t电源状态\t电压\t电流\t有功功率\t有功电能\t功率因数')
    # tab1_label1.grid(column=0, row=0, sticky='W')
    # tab1_label2 = ttk.Label(tab1, text='null', textvariable=tab1_label2text)
    # tab1_label2.grid(column=0, row=1, sticky='W')

    top.mainloop()


def tick_s():
    count = 0
    while True:
        count = count + 1
        tab1_label2text.set(str(count))
        print(count)
        time.sleep(1)


def gui_event():
    while True:
        dat = db.select_all()
        # print(dat)
        for i in (tab1_tree.get_children()):
            tab1_tree.delete(i)
        for i in range(len(dat)):
            tab1_tree.insert("", i, values=(dat[i]['uuid'], dat[i]['local'], dat[i]['state'], dat[i]['vlotage'], dat[i]['current'], dat[i]['apower'], dat[i]['aelectricity'], dat[i]['powerfactor']))
        time.sleep(1)


# def gui_start():
#     print('gui start!')

# gui_set()
