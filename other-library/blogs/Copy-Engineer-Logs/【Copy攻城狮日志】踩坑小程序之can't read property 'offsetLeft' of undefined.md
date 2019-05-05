
*Created by **[huqi](https://github.com/hu-qi)** at 2019-4-2 22:17:34*    
*Updated by **[huqi](https://github.com/hu-qi)** at 2019-4-2 23:17:34*

![clipboard.png](https://segmentfault.com/img/bVbqOLH?w=1526&h=818)

↑开局一张图，故事全靠编↑

# 从一个需求说起
接触过小程序的同学应该都接触过这样一个需求：点击列表页的某一项，进入详情页。同样，今天我也遇到这样一个需求，其实很简单的一个需求，无非就是一个tap事件加dataset传参实现路由带参数跳转到详情页。以前开发小程序的时候，也处理过这样的需求，本来应该是得心应手的。不过，可能是Copy别人代码Copy得太多太久太深，也从来没自主去想过别人为什么这样写、换种方式要怎样写、为什么换种方式就会报错等等诸如此类的问题，更别说去熟读开源源码，甚至自己造轮子。有时候反思，自己入行这么多年了，资质依旧平平，别说造轮子，就算是把别人轮子拿过来安上，都能整出一堆B.U.G。就比如开头的图片上，用的是鹅厂旗下某著名公司的豪华套餐，居然被我用得翻车了！--**TypeError: Cannot read property 'offsetLeft' of undefined !!!**简直了，还是只能怪自己技术太low了。

![clipboard.png](https://segmentfault.com/img/bVbqOOk?w=549&h=367)
（图片来源于网络）

# [提问的智慧](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)
自从朋友给了我一个SS的IP和密码，现在我一有问题就是直接google开干。在我看来，与其把问题抛到各种广告满天飞的技术群或者丢给朋友圈里边的大佬，倒不如自己先动手解决，哪怕是尝试了所有的答案，至少对问题会有更深的理解，以后面试中遇到面试官问您在项目中遇到过什么问题之类的，因为经过自己的一番搜索加实践，一般印象会深刻很多。反而别人直接告诉您答案的，可能您的成本更小，但是收获甚微。根据以往的经验，遇到问题，自己动手，是更接近答案的唯一出路。或许您在开发中，遇到了某些问题，您通过一些途径解决了这个问题，然后，您又记录了下来，后续您遇到同样的问题，应该是可以迎刃而解的。如果您还把解决方案分享出来了，您简直是在造福人类。后来者，托您的福，更快的解决了同样的问题。

![clipboard.png](https://segmentfault.com/img/bVbqOQu?w=954&h=397)

# 尝试方案1--重启开发者工具
[can't read property 'offsetLeft' of undefined #1132](https://github.com/NervJS/taro/issues/1132)
这是来自全球最大的同性交友网站GitHub上的一个issue，是由@yuwanlin 在一套遵循 React 语法规范的多端统一开发框架[Taro](https://github.com/NervJS/taro)中提出来的。根据当时的情境，是在微信开发者工具中删掉该小程序然后重新载入就解决了，大家给出的结论是微信小程序开发者工具的B.U.G。(注：该操作不会删除文件，请放心使用)--但是，我按照楼主的说法操作了一遍，结果然并卵，还是原来的B.U.G，还是一样的报错。
**该方案失败**
![clipboard.png](https://segmentfault.com/img/bVbqOSQ?w=1103&h=535)

# 尝试方案2--外层加view
[自定义组件在首次点击后会报错](https://developers.weixin.qq.com/community/develop/doc/0002c47de9c208f59ce6028a25b400?highLine=Cannot%2520read%2520property%2520%27offsetLeft%27%2520of%2520undefined)
@欧新志 这个小咯咯在2018-06-14向微信社区提出了类似的问题，他那个是自定义组件在点击之后出现了和我同款的B.U.G，而且也是存在嵌套子组件。评论中各位大神给出的答案是嵌套view。我也尝试了，试着加了一层view，但是问题依旧存在。不过我感还是和嵌套的子组件有关。于是，我各种尝试终于找到了一个方案。

> 第一次滚动和点击的时候都有这个报错,

> 下面是报错时的组件wxml

 >  <view class="wraper" bindtap="onClick">

 >      <slot></slot>

 >  </view>

> 如果换成下面这样就不报错了

> <view>

> <view class="wraper" bindtap="onClick">

>       <slot></slot>

>   </view>

> </view>

# 解决方案3--tap事件加在子组件里面
原代码：

```
    <block wx:for="{{itemList}}" wx:key="key" wx:code="{{item}}">
      <view style="margin-top: 15px" bindtap="toDetail">
        <dgd-preview>
          <!--常规 preview-list 控件  -->
          <view class="dgd-preview-list"  data-item="{{item}}">
            <dgd-preview-item label="服务中心名称" style="color:#000;">
              {{item.name}}
            </dgd-preview-item>
            <dgd-preview-item label="预约业务" style="color:#000;">
              {{item.business}}
            </dgd-preview-item>
            <dgd-preview-item label="预约时间" style="color:#000;">
              {{item.time}}
            </dgd-preview-item>
            <dgd-preview-item label="预约状态" style="color:#000;">
              {{item.status}}
            </dgd-preview-item>
          </view>
        </dgd-preview>
      </view>
    </block>
```

修改之后：

```
    <block wx:for="{{itemList}}" wx:key="key" wx:code="{{item}}">
      <view style="margin-top: 15px">
        <dgd-preview>
          <!--常规 preview-list 控件  -->
          <view class="dgd-preview-list" bindtap="toDetail" data-item="{{item}}">
            <dgd-preview-item label="服务中心名称" style="color:#000;">
              {{item.name}}
            </dgd-preview-item>
            <dgd-preview-item label="预约业务" style="color:#000;">
              {{item.business}}
            </dgd-preview-item>
            <dgd-preview-item label="预约时间" style="color:#000;">
              {{item.time}}
            </dgd-preview-item>
            <dgd-preview-item label="预约状态" style="color:#000;">
              {{item.status}}
            </dgd-preview-item>
          </view>
        </dgd-preview>
      </view>
    </block>
```
只是把方法挂载到了不同的位置，确实截然不同的效果。看来接下来应该再研究一下小程序的组件。