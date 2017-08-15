基本上也是校内的人用吧我就不用英文了233333<br>
网站根是anti-captcha.shuosc.org，只接https，以captcha为key post上来验证码就行，大于2M不收，只收jpg格式。<br>
教务处和选课是一套，做在/jwc下面；成就系统和学工办是一套，做在/xgb下面；物理实验是一套，做在/phylab下面<br>
返回的json无非就是成功和失败，如下<br>
{"result": "1045", "succeed": 1}<br>
{"reason": "this file type is no supported.", "succeed": 0}<br>
<br>
没什么技术含量（捂脸），教务处和物理实验是自己打标签训练的卷积神经网络，学工办那一套太听话了直接tesseract摸了。<br>
应该会找时间写个博文，训练集可以群里找我要，不过你直接爬虫爬一堆问这个系统要结果准确率应该也都在95%以上（溜了）