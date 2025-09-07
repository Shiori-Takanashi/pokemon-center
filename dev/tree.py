from __future__ import annotations
from pathlib import Path
from typing import Iterable

import click
from pathspec import PathSpec
from rich.console import Console
from rich.tree import Tree

console = Console(record=True)

def build_spec(patterns: Iterable[str]) -> PathSpec:
    """gitignore 互換（gitwildmatch）でパターンを構築"""
    return PathSpec.from_lines("gitwildmatch", (p for p in patterns if p))

def should_ignore(root: Path, path: Path, spec: PathSpec) -> bool:
    rel = path.relative_to(root).as_posix()
    return spec.match_file(rel)

def add_branch(node: Tree, root: Path, path: Path, spec: PathSpec) -> None:
    if should_ignore(root, path, spec):
        return
    if path.is_dir():
        branch = node.add(f"[bold blue]{path.name}/[/]")
        for child in sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower())):
            add_branch(branch, root, child, spec)
    else:
        node.add(path.name)

def build_tree_text(root: Path, spec: PathSpec) -> str:
    t = Tree(f"[bold]{root.name}/[/]")
    add_branch(t, root, root, spec)
    console.print(t)
    return console.export_text(clear=False).rstrip("\n")

@click.command()
@click.argument("rootdir", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option("-d", "--deldir", multiple=True, help="除外ディレクトリ（gitignore形式）。例: '__pycache__/'")
@click.option("-f", "--delfile", multiple=True, help="除外ファイル（gitignore形式）。例: '*.pyc'")
@click.option("-o", "--out", type=click.Path(dir_okay=False, path_type=Path), help="出力先ファイル。未指定なら標準出力。")
def cli(rootdir: Path, deldir: tuple[str, ...], delfile: tuple[str, ...], out: Path | None) -> None:
    # デフォルト除外（生成物・VCS・仮想環境）
    default_patterns = [
        ".git/",        # Git メタデータ
        ".venv/",       # 仮想環境
        "__pycache__/", # Python バイトコードキャッシュ
        "*.pyc",        # バイトコード
        ".pytest_cache"
    ]

    # ディレクトリは末尾 '/' を推奨（ディレクトリ限定マッチ）
    dir_patterns = [p if p.endswith("/") else p + "/" for p in deldir]
    file_patterns = list(delfile)

    spec = build_spec([*default_patterns, *dir_patterns, *file_patterns])

    root = Path(rootdir)
    text = build_tree_text(root, spec)

    if out:
        out = Path(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    else:
        click.echo(text)

if __name__ == "__main__":
    cli()
