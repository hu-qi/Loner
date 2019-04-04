*Created 2019-4-4 22:02:27 by [huqi](https://github.com/hu-qi)*    
*Updated 2019-4-4 23:12:34 by [huqi](https://github.com/hu-qi)*


![clipboard.png](https://segmentfault.com/img/bVbqUHD?w=1164&h=834)
↑开局一张图，故事全靠编↑
# 本地资源无法通过 WXSS 获取
都9102年了，我居然还会犯如此低级的错误。不经想起去年犯的一个更低级的错误，事情的经过是这样的，去年@肖蜀黍 在某个群里丢了一个小程序链接--[tell心语](https://minapp.com/miniapp/8080/),这个小程序本身就具有传奇色彩，背后的故事更是感动人心，就是现实版的解忧杂货店；主要的功能是写信，也就是文字输入。然后，我居然脑残地去测试xss！！！不学无术，还要自命不凡，像我这样的没被祭天就是万幸了。这次，又是基本的常识都没掌握，直接淹死在浅坑里。**background-image：可以使用网络图片，或者 base64，或者使用<image/>标签。**这个是常识，连入门级小程序员都知道的。那我究竟写了个什么B.U.G？毫无疑问，一定是在BG中直接引用了本地图片。
乳此低级的错误，一定要贴出来，示众以鞭策！

```
.refresh-icon{
  background: url('refresh.svg');
}
.del-icon{
  background: url('del.svg');
}
```
# 获取iconfont的svg图
作为老司机的“幼儿班程序员”，应该是没有资格拿到切好的图标了，没办法，技不如人，只能自己动手去啥都有的网上找找。关于图标，我最先想到的是[阿里巴巴矢量图标库](https://www.iconfont.cn/home/index)，这个由阿里妈妈MUX倾力打造的矢量图标管理、交流平台，设计师可以将图标上传到这个平台，用户可以自定义下载多种格式的icon，平台也可将图标转换为字体，便于前端工程师自由调整与调用。虽然可以将图标转化为字体应用，但对于我来说，就使用那么几个图标，实在是不想引用一大堆css、ttf等文件，只想用下svg。具体怎么操作，胸中自然有了竹子。
- 搜索和UI图一模一样的图标，建议按照英文关键字查询，如del、refresh等
- 点击下载进入下载模态详情页，选择合适的颜色下载svg

![clipboard.png](https://segmentfault.com/img/bVbqUVQ?w=1892&h=936)

# 转换svg为background
既然官方文档说了，不让直接引用本地图片，但给了三条路，那我就随便远一条喽，反正我不想用网络图片，我也不想用image标签，那就只有转成base64喽，至于什么是base64，我也不知道，那就超度一下喽：☛[base64](https://baike.baidu.com/item/base64/8545775?fr=aladdin)。但是怎么快速将svg转换成这个base64甚至直接输出成css样式呢？我说，首先您得有工具得到svg源码，我用vscode，直接打开svg就是svg源代码；然后转base64，偶然发现了国外大佬在[codepan上的在线实现](https://codepen.io/jakob-e/pen/doMoML/),文章的话可以参考下[“优化数据uris中的svgs” ](https://codepen.io/tigt/post/optimizing-svgs-in-data-uris),我特意fork了一份来学习，感兴趣的可以看下[源码](https://codepen.io/hu-qi/pen/MRKOOG)。有了这个工具，svg生成background也就是我专门干的事=copy&paste
- 获取svg源码
- 生成background

![clipboard.png](https://segmentfault.com/img/bVbqUYA?w=1854&h=884)

# 重写background
既然base64已经手到擒来了，那么实现图标按钮还会远吗，来来来，有请代码说话：
超级简单！！！搜衣滋！

```
.my-icon{
  background-size: cover;
  display: inline-block;
  width: 50rpx;
  height: 50rpx;
  vertical-align: middle;
  margin-right: 4px;
}
.refresh-icon{
  background-image: url("data:image/svg+xml,%3C?xml version='1.0' standalone='no'?%3E%3C!DOCTYPE svg PUBLIC '-//W3C//DTD SVG 1.1//EN' 'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'%3E%3Csvg t='1554354671724' class='icon' style='' viewBox='0 0 1024 1024' version='1.1' xmlns='http://www.w3.org/2000/svg' p-id='1543' xmlns:xlink='http://www.w3.org/1999/xlink' width='200' height='200'%3E%3Cdefs%3E%3Cstyle type='text/css'%3E%3C/style%3E%3C/defs%3E%3Cpath d='M936.571429 603.428571q0 2.857143-0.571429 4-36.571429 153.142857-153.142857 248.285715T509.714286 950.857143q-83.428571 0-161.428572-31.428572T209.142857 829.714286l-73.714286 73.714285q-10.857143 10.857143-25.714285 10.857143t-25.714286-10.857143-10.857143-25.714285v-256q0-14.857143 10.857143-25.714286t25.714286-10.857143h256q14.857143 0 25.714285 10.857143t10.857143 25.714286-10.857143 25.714285l-78.285714 78.285715q40.571429 37.714286 92 58.285714t106.857143 20.571429q76.571429 0 142.857143-37.142858t106.285714-102.285714q6.285714-9.714286 30.285714-66.857143 4.571429-13.142857 17.142858-13.142857h109.714285q7.428571 0 12.857143 5.428572t5.428572 12.857142z m14.285714-457.142857v256q0 14.857143-10.857143 25.714286t-25.714286 10.857143h-256q-14.857143 0-25.714285-10.857143t-10.857143-25.714286 10.857143-25.714285l78.857142-78.857143q-84.571429-78.285714-199.428571-78.285715-76.571429 0-142.857143 37.142858T262.857143 358.857143q-6.285714 9.714286-30.285714 66.857143-4.571429 13.142857-17.142858 13.142857H101.714286q-7.428571 0-12.857143-5.428572T83.428571 420.571429v-4q37.142857-153.142857 154.285715-248.285715T512 73.142857q83.428571 0 162.285714 31.714286T814.285714 194.285714l74.285715-73.714285q10.857143-10.857143 25.714285-10.857143t25.714286 10.857143 10.857143 25.714285z' p-id='1544' fill='%23ffffff'%3E%3C/path%3E%3C/svg%3E");
}
.del-icon{
  background-image: url("data:image/svg+xml,%3C?xml version='1.0' standalone='no'?%3E%3C!DOCTYPE svg PUBLIC '-//W3C//DTD SVG 1.1//EN' 'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'%3E%3Csvg t='1554355910565' class='icon' style='' viewBox='0 0 1024 1024' version='1.1' xmlns='http://www.w3.org/2000/svg' p-id='2306' xmlns:xlink='http://www.w3.org/1999/xlink' width='200' height='200'%3E%3Cdefs%3E%3Cstyle type='text/css'%3E%3C/style%3E%3C/defs%3E%3Cpath d='M817.968553 215.897142l-169.357176 0 0-58.869782c0-25.391297-20.657482-46.048779-46.048779-46.048779l-181.125197 0c-25.391297 0-46.048779 20.657482-46.048779 46.048779l0 58.869782-169.357176 0c-25.391297 0-46.048779 20.657482-46.048779 46.048779l0 71.631434c0 25.391297 20.657482 46.048779 46.048779 46.048779l28.321022 0 0 425.947112c0 59.246359 48.200792 107.447151 107.447151 107.447151l340.40076 0c59.246359 0 107.447151-48.200792 107.447151-107.447151L789.647531 379.626133l28.321022 0c25.391297 0 46.048779-20.657482 46.048779-46.048779l0-71.631434C864.017332 236.554624 843.35985 215.897142 817.968553 215.897142zM426.553932 162.14389l170.892135 0 0 53.753251-170.892135 0L426.553932 162.14389zM738.482221 805.574269c0 31.033807-25.248034 56.281841-56.281841 56.281841L341.79962 861.85611c-31.033807 0-56.281841-25.248034-56.281841-56.281841L285.517779 379.626133l452.964442 0L738.482221 805.574269zM812.852022 328.460824l-601.704045 0 0-61.398372 203.227588 0c2.302439 0.356111 4.66116 0.542352 7.061836 0.542352l181.125197 0c2.400676 0 4.759397-0.186242 7.062859-0.542352l203.226564 0L812.852022 328.460824zM513.023306 783.320429c14.128789 0 25.582655-11.453866 25.582655-25.582655l0-288.572348c0-14.128789-11.453866-25.582655-25.582655-25.582655-14.128789 0-25.582655 11.453866-25.582655 25.582655l0 288.572348C487.440651 771.866562 498.894518 783.320429 513.023306 783.320429zM645.541459 783.320429c14.128789 0 25.582655-11.453866 25.582655-25.582655l0-288.572348c0-14.128789-11.453866-25.582655-25.582655-25.582655s-25.582655 11.453866-25.582655 25.582655l0 288.572348C619.958804 771.866562 631.41267 783.320429 645.541459 783.320429zM380.505154 783.320429c14.128789 0 25.582655-11.453866 25.582655-25.582655l0-288.572348c0-14.128789-11.453866-25.582655-25.582655-25.582655s-25.582655 11.453866-25.582655 25.582655l0 288.572348C354.922499 771.866562 366.376365 783.320429 380.505154 783.320429z' p-id='2307' fill='%23ffffff'%3E%3C/path%3E%3C/svg%3E");
}
```
附上效果图：

![clipboard.png](https://segmentfault.com/img/bVbqUYZ?w=1080&h=1920)

# svg转换核心源码

```
//  用于创建优化的svg url的函数
//  Version: 1.0.6
@function svg-url($svg){
    //
    //  补齐命名空间
    //
    @if not str-index($svg,xmlns) {
        $svg: str-replace($svg, '&ltsvg','&ltsvg xmlns="http://www.w3.org/2000/svg"');   
    }        
    //    
    //  避免一大块的字符串
    //  抛出“堆栈级别太深”错误
    //     
    $encoded:'';
    $slice: 2000;
    $index: 0;
    $loops: ceil(str-length($svg)/$slice);
    @for $i from 1 through $loops {
        $chunk: str-slice($svg, $index, $index + $slice - 1); 
        //
        //   编码
        //
        $chunk: str-replace($chunk, '"', '\'');
        $chunk: str-replace($chunk, '%', '%25');
        $chunk: str-replace($chunk, '#', '%23');       
        $chunk: str-replace($chunk, '{', '%7B');
        $chunk: str-replace($chunk, '}', '%7D');         
        $chunk: str-replace($chunk, '&lt;', '%3C');
        $chunk: str-replace($chunk, '&gt;', '%3E');
        
        // 
        //    预计列表 
        //
        //    保持大小并缩短编译时间
        //    ... 只添加记录的失败 
        // 
        //  $chunk: str-replace($chunk, '&', '%26');        
        //  $chunk: str-replace($chunk, '|', '%7C');
        //  $chunk: str-replace($chunk, '[', '%5B');
        //  $chunk: str-replace($chunk, ']', '%5D');
        //  $chunk: str-replace($chunk, '^', '%5E');
        //  $chunk: str-replace($chunk, '`', '%60');
        //  $chunk: str-replace($chunk, ';', '%3B');
        //  $chunk: str-replace($chunk, '?', '%3F');
        //  $chunk: str-replace($chunk, ':', '%3A');
        //  $chunk: str-replace($chunk, '@', '%40');
        //  $chunk: str-replace($chunk, '=', '%3D');      
        
        $encoded: #{$encoded}#{$chunk};
        $index: $index + $slice; 
    }
    @return url("data:image/svg+xml,#{$encoded}");   
}
        
//  Background svg mixin          
@mixin background-svg($svg){
    background-image: svg-url($svg);        
}        
            
//  替换字符串中的字符的辅助函数
@function str-replace($string, $search, $replace: '') {
    $index: str-index($string, $search); 
    @return if($index, 
        str-slice($string, 1, $index - 1) + $replace + 
        str-replace(str-slice($string, $index + 
        str-length($search)), $search, $replace), 
        $string); 
}              
```

总算是又get了一个知识点，最近做小程序，遇到的难题还是挺多的，比如还没有解决的**wx.redirectTo闪屏问题**，有大佬要是恰好遇到过类似的坑，欢迎多多指教！
