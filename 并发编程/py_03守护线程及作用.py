import threading


# 定义后台线程的线程执行体与普通线程没有任何区别
def action(max):
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))


t = threading.Thread(target=action, args=(10,), name='后台线程')
# 将此线程设置成后台线程
# 也可在创建Thread对象时通过daemon参数将其设为后台线程

t.daemon = True  # 启动后台线程
t.start()

for i in range(10):
    print(threading.current_thread().name + "  " + str(i))
# -----程序执行到此处，前台线程（主线程）结束------
# 后台线程也应该随之结束
