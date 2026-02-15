from tkinter import Tk

from linux_setup.wallpaper_ui import build_wallpaper_ui


def main():
    root = Tk()
    build_wallpaper_ui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
