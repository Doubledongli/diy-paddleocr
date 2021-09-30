## 简介
diy-paddleocr是基于paddleocr的私人开发版本。

## 效果展示
``启动: python diy-paddleocr/deploy/pdserving/service/ocr_web_server.py``


``接口:http://localhost:9292/ocr/prediction``

``请求参数:{"feed": [{"image": "https://obohe.com/i/2021/09/30/mchaft.jpg"}]}``

``返回结果:{
    "message": "ok",
    "result": [
        {
            "locations": {
                "height": 37,
                "left": 0,
                "top": 2,
                "width": 88
            },
            "score": 0.993586540222168,
            "text": "姓名"
        }
    ],
    "status": 200
}``