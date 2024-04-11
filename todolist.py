import tkinter as tk


todos=[]

def add_todo():
    title = entry_title.get()
    description = entry_description.get()
    todo = {"標題": title, "描述": description, "完成狀態":False}
    todos.append(todo)
    update_todo_list()
    entry_title.delete(0, tk.END)
    entry_description.delete(0, tk.END)



def show_todo():
    for index, todo in enumerate(todos):
        print(f"編號 : {index + 1}")
        print(f"標題 : {todo['標題']}")
        print(f"描述 : {todo['描述']}")
        print(f"完成狀態 :{'是' if todo['完成狀態'] else '否'}")
        print("------------------")



def mark_complete():
    selection = todo_list.curselection()
    if selection:
        index = selection[0]
        todos[index]["完成狀態"] = True
        update_todo_list()

   


def delete_todo():
    selection = todo_list.curselection()
    if selection:
        index = selection[0]
        del todos[index]
        update_todo_list()
   


def update_todo_list():
    todo_list.delete(0, tk.END)
    for index, todo in enumerate(todos):
        status = "完成" if todo["完成狀態"] else "未完成"
        todo_list.insert(tk.END,f"標題 : {todo['標題']}, 描述 : {todo['描述']},狀態 : {status}")


window = tk.Tk()
window.title("代辦事項應用程序")


todo_list = tk.Listbox(window)
todo_list.config(width=40, height=15)
todo_list.pack()


label_title = tk.Label(window, text="標題: ")
label_title.pack()
entry_title = tk.Entry(window)
entry_title.pack()


label_description = tk.Label(window, text="描述: ")
label_description.pack()
entry_description = tk.Entry(window)
entry_description.pack()


button_add = tk.Button(window, text="添加", command=add_todo)
button_add.pack()


button_complete = tk.Button(window, text="標記為完成", command=mark_complete)
button_complete.pack()


button_delete = tk.Button(window, text="刪除", command = delete_todo)
button_delete.pack()


button_show = tk.Button(window, text="顯示代辦事項", command = show_todo)
button_show.pack()

window.geometry("1600x900")
window.mainloop()