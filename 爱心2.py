import tkinter as tk
import math
import time

# ==========自定义修改区==========
NUM_POINTS = 300        #心形点数
POPUP_DURATION = 3000   #弹窗停留毫秒
WINDOW_W = 300           #单个弹窗宽度
WINDOW_H = 100           #单个弹窗高度
# ===============================
def get_screen_size():
    try:
        root = tk.Tk()
        root.withdraw()
        root.update_idletasks()
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        root.destroy()
        return w, h
    except:
        return 1920, 1080

SCREEN_W, SCREEN_H = get_screen_size()
def generate_heart_points(
    num_points, screen_w, screen_h, window_w, window_h
):
    points = []
    center_x = screen_w // 2
    center_y = screen_h // 2

    for i in range(num_points):
        t = i / num_points * 2 * 3.14159
        x = 16 * (math.pow(math.sin(t), 3))
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        y = -y
        scale = min(screen_w // 30, screen_h // 30)
        x = center_x + x * scale
        y = center_y + y * scale

        x = max(window_w // 2, min(x, screen_w - window_w // 2))
        y = max(window_h // 2, min(y, screen_h - window_h // 2))
        points.append((int(x), int(y)))
    return points
def show_heart_tip(x, y, w, h):
    root = tk.Toplevel()
    root.overrideredirect(False)
    root.geometry(f"{w}x{h}+{x - w // 2}+{y - h // 2}")
    root.attributes('-topmost', True)
    root.configure(bg="#ffc0cb")
    lab = tk.Label(root, text="满心欢喜❤️", font=("微软雅黑",13),bg="#ffc0cb",fg="#d62858")
    lab.pack(expand=True)
    return root
if __name__ == '__main__':
    point_list = generate_heart_points(NUM_POINTS, SCREEN_W, SCREEN_H, WINDOW_W, WINDOW_H)
    win_group = []
    for px, py in point_list:
        win = show_heart_tip(px, py, WINDOW_W, WINDOW_H)
        win_group.append(win)
        tk._default_root.update()
        time.sleep(0.015)

    time.sleep(POPUP_DURATION / 1000)
    for win in win_group:
        win.destroy()