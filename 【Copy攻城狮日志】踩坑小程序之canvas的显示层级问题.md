*Created 2019-4-3 18:29:53 by [huqi](https://github.com/hu-qi)*
*Updated 2019-4-3 19:12:22 by [huqi](https://github.com/hu-qi)*

![clipboard.png](https://segmentfault.com/img/bVbqRBl?w=1080&h=1920)

↑开局一张图，故事全靠编↑

# 从一个需求说起
狼叔@i5ting[i5ting] 曾说过：“单纯讲技术进阶点意义不大，脱离场景都是耍流氓”。今天，依旧从一个需求说起。什么需求呢？一个二维码，一个二次确认弹窗。这里的二维码是前端生成的，二维码下边有个button，点击button调起自定义的弹窗组件。依旧是很简单的需求，但是对于“资深”的Copy攻城狮来说，除了布局，其他的就只能去Copy了。分析了一下可能需要的代码，就开始'刷刷刷'一顿CP(Copy&Paste)操作猛如虎，结果跑下代码发现error二百五。特别是真机跑的时候，问题特别多。像这次的问题，开发者工具上压根就发现不了，幸好习惯性真机预览，不然一通push就等着失业了。还是坑在基础不牢固，文档看得不深入，对小程序原生组件应该注意的事项把握不准，才会掉入这个非常基础的坑。

![clipboard.png](https://segmentfault.com/img/bVbqRyB?w=378&h=133)
(图片来源于网络)

# canvas生成二维码
通常来说，遇到这种类似的需要，我都会先找找被人造的轮子，尝试一下，有合适的就直接拿过来用了。这次用的是@yingye 大佬开源的[weapp-qrcode](https://github.com/yingye/weapp-qrcode),这个js应该是借鉴了[jquery-qrcode](https://github.com/jeromeetienne/jquery-qrcode) 和 [node-qrcode](https://github.com/soldair/node-qrcode),有兴趣的同学可以研究研究，生码的逻辑应该是类似的，只是小程序中没有DOM操作，都是利用canvas来实现的。具体怎么实现，各位看客可以直接看相关的源码或文档。我的实现：

wxml

```
<canvas style="width: 140px; height: 140px;" canvas-id="myQrcode"></canvas>
```
wxss

```
canvas{
  display: block;
  margin: 0rpx auto;  /** 居中 **/
}
```
js

``` 
    drawQrcode({
      width: 140,  // 必须，二维码宽度，与canvas的width保持一致
      height: 140, // 必须，二维码高度，与canvas的height保持一致
      x: 0, // 非必须，二维码绘制的 x 轴起始位置，默认值0
      y: 0, // 非必须，二维码绘制的 y 轴起始位置，默认值0
      canvasId: 'myQrcode', // 非必须，绘制的canvasId
      typeNumber: 10, // 非必须，二维码的计算模式，默认值-1
      text: '您的二维码内容',  // 必须，二维码内容
      callback(e) { // 非必须，绘制完成后的回调函数
        console.log('e: ', e)
      }
    })
```
二维码效果：

![clipboard.png](https://segmentfault.com/img/bVbqRDP?w=420&h=719)

# canvas使用限制
当我页面如上图一样。底部有个按钮。点击唤起自定义的弹窗组件，在开发者工具上呈现的效果十分正常。但是在真机上就会出现文字开头的不和谐现象。canvas直接覆盖住了自定义组件。通过翻阅文档，您会发现官方特别写出了**[Bug&Tip](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)**：
- 3.tip：请注意[原生组件使用限制](https://developers.weixin.qq.com/miniprogram/dev/component/native-component.html)。
- 4.bug: 避免设置过大的宽高，在安卓下会有crash的问题
然后点开原生组件使用限制，就会发现本B.U.G的根本原因了：
- 原生组件的层级是最高的，所以页面中的其他组件无论设置 z-index 为多少，都无法盖在原生组件上。
也就是说canvas会覆盖自定义的dialog组件。那么怎么解决呢？我的思路是“曲线救国”--将canvas转成image。一不做二不休，撸起袖子，开干！

![clipboard.png](https://segmentfault.com/img/bVbqREM?w=594&h=894)

# 将canvas转换成image
既然原生组件（[camera](https://developers.weixin.qq.com/miniprogram/dev/component/camera.html)、[canvas](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)、[focus时的input](https://developers.weixin.qq.com/miniprogram/dev/component/input.html)、[live-player](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html)、[live-pusher](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)、[map](https://developers.weixin.qq.com/miniprogram/dev/component/map.html)、[textarea](https://developers.weixin.qq.com/miniprogram/dev/component/textarea.html)、[video](https://developers.weixin.qq.com/miniprogram/dev/component/video.html)）这么牛逼，那就打压一下，去掉他们高贵的身份，豁免他们享有的特权，彻底ge他们的命，恢复他们的平民身份。按照这个思路，开始一步一步来实现
wxml
```
 <canvas wx:if="{{!renderImg}}"  style="width: 140px; height: 140px;" canvas-id="myQrcode"></canvas>
 <image wx:else mode="scaleToFill" class="image" style="width: 140px; height: 140px;" src="{{renderImg}}"></image>
```
js

```
    data: {
      renderImg: ''
    },
    onLoad: function(){
        drawQrcode({
          width: 140,  // 必须，二维码宽度，与canvas的width保持一致
          height: 140, // 必须，二维码高度，与canvas的height保持一致
          x: 0, // 非必须，二维码绘制的 x 轴起始位置，默认值0
          y: 0, // 非必须，二维码绘制的 y 轴起始位置，默认值0
          canvasId: 'myQrcode', // 非必须，绘制的canvasId
          typeNumber: 10, // 非必须，二维码的计算模式，默认值-1
          text: '您的二维码内容',  // 必须，二维码内容
          callback(e) { // 非必须，绘制完成后的回调函数
            console.log('e: ', e)
            if(e.errMsg == 'drawCanvas:ok') { // 新增转图片
              wx.canvasToTempFilePath({
                x: 0,
                y: 0,
                width: 140,
                height: 140,
                canvasId: 'myQrcode',
                success: function(res) {
                  me.setData({ renderImg: res.tempFilePath});
                }
              });   
            }
          }
        })
    }
```
以上将canvas替换成image，不过遇到闪烁的问题，这是wx:if特有的，这里通过取巧的办法，只改了canvas的样式：
wxss

```
canvas{
  display: block;
  margin: 0rpx -9999px;  /** 占位解决二维码闪屏 **/
}
image{
  display: block;
  margin: 0rpx auto;  /** 居中 **/
}
```
至此，已填了这个canvas显示层级过高的坑。

![clipboard.png](https://segmentfault.com/img/bVbqRIR?w=1080&h=1920)

**如您有更好的方案，欢迎提出指正！**
**如您觉得文章解决了您的问题，欢迎打赏!**