# Spark Simple job server prototype #

간단한 수준의 RESTful API로 Spark를 돌릴 수 있는 지 테스트 중.

##Web server 실행하기##

 Flask를 이용해서 간단한 Web server를 만들었다.
```
python ~/work/web_main.py
```


##API 호출하기 ##

 POSTMAN이나 request로 아래 주소를 호출해본다. (간단하게 S3에서 Text를 읽어서 글자수 세는 것을 이용했다.)

```
POST http://192.168.18.31:5000/S3Data
{"uri": "S3 URL",
 "AWS_SECRET_ACCESS_KEY":"~~~",
 "AWS_ACCESS_KEY_ID":"~~~" }
```

아래와 같이 결과가 나온다.

```
{ "output": "[(u'', 4792), (u'horses', 17), (u'description--Trade--Niu-chwang', 1), (u'Attorneys-at-law', 1), (u'hordes', 1), .....

```
