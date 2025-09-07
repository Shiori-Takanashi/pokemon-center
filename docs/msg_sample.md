# msg_sample.md


## 一行サンプル（PREFIX のみ）
- COMPLETE: プロジェクト構成決定
- ADD: 初期READMEを追加
- ADD: pyproject.toml を追加
- ADD: uv.lock を追加
- ADD: .gitignore を追加
- ADD: robots処理の骨組みを追加
- ADD: TOML読み込みユーティリティを追加
- ADD: pytest 初期テストを追加
- ADD: 例外クラスの雛形を追加
- ADD: ログ設定を追加
- FIX: find_project_root の終了条件を修正
- FIX: TOMLパース時のエンコーディング不一致を修正
- FIX: robots.txt レスポンスの空判定を修正
- FIX: Windows環境のパス結合不具合を修正
- FIX: pytest 失敗の原因となる一時ディレクトリの扱いを修正
- CHANGE: .gitignore に out/debug/dev を追加
- CHANGE: config/urls 配下の toml を既定で無視する方針へ変更
- CHANGE: README のセットアップ手順を現状に合わせて更新
- CHANGE: 返り値の型を Path へ統一
- CHANGE: コマンド出力の標準化（静かな出力をデフォルトに）
- REFACTOR: robots 処理を関数へ抽出
- REFACTOR: ルート探索ロジックを分割
- REFACTOR: 命名と責務の整理
- REFACTOR: 例外の発生箇所を一箇所に集約
- REFACTOR: I/O とロジックの分離
- REMOVE: 使われていないデバッグスクリプトを削除
- REMOVE: 不要な依存の参照を削除
- REMOVE: 暫定のprintデバッグを削除
- REMOVE: 未使用の引数を削除
- REMOVE: 古いテストデータを削除
- RENAME: test_root.py を test_project_root.py に変更
- RENAME: tree.py の関数名を明確化
- RENAME: output.py を writer.py に変更
- RENAME: モジュール名の表記ゆれを統一
- RENAME: 変数名を snake_case に統一
- MOVE: utils/tree.py を utils/fs/tree.py へ移動
- MOVE: robots関連を src/ 直下から src/code/ へ移動
- MOVE: サンプルデータを tests/fixtures へ移動
- MOVE: 画像/資料を docs/ へ移動
- MOVE: 共通関数を utils/common.py へ移動
- DOCS: README に実行手順を追記
- DOCS: msg_rule.md を追加
- DOCS: CONTRIBUTING の方針を草案化
- DOCS: ディレクトリ構成図を更新
- DOCS: FAQ を追加
- TEST: test_about_toml の正常系/異常系を追加
- TEST: find_project_root の深い階層ケースを追加
- TEST: robots 応答の境界値テストを追加
- TEST: フィクスチャを fixtures/ に整理
- TEST: 失敗時メッセージを明確化
- ENSURE: 初期状態の固定（基準点）
- ENSURE: GitHub 追跡対象の見直しを確定
- ENSURE: コーディング規約の適用開始点を固定

---

## scope付きサンプル（PREFIX(scope): subject）
- ADD(src): robots エントリポイントを追加
- ADD(utils): path 関連ユーティリティを追加
- ADD(tests): test_about_toml の基本ケースを追加
- ADD(config): logging 設定を追加
- FIX(src): robots の空レスポンス処理を修正
- FIX(utils): find_project_root の親到達処理を修正
- FIX(tests): 一時ディレクトリの後始末を修正
- CHANGE(config): .gitignore の例外ルールを調整
- CHANGE(docs): インストール手順を uv 前提に改訂
- REFACTOR(src): process_toml の責務分割
- REFACTOR(utils): 共通関数を common.py に抽出
- REFACTOR(tests): 冗長な期待値生成を関数化
- REMOVE(dev): 私用の試験コードを削除
- REMOVE(debug): 手元ログを削除
- RENAME(tests): test_root.py → test_project_root.py
- RENAME(src): output.py → writer.py
- MOVE(utils): tree.py → fs/tree.py
- MOVE(src): robots.py → code/robots.py
- DOCS(docs): msg_rule.md を追加
- DOCS(readme): 使用例を現行コードに合わせて更新
- TEST(tests): TOML 読み込みの例外ケースを追加
- TEST(tests): ルート探索の循環検出を追加
- ENSURE(repo): プロジェクト構成決定を固定

