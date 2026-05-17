from pathlib import Path
from getpass import getpass

def main(*, pypi_tkn):
    path_pypirc = Path.home() / ".pypirc"
    
    # Se modifica el template con el token.
    pypirc_file = Path(".pypirc.template").read_text().replace("{{PYPI_TKN}}", pypi_tkn)
    
    # Se borra si ya existía.
    path_pypirc.unlink(missing_ok=True)

    # Se escribe el nuevo.
    path_pypirc.write_text(pypirc_file)


if __name__ == "__main__":
    main(pypi_tkn=getpass("PYPI_TKN: "))