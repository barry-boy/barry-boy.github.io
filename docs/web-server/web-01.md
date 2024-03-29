
## **一、域名概述**

1、域名解析的作用 
  方便记忆，IP地址不容易记忆，但是域名更加直观。

2、早起使用的 hosts 文件解析域名 
早起使用 hosts 文件进行域名的解析， Linux 中 hosts 文件存放路径为/etc/hosts ，Windows 系统中存放路径为 C:\Windows\System32\drivers\etc\hosts 内。 

但后期，随着 Internet 网上的网站发展迅速，一个小小的 hosts 文件以不足以存放，再 加上主机名称重复、主机维护困难等问题，出现了 DNS 域名解析服务

3、DNS （Domain Name System）域名系统 

- 两大特点：分布式、层次性 

- 域名空间结构：根域、顶级域（国家/ 地区域名）、二级域 

- 完整域名格式：FQDN= 主机名.DNS 后缀，例：www.baidu.com. 

## **二、网页概述**

1、网页：纯文本格式文件，其编写语言为 HTML，在用户的浏览器中被“翻译”成网页形 式显示出来 

2、网站：网站是由一个一个页面构成的，是多个网页的结合体 

3、主页：打开网站后出现的第一个网页称为网站主页（或首页） 

4、域名：浏览网页时输入的网址（例如：www.benet.wang ）

5、HTTP ：用来传输网页的通信协议 

6、URL ：是一种万维网寻址系统 

7、HTML ：用来编写网页的超文本标记语言

8、超链接：将网站中不同网页链接起来的功能

9、发布：将制作好的网页上传到服务器供用户访问的过程 

## **三、HTML(超文本标签语言)**

1、HTML ：Hyper Text Markup Language ，网页的“源码” 

2、浏览器：“解释和执行”HTML 源码的工具 

3、HTML 文档的结构 

头部部分 

标题部分 

主体部分 

网页内容，包括文本、图像等 

## **四、Web概述**

Web 内容储存在 Web 服务器上，最简单的 Web 资源就是 Web 服务器文件系统中的静 态文件，这些文件可以包含任意内容：文本文件、HTML 文件、微软的 Word 文件、Adobe 的 Acrobat 文件、JPEG 图片文件、AVI 电影文件。 

资源不一定是静态文件，资源还可以是根据需要生成内容的软件程序。这些动态内容资 源可以根据你的身份、所请求的信息或每天的不同时段来产生内容。

![20231030105618](https://barry-boy-1311671045.cos.ap-beijing.myqcloud.com/blog/20231030105618.png)

1、Web1.0 与 Web2.0 

Web1.0 是以编辑为特征，网站提供给用户的内容是编辑处理后提供的，然后用户阅读 网站提供的内容。这个过程是网站到用户的单向行为。 

Web2.0 更注重用户的交互作用，用户既是网站内容的消费者（浏览者），也是网站内容 的制造者。Web2.0 加强了网站与用户之间的互动，网站内容基于用户提供，网站的诸多功 能也由用户参与建设，实现了网站与用户双向的交流与参与。 

2、静态网页与动态网页 

（1 ）静态网页 

在网站设计中，纯粹 HTML 格式的网页通常被称为“静态网页”，静态网页是标准的 HTML 文件，扩展名是.htm 、.html，可包含文本、图像、声音、 FLASH 动画、客户端脚本和 ActiveX

控件及 JAVA 小程序等。静态网页是网站建设的基础，早期的网站一般都是静态网页制作的。

静态网页相对于动态网页而言，是没有后台数据库、不含程序和不可交互的网页。静态 网页相对更新起来比较麻烦，适用于一般更新叫少的展示型网站。 

静态网页的内容相对稳定，因此容易被搜索引擎检索。 

静态网页没有数据库的支持，在网站制作和维护方面工作量较大，因此当网站信息量很 大时完全依靠静态网页制作方式比较困难。静态网页的交互性较差，在功能方面有较大的限 制。页面浏览速度迅速，过程无需连接数据库，开启页面速度快于动态页面。

（2 ）动态网页 

动态网页是与静态网页相对应的，网页 URL 的后缀不是.htm 、.html 、.shtml 、xml 等静 态网页的常见形式，而是以.aspx 、.asp 、.jsp 、.php 、.perl 、.cgi 等形式为后缀，并且在动态 网页网址中有一个标志性的符号——“?” 

动态网页显示的内容可以随着时间、环境或者数据库操作的结果而发生改变。动态网页 与网页上的各种动画、滚动字幕等视觉上的动态效果没有直接关系，只要是采用了动态网站 技术生产的网页都可以称为“动态网页”。

动态网页是基本的 html 语法与 Java、PHP 等高级程序设计语言、数据库编程等多种技 术的融合，以实现对网站内容和风格的高效、动态和交互式管理。 

动态网页一般以数据库技术为基础，可以大大降低网站维护的工作量。采用动态网页技 术的网站可以实现更多的功能，如用户注册、用户登录、在线调查、用户管理、订单管理等

## **http协议分析**

一. HTTP 协议概述

每天都有数以亿万计的 JPEG 图片、 HTML 页面、文本文件、 MPEG 电影、 WAV 音频文件、 JAVA 小程序和其他资源在因特网上游弋。 HTTP 可以通过遍布全世界的 Web 服务器上将这些 信息快迅速、便捷、可靠地搬移到人们桌面上的 Web 浏览器上去。 

Web 服务器所使用的是 HTTP 协议，因此经常会被称为 HTTP 服务器。 HTTP 服务器存储 了因特网中的数据，如果 HTTP 客户端发出请求的话，它们会提供数据，客户端向服务器发送 HTTP 请求，服务器会在 HTTP 响应中回送所有请求的数据。 


二. HTTP 协议版本

HTTP 协议是互联网上应用最为广泛的一种网络协议，设计这个协议的目的是为了发布和接收 Web 服务器上的 HTML 页面。

HTTP 协议的版本： 

**HTTP 0.9** 

已过时。只接受  GET  一种请求方法，没有在通讯中指定版本号，且不支持请求头。由 于该版本不支持  POST  方法，所以客户端无法向服务器传递太多信息。 

**HTTP 1.0** 

这是第一个在通讯中指定版本号的 HTTP  协议版本，至今仍被广泛采用，特别是在代理 服务器中。 

**HTTP 1.1** 

当前版本。持久连接被默认采用，并能很好地配合代理服务器工作。还支持以管道方式 同时发送多个请求，以便降低线路负载，提高传输速度。 

**HTTP/1.1** 相较于  **HTTP/1.0**  协议的区别主要体现在： 

1  缓存处理 

2  带宽优化及网络连接的使用 

3  错误通知的管理 

4  消息在网络中的发送 

5  互联网地址的维护 

6  安全性及完整性 

三. HTTP方法

HTTP 支持几种不同的请求命令，这些命令被称为 HTTP 方法（ HTTP method）每条 HTTP 请求报文会包含一个方法，告诉服务器要执行什么动作： 

- 获取一个 Web 页面 
- 运行一个网关程序 
- 删除一个文件等 

HTTP 协议有多种获得 Web 资源的方法，常用的有两种：GET 和 POST 

![20231030111012](https://barry-boy-1311671045.cos.ap-beijing.myqcloud.com/blog/20231030111012.png)

**GET** 和 **POST** 

例如访问： http://www.test.com/a.php?Id=123 就是一个 GET 请求，如果访问正常，我们 会从服务器的日志中获取 200 状态码。 

假如此请求使用 POST 方法，那么我们会传递给 a.php 的 Id 参数依旧是 123，但是浏览 器的 URL 将不会显示后面的 Id=123 字样，因此表单类或者有用户名、密码等内容提交时建议使用 POST 方式。 

不管使用哪种方式，最终 a.php 获取到的值是一样的。 






