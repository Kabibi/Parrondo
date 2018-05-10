#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 08, 2018 09:07:07 PM

import sys
import numpy as np
import random
import xlwt
import tkinter.messagebox

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import parrondo_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Parrondo____(root, size=5, init_reward=100, p1=0.8, p2=0.5, n_sampels=12)
    parrondo_support.init(root, top)
    root.mainloop()


w = None


def create_Parrondo____(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Parrondo____(w)
    parrondo_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Parrondo____():
    global w
    w.destroy()
    w = None


class Parrondo____:
    def __init__(self, top=None, size=5, init_reward=100, p1=0.8, p2=0.5, n_sampels=2):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self.p1 = p1
        self.p2 = p2
        self.points = np.array(range(size ** 2)).reshape((size, size))
        self.rewards = np.array([init_reward] * (size ** 2))
        self.size = size
        self.n_samples = n_sampels
        self.num = -1  # 随机选择的点
        self.neighbors = []
        # fine neighbors
        for i in range(size):
            for j in range(size):
                neighbors = [self.points[i - 1, j],
                             self.points[(i + 1) % size, j],
                             self.points[i, j - 1],
                             self.points[i, (j + 1) % size]]
                self.neighbors.append(list(set(neighbors)))

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'

        top.geometry("960x772+296+115")
        top.title("Parrondo游戏系统")
        top.configure(highlightcolor="black")

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.63, rely=-0.41, relheight=1.12, relwidth=0.36)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(width=345)

        self.Text_log = Text(self.Frame1)
        self.Text_log.place(relx=0.03, rely=0.38, relheight=0.57, relwidth=0.94)
        self.Text_log.configure(background="white")
        self.Text_log.configure(font="TkTextFont")
        self.Text_log.configure(selectbackground="#c4c4c4")
        self.Text_log.configure(width=326)
        self.Text_log.configure(wrap=WORD)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.0, rely=0.0, relheight=0.78, relwidth=0.61)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(width=585)

        self.Canvas1 = Canvas(self.Frame2)
        self.Canvas1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(width=561)

        self.space = 325 / (size + 1)
        self.diameter = 225 / size

        for i in range(size):
            t = (i + 1) * self.space + ((i + 1) * 2 - 1) / 2 * self.diameter
            self.Canvas1.create_line(0, t, 550, t, width='5')
            self.Canvas1.create_line(t, 0, t, 550, width='5')

        for i in range(size ** 2):
            x1 = (i % size + 1) * self.space + (i % size) * self.diameter
            y1 = (i // size + 1) * self.space + (i // size) * self.diameter
            x2 = x1 + self.diameter
            y2 = y1 + self.diameter
            self.Canvas1.create_oval(x1, y1, x2, y2, fill='red')
            self.Canvas1.create_text((x1 + x2) / 2, (y1 + y2) / 2, font="Times " + str(80 // size) + " italic bold",
                                     text=str(i))

        self.Frame3 = Frame(top)
        self.Frame3.place(relx=0.0, rely=0.79, relheight=0.2, relwidth=0.62)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(width=595)

        self.Label1 = Label(self.Frame3)
        self.Label1.place(relx=0.02, rely=0.13, height=28, width=56)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''操作提示:''')
        self.Label1.configure(width=56)

        self.Entry_info = Entry(self.Frame3)
        self.Entry_info.place(relx=0.12, rely=0.1, height=34, relwidth=0.87)
        self.Entry_info.configure(background="white")
        self.Entry_info.configure(font="TkFixedFont")
        self.Entry_info.configure(selectbackground="#c4c4c4")
        self.Entry_info.configure(width=516)

        self.Button_startGame = Button(self.Frame3)
        self.Button_startGame.place(relx=0.42, rely=0.52, height=56, width=114)
        self.Button_startGame.configure(activebackground="#d9d9d9")
        self.Button_startGame.configure(text='''开始游戏''')
        self.Button_startGame.configure(width=114)
        self.Button_startGame.configure(command=self.start_game)

        self.Frame4 = Frame(top)
        self.Frame4.place(relx=0.63, rely=0.71, relheight=0.28, relwidth=0.36)
        self.Frame4.configure(relief=GROOVE)
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief=GROOVE)
        self.Frame4.configure(width=345)

        self.Button_Conn = Button(self.Frame4)
        self.Button_Conn.place(relx=0.61, rely=0.74, height=40, width=122)
        self.Button_Conn.configure(activebackground="#d9d9d9")
        self.Button_Conn.configure(text='''断开连接''')
        global var
        var = IntVar()
        self.Button_Conn.configure(command=lambda: var.set(1))

        self.Text_neighborInfo = Text(self.Frame4)
        self.Text_neighborInfo.place(relx=0.03, rely=0.05, relheight=0.61
                                     , relwidth=0.94)
        self.Text_neighborInfo.configure(background="white")
        self.Text_neighborInfo.configure(font="TkTextFont")
        self.Text_neighborInfo.configure(selectbackground="#c4c4c4")
        self.Text_neighborInfo.configure(width=326)
        self.Text_neighborInfo.configure(wrap=WORD)

        self.Text_startConn = Text(self.Frame4)
        self.Text_startConn.place(relx=0.17, rely=0.74, relheight=0.14
                                  , relwidth=0.19)
        self.Text_startConn.configure(background="white")
        self.Text_startConn.configure(font="TkFixedFont")
        self.Text_startConn.configure(selectbackground="#c4c4c4")
        self.Text_startConn.configure(width=64)

        self.Label2 = Label(self.Frame4)
        self.Label2.place(relx=0.06, rely=0.77, height=18, width=16)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''与''')

        self.Label3 = Label(self.Frame4)
        self.Label3.place(relx=0.39, rely=0.74, height=32, width=59)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''号节点''')
        self.Label3.configure(width=59)

    def start_game(self):
        self.Button_Conn.configure(state=NORMAL)
        # clear
        self.Text_log.delete('1.0', END)
        self.Text_startConn.delete('1.0', END)
        self.Text_neighborInfo.delete('1.0', END)
        self.Button_startGame.configure(state=DISABLED)

        global v
        global neighbors_info
        v = StringVar()  # 提示信息
        neighbors_info = StringVar()
        self.Entry_info.configure(textvariable=v, state='readonly')
        v.set("游戏已经开始!")

        log_file = []

        for i in range(self.n_samples):
            data_i = []  # 存储第i次游戏的数据
            self.show_log("========第" + str(i) + "次========")  # 在窗口显示游戏过程
            data_i.append(i + 1)  # 第i次游戏的数据list

            # 随机选择一个编号
            num = random.randint(0, self.size ** 2 - 1)
            self.num = num
            self.show_log("系统已随机选择编号" + str(num) + "的节点!")
            data_i.append(num)

            neighbors_info.set(self.get_neighbors_info(num))

            # 随机选择进入A环节还是B博弈
            if random.randint(0, 1) == 0:
                self.show_log('系统随机选择进入 A 环节')
                data_i.append('A环节')

                # 画num和其邻居的图
                self.draw(num)

                # 显示邻居信息
                self.Text_neighborInfo.delete('1.0', END)
                self.Text_neighborInfo.insert(END, self.get_neighbors_info(self.num))

                v.set("请在右侧输入框中输入希望断开连接的节点编号, 确认后点击断开连接!")
                ############################################
                ###### 断开连接 #########
                ############################################

                self.Button_Conn.wait_variable(var)  # ##################

                # 选择一个邻居断开连接
                neighbor_cut = self.Text_startConn.get('1.0', END).strip()
                while not str.isdigit(neighbor_cut) or int(neighbor_cut) not in self.neighbors[self.num] or len(
                        self.neighbors[int(neighbor_cut)]) == 1:
                    messagebox.showerror(title='错误', message='邻居输入有误或输入的邻居只有一个邻居, 无法断开该邻居, 请重新输入!')
                    self.Button_Conn.wait_variable(var)
                    neighbor_cut = self.Text_startConn.get('1.0', END).strip()

                neighbor_cut = int(neighbor_cut)

                self.neighbors[self.num].remove(neighbor_cut)
                self.neighbors[neighbor_cut].remove(self.num)
                messagebox.showinfo(title='成功',
                                    message='成功断开节点' + str(self.num) + '与节点' + str(neighbor_cut) + '的邻居关系')
                self.show_log('成功断开节点' + str(self.num) + '与节点' + str(neighbor_cut) + '的邻居关系')
                data_i.append(neighbor_cut)

                # 显示节点的次邻居信息
                neighbors_info.set(self.get_neighbors_info(neighbor_cut))
                self.Text_neighborInfo.delete('1.0', END)
                self.Text_neighborInfo.insert(END, self.get_neighbors_info(neighbor_cut))

                #######################################
                ###  建立连接
                #######################################

                v.set("请在右侧输入框中输入希望建立连接的节点编号, 确认后点击建立连接!")
                # 设置按钮为"断开连接"or"建立连接"
                self.Button_Conn.configure(text='建立连接', bg='yellow')
                # 清空输入框的内容
                self.Text_startConn.delete('1.0', END)

                self.draw(neighbor_cut)

                # 选择一个次邻居建立连接
                self.Button_Conn.wait_variable(var)
                neighbor_connect = self.Text_startConn.get('1.0', END).strip()
                while not str.isdigit(neighbor_connect) or int(neighbor_connect) not in self.neighbors[neighbor_cut]:
                    messagebox.showerror(title='错误', message='邻居输入有误, 无法与该邻居建立连接, 请重新输入!')
                    self.Button_Conn.wait_variable(var)
                    neighbor_connect = self.Text_startConn.get('1.0', END).strip()
                    self.Button_Conn.wait_variable(var)

                neighbor_connect = int(neighbor_connect)

                self.neighbors[self.num].append(neighbor_connect)  # 建立连接
                self.neighbors[neighbor_connect].append(self.num)

                messagebox.showinfo(title='成功',
                                    message='成功建立节点 ' + str(self.num) + ' 与节点 ' + str(neighbor_connect) + '的邻居关系')
                self.show_log('成功建立节点' + str(self.num) + '与节点' + str(neighbor_connect) + '的邻居关系')
                data_i.append(neighbor_connect)

                self.Button_Conn.configure(text='断开连接', bg='yellow')
                self.Text_startConn.delete('1.0', END)

            else:
                # print("----------------------进入 B 博弈---------------------")
                self.show_log('系统随机选择进入 B 博弈')
                data_i.append('B博弈')
                # self.rewards[self.neighbors[num]]
                if self.rewards[num] <= self.rewards[self.neighbors[num]].mean():  # 当被挑选节点的资本"不大于"其所有邻居资本的平均数, 玩分支1
                    sampled_prob = random.uniform(0, 1)
                    self.show_log('进入分支1')
                    data_i.append('分支1')
                    if sampled_prob <= self.p1:  # 分支1赢的概率p1
                        self.rewards[num] += 1
                        self.show_log("采样的概率为 %f, 赢了!" % sampled_prob)
                        data_i.append('赢')

                    else:
                        self.show_log("采样的概率为 %f, 输了!" % sampled_prob)
                        data_i.append('输')


                else:  # 当被挑选节点的资本"大于"其所有邻居资本的平均数, 玩分支2
                    self.show_log('进入分支2')
                    data_i.append('分支2')
                    sampled_prob = random.uniform(0, 1)
                    if sampled_prob <= self.p2:  # 赢的概率是p2
                        self.rewards[num] += 1
                        self.show_log("采样的概率为 %f, 赢了!" % sampled_prob)
                        data_i.append('赢')
                    else:
                        self.show_log("采样的概率为 %f, 输了!" % sampled_prob)
                        data_i.append('输')

            self.show_log('群体收益: ' + str(sum(self.rewards)))
            data_i.append(str(sum(self.rewards)))
            log_file.append(data_i)
            # print(log_file)
        self.write_to_log(log_file)
        self.Button_Conn.configure(state=DISABLED)
        messagebox.showinfo(title='游戏结束', message='本次游戏已结束, 结果已保存为 log.xls')

    def draw(self, num):
        self.Canvas1.delete('all')
        n_neighbors = len(self.neighbors[num])
        cx1 = 550 / 2 - self.space / 2
        cy1 = 550 / 3 - self.space / 2
        cx2 = cx1 + self.space
        cy2 = cy1 + self.space

        space = (550 - n_neighbors * self.space) / (n_neighbors + 1)
        y = []
        for i in range(n_neighbors):
            x1 = (i + 1) * space + i * self.space
            y1 = 550 * 2 / 3
            x2 = x1 + self.space
            y2 = y1 + self.space
            self.Canvas1.create_line((cx1 + cx2) / 2, (cy1 + cy2) / 2, (x1 + x2) / 2, (y1 + y2) / 2, width='5')
            self.Canvas1.create_oval(x1, y1, x2, y2, fill='red')
            self.Canvas1.create_text((x1 + x2) / 2, (y1 + y2) / 2,
                                     font="Times " + str(80 // self.size) + " italic bold",
                                     text=str(self.neighbors[num][i]))
            self.Canvas1.create_text((x1 + x2) / 2, (y1 + y2) / 2 + self.diameter,  ######
                                     font="Times " + str(10) + " italic bold",
                                     text='收益:' + str(self.rewards[self.neighbors[num][i]]))

        self.Canvas1.create_oval(cx1, cy1, cx2, cy2, fill='yellow')
        self.Canvas1.create_text((cx1 + cx2) / 2, (cy1 + cy2) / 2,
                                 font="Times " + str(80 // self.size) + " italic bold",
                                 text=str(num))
        self.Canvas1.create_text((cx1 + cx2) / 2, (cy1 + cy2) / 2 - self.diameter,  #####
                                 font="Times " + str(10) + " italic bold",
                                 text='收益:' + str(self.rewards[num]))

    def write_to_log(self, data):
        # 写标题
        workbook = xlwt.Workbook(
            encoding='utf-8')  # 新建一个excel文件 如果对一个单元格重复操作，会引发错误，>所以在打开时加cell_overwrite_ok=True 解决
        worksheet = workbook.add_sheet('Parrondo游戏日志', cell_overwrite_ok=True)  # 新建一个sheet
        worksheet.write(0, 0, label='取样次数')  # 写入数据table.write(行,列,value)
        worksheet.write(0, 1, label='系统随机选择节点编号')
        worksheet.write(0, 2, label='A环节/B博弈')
        worksheet.write(0, 3, label='断开邻居节点编号(A环节)/进入的分支(B博弈)')
        worksheet.write(0, 4, label='建立连接的次邻居编号(A环节)/输赢(B博弈)')
        worksheet.write(0, 5, label='总收益')
        # 写内容
        for i in range(len(data)):
            # worksheet.write(1,i,items[i])
            worksheet.write(i + 1, 0, data[i][0])
            worksheet.write(i + 1, 1, data[i][1])
            worksheet.write(i + 1, 2, data[i][2])
            worksheet.write(i + 1, 3, data[i][3])
            worksheet.write(i + 1, 4, data[i][4])
            worksheet.write(i + 1, 5, data[i][5])

        workbook.save('./log.xls')

    def show_log(self, str):
        self.Text_log.insert('end', str + '\n')

    def get_neighbors_info(self, num):
        content = str(num) + " 号的邻居\t收益\n--------------------\n"
        for i in range(len(self.neighbors[num])):
            content += (str(self.neighbors[num][i]) + '\t' + str(self.rewards[self.neighbors[num][i]]))
            content += '\n'
        content += '--------------------'
        return content


if __name__ == '__main__':
    vp_start_gui()
