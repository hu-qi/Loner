*Created by **[huqi](https://github.com/hu-qi)** at 2019-4-5 22:24:33*    
*Updated by **[huqi](https://github.com/hu-qi)** at 2019-4-5 23:23:56*

![clipboard.png](https://segmentfault.com/img/bVbqV5x)
↑开局一张图，故事全靠编↑

# 从解答一个知否上的问题说起
有时候，自己就像自己在知否的签名一样--我以为的就是我以为的？一直以来，对前端技术的一知半解一叶障目，导致我遇到问题总是片面，比如这次，就翻车了。技术水平就那样，然后我居然还想着帮人家解答，这不是误人子弟吗？昨天解答的这个问题，是关于node.js的http方法，根据Url获取网络图片写入到本地文件夹，这个需求我之前是玩过的，但用的是Copy&Paste的代码，也没有细细研究源码，只知道用的是request的模块，不过这次的哥们没有依赖任何第三方模块，只是用的内置的http模块。他遇到的问题就是上图所见，有一张图片没有下载成功无法正常显示。具体问题见@夜鹰 ：[**用Node.js读取远程的图片文件并写入本地？**](https://segmentfault.com/q/1010000018760426/a-1020000018760914)

![clipboard.png](https://segmentfault.com/img/bVbqV64)

# 通过内置http模块下载图片源码

- 引入内置http模块发起请求获取文件
- 引入内置fs模块写入文件
```
const http = require('http')
const fs = require('fs')

const urlArr = [
'http://img.zcool.cn/community/01e505554437be0000019ae95582a2.jpg@900w_1l_2o_100sh.jpg',
'http://static.pig66.com/uploadfile/2017/1102/20171102095531217.png',
]

urlArr.forEach(url => {
    getImg(url)
})

function getImg(url, name) {
    http.get(url, {encoding: null}, res => {
        let img = []
        let size = 0
        // 将图片地址以【.】符号分割，取最后一项，即为格式后缀
        const _arr = url.split('.')
        const format = _arr[_arr.length - 1]
        // 如果没有传入图片名字，则使用随机数
        const _name = name ? name : 'image-' + Math.floor(Number(new Date()) * Number(Math.random()))
        res.on('data', chunk => {
            img.push(chunk)
            size += chunk.length
        })
        res.on('end', () => {
            // 合并 Buffer
            const buffer = Buffer.concat(img, size)
            fs.writeFileSync(`img/${_name}.${format}`, buffer, (err) => {
                if (err) {
                    return console.error(err);
                }
                console.log("数据写入成功！");
            })
        })
    })
}

```
对来说，起初我以为是文件太大的原因，因为通过输出查看到Buffer数据中断并直接结束了。后来我试了下1M左右的图片，完全能够成功下载，然而，打脸啪啪啪。接下来，我草率地下了结论，并丢给博主一段使用第三方模块request的同样功能的实现(见历史版本：[共被编辑 4 次](https://segmentfault.com/q/1010000018760426/a-1020000018760914/revision))。真相纠结是怎样的？另一位答主@啊哦 已经给出了相当明确的答案！
[!aa](https://segmentfault.com/img/bVbqWbT?w=1071&h=515)

# “罪魁祸首”--301重定向

> 301重定向（）页面永久性移走）是一种非常重要的“自动转向”技术。网址重定向最为可行的一种办法。当用户或搜索引擎向网站服务器发出浏览请求时，服务器返回的HTTP数据流中头信息(header)中的状态码的一种，表示本网页永久性转移到另一个地址。

打开图片链接：http://www.pig66.com/uploadfile/2017/1102/20171102095531217.png，通过查看Network，我们清晰地看到源图片有做301重定向。通过在源代码中添加日志输出，我们也能清楚地看到301的状态码。
![clipboard.png](https://segmentfault.com/img/bVbqV9y)


![clipboard.png](https://segmentfault.com/img/bVbqV9R)

既然问题的根源已经找到，那就对症写bug，如果是301的话获取请求返回的真实地址再次发起请求。

```
        const { statusCode } = res
        if ( statusCode === 301 ) {
            const url = res.headers['location']
            return getImg(url)
        }
```
修改后的代码：
```
const http = require('http')
const fs = require('fs')

const urlArr = [
'http://img.zcool.cn/community/01e505554437be0000019ae95582a2.jpg@900w_1l_2o_100sh.jpg',
'http://static.pig66.com/uploadfile/2017/1102/20171102095531217.png',
]

urlArr.forEach(url => {
    getImg(url)
})

function getImg(url, name) {
    http.get(url, {encoding: null}, res => {
        const { statusCode } = res
        console.log(statusCode)
        if ( statusCode === 301 ) {
            const url = res.headers['location']
            return getImg(url)
        }
        let img = []
        let size = 0
        // 将图片地址以【.】符号分割，取最后一项，即为格式后缀
        const _arr = url.split('.')
        const format = _arr[_arr.length - 1]
        // 如果没有传入图片名字，则使用随机数
        const _name = name ? name : 'image-' + Math.floor(Number(new Date()) * Number(Math.random()))
        res.on('data', chunk => {
            img.push(chunk)
            size += chunk.length
        })
        res.on('end', () => {
            // 合并 Buffer
            const buffer = Buffer.concat(img, size)
            fs.writeFileSync(`img/${_name}.${format}`, buffer, (err) => {
                if (err) {
                    return console.error(err);
                }
                console.log("数据写入成功！");
            })
        })
    })
}
成功拿到图片，并能直观的感受到301重定向之后又发起了一次请求，

![clipboard.png](https://segmentfault.com/img/bVbqWaH?w=326&h=188)

![clipboard.png](https://segmentfault.com/img/bVbqWaI?w=346&h=65)

# 后记
这两天朋友托我写两个简单的页面，我发现自己啥也不会！想想我，居然还这么热心地去帮人解答，真的是误人子弟害人不浅。谨以此次经历深刻反省自我，对被我坑过的各位表示深切的歉意。同时，也希望各位大佬不惜多多赐教!最后，祝@jsliang 生日快乐！[写在生日，一年前端拼搏记](https://juejin.im/post/5ca718c9f265da30c507d908)
