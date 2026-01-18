import tkinter as tk
from chitieu import QuanLyChiTieu

# ===== DATA =====
ql = QuanLyChiTieu()
so_du = 10_000_000

# ===== ROOT =====
root = tk.Tk()
root.title("Quản lý chi tiêu")
root.geometry("420x700")
root.resizable(False, False)

# ===== BACKGROUND =====
bgimg = tk.PhotoImage(file="bgr.png")
canvas = tk.Canvas(root, width=420, height=700, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bgimg, anchor="nw")

# ===== FONT =====
FONT_TITLE = ("Segoe UI Semibold", 20)
FONT_SUB   = ("Segoe UI", 13)
FONT_TEXT  = ("Segoe UI", 11)
FONT_BTN   = ("Segoe UI Semibold", 13)
FONT_LABEL = ("Segoe UI Semibold", 11)
FONT_INPUT = ("Segoe UI", 11)

# ===== HEADER =====
canvas.create_text(210, 38, text="Nguyễn Minh Quân", fill="white", font=FONT_TITLE)
lbl_sodu = canvas.create_text(
    210, 75,
    text=f"Số dư: {so_du:,} VND",
    fill="#e8fff6",
    font=FONT_SUB
)

def cap_nhat_sodu():
    canvas.itemconfig(lbl_sodu, text=f"Số dư: {so_du:,} VND")

# ===== BUTTON BO TRÒN =====
def nut_bo_tron(x, y, w, h, text, command):
    r = h // 2
    color = "#1abc9c"

    left = canvas.create_oval(x, y, x+h, y+h, fill=color, outline=color)
    right = canvas.create_oval(x+w-h, y, x+w, y+h, fill=color, outline=color)
    mid = canvas.create_rectangle(x+r, y, x+w-r, y+h, fill=color, outline=color)

    txt = canvas.create_text(
        x + w//2, y + h//2,
        text=text, fill="white", font=FONT_BTN
    )

    for item in (left, right, mid, txt):
        canvas.tag_bind(item, "<Button-1>", lambda e: command())

# ===== AUTO +600K / 30 PHÚT =====
def cong_tien_tu_dong():
    global so_du
    so_du += 600_000
    cap_nhat_sodu()
    root.after(1_800_000, cong_tien_tu_dong)

root.after(1_800_000, cong_tien_tu_dong)

# ===== NẠP TIỀN =====
def nap_tien():
    win = tk.Toplevel(root)
    win.title("Cộng tiền")
    win.geometry("300x200")
    win.resizable(False, False)

    tk.Label(win, text="Số tiền cần cộng", font=FONT_LABEL).pack(pady=(20, 5))
    e = tk.Entry(win, font=FONT_INPUT, justify="center")
    e.pack(ipady=4)

    def cong():
        global so_du
        so_du += int(e.get())
        cap_nhat_sodu()
        win.destroy()

    tk.Button(
        win, text="Cộng tiền",
        font=FONT_BTN,
        bg="#1abc9c", fg="white",
        relief="flat",
        padx=20, pady=6,
        command=cong
    ).pack(pady=20)

# ===== THÊM CHI =====
def them_chi():
    win = tk.Toplevel(root)
    win.title("Thêm khoản chi")
    win.geometry("300x320")
    win.resizable(False, False)

    def inp(label):
        tk.Label(win, text=label, font=FONT_LABEL).pack(pady=(10, 3))
        e = tk.Entry(win, font=FONT_INPUT, justify="center")
        e.pack(ipady=4)
        return e

    ten = inp("Tên khoản chi")
    so  = inp("Số tiền")
    ngay = inp("Ngày")

    def them():
        global so_du
        tien = int(so.get())
        ql.them(ten.get(), tien, ngay.get())
        so_du -= tien
        cap_nhat_sodu()
        win.destroy()

    tk.Button(
        win, text="Thêm khoản chi",
        font=FONT_BTN,
        bg="#e74c3c", fg="white",
        relief="flat",
        padx=20, pady=6,
        command=them
    ).pack(pady=20)

# ===== XEM CHI =====
def xem_chi():
    win = tk.Toplevel(root)
    win.title("Danh sách chi")
    win.geometry("380x420")
    win.resizable(False, False)

    tong = 0
    for x in ql.danh_sach():
        tk.Label(
            win,
            text=f"{x.ngay} | {x.ten} | {x.so_tien:,} VND",
            font=FONT_TEXT,
            anchor="w"
        ).pack(fill="x", padx=10, pady=2)
        tong += x.so_tien

    tk.Label(
        win,
        text=f"Tổng chi: {tong:,} VND",
        font=FONT_LABEL,
        fg="#e74c3c"
    ).pack(pady=15)

# ===== BUTTON =====
nut_bo_tron(60, 140, 300, 50, "➕  Cộng tiền", nap_tien)
nut_bo_tron(60, 210, 300, 50, "➖  Thêm khoản chi", them_chi)
nut_bo_tron(60, 280, 300, 50, "📄  Xem khoản chi", xem_chi)

root.mainloop()
