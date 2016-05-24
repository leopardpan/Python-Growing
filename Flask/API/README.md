# Flask 学习笔记

### 安装pip
```bash
sudo easy_install pip
```

### 安装Flask
```bash
sudo pip install flask
```

### 安装Flask-RESTful
```bash
sudo pip install flask-restful
```

### 学习资料：
[flask-restful官方文档](http://www.pythondoc.com/Flask-RESTful/index.html)                                     
[flask官方文档](http://flask.pocoo.org/)                   
[浅入浅出Flask框架：处理客户端通过POST方法传送的数据](http://www.letiantian.me/2014-06-24-flask-process-post-data/)

### 注意：
启动Server时必须指定主机地址为 `0.0.0.0` , 才能让其它电脑访问。 Port不要为80端口, 否则会有防火墙限制。例如：
```bash
app.run(host='0.0.0.0',port=4000,debug=True)
```




