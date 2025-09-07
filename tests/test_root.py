import pytest
from pathlib import Path
from utils.root import find_project_root

@pytest.fixture
def git_project(tmp_path: Path) -> Path:
    """疑似的なgitプロジェクトルートを作成して返す"""
    (tmp_path / ".git").mkdir()
    return tmp_path

def test_with_file_input(git_project: Path):
    file = git_project / "sample.py"
    file.write_text("print('x')")
    assert find_project_root(file) == git_project

def test_with_dir_input(git_project: Path):
    assert find_project_root(git_project) == git_project

def test_recursive_search(git_project: Path):
    subdir = git_project / "a" / "b"
    subdir.mkdir(parents=True)
    assert find_project_root(subdir) == git_project

def test_raise_if_no_git(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        find_project_root(tmp_path)

def test_raise_if_rootdir_no_git(tmp_path: Path):
    # tmp_path 自体をファイルシステムのルートに見立てるケース
    # pathlib の parent が self になる状況を模倣
    p = tmp_path
    while p.parent != p:
        p = p.parent
    with pytest.raises(FileNotFoundError):
        find_project_root(p)
