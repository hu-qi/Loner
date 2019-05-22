![taro.png](/img/bVbnCCN)
↑开局一张图，故事全靠编↑
## 从一个需求说起 ##
作为底层的程序猿，哦不，我连猿都算不上，混的好的叫码神，混得一般的叫码农，混得有点差的叫码畜，混得极差的，就像我这样的，叫码渣。去年，2018年年底，12月份，运营的大佬提出了想做电商类支付宝小程序的想法，需求很简单：做一个自己的商城，上架到支付宝小程序应用市场。一句话，简单明了，需求很明确啊，可这句话对我来说，要实现的难度，比起李白上蜀道还难，比难于上青天还难。细细一想，做商城，得有后台管理系统吧？得有支付系统吧？得有订单管理等一系列业务支撑的后台吧？我一小小的前端，本身业务基础又差，每天上班8小时划水10小时，竟然让我独自完成一个电商支付宝小程序，哈哈哈哈哈。不过，本来没做实质性项目的我，怎么会畏惧，怎么能退缩，生死看淡，不服就干！谁给我的自信？开源社区啊！作为“资深”的Copy码渣，接到任务我就在github开始寻符合需求的demo，皇天不负有心人，我把github翻了个遍，收获寥寥无几，**各位大佬有啥支付宝小程序开源的项目请一定推荐给我**，Copy选不中对象，就无法愉快地进行Paste。为了快速交付，经过对比选用[@tumobi](https://github.com/tumobi)大佬的[Nideshop](https://www.nideshop.com/)“全家桶”，于是就有了这次借助[Taro](https://github.com/NervJS/taro)的`taro convert`转化微信小程序为支付宝小程序的经历。在我看来，我写不出如此出色的开源项目，倘若我能借助这些项目快速完成自己的工作，享受开源带来的乐趣，对于现阶段的我而言，足矣！(绝逼不敢相信，从业多年的程序员依旧是这么low！)
![taro.png](/img/bVbnCDB)
（图片来源于网络）

## 环境准备 ##
工欲善其事必先利其器。9102年了，还有谁在用notepad写代码？当然，对于我们前端而言，谁的电脑没装个node\git\vscode之类的软体？如果您还没装的话，赶紧装吧，装完您就会嘿嘿嘿，对于我而言没有ndoe我无法工作，没有前端开发环境，我就不快乐。
![图片描述][1]
(图片来源于网络)
- 在您的平台上下载 Node.js 源码或预编译安装包，然后即可马上进行开发。[去下载](https://nodejs.org/zh-cn/download/)
- git--distributed-is-the-new-centralized。[去下载](https://git-scm.com/downloads)
- 小程序开发者工具定位于「一站式小程序研发工具」，专门为小程序开发打造，提供了项目管理、编码、调试、真机测试等功能。[去下载](https://docs.alipay.com/mini/ide/download)
- 其他的好像也没啥了，当年好像我的还装了Python|jJava|Android等环境，那是2016年的事了[追忆](https://www.cnblogs.com/hu-qi/p/5652073.html),现在看来很傻很天真，其实没必要。

##Copy进行时##
Taro 可以将你的[原生微信小程序应用转换为 Taro 代码](https://nervjs.github.io/taro/docs/taroize.html)，进而你可以通过 taro build 的命令将 Taro 代码转换为对应平台的代码，或者对转换后的 Taro 代码进行用 React 的方式进行二次开发。之前一直在期待taro的这个功能，虽然不会React，也要尝试一下，也希望通过这些实践更加了解React并好好学习，从我接触的内容来说，React是前端开发必备的技术栈。
###[Taro](https://taro.js.org/)安装###
        /** Quick Start With NPM Or Yarn **/
            $ npm install -g @tarojs/cli
            $ yarn global add @tarojs/cli

###[nideshop-mini-program](https://github.com/tumobi/nideshop-mini-program/)下载###
        git clone https://github.com/tumobi/nideshop-mini-program.git
        cd nideshop-mini-program

###转化为taro###
    taro convert
  通过以上步骤可以得到一个taroConvert的文件夹，就算暂时成功的了。
![clipboard.png](/img/bVbnDcl)

###安装依赖###
    cd taroConvert
    npm i
对于大多数前端项目来说，现阶段不可避免的问题是可能一个不算复杂的项目会依赖上百个npm包，也正是因为这些包，大大解放了生产力，一定程度上提高了开发效率。当然，如同硬币有两面，伴随着便捷高效的同时也带来了一定的安全风险。可能大厂都是自己造轮子吧！
![clipboard.png](/img/bVbnDeE)
###打包成支付宝小程序###
    npm run build:alipay
理想状态是可直接打包成dist的，but……
接下来就捋一捋存在的问题，为什么要手动修改一些问题？
##为什么要暴力修改##
首先回到taro的官方文档看下 `taro convet`会遇到哪些坑
- 在小程序 IDE 显示 _createData 错误☞[了解](https://nervjs.github.io/taro/docs/taroize.html#%E5%9C%A8%E5%B0%8F%E7%A8%8B%E5%BA%8F-ide-%E6%98%BE%E7%A4%BA-createdata-%E9%94%99%E8%AF%AF)
    这里我们好像暂时没遇到这个问题，也不知道是哪个小程序IDE会有如此问题，先忽略了。
- 转换 wxParse 报错不存在文件☞[了解](https://nervjs.github.io/taro/docs/taroize.html#%E8%BD%AC%E6%8D%A2-wxparse-%E6%8A%A5%E9%94%99%E4%B8%8D%E5%AD%98%E5%9C%A8%E6%96%87%E4%BB%B6)
    这个问题我们要及时改正，在执行`taro conver`前先把wxParse.wxml中46行到128行的`wxParse1`修改为`wxParse0`
- 不支持 relations 和 Behavior[了解](https://nervjs.github.io/taro/docs/taroize.html#%E4%B8%8D%E6%94%AF%E6%8C%81-relations-%E5%92%8C-behavior)
    这个问题我们代码里好像没有这些组件，暂时忽略
- 转换 wepy 文件不成功[了解](https://nervjs.github.io/taro/docs/taroize.html#%E8%BD%AC%E6%8D%A2-wepy-%E6%96%87%E4%BB%B6%E4%B8%8D%E6%88%90%E5%8A%9Fr)
    这个问题我们肯定不存在，因为这个项目没有使用[wepy](https://github.com/Tencent/wepy),继续忽略。
现在看来，以上问题貌似都不存在，那么我们先回到这个报错
![clipboard.png](/img/bVbnDje)
凭我多年的copy经验，一定是文件不存在或者文件引用路径有问题。不慌，对比了原文件`taro convert`之后的taroConvert目录里边的wxParse,的确发现了小问题：[wxParse目录下的文件缺失](https://github.com/NervJS/taro/issues/1766),除了wxParse.js过来了，其他的都没有被转换。那就暴力一回，使出我的Copy大法，手动转换过去，并修改几处引用的相对路径，继续build。
接下来，在支付宝小程序开发者工具中打，不出意外能跑起来一个电商支付宝小程序雏形。
github地址☞☞[nideshop-alipay by taro convert](https://github.com/hu-qi/nideshop-alipay)

以上是我这个Copy攻城狮对使用`taro convert`转换原生微信小程序为支付宝小程序的一次微不足道的实践。

  [1]: /img/bVbnC6u