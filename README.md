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

   1. 静的ファイルを集めておく

      Djangoには自動的に静的ファイルを集める`python manage.py collectstatic`というコマンドがあります。

      このコマンドを実行して静的ファイルを予め集めておく必要があります。

      このコマンドは開発環境を起動している際に実行してください。

      このプロジェクトでは生成するフォルダ名を`docker/app/.env`から変更できます。

      ※2回目以降は上書きの確認が表示されるので、問題なければ`yes`を入力してください。

      ``` bash
      django collectstatic
      ```

   2. イメージをビルドする

      下記、コマンドを実行して開発環境イメージをビルドします。

      ``` bash
      build pro
      ```

   3. コンテナを起動する

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
- `web` = `docker exec -it django-web`
- `db` = `docker exec -it django-db`
- `test` = `docker exec -it django-test`
- `pip` = `docker exec -it django-app pip`
- `django` = `docker exec -it django-app python manage.py`
- `init` = `docker build -t django-setup -f docker/setup/Dockerfile . && docker run --name django-setup --volume .:/setup --rm django-setup python project_setup.py && docker rmi django-setup`

## CIスクリプト

このリポジトリには予めGitHubとGitLabでどちらでも使えるCIスクリプトが入っています。

不要な場合は削除してください。

- GitHub = `.github/workflows/python-ci.yml`
- GitLab = `.gitlab-ci.yml`

### テスト内容

テストされる内容は以下の通りです

- pytest
- black
- flake8
- isort
- mypy
- bandit
- safety

safetyは予め環境変数`SAFETY_API_KEY`にAPIキーを入力しておく必要があります。

### ローカル実行

また、このCIで実行されるものを予めローカルで実行したい場合は`django-test`コンテナが起動しているので、実行したいコマンドの頭に`test`をつけてコマンドを実行してください。

## 注意事項

- このリポジトリのライセンスはMIT Licenseです。

  必要がなければ、`LICENSE`ファイルを削除してください。

- 開発環境でAppコンテナのシェル操作をする場合、各コマンドの前に`app`をつけて実行する必要があります。

## Copyright

このテンプレートリポジトリはSoma Andoによって制作されました。

[Django Template Repository｜GitHub](https://github.com/somando/DjangoTemplate)

[Soma Ando's Portfolio](https://somando.jp)
