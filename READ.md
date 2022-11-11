### 背景 ###
用来存储查看联系人的相关信息


### 项目结构 ###
```
├─contactslist
│  ├─migrations
│  │  └─__pycache__
│  ├─templates
│  │  ├─contactslist
│  │  └─registration
│  └─__pycache__
└─contactsprojects
    └─__pycache__
```
##### contactslist ####
```
├─migrations
│  └─__pycache__
├─templates
│  ├─contactslist
│  └─registration
└─__pycache__
```
contactslist文件夹是项目的主体：
* templates文件夹中的contctslist定义了进入相应页面所使用的HTML文件
* registration文件夹存储的是登录使用的登录页面
* base_bootstrap.html 为基础文件夹，后使用的html文件基本继承于此文件
* forms.py 中的CreateForm 用于将对象的字段展现出来，同时对输入的数据进行相关的检测
* humanize.py 中的函数将可上传的照片的最大大小由像素转化为内存单位
* model.py 定义了模型的字段
* urls.py 定义了相关路径
* view.py定义当用户想进入路径后台的操作