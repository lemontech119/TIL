## mac postgresql 사용

``` bash
## postgresql search
$ brew search postgresql
==> Formulae
postgresql                 postgresql@11              postgresql@9.5
postgresql@10              postgresql@9.4             postgresql@9.6
==> Casks
navicat-for-postgresql

## postgresql install
$ brew install postgresql
......
## 아래와 같이 나오면 성공
To have launchd start postgresql now and restart at login:
  brew services start postgresql
Or, if you don't want/need a background service you can just run:
  pg_ctl -D /usr/local/var/postgres start

$ pg_ctl -D /usr/local/var/postgres start
$ export PGDATA='/usr/local/var/postgres'
$ pg_ctl status 
pg_ctl: server is running (PID: 29590)
/usr/local/Cellar/postgresql/12.2/bin/postgres "-D" "/usr/local/var/postgres"
## server is running 나오면 성공


## Initialize database Cluster
$ initdb /usr/local/var/postgres

## Create a new database
$ createdb postgis_test

## start 
$ psql postgis_test
```

