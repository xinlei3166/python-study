#### cookie
一个概念就是cookie, HTTP是一种无状态的协议, 当一个浏览器客户端向服务器
提交一个request, 服务器回应一个response后, 他们之间的联系就中断了. 就导致了
这个客户端在向服务器发送请求时, 服务器无法判别这两个客户端是不是一个了.
cookie的作用就体现出来了, 当客户端向服务器发送一个请求后, 服务器会给它分配一个
标识(cookie), 保存到客户端本地, 下次该客户端再次发送请求时连带着cokie一并发送
给服务器.

#### 一个爬虫模拟登陆就是要做到模拟一个浏览器客户端的行为
首先将你的基本登录信息发送给指定的url, 服务器验证成功后会返回一个cookie, 我们
就利用这个cookie进行后续的爬取工作就行了.
**http.cookiejar**
http.cookiejar模块的主要作用是提供可存储cookie的对象, 以便与urllib模块配合
使用来访问Internet资源.**
CookieJar类的对象来捕获cookie并在后续连接请求时重新发送, 比如可以实现模拟登录功能.
该模块主要的对象有CookieJar, FileCookie, MozillaCookieJar, LWPCookieJar.

**urllib**
该模块包含urllib.request, urllib.parse
urllib.request.urlencode()用来编码
urllib.request.urlopen()返回的文件对象
u.read([nbytes])以字节字符串形式读取nbytes个数据


