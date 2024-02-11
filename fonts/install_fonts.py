import os

def main() -> None:
    path_fonts = "/usr/local/share/fonts"
    os.system(f"mkdir -p {path_fonts}")
    os.system(f"sudo cp ./*.ttf {path_fonts}")

if __name__ == "__main__":
    main()
