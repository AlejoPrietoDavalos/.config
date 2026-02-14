from tkinter import (
    BOTH,
    LEFT,
    RIGHT,
    Y,
    Canvas,
    Frame,
    Label,
    Scrollbar,
    StringVar,
    Button,
)

from linux_setup.paths import get_paths_wallpaper
from linux_setup.programs.feh import set_wall


def _apply_wallpaper(path_wall, status_var: StringVar):
    status_var.set(f"Aplicando {path_wall.name}...")
    set_wall(path_wall=path_wall)
    status_var.set(f"Wallpaper cambiado: {path_wall.name}")


def build_wallpaper_ui(root) -> None:
    """Create a simple scrollable list of wallpapers with one-click apply."""
    root.title("Selector de Wallpapers")
    root.geometry("420x520")

    # Header with close button on the right
    header = Frame(root)
    header.pack(fill="x")
    Button(header, text="✕", command=root.destroy, padx=8, pady=4).pack(side=RIGHT, padx=8, pady=8)

    container = Frame(root)
    container.pack(fill=BOTH, expand=True)

    canvas = Canvas(container, borderwidth=0)
    scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
    scroll_frame = Frame(canvas)

    scroll_frame.bind(
        "<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    status_var = StringVar(value="Selecciona un wallpaper para aplicarlo")

    wallpapers = get_paths_wallpaper()
    if not wallpapers:
        Label(scroll_frame, text="No se encontraron wallpapers").pack(padx=12, pady=12)
    else:
        for path_wall in wallpapers:
            Button(
                scroll_frame,
                text=path_wall.stem,
                anchor="w",
                command=lambda p=path_wall: _apply_wallpaper(p, status_var),
            ).pack(fill="x", padx=12, pady=6)

    Label(root, textvariable=status_var, anchor="w").pack(fill="x", padx=12, pady=12)