---

## 本文付きサンプル（詳細・Breaking の記法）
ADD(src): process_toml を追加
- TOML 読み込みと検証を分離
- エラー時に ValueError を送出
- 最低限の型アノテーションを付与

FIX(utils): find_project_root の終了条件を修正
- ルート到達判定を `p.parent == p` に統一
- 親探索の再帰で戻り値を返さない不具合を修正
- 追加テストを同時に整備

CHANGE(config): .gitignore に out/debug/dev を追加
- out/ の生成物を一括除外
- 例外として `!config/urls/example_com.toml` を保持
- 既存追跡分はなし（--cached は不要）

REFACTOR(src): robots ロジックを関数へ抽出
- I/O と解析を分離
- テスト容易性を優先
- 振る舞いは不変

REMOVE(debug): 個人向けデバッグコードを削除
- 公開リポジトリに不要なため
- 再現性に寄与しないログを除去

RENAME(tests): test_root.py を test_project_root.py へ
- テスト対象に合わせた名称へ
- 参照パスを一括更新

MOVE(utils): tree.py を utils/fs/tree.py へ移動
- 役割に応じて fs 配下へ整理
- 相対 import を調整

DOCS: README にセットアップ手順を追記
- uv 利用手順（`uv sync --locked`）
- pytest の実行方法（`uv run pytest`）
- 最低限のトラブルシュート

TEST(tests): test_about_toml の異常系を追加
- 不正キー
- エンコーディング不一致
- ファイル不存在

CHANGE(src): 返り値の型を Path に統一
- 関数群の戻り値を str → Path へ
- 呼び出し箇所を調整
- **Breaking:** 外部APIの引数に影響する可能性あり

ENSURE(repo): 基準コミットを確定
- 現行ディレクトリ構成の固定
- 今後の差分評価の起点とする
- タグ `baseline-structure` を付与予定

サンプルのみを列挙する。**一行系 → scope付き → 本文付き**の順。

---

## 一行サンプル（PREFIX のみ）
- COMPLETE: プロジェクト構成決定
- ADD: 初期READMEを追加
- ADD: pyproject.toml を追加
- ADD: uv.lock を追加
- ADD: .gitignore を追加
- ADD: robots処理の骨組みを追加
- ADD: TOML読み込みユーティリティを追加
- ADD: pytest 初期テストを追加
- ADD: 例外クラスの雛形を追加
- ADD: ログ設定を追加
- FIX: find_project_root の終了条件を修正
- FIX: TOMLパース時のエンコーディング不一致を修正
- FIX: robots.txt レスポンスの空判定を修正
- FIX: Windows環境のパス結合不具合を修正
- FIX: pytest 失敗の原因となる一時ディレクトリの扱いを修正
- CHANGE: .gitignore に out/debug/dev を追加
- CHANGE: config/urls 配下の toml を既定で無視する方針へ変更
- CHANGE: README のセットアップ手順を現状に合わせて更新
- CHANGE: 返り値の型を Path へ統一
- CHANGE: コマンド出力の標準化（静かな出力をデフォルトに）
- REFACTOR: robots 処理を関数へ抽出
- REFACTOR: ルート探索ロジックを分割
- REFACTOR: 命名と責務の整理
- REFACTOR: 例外の発生箇所を一箇所に集約
- REFACTOR: I/O とロジックの分離
- REMOVE: 使われていないデバッグスクリプトを削除
- REMOVE: 不要な依存の参照を削除
- REMOVE: 暫定のprintデバッグを削除
- REMOVE: 未使用の引数を削除
- REMOVE: 古いテストデータを削除
- RENAME: test_root.py を test_project_root.py に変更
- RENAME: tree.py の関数名を明確化
- RENAME: output.py を writer.py に変更
- RENAME: モジュール名の表記ゆれを統一
- RENAME: 変数名を snake_case に統一
- MOVE: utils/tree.py を utils/fs/tree.py へ移動
- MOVE: robots関連を src/ 直下から src/code/ へ移動
- MOVE: サンプルデータを tests/fixtures へ移動
- MOVE: 画像/資料を docs/ へ移動
- MOVE: 共通関数を utils/common.py へ移動
- DOCS: README に実行手順を追記
- DOCS: msg_rule.md を追加
- DOCS: CONTRIBUTING の方針を草案化
- DOCS: ディレクトリ構成図を更新
- DOCS: FAQ を追加
- TEST: test_about_toml の正常系/異常系を追加
- TEST: find_project_root の深い階層ケースを追加
- TEST: robots 応答の境界値テストを追加
- TEST: フィクスチャを fixtures/ に整理
- TEST: 失敗時メッセージを明確化
- ENSURE: 初期状態の固定（基準点）
- ENSURE: GitHub 追跡対象の見直しを確定
- ENSURE: コーディング規約の適用開始点を固定

