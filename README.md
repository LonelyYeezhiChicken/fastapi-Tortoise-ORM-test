# fastapi-Tortoise-ORM-test
Fastapi + Tortoise ORM 測試


## 啟動
1. 安裝依賴包
```
pip install -r requirements.txt
```
2. 執行
```
uvicorn main:app --reload
```

## docker
1. build image
```
docker build -t my-fast-app .
```
2. run container
```
docker run -p 8099:8099 my-fast-app
```