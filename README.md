# gpu-util-bot (日本語)

Discord経由で`nvidia-smi`を実行するためのbot

## 準備

1. Discord Developer PortalでApplicationを作成する
2. 「settings」から「OAuth2」を選び、「URL Generator」で「scopes」として「bot」を指定、「bot permissions」として「View Channels」、「Send Messages」、「Attatch Files」の3つにチェックを入れる
3. 「generated url」を使用してApplicationを使用したいDiscordのサーバーにインストールする
4. 「settings」から「Bot」を選び、「Reset Token」をクリックしてトークンを取得し、gpu-util-bot.pyの`TOKEN`にペーストする

## 実行

### スクリプト実行

必要なパッケージをインストールする。

```bash
pip install -r requirements.txt
```

GPUを搭載したマシン内で以下コマンドを実行する。

```bash
python gpu-util-bot.py
```

### ビルド＆実行

Windowsの場合には実行ファイル化しておくと取り回しが楽になる。

Windows環境でpyinstallerをインストールする。

```bash
pip install pyinstaller
```

ビルドを実行する。`--onefile`は1つのファイルにまとめるオプション、`-w`はコンソールを表示せずバックグラウンド実行するオプション。

```bash
pyinstaller gpu-util-bot.py --onefile -w
```

distディレクトリ内にexeファイルが出来上がるので、これを実行する。

`C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`にファイルを配置するとWindows立ち上げ時に自動起動してくれて便利。

## 使い方

以下コマンドを実行すると`nvidia-smi`の実行結果を画像で返却してくれる。(Discordの2000字制限のため画像で送っている)

```
/nvidia-smi
```

もしくはbotに対してメンションを送ってもよい。

```
@gpu-util-bot
```

# gpu-util-bot (English)

A bot for running `nvidia-smi` via Discord

## Preparation

1. Create an Application in the Discord Developer Portal.
2. Select "OAuth2" from settings, and in the URL Generator, specify `bot` as the scope. Under bot permissions, check `View Channels`, `Send Messages`, and `Attach Files`.
3. Use the generated URL to install the Application in the desired Discord server.
4. In settings, select "Bot", click `Reset Token` to get the token, and paste it into `TOKEN` in `gpu-util-bot.py`.

## Execution

### Running the Script

Install the necessary packages.

```bash
pip install -r requirements.txt
```

Run the following command on a machine with a GPU:

```bash
python gpu-util-bot.py
```

### Building and Running

Creating an executable file is convenient when running on Windows.

Install `pyinstaller` in the Windows environment.

```bash
pip install pyinstaller
```

Execute the build. The `--onefile` option compiles everything into a single file, and `-w` allows it to run in the background without showing a console.

```bash
pyinstaller gpu-util-bot.py --onefile -w
```

An executable file will be created in the `dist` directory. Place it in `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` to start automatically when Windows boots.

## Usage

The following command will return the output of `nvidia-smi` as an image (sent as an image to avoid Discord’s 2000-character limit).

```
/nvidia-smi
```

Or, you can mention the bot directly:

```
@gpu-util-bot
```

