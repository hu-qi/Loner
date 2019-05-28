<!--
 * @Description: file content
 * @Author: huqi
 * @GitHub: https://github.com/hu-qi
 * @Email: me@huqi.me
 * @Date: 2019-05-21 14:09:00
 * @LastEditors: huqi
 * @LastEditTime: 2019-05-28 16:04:39
 -->
### 前言
最近在学习React Native，准确的说是学习Copy React Native，找了一圈的资料，发现教程还是很多的。虽然我已将React Native官方文档(中文)粗略的过了一遍，动手复制粘贴了一些示例代码，但是印象非常淡薄，以至于在提交一些技术预研报告的时候还出了大洋相，比如对link指令不熟悉……不管那么多了，大半年没做项目了，实在是找不着方向了，既然现在要储备React Native的技术，那就好好学吧，自学都学不会的话那就继续Copy吧！本次学习的是3年前的一个开源项目--[30-days-of-react-native](https://github.com/fangwei716/30-days-of-react-native),酒，是陈年的好；代码，就不一定了。那这次新瓶装旧酒吧。

### 前置准备 step0
安装react-native cli

初始化



初次运行


题外话：同事说他们装React Native的环境装得很是郁闷，各种问题，但是mac下装起来非常得心应手，本人window感觉还可以，就是本本比较烫。苦于没有mac环境，本次学习以```react-native run-android```为主,目前除了项目运行慢以外，其他还能接受。


打包apk
详情请查看[☞官方文档](https://facebook.github.io/react-native/docs/signed-apk-android)
至于为什么要这这里先提打包，因为我遇到了一个坑：在做秒表功能的时候在安卓模拟器上点击事件响应慢，导致我怀疑代码哪里出bug了，于是想打包看看实际效果，结果喜出望外--点击事件响应很灵敏。具体是什么原因造成的，姑且认为是模拟器和真机的差异导致的。

### home页准备
### day1--秒表
效果：

用到插件 

坑：
f:\learn\react\30-days-of-react-native\node_modules\react-native\Libraries\Core\ExceptionsManager.js:82 Warning: ViewPagerAndroid has been extracted from react-native core and will be removed in a future release. It can now be installed and imported from '@react-native-community/viewpager' instead of 'react-native'. See https://github.com/react-native-community/react-native-viewpager
Deprecated. Use react-native-community/react-native-viewpager instead.