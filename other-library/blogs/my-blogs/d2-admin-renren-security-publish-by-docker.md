Docker部署D2Admin 人人企业版
===

> Created by **[huqi](https://github.com/hu-qi)** at **2019-5-24 21:01:30**  
> Updated by **[huqi](https://github.com/hu-qi)** at **2019-5-24 21:20:41**

## 前言
最近后端的小伙伴在探索docker部署，给我也提了需求，希望我别掉链子，也能将前端服务通过docker部署。于是乎，我在大掘金找到了一篇不错的实践，@[快狗打车前端团队](https://juejin.im/user/5c90d966f265da61173a2cd8) 的 [[手把手系列之]Docker 部署 vue 项目](https://juejin.im/post/5cce4b1cf265da0373719819)。出于Copy的职业本能，看完文章立马动手尝试了一下，一顿操作猛如虎，通过Docker部署了一个vue-cli生成的demo，当然，理论上来看，也就是部署了一个静态目录dist。效果如图。介于目前项目的前端开发基于[D2Admin 人人企业版](https://github.com/d2-projects/d2-admin-renren-security-enterprise),有了快狗团队的手摸手，很快就能用Docker部署这样一个后台管理平台。本文默认使用linux且安装了docker@18.09.6、node@8.9.0及git@1.8.3.1。

## git clone及项目打包
“巧妇难为无米之炊”，代码都没有，何谈部署？说时迟那时快，先clone一下源代码。D2Admin 人人企业版大概9.25M的样子，我的ECS配置极差，网络环境也比较差，拉取的时间稍微长一点，都吃完一片西瓜了，都还在95%的进度。当然，乳沟您本地已经打包好了请略过一下操作，还有时间可以多吃几片西瓜。一般来说在实际上线中，前端可能只要给到打包之后的文件夹就够了。
```bash
git clone https://github.com/d2-projects/d2-admin-renren-security-enterprise.git
cd d2-admin-renren-security-enterprise
npm install
npm run build
```
这里build主要还是获取到dist目录。

## 构建镜像，部署静态资源
这里借助docke获取nginx镜像，通nginx镜像作为基础来构建D2Admin 人人企业版镜像。   
拉取nginx镜像：
```bash
docker pull nginx
```

创建nginx配置文件：
```bash
mkdir nginx
vi nginx/deafult.conf
```
default.conf文件：
```conf
server {
    listen       80;
    server_name  localhost;

    #charset koi8-r;
    access_log  /var/log/nginx/host.access.log  main;
    error_log  /var/log/nginx/error.log  error;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```
新建Dockerfile文件：
```bash
vi Dockerfile
```
Dockerfile文件：
```
FROM nginx
```
新建sh文件，如：
```
vi D2AdminRenren.sh
```
.sh文件：
```
docker run \
-p 4443:80 \
-d --name d2adminrenren \
--mount type=bind,source=/home/huqi/d2-admin-renren-security-enterprise/nginx,target=/etc/nginx/conf.d \
--mount type=bind,source=/home/huqi/d2-admin-renren-security-enterprise/dist,target=/usr/share/nginx/html \
nginx
```
部署静态资源：
```
sh D2AdminRenren.sh
```

这就完事了？五秒真男人？我裤子都脱了，你就给我看这个？

## 给nginx加buff--https
