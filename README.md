# fastapi-Tortoise-ORM-test

Fastapi + Tortoise ORM 測試

## 筆記

### [筆記連結](https://blog.lychicken.com/docs/daylily/pyDaylily/fastapiTortoiseORM)

## 啟動

### 1. 安裝依賴包

```shell
pip install -r requirements.txt
```

### 2. 執行

```shell
uvicorn main:app --reload
```

## docker

### 1. build image

```shell
docker build -t my-fast-app .
```

### 2. run container

```shell
docker run -p 8099:8099 my-fast-app
```
