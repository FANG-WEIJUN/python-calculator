import tkinter as tk
from tkinter import font
import math

class RoundedButton(tk.Canvas):
    def __init__(self, master=None, text="", bg="white", fg="black", 
                 active_bg="#f0f0f0", command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bd=0, highlightthickness=0, relief="ridge", bg="#121212")
        self.bg = bg
        self.fg = fg
        self.active_bg = active_bg
        self.command = command
        self.text = text
        self.font = ('Arial', 18)
        
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.draw_button()
        
    def draw_button(self, active=False):
        self.delete("all")
        bg = self.active_bg if active else self.bg
        
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()
        
        # 圆角矩形参数 - 增大按钮尺寸
        corner_radius = 20
        padding = 5
        
        # 绘制圆角矩形
        self.create_round_rect(
            padding, padding, 
            width - padding, height - padding,
            radius=corner_radius,
            fill=bg, outline=bg
        )
        # 添加按钮文本
        self.create_text(width//2, height//2, 
                        text=self.text, 
                        font=self.font, 
                        fill=self.fg)
        # 确保背景色与主背景一致
        self.config(bg="#121212")
        
    def create_round_rect(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        return self.create_polygon(points, **kwargs, smooth=True)
    
    def _on_press(self, event):
        self.draw_button(active=True)
    
    def _on_release(self, event):
        self.draw_button(active=False)
        if self.command:
            self.command()

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python 计算器")
        
        # 设置黑色背景
        self.bg_canvas = tk.Canvas(master, highlightthickness=0, bg="#121212")
        self.bg_canvas.place(relwidth=1, relheight=1)
        
        # 创建纯黑背景
        width = master.winfo_screenwidth()
        height = master.winfo_screenheight()
        self.bg_canvas.create_rectangle(0, 0, width, height, 
                                      fill="#121212", outline="")
        
        # 创建暗色显示区域
        self.display = tk.Entry(master, width=24, font=('Arial', 36), 
                              borderwidth=8, justify=tk.RIGHT,
                              highlightthickness=2, highlightbackground="#333333",
                              bg="#1e1e1e", fg="white", insertbackground="white")
        self.display.grid(row=0, column=0, columnspan=4, padx=20, pady=10)  # 左右20，上下10
        
        # 创建顶部功能键行
        top_functions = [
            ('%', 1, 0), ('CE', 1, 1),
            ('C', 1, 2), ('←', 1, 3)
        ]
        
        # 创建顶部功能键按钮（统一尺寸）
        for (text, row, col) in top_functions:
            btn = RoundedButton(self.master, text=text, width=80, height=80,
                              bg="#e0e0e0", fg="black", active_bg="#d0d0d0",
                              command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=2, pady=2)
        
        # 创建第二功能键行
        functions = [
            ('1/x', 2, 0), ('x²', 2, 1),
            ('√x', 2, 2), ('÷', 2, 3)
        ]
        
        # 创建功能键按钮（统一尺寸）
        for (text, row, col) in functions:
            btn = RoundedButton(self.master, text=text, width=80, height=80,
                              bg="#e0e0e0", fg="black", active_bg="#d0d0d0",
                              command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=2, pady=2)
        
        # 初始化计算变量
        self.current_input = ""
        self.operation = None
        self.first_number = 0
        
        # 创建按钮
        self.create_buttons()
        
    def create_buttons(self):
        # 数字按钮（行号调整）
        buttons = [
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2),
            ('0', 6, 1), ('.', 6, 2)
        ]
        
        # 运算符按钮（行号调整）
        operators = [
            ('X', 3, 3), ('-', 4, 3),
            ('+', 5, 3), ('+/-', 6, 0),
            ('=', 6, 3)
        ]
        
        # 统一按钮尺寸参数
        btn_width = 6
        btn_height = 2
        
        # 创建数字按钮（带红绿点缀）
        color_variation = {
            0: "#f5f5f5", 1: "#f5f5f5", 2: "#f5f5f5",
            3: "#f5f5f5", 4: "#f5f5f5", 5: "#f5f5f5",
            6: "#f5f5f5", 7: "#f5f5f5", 8: "#f5f5f5",
            9: "#f5f5f5", '.': "#f5f5f5"
        }
        
        # 创建数字按钮（统一尺寸）
        for (text, row, col) in buttons:
            btn = RoundedButton(self.master, text=text, width=80, height=80,
                              bg="#333333", fg="white", active_bg="#444444",
                              command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=2, pady=2)
            
        # 创建运算符按钮（白底黑字，=按钮特殊）
        for (text, row, col) in operators:
            if text == "=":
                bg = "#1a5276"
                fg = "white"
            else:
                bg = "#333333"
                fg = "white"
                
            btn = RoundedButton(self.master, text=text, width=80, height=80,
                              bg=bg, fg=fg, active_bg="#e0e0e0",
                              command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=2, pady=2)
            
        # 调整布局权重和边距（行数增加到7行）
        for i in range(7):
            self.master.grid_rowconfigure(i, weight=1, minsize=80)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1, minsize=80)
        
        # 设置窗口初始尺寸和边距
        self.master.geometry("400x600")  # 设置固定窗口大小
        self.master['padx'] = 20  # 减少水平边距
        self.master['pady'] = 15  # 减少垂直边距
        self.master.minsize(350, 550)  # 设置最小窗口尺寸
            
    def on_button_click(self, text):
        if text == '%' and self.current_input:
            num = float(self.current_input)
            result = num / 100
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.current_input = str(result)
        elif text == 'CE':
            self.current_input = ""
            self.display.delete(0, tk.END)
        elif text == 'C':
            self.current_input = ""
            self.first_number = 0
            self.operation = None
            self.display.delete(0, tk.END)
        elif text == '←' and self.current_input:
            self.current_input = self.current_input[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_input)
        elif text == '1/x' and self.current_input:
            try:
                num = float(self.current_input)
                result = 1 / num
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.current_input = str(result)
            except ZeroDivisionError:
                self.display.delete(0, tk.END)
                self.display.insert(0, "错误: 不能除以零")
                self.current_input = ""
        elif text == 'x²' and self.current_input:
            num = float(self.current_input)
            result = num ** 2
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.current_input = str(result)
        elif text == '√x' and self.current_input:
            num = float(self.current_input)
            if num >= 0:
                result = math.sqrt(num)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.current_input = str(result)
            else:
                self.display.delete(0, tk.END)
                self.display.insert(0, "错误: 负数不能开平方")
                self.current_input = ""
        elif text == '+/-' and self.current_input:
            if self.current_input[0] == '-':
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_input)
        elif text in '0123456789':
            self.current_input += text
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_input)
        elif text == '.' and '.' not in self.current_input:
            if not self.current_input:
                self.current_input = '0'
            self.current_input += text
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_input)
        elif text in '+-*X÷':
            self.first_number = float(self.current_input)
            self.operation = '*' if text == 'X' else ('/' if text == '÷' else text)
            self.current_input = ""
        elif text == '=':
            if self.operation:
                second_number = float(self.current_input)
                if self.operation == '+':
                    result = self.first_number + second_number
                elif self.operation == '-':
                    result = self.first_number - second_number
                elif self.operation == '*':
                    result = self.first_number * second_number
                elif self.operation == '/':
                    try:
                        result = self.first_number / second_number
                    except ZeroDivisionError:
                        self.display.delete(0, tk.END)
                        self.display.insert(0, "错误: 不能除以零")
                        self.current_input = ""
                        self.operation = None
                        return
                
                # 格式化结果，如果是整数则去掉小数部分
                if result.is_integer():
                    result = int(result)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.current_input = str(result)
                self.operation = None
        
    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-alpha', 0.95)  # 设置窗口不透明度为95%
    root.resizable(False, False)  # 禁止调整窗口大小
    app = Calculator(root)
    app.run()