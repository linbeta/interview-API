# API 練習

這個作業我的思路分為幾個部分：

1. 先處理原本的flask api，加了一些內容讓最外層的docker-compose.yaml可以直接把服務架起來。

2. 再來將flask api的內容用FastAPI改寫，另外跑一個container，並且將這個服務加到最外層的docker-compose.yaml檔案中。

3. 最終只要在根目錄跑這個指令就可以將服務跑起來了：
    ```docker
    docker-compose up
    ```
4. 服務跑起來以後直接進入資料庫進行資料表處理。

在本機端執行的API endpoints:
Flask版本：[http://localhost:8080/example/endpoint1](http://localhost:8080/example/endpoint1)
FastAPI版本：[http://localhost:8000/example/endpoint1](http://localhost:8000/example/endpoint1)

##### 更多細節如下列說明
---

## Flask api 優化部分
dockerfile使用的主機為輕量化的alpine，跑起來以後的API endpoint為：[http://localhost:8080/example/endpoint1](http://localhost:8080/example/endpoint1)


## FastAPI 部分
dockerfile同樣使用alpine來實作，架構同flask的版本，只是啟動的cmd略有不同，port開在8000，跑起來以後的API endpoint為：[http://localhost:8000/example/endpoint1](http://localhost:8000/example/endpoint1)
（時間有限僅先做開發版本的測試連結）

FastAPI的內建Swagger文件：[http://localhost:8000/docs](http://localhost:8000/docs)

## PostgreSQL
這部分我沒有去處理service之間的連結，依照我理解的題目，把PostgreSQL跑起來之後我是直接進去postgresql-container裡面建立資料表的，相關操作與截圖如下：
1. 先建立一個名為```betalin```的database
2. 再建立一個名為```users```的table
![CREATE TABLE](https://github.com/linbeta/interview-API/blob/main/screenshots/Screen%20Shot%202022-11-12%20at%202.43.51%20AM.png?raw=true)
3. 列出建立的資料表之schema
![data schema](https://github.com/linbeta/interview-API/blob/main/screenshots/Screen%20Shot%202022-11-12%20at%202.41.23%20AM.png?raw=true)
