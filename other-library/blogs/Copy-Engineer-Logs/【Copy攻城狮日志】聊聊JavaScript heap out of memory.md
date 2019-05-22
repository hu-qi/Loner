![JavaScript heap out of memory][1]
↑开局一张图，故事全靠编↑

----------

从一次宕机说起
----
这是一个很狗血的故事，故事的开头是一个项目，这个项目十分草率，草率到什么程度？没有设计稿，没有文档，需求全靠口口相传，当然最草率的是交给了我，我简单列了下需求：

 - 官网的形式，主要介绍公司某些业务
 - 要能发文章
尽管很简单的需求，对于水得一匹的我来说，简直是“难于上青天”，三大件(html,css,javascript)我样样精通个P，网站部署我也只略知一二，代码编水平更是不学无术。作为Copy工程师，遇到需求我便开始了copy之路，先github溜达了一圈，找了几个满足需求的项目，最终对比了一下，选择了一个名叫[iBlog2](https://github.com/eshengsky/iBlog2)的项目--基于 Node.js 的个人开源博客系统。您没看错，就是一个博客系统！这跟官网有个毛关系？这个宕机又有个毛关系？我想说的是，经过copy然后小改之后，iBlog2摇身一变就成了能发布文章的官网项目，就是这么简单粗暴，就是这么不学无术(温馨提示：少壮不努力，老大偷代码)。

![iBlog2.png](/img/bVbnyTT)

这个3年之前的项目，在现在看来的确是有些陈旧，但作者[@eshengsky](https://github.com/eshengsky)依旧坚持不懈的在更新维护,而对于我而言，只是为了完成能发文章的官网，所以只关注文章是如何发布和储存的，恰恰是因为我关注的面窄，忽略了部署和部署之后可能会遇到的各种问题，比如window下pm2可能出现问题、比如这次的**JavaScript heap out of memory**。当然并不是人家开源项目有问题，而是实际部署的时候压根没按照作者的文档来，如果按照文档，我应该用pm2部署，或者启用redis，或者使用[Noginx](https://github.com/eshengsky/noginx),或者使用本机的MongoDB服务，然而，这一切，我只是在我们那个服务器新开了个端口，然后直接`npm run dev`就开始跑在线上了，所以呢，这么“锈”的操作，不宕机才是天理难容，印象中**JavaScript heap out of memory**遇到两次了，才两三个月啊！
## 检索**JavaScript heap out of memory** ##
通常遇到问题，我首选的解决流程是打开Chrome--输入关键词--搜索--浏览--copy--尝试，好像从来没有去思考过产生问题的根源，甚至都没有去记录这个问题以及解决的方案，导致再遇到同样的坑，又掉进去了，然后又是一通检索尝试等操作，这也是我从业这么多年来，一直没养成的习惯，也是这么多年一直没成长的某一个小的原因，“少抱怨，多思考，未来会更美好”，而我一直以反面教材在诠释这个金句。

![JavaScript heap out of memory.png](/img/bVbny4c)

通常来说，只要您的关键词够准确，您就能通过google搜索找到尽可能满意的解决方案，如果连关键词都没把握好，我想就算请教的大牛，也不一定能有效的回答，当然[思否](https://segmentfault.com/q/1010000009208402)和[Stack Overflow](https://stackoverflow.com/questions/38558989/node-js-heap-out-of-memory)都可能有填您那个坑的“铁楸”，还有一个阵地就是[github](https://github.com/nodejs/node/issues/10137)。

![clipboard.png](/img/bVbny5x)

通常来说，程序报错一般都有详细的报错说明，比如哪一行、出了什么错、出错明细等，就比如文章开头的那张报错图，我找到了其他用户遇到的一模一样的问题：
        <--- Last few GCs --->
        
        [8138:0x102801600]   145460 ms: Mark-sweep 1265.6 (1301.6) -> 1265.6 (1308.6) MB, 289.8 / 0.0 ms  allocation failure GC in old space requested
        [8138:0x102801600]   145740 ms: Mark-sweep 1265.6 (1308.6) -> 1265.6 (1277.6) MB, 280.6 / 0.0 ms  last resort gc 
        [8138:0x102801600]   146035 ms: Mark-sweep 1265.6 (1277.6) -> 1265.6 (1277.6) MB, 295.0 / 0.0 ms  last resort gc 
        
        
        <--- JS stacktrace --->
        
        ==== JS stack trace =========================================
        
        Security context: 0x39c891dc0d31 <JS Object>
            1: DoJoin(aka DoJoin) [native array.js:~97] [pc=0x5d1facabad4](this=0x39c891d04311 <undefined>,q=0x5a024bf3be1 <JS Array[2241635]>,r=2241635,F=0x39c891d043b1 <true>,B=0x39c891ddafe9 <String[1]\: \n>,A=0x39c891d04421 <false>)
            2: Join(aka Join) [native array.js:~122] [pc=0x5d1fb5cde96](this=0x39c891d04311 <undefined>,q=0x5a024bf3be1 <JS Array[2241635]>,r=2241635,B=0x39c891ddafe9 <String[1...
        
        FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory
         1: node::Abort() [/Users/erossignon/.nvm/versions/node/v7.2.0/bin/node]
         2: node::FatalException(v8::Isolate*, v8::Local<v8::Value>, v8::Local<v8::Message>) [/Users/erossignon/.nvm/versions/node/v7.2.0/bin/node]
         3: v8::internal::V8::FatalProcessOutOfMemory(char const*, bool) [/Users/erossignon/.nvm/versions/node/v7.2.0/bin/node]
         4: v8::internal::Factory::NewRawTwoByteString(int, v8::internal::PretenureFlag) [/Users/erossignon/.nvm/versions/node/v7.2.0/bin/node]
         5: v8::internal::Runtime_StringBuilderJoin(int, v8::internal::Object**, v8::internal::Isolate*) [/Users/erossignon/.nvm/versions/node/v7.2.0/bin/node]
         6: 0x5d1faa063a7
        Abort trap: 6

`FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory`这个是报错的关键词，通常也是我们检索的关键词，至于为什么会导致这个错误，报错信息就显示**JavaScript堆内存不足**，信息中也显示了最近几次GC的详情，[GC](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Internals/Garbage_collection)(Garbage collection
)是垃圾回收机制，具体可以阅读一下[JavaScript 内存泄漏教程](http://www.ruanyifeng.com/blog/2017/04/memory-leak.html)。经过初步了解，就是我们的应用内容泄露的，通常治标不治本的解决方案就是加大Node.js运行时内存中保留的“未使用”空间量：
    node --max-old-space-size=4096 yourFile.js

## JavaScript heap out of memory的原因 ##
  [1]: /img/bVbnysD
