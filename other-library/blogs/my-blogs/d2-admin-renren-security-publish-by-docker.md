> Created by **[huqi](https://github.com/hu-qi)** at **2019-5-24 21:01:30**  
> Updated by **[huqi](https://github.com/hu-qi)** at **2019-5-26 00:00:42**

### 前言

最近后端的小伙伴在探索docker部署，给我也提了需求，希望我别掉链子，也能将前端服务通过docker部署。于是乎，我在大掘金找到了一篇不错的实践，@[快狗打车前端团队](https://juejin.im/user/5c90d966f265da61173a2cd8) 的 [[手把手系列之]Docker 部署 vue 项目](https://juejin.im/post/5cce4b1cf265da0373719819)。出于Copy的职业本能，看完文章立马动手尝试了一下，一顿操作猛如虎，通过Docker部署了一个vue-cli生成的demo，当然，理论上来看，也就是部署了一个静态目录dist。简单的实践效果如图。介于目前项目的前端开发基于[D2Admin 人人企业版](https://github.com/d2-projects/d2-admin-renren-security-enterprise),有了快狗团队的手摸手，很快就能用Docker部署这样一个后台管理平台。本文默认使用linux且安装了docker@18.09.6、node@8.9.0及git@1.8.3.1。

![](https://user-gold-cdn.xitu.io/2019/5/25/16aef78a66663a12?w=1920&h=1080&f=png&s=97812)

### git clone及项目打包

“巧妇难为无米之炊”，代码都没有，何谈部署？说时迟那时快，先clone一下源代码。D2Admin 人人企业版大概9.25M的样子，我的ECS配置极差，网络环境也比较差，拉取的时间稍微长一点，都吃完一片西瓜了，都还在95%的进度。当然，乳沟您本地已经打包好了请略过一下操作，还有时间可以多吃几片西瓜。一般来说在实际上线中，前端可能只要给到打包之后的文件夹就够了。
```bash
git clone https://github.com/d2-projects/d2-admin-renren-security-enterprise.git
cd d2-admin-renren-security-enterprise
npm install
npm run build
```

![](https://user-gold-cdn.xitu.io/2019/5/25/16aef890446d9491?w=1135&h=40&f=png&s=8755)
这里build主要目的还是为了获取到dist目录。

### 构建镜像，部署静态资源
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
<details>
    <summary>deafult.conf</summary>
    
    server {
        listen  80;
        server_name  localhost;
    
        #charset koi8-r;
        access_log  /var/log/nginx/host.access.log  main;
        error_log  /var/log/nginx/error.log  error;
    
        location / {
            root   /usr/share/nginx/html;
            index  index.html index.htm;
        }
    
        #error_page  404  /404.html;
    
        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /usr/share/nginx/html;
        }
    }
</details>

新建Dockerfile文件：     
```bash
vi Dockerfile
```
<details>
    <summary>Dockerfile</summary>
    
    FROM nginx
</details>

新建sh脚本文件，如：   
```
vi D2AdminRenren.sh
```
<details>
    <summary>.sh</summary>
    
    docker run  -p 4443:80 -d --name d2adminrenren --mount type=bind,source=/home/huqi/d2-admin-renren-security-enterprise/nginx,target=/etc/nginx/conf.d --mount type=bind,source=/home/huqi/d2-admin-renren-security-enterprise/dist,target=/usr/share/nginx/html nginx

</details>

部署静态资源：   
```
sh D2AdminRenren.sh
```

一波操作下来基本上就把D2Admin 人人企业版部署上去了。

![](https://user-gold-cdn.xitu.io/2019/5/25/16aef8bb14a2a1e5?w=1916&h=1080&f=png&s=84449)
简单说下上面几个操作的作用。docker拉取nginx，这里能够在不影响本机之前装的nginx的情况下，在docker容器中装了一个单独的nginx，一个简单的命令似乎见识到了docker的强大之处。nginx的配置文件我就不细说，因为我不会，这方面的资料还是蛮多的，之前看极客学院就推出过相关的专栏还是蛮火的，也可以参考@[快狗打车前端团队](https://juejin.im/user/5c90d966f265da61173a2cd8) 写的几篇相关的文章，这里为啥设置目录为 **/usr/share/nginx/html**，是因为后续会复制dist目录到这个文件夹，从而达到静态部署的目的。至于Dockerfile这个文件为啥只有 **FROM nginx**这一行仅仅说明镜像来源于官方nginx，是因为具体的配置写到了后边的sh脚本中。这里的sh脚本又长又臭，主要还是因为我不会断行，不过还是很好理解，其实就一条 **docker run** 的指令，**-p**指定容器暴露的端口，**-d**指定容器将会运行在后台模式,**--name** 指定容器名字，后续可以通过名字进行容器管理，**--mount**这里是关键，主要用于容器数据持久化，这样一来无论是修改nginx配置文件还是重新打包vue应用，都只要重启容器**docker restart** 就能生效。

### 跨域转发
一般来说，前后分离的项目都会存在跨域的问题，D2Admin人人企业版看似不存在跨域，那是因为后台接口做了跨域处理，这样一来，谁都可以调这个接口，如图所示，后台接口展示得比较明显，接下来想处理一来，在nginx上做一下代理转发。

![](https://user-gold-cdn.xitu.io/2019/5/25/16aefab4eef7a55c?w=1920&h=1080&f=png&s=255444)
修改前端api配置：   
```bash
vi scr/.env
```
<details>
    <summary>.env</summary>
    
    # 所有环境默认
    # 优先级最低
    
    # 网络请求公用地址
    VUE_APP_API=security-enterprise-server


</details>

重新build：   
```
npm run build
```
修改nginx配置，增加接口转发,将 **security-enterprise-server**路径下的请求全部转发到后台。
<details>
    <summary>修改后的deafult.conf</summary>
    
    server {
        listen  80;
        server_name  localhost;
    
        #charset koi8-r;
        access_log  /var/log/nginx/host.access.log  main;
        error_log  /var/log/nginx/error.log  error;
    
        location / {
            root   /usr/share/nginx/html;
            index  index.html index.htm;
        }
    
        #error_page  404  /404.html;
    
        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /usr/share/nginx/html;
        }
        location ~  /security-enterprise-server/ {
            proxy_pass https://demo.renren.io;
        }
    }
</details>

重启：   
```bash
docker restart d2adminrenren
```

![](https://user-gold-cdn.xitu.io/2019/5/25/16aefb19d5be59b4?w=1918&h=1078&f=png&s=232447)

### 后记
一次简单的尝试，居然踩了很多莫名其妙的坑，比如我的docker没有快狗前端团队文中提到的**docker exect**指令，只有 **docker exec**，比如**docker ps** 查看到端口已开，**netstat -tnpl**没看到端口……不管怎样，总算是又迈出了一步，至少在后端都讨论docker的时候，也能插上一句“那个，前端也能用docker部署”。也许是又做了一个梦，梦中copy了不少代码，梦醒时分，继续漫无目的地前行！

> <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://user-gold-cdn.xitu.io/2019/5/22/16adeb2bef0a04db?w=88&h=31&f=png&s=1888" /></a><br /><a xmlns:dct="http://purl.org/dc/terms/" property="dct:title">本作品</a> 由 <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/hu-qi/Loner" property="cc:attributionName" rel="cc:attributionURL">Loner</a> 采用 <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议</a>进行许可。<br />基于<a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/hu-qi/Loner" rel="dct:source">https://github.om/hu-qi/Loner</a>上的作品创作。<br />本许可协议授权之外的使用权限可以从 <a xmlns:cc="http://creativecommons.org/ns#" href="https://creativecommons.org/licenses/by-nc-sa/2.5/cn/" rel="cc:morePermissions">https://creativecommons.org/licenses/by-nc-sa/2.5/cn/</a> 处获得。
