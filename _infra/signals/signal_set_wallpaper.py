from _utils import get_path_config_tmp, start_signal
from feh import get_random_wall, set_wall

def main(signum, frame):
    set_wall(get_random_wall())

if __name__ == "__main__":
    path_config_tmp = get_path_config_tmp()
    start_signal(main, path_config_tmp, __file__)