from pathlib import Path


def _path_of_this() -> Path:
    return Path(__file__)


def find_project_root(p: Path | None = None) -> Path:
    if p is None:
        p = _path_of_this().parent

    if p.is_file():
        p = p.parent

    for elm in p.iterdir():
        if elm.name == ".git" and elm.is_dir():
            return p  # ← ここで親ディレクトリを返す

    if p.parent == p:  # ファイルシステムのルートに到達
        raise FileNotFoundError(".git not found")

    return find_project_root(p.parent)  # ← 再帰の結果を必ず返す
