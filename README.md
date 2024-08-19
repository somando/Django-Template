# Django Template Repository

Django + PostgreSQL + NginxでDockerコンテナを起動するテンプレートリポジトリです。

このリポジトリには2種類の`docker-compose.yaml`ファイルが含まれています。

## 使い方（共通）

> [!WARNING]
> 
> 以下のコードを実行するには、各種ライブラリがインストールされた環境が必要です。
> 
> 仮想環境を利用する場合はアクティベートしてから実行してください。
> 
> ``` bash
> pip install -r requirements.txt
> ```

1. `docker/app/`と`docker/db/`の中に`.env`ファイルをそれぞれ新しく作成します

   - ファイルの例は`.env.example`です。この中に書かれている環境変数は必ず指定する必要があります。
  
   - まずは、`.env.example`の中身を`.env`にそのままコピーすることをお勧めします。

   - `DJANGO_SECRET_KEY`は下記の手順に沿って生成してください。

        1. シェルで以下のコードを実行する
           ``` bash
           python manage.py shell
           ```

        2. 起動したPythonシェル内で以下のように実行する
           ``` python
           from django.core.management.utils import get_random_secret_key
           ```
           ``` python
           get_random_secret_key()
           ```
           `'v#wt+ag1)vuubl!9t5ca@lks402vr3#-aab*=$i3d7r+xzv&j5'`のように出力されます。

           （Pythonシェルを終了するには、`exit()`と入力します）

        3. `.env`の中の`[DjangoSecretKey]`を先ほどの文字列に置き換える

           `.env`ファイル内のシークレットキーはこのようになります。
           ```
           DJANGO_SECRET_KEY=django-insecure-v#wt+ag1)vuubl!9t5ca@lks402vr3#-aab*=$i3d7r+xzv&j5
           ```

   - データベースの接続設定は下記のように対応しています。

     （左側が`docker/app/.env`、右側が`docker/db/.env`に対応 / `DB_HOST`にはDBコンテナのネットワークエイリアス`db`を使用）

     - `DB_NAME` = `POSTGRES_DB`
     - `DB_USER` = `POSTGRES_USER`
     - `DB_PASS` = `POSTGRES_PASSWORD`

2. 起動方法は起動環境によって異なります

## 起動方法（開発環境）

   開発環境ではAppコンテナとDBコンテナのみ起動します。

   Appコンテナのサーバー起動にはDjangoのRunserverが使用されています。

> [!WARNING]
> ここから先の操作はDocker Engineが起動している必要があります。

   1. イメージをビルドする

      下記、コマンドを実行して開発環境イメージをビルドします。

      ``` bash
      docker-compose -f docker-compose-develop.yaml build
      ```

   2. コンテナを起動する

      下記、コマンドを実行してコンテナを起動します。

      ``` bash
      docker-compose -f docker-compose-develop.yaml up -d
      ```

> [!NOTE]
> ローカルで起動した場合、 http://localhost:8000 で接続できます。

## 起動方法（本番環境）

   本番環境ではWebコンテナとAppコンテナ、DBコンテナが起動します。

   Appコンテナの起動方法にはGunicornが使われており、WebコンテナとAppコンテナはソケット通信で接続されています。

> [!TIP]
> DBサーバーにRDSなどを使用して別途起動する場合にはDBコンテナを削除し、`docker/app/.env`の`DB_HOST`にDBサーバーのDNSを指定する必要があります。

> [!WARNING]
> ここから先の操作はDocker Engineが起動している必要があります。

   1. イメージをビルドする

      下記、コマンドを実行して開発環境イメージをビルドします。

      ``` bash
      docker-compose -f docker-compose-production.yaml build
      ```

   2. コンテナを起動する

      下記、コマンドを実行してコンテナを起動します。

      ``` bash
      docker-compose -f docker-compose-production.yaml up -d
      ```

> [!NOTE]
> ローカルで起動した場合、 http://localhost:80 で接続できます。

## 注意事項

- このリポジトリのライセンスはMIT Licenseです。

  必要がなければ、`LICENSE`ファイルを削除してください。

- 開発環境でAppコンテナのシェル操作をする場合、各コマンドの前に`docker container exec django-app`をつけて実行する必要があります。

## Copyright

このテンプレートリポジトリはSoma Andoによって制作されました。

[Django Template Repository｜GitHub](https://github.com/somando/DjangoTemplate)

[Soma Ando's Portfolio](https://somando.jp)
