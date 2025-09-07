# コミットメッセージ規約

## 目的
履歴の意図を最小コストで明確化するための自作プレフィックス規約である。書式と最小プレフィックスのみを定義する。

## 書式

- 形式: `PREFIX(:scope)?: subject`
  - `PREFIX` は下表のいずれか。
  - `scope` は任意。モジュールやディレクトリ名など（例: `utils`, `tests`）。

  - `subject` は要約（終止符不要、命令形にしない）。
- 本文（任意）:
  - 箇条書きで詳細を記述可。
  - 破壊的変更を含む場合は **本文に** `Breaking: 具体的な影響` を記載。

## プレフィックス一覧（最小）
- **COMPLETE:** 節目の完了点・基準化・大枠の確定。
- **ADD:** 新規追加（機能・ファイル・設定）。
- **FIX:** 不具合修正（誤動作・例外）。
- **CHANGE:** 仕様／挙動の変更（互換性の有無は本文で明記）。
- **REFACTOR:** 振る舞い不変の内部整理（責務分割・命名・構造化）。
- **REMOVE:** 削除（機能・ファイル・依存）。
- **RENAME:** 名前変更（ファイル／シンボル）。
- **MOVE:** 物理的移動（ディレクトリ構成の変更）。
- **DOCS:** ドキュメント・注釈の追加／修正。
- **TEST:** テストの追加／修正。

> 任意運用: **ENSURE:** 初期構成確定などの「基準点」を強調したい場合に限って使用。

## 例
- COMPLETE: プロジェクト構成決定
- ADD(src): process_toml と robots 処理を追加
- FIX(utils): find_project_root の再帰終了条件を修正
- CHANGE(config): .gitignore に out/debug/dev を追加
- REFACTOR(src): robots ロジックを関数へ抽出
- REMOVE(dev): 使われていない試験用スクリプトを削除
- RENAME(tests): test_root.py を test_project_root.py へ
- MOVE(src): utils/tree.py を utils/fs/tree.py へ移動
- DOCS: README にセットアップ手順を追記
- TEST: test_about_toml の正常系/異常系を拡充


## 運用ルール（最低限）
1. 1コミット=1意図。`ADD` と `FIX` を混在させない。
2. 破壊的変更は本文に `Breaking:` を必ず記載。
3. 追加・修正の範囲が限定できる場合は `:scope` を付ける。
4. コミット前に `git diff --staged` で確認すること。