---

## scope付きサンプル（PREFIX(scope): subject）
- ADD(src): robots エントリポイントを追加
- ADD(utils): path 関連ユーティリティを追加
- ADD(tests): test_about_toml の基本ケースを追加
- ADD(config): logging 設定を追加
- FIX(src): robots の空レスポンス処理を修正
- FIX(utils): find_project_root の親到達処理を修正
- FIX(tests): 一時ディレクトリの後始末を修正
- CHANGE(config): .gitignore の例外ルールを調整
- CHANGE(docs): インストール手順を uv 前提に改訂
- REFACTOR(src): process_toml の責務分割
- REFACTOR(utils): 共通関数を common.py に抽出
- REFACTOR(tests): 冗長な期待値生成を関数化
- REMOVE(dev): 私用の試験コードを削除
- REMOVE(debug): 手元ログを削除
- RENAME(tests): test_root.py → test_project_root.py
- RENAME(src): output.py → writer.py
- MOVE(utils): tree.py → fs/tree.py
- MOVE(src): robots.py → code/robots.py
- DOCS(docs): msg_rule.md を追加
- DOCS(readme): 使用例を現行コードに合わせて更新
- TEST(tests): TOML 読み込みの例外ケースを追加
- TEST(tests): ルート探索の循環検出を追加
- ENSURE(repo): プロジェクト構成決定を固定

---

## 本文付きサンプル（詳細・Breaking の記法）
ADD(src): process_toml を追加
- TOML 読み込みと検証を分離
- エラー時に ValueError を送出
- 最低限の型アノテーションを付与

FIX(utils): find_project_root の終了条件を修正
- ルート到達判定を `p.parent == p` に統一
- 親探索の再帰で戻り値を返さない不具合を修正
- 追加テストを同時に整備

CHANGE(config): .gitignore に out/debug/dev を追加
- out/ の生成物を一括除外
- 例外として `!config/urls/example_com.toml` を保持
- 既存追跡分はなし（--cached は不要）

REFACTOR(src): robots ロジックを関数へ抽出
- I/O と解析を分離
- テスト容易性を優先
- 振る舞いは不変

REMOVE(debug): 個人向けデバッグコードを削除
- 公開リポジトリに不要なため
- 再現性に寄与しないログを除去

RENAME(tests): test_root.py を test_project_root.py へ
- テスト対象に合わせた名称へ
- 参照パスを一括更新

MOVE(utils): tree.py を utils/fs/tree.py へ移動
- 役割に応じて fs 配下へ整理
- 相対 import を調整

DOCS: README にセットアップ手順を追記
- uv 利用手順（`uv sync --locked`）
- pytest の実行方法（`uv run pytest`）
- 最低限のトラブルシュート

TEST(tests): test_about_toml の異常系を追加
- 不正キー
- エンコーディング不一致
- ファイル不存在

CHANGE(src): 返り値の型を Path に統一
- 関数群の戻り値を str → Path へ
- 呼び出し箇所を調整
- **Breaking:** 外部APIの引数に影響する可能性あり

ENSURE(repo): 基準コミットを確定
- 現行ディレクトリ構成の固定
- 今後の差分評価の起点とする
- タグ `baseline-structure` を付与予定
