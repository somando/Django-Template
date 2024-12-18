# Django Template Repository

Django + PostgreSQL + NginxでDockerコンテナを起動するテンプレートリポジトリです。

このリポジトリには2種類の`docker-compose.yaml`ファイルが含まれています。

> [!WARNING]
> README内のコードを実行するには、下記コードが実行されたターミナルで実行する必要があります。
> 
> ``` bash
> source env.sh
> ```

## 使い方（初期設定）

> [!WARNING]
> ここから先の操作はDocker Engineが起動している必要があります。

初期設定を行うには下記のコマンドを実行してください。

``` bash
init
```

このコマンドを実行することで以下の処理を行います。

- .envファイルの生成
- Django Secret Keyの発行・登録

実行後、自動的に必要なファイルを削除します。

## 起動方法（開発環境）

   開発環境ではAppコンテナとDBコンテナのみ起動します。

   Appコンテナのサーバー起動にはDjangoのRunserverが使用されています。

> [!WARNING]
> ここから先の操作はDocker Engineが起動している必要があります。

   1. イメージをビルドする

      下記、コマンドを実行して開発環境イメージをビルドします。

      ``` bash
      build dev
      ```

   2. コンテナを起動する

      下記、コマンドを実行してコンテナを起動します。

      ``` bash
      up dev
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
      build pro
      ```

   2. コンテナを起動する

      下記、コマンドを実行してコンテナを起動します。

      ``` bash
      up pro
      ```

> [!NOTE]
> ローカルで起動した場合、 http://localhost:80 で接続できます。

## エイリアス

このリポジトリでは以下のエイリアスを導入しています。

### Docker Compose

Docker Composeにまつわるものは下記のとおりです。

各コマンドの後に引数をつけることも可能です。

- `build [dev|pro]` ... イメージのビルド
- `up [dev|pro]` ... コンテナの起動
- `stop [dev|pro]` ... コンテナの停止
- `down [dev|pro]` ... コンテナの削除

### その他

その他の操作は下記のエイリアスが設定されています。

- `app` = `docker exec -it django-app`
- `pip` = `docker exec -it django-app pip`
- `django` = `docker exec -it django-app python manage.py`
- `init` = `docker build -t django-setup -f docker/setup/Dockerfile . && docker run --name django-setup --volume .:/setup --rm django-setup python project_setup.py && docker rmi django-setup`

## 注意事項

- このリポジトリのライセンスはMIT Licenseです。

  必要がなければ、`LICENSE`ファイルを削除してください。

- 開発環境でAppコンテナのシェル操作をする場合、各コマンドの前に`app`をつけて実行する必要があります。

## Copyright

このテンプレートリポジトリはSoma Andoによって制作されました。

ライセンスはMIT Licenseです。

[Django Template Repository｜GitHub](https://github.com/somando/DjangoTemplate)

[Soma Ando's Portfolio](https://somando.jp)
