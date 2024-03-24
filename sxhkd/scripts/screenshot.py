from typing import Literal, List
from pathlib import Path
import shutil
import subprocess
import tempfile
import sys


class CMDScrot:
    @staticmethod
    def _base_cmd() -> List[str]:
        return ["scrot", "-q", "100"]
    
    @staticmethod
    def bbox(path_out: Path) -> None:
        cmd = CMDScrot._base_cmd() + ["-f", "-s", str(path_out)]
        subprocess.run(cmd)

    @staticmethod
    def focused(path_out: Path) -> None:
        cmd = CMDScrot._base_cmd() + ["-u", str(path_out)]
        subprocess.run(cmd)

    @staticmethod
    def full_screen(path_out: Path) -> None:
        cmd = CMDScrot._base_cmd() + ["-m", str(path_out)]
        subprocess.run(cmd)


class CMDXClip:
    @staticmethod
    def copy_img(path_img: Path) -> None:
        subprocess.run([
            "xclip",
            "-selection",
            "clipboard", "-t", "image/png",
            "-i", str(path_img)
        ])


def main(path_screenshots: Path, mode: str, with_save: Literal[0, 1]) -> None:
    path_tmp_folder = Path(tempfile.gettempdir())
    path_img_tmp = path_tmp_folder / f"{next(tempfile._get_candidate_names())}.png"
    
    if mode == "bbox":
        CMDScrot.bbox(path_img_tmp)
    elif mode == "focused":
        CMDScrot.focused(path_img_tmp)
    elif mode == "full_screen":
        CMDScrot.full_screen(path_img_tmp)
    CMDXClip.copy_img(path_img_tmp)
    
    if with_save == 0:
        path_img_tmp.unlink(missing_ok=True)
    elif with_save == 1:
        # Poner que verifique si el string es un entero o no.
        n_screens = [int(screenshot.stem) for screenshot in path_screenshots.iterdir()]
        idx_max_screen = max(n_screens) if len(n_screens)!=0 else 0
        path_img_save = path_screenshots / f'{idx_max_screen + 1}.png'
        shutil.move(path_img_tmp, path_img_save)
    else:
        # ERROR.
        pass


if __name__ == "__main__":
    path_screenshots = Path.home() / "images" / "screenshots"
    mode = str(sys.argv[1])
    with_save = int(sys.argv[2])     # TODO Mejorar: 0 no guarda, 1 lo guarda.
    main(path_screenshots, mode, with_save)

