<!--
 * @Description: file content
 * @Author: huqi
 * @GitHub: https://github.com/hu-qi
 * @Email: me@huqi.me
 * @Date: 2019-05-08 18:53:52
 * @LastEditors: huqi
 * @LastEditTime: 2019-05-08 18:53:52
 -->

> Created by **[huqi](https://github.com/hu-qi)** at **2019-5-5 13:01:14**  
> Updated by **[huqi](https://github.com/hu-qi)** at **2019-5-20 15:57:37** 

### 前言
上个月月底@[D2开源组](https://juejin.im/user/57a48b632e958a006691b946) 开源了使用 D2Admin 适配 人人企业版(专业版) 的前端工程--[d2-admin-renren-security-enterprise](https://github.com/d2-projects/d2-admin-renren-security-enterprise),具体详情见☞[D2Admin 人人企业版适配发布](https://juejin.im/post/5cc69b406fb9a032297b08b6)。由于最近有开发后台管理系统的需求，加上其他诸多因素，如：想学习优秀的开源项目、刚好参加@[jsliang](https://juejin.im/user/584613ba128fe10058b3cf68) 组织的[暴走前端](https://github.com/LiangJunrong/document-library/blob/master/other-library/Monologue/GitHubRunawayRace.md)、之前项目使用过[renren-fast-vue](https://github.com/renrenio/renren-fast-vue)等等，于是乎萌生了根据commits学习了解[d2-admin](https://github.com/d2-projects/d2-admin)如何改造renren-security前端的想法。当然，也督促自己产出一篇相关的文章，来记录这次有趣的学习之旅。

### 前置准备
所谓“工欲善其事必先利其器”，连我这样的Copy攻城狮都要搭建的前端基础开发环境，都9102年啦，再没有node环境都没法进行前端开发了，再不济运行d2-admin的环境总该有吧！
- 安装环境   
这里请参考D2 Admin快速上手部分：[☞安装环境](https://doc.d2admin.fairyever.com/zh/learn-guide/getting-started.html#安装环境)
- Fork D2-Admin@1.6.18   
这里紧跟@[FairyEver](https://github.com/FairyEver) 大大的思路，基于D2-Admin@1.6.18 开发。当然也可以通过[D2 Admin CLI](https://github.com/d2-projects/d2-admin-cli)来初始化项目,具体操作参照：[☞下载项目](https://doc.d2admin.fairyever.com/zh/learn-guide/getting-started.html#%E4%B8%8B%E8%BD%BD%E9%A1%B9%E7%9B%AE)
- 了解D2Admin项目结构   
有过开发经历的同学在项目开发之前一般都有过项目结构搭建的经历，当然如果您不幸和我一样只会用别人搭建好的工程脚手架，那您一定会先了解整个项目目录结构，不然还真不知道源码要写在哪里。
    <details>
       <summary>项目结构</summary>

    ~~~
      ├─ docs                    // 文档
      ├─ packages                // 额外的包
      ├─ public                  // 公共文件
      ├─ src                     // 源码目录
      │  ├─ assets                 // 资源
      │  │  ├─ icons
      │  │  ├─ image
      │  │  ├─ library
      │  │  └─ style
      │  ├─ components             // 组件
      │  │  ├─ charts
      │  │  ├─ core
      │  │  └─ demo
      │  ├─ i18n                   // 多语言
      │  ├─ menu                   // 菜单
      │  ├─ mock                   // 模拟数据
      │  ├─ pages                  // 页面
      │  ├─ plugin                 // 插件
      │  ├─ router                 // 路由
      │  ├─ store                  // vuex
      │  ├─ utils
      │  ├─ App.vue
      │  └─ main.js
      ├─ tests                   // 测试文件
      ├─ .browserslistrc         // 浏览器兼容设置
      ├─ .env                    // 环境变量
      ├─ .env.development        // 开发环境变量
      ├─ .env.nomock             // nomock环境变量
      ├─ .env.travis             // 生成环境变量
      ├─ .eslintignore           // ESLint忽略
      ├─ .eslintrc.js            // ESLint配置
      ├─ .gitignore              // git忽略
      ├─ .postcssrc.js           // postcss配置
      ├─ .travis.yml             // 持续集成服务
      ├─ babel.config.js         // babel配置
      ├─ cdnrefresh-dirs.txt     // cdn设置
      ├─ jest.config.js          // jest设置
      ├─ LICENSE                 // 开源协议
      ├─ package-lock.json       // 包文件锁版本
      ├─ package.json            // 包文件
      ├─ qiniu-config            // 七牛云配置
      ├─ qshell                  // 七牛API服务命令行工具
      ├─ README.md
      |— README.zh.md                
      ├─ vue.config.js           // vue配置
    ~~~
    </details>
    
- 删除无关文件   
 删除.browserslistrc、.env.nomock、.env.travis 、.gitignore、.postcssrc.js、.travis.yml、cdnrefresh-dirs.txt 、package-lock.json、 qiniu-config 、qshell、README.zh.md、README.md、doc/image、package/\*。具体可查看：[☞删除暂时未用到模块](https://github.com/hu-qi/d2-admin-renren-security-study/commit/fa0e2ee4e5f5ee447bac4b33be81a36918958030)

- 修改package.json  
 移除暂时未用到的包,如多语言，这个版本将简化多语言目录结构，如图表库、富文本编辑、右键菜单等：   
 countup.js   
 echarts   
 github-markdown-css   
 highlight.js   
 marked   
 mockjs   
 simplemde   
 v-charts   
 v-contextmenu   
 vue-grid-layout
 vue-i18n   
 vue-json-tree-view   
 vue-splitpane  
 vue-ueditor-wra   
 @kazupon/vue-i18n-loader   
 删除build:nomock命令，增加环境变量文件.env、.env.production、.env.production.sit、.env.production.uat等。至此，可以通过```npm install ``` 或 ``` yarn ```来安装项目依赖，并通过```npm run dev```之类的指令运行项目，具体指令可查看  **package.json** 文件中 **scripts** 部分。

### 重写国际化
至于为什么要重写，要问大佬了。我也只能妄加揣测：简化结构！之前的结构是一个index.js+lang文件夹，lang文件夹里又包含多个语言文件夹，现在的结构直接了当--index.js+多个语言js文件。关于国际化我也只是很肤浅的了解，虽然之前接触过的项目也做过，里边坑的确挺多的，除了基本的翻译还要结合当地的文化习俗，这里就不展开讨论，搜索关键字**i18n**便有众多的解决方案。回到大佬@[FairyEver](https://github.com/FairyEver) 的源码，跟着他了解一下vue-i18n的使用：
- 安装依赖   
 ```bash
 npm install vue-i18n
 ```
 - main.js中引入
 ```js
 // ...

// i18n
import i18n from '@/i18n'

// ...

new Vue({
  i18n,
  // ...
)}
 ```
 - 新建语言包，构建js  
  核心代码：   
    <details>
       <summary>index.js</summary>

    ~~~js
    // 引入相关依赖及语言包
    import Vue from 'vue'
    import VueI18n from 'vue-i18n'
    import Cookies from 'js-cookie'
    // 附带引入element-ui的多语言切换
    import zhCNLocale from 'element-ui/lib/locale/lang/zh-CN'
    import zhTWLocale from 'element-ui/lib/locale/lang/zh-TW'
    import enLocale from 'element-ui/lib/locale/lang/en'
    // 引入语言包
    import zhCN from './zh-CN'
    import zhTW from './zh-TW'
    import enUS from './en-US'
    
    Vue.use(VueI18n)
    
    // 定义使用的语言
    export const messages = {
      'zh-CN': {
        '_lang': '简体中文',
        ...zhCN,
        ...zhCNLocale
      },
      'zh-TW': {
        '_lang': '繁體中文',
        ...zhTW,
        ...zhTWLocale
      },
      'en-US': {
        '_lang': 'English',
        ...enUS,
        ...enLocale
      }
    }
    
    // 默认从cookie中读取或设置为中文
    export default new VueI18n({
      locale: Cookies.get('language') || 'zh-CN',
      messages
    })
    ~~~
    </details>
    
    语言包以湾湾繁体为例：
    <details>
       <summary>zh-TW.js</summary>

    ~~~js
    // 定义语言对象
    const t = {}
    
    t.loading = '加載中...'
    
    // 构建对象
    t.brand = {}
    t.brand.lg = '人人權限企業版'
    t.brand.mini = '人人'
    
    // ...
    export default t
    ~~~
    </details>
    
- 使用   
    <details>
       <summary>App.vue</summary>

    ~~~js
    // 选择语言
    import Cookies from 'js-cookie'
    import { messages } from '@/i18n'
    export default {
      name: 'app',
      watch: {
        '$i18n.locale': 'i18nHandle'
      },
      created () {
        this.i18nHandle(this.$i18n.locale)
      },
      methods: {
        i18nHandle (val, oldVal) {
          Cookies('language', val)
          document.querySelector('html').setAttribute('lang', val)
          document.title = messages[val].brand.lg
          // 非登录页面，切换语言刷新页面
          if (this.$route.name !== 'login' && oldVal) {
            window.location.reload()
          }
        }
      }
    }
    ~~~
    </details>
    
   页面中使用，如：
   ```js
    // template
    {{ $t('login.motto.text') }}
    :placeholder="$t('login.form.placeholderUsername')"
    // script
    this.$t('login.motto.text')
    ```
- 检验成果   
实践是检验真理的唯一标准。
修改i18n/index.js 将locale改为湾湾繁体，就能直观的看到title的变化，（别问我为啥页面上的文字怎么没变化？因为写死为简体中文啦！）

![d2-admin-renren-security-enterprise-i18n](https://user-gold-cdn.xitu.io/2019/5/20/16ad4ae6c0a7a949?w=1611&h=836&f=png&s=84455)
注意：
实现vue-i18n+element-ui多语言切换需手动注册如，参考[element-ui国际化](https://element.eleme.io/#/zh-CN/component/i18n)：
```js
// i18n
import i18n from '@/i18n'
// Element
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// Element
Vue.use(ElementUI, {
  i18n: (key, value) => i18n.t(key, value)
})
```
文字部分全部修改为国际化后，就可以看到明显的效果啦：

![d2-admin-renren-security-enterprise-i18n](https://user-gold-cdn.xitu.io/2019/5/20/16ad4b29e25ec072?w=1609&h=840&f=png&s=81822)

### 多语言切换
既然有了国际化的基础，那么实现一个多语言切换的小功能应该是水到渠成。来看看@[FairyEver](https://github.com/FairyEver)是怎么教的！
偶然间看到d2-admin中的标签可以使用flex这个属性，感到很好奇。

![](https://user-gold-cdn.xitu.io/2019/5/20/16ad4b6889aa7ed7?w=1236&h=1001&f=png&s=191095)
flex，对于新世纪的前端开发来说最熟悉不过，但是标签上直接写flex属性，作为很水很水的老菜鸟却是孤落寡闻，不过职业病的直觉告诉我一定是跟flex布局有关。于是我按图索骥，先翻阅了一下package.json，里边果然找到一个[flex.css](https://github.com/lzxb/flex.css/blob/master/docs/zh-ch.md)的依赖包。大概实现怎样的效果呢？我的认知是通过标签的flex属性，无需写css即可实现flex布局，flex.css内部通过定义属性选择器样式来实现flex布局，更多关于flex.css请戳[☞flex.cc](https://github.com/lzxb/flex.css)。

这里通过elemen-ui的[el-dropdown](https://element.eleme.io/#/zh-CN/component/dropdown)实现,通过command事件修改语言设置
```html
<el-dropdown size="small" @command="command => $i18n.locale = command">
   <span class="page-login--content-header-side-text"><d2-icon name="language"/> {{ $t('login.language') }}</span>
   <el-dropdown-menu slot="dropdown">
      <el-dropdown-item v-for="(language, index) in $languages" :key="index" :command="language.value">{{ language.label }}</el-dropdown-item>
    </el-dropdown-menu>
</el
```
### 对接人人验证码
一般来说，做登录页的时候，我们或多或少会遇到验证码的需求，对了，这里的验证码指的是图形验证码。最简单的实践是直接拿后台给过来的图片直接渲染的在页面上，使用 **img标签** 或者 **background-image** 引入。之前做renren-fast-vue二次开发的时候用的img标签，这里用的背景图片，思路都一样：拿后台给的图片直接渲染。众所周知，Just do it！

定义获取[uuid](https://zh.wikipedia.org/wiki/%E9%80%9A%E7%94%A8%E5%94%AF%E4%B8%80%E8%AF%86%E5%88%AB%E7%A0%81)的工具函数:
```js
/**
 * @description [ renren ] 获取uuid
 */
util.getUUID = function () {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
    return (c === 'x' ? (Math.random() * 16 | 0) : ('r&0x3' | '0x8')).toString(16)
  })
}
```   
<details>
       <summary>使用uuid获取图形验证码</summary>
       
~~~html
<template slot="append">
  <div class="login-captcha" :style="{ backgroundImage: `url(${captchaPath})` }" @click="updateUUID" />
</template>
~~~
~~~js
    // 选择语言
    import Cookies from 'js-cookie'
    import { messages } from '@/i18n'
    export default {
      name: 'app',
      watch: {
        '$i18n.locale': 'i18nHandle'
      },
      created () {
        this.i18nHandle(this.$i18n.locale)
      },
      methods: {
        i18nHandle (val, oldVal) {
          Cookies('language', val)
          document.querySelector('html').setAttribute('lang', val)
          document.title = messages[val].brand.lg
          // 非登录页面，切换语言刷新页面
          if (this.$route.name !== 'login' && oldVal) {
            window.location.reload()
          }
        }
      }
    }
~~~
</details>


### axios及登录逻辑

![d2-admin-renren-security-enterprise-login](https://user-gold-cdn.xitu.io/2019/5/20/16ad4cc774873260?w=1508&h=828&f=gif&s=1126308)
自从摆脱了JQuery大法，阿贾克斯和我从此是陌生人，以至于面试官要我阐述阿贾克斯原理，我真是哑巴吃黄连，哦不，是哑口无言，一个以CP(Copy&Paste)为生的搬砖工，你们还指望他侃侃而谈什么原理什么底层？至于什么[axios](https://github.com/axios/axios)拦截，总之，这一块涉及到前后交互的知识点还是蛮多的，我也是七窍通灵六窍--一窍不通，勉勉强强解读一下大佬的封装：

  <details>
       <summary>axios简单封装</summary>

    // 引用相关依赖及方法
    import axios from 'axios'
    import { Message } from 'element-ui'
    import Cookies from 'js-cookie'
    import { isPlainObject } from 'lodash'
    import qs from 'qs'
    // import util from '@/libs/util'
    import router from '@/router'
    import store from '@/store'
    
    // 记录和显示错误
    function errorLog (error) {
      // 添加到日志
      store.dispatch('d2admin/log/push', {
        message: '数据请求异常',
        type: 'danger',
        meta: {
          error
        }
      })
      // 打印到控制台
      if (process.env.NODE_ENV === 'development') {
        // util.log.danger('>>>>>> Error >>>>>>')
        console.log(error)
      }
      // 显示提示
      Message({
        message: error.message,
        type: 'error',
        duration: 5 * 1000
      })
    }
    
    // 创建一个 axios 实例
    const service = axios.create({
      baseURL: process.env.VUE_APP_API,
      timeout: 1000 * 180, // 请求超时时间
      withCredentials: true // 当前请求为跨域类型时是否在请求中协带cookie
    })
    
    /**
     * 请求拦截
     */
    service.interceptors.request.use(
      config => {
        // 在请求发送之前做一些处理，如设置headers
        config.headers['Accept-Language'] = Cookies.get('language') || 'zh-CN'
        config.headers['token'] = Cookies.get('token') || ''
        // 默认参数
        var defaults = {}
        // 防止缓存，GET请求默认带_t参数
        if (config.method === 'get') {
          config.params = {
            ...config.params,
            ...{ '_t': new Date().getTime() }
          }
        }
        if (isPlainObject(config.data)) {
          // 纯粹对象解构赋值
          config.data = {
            ...defaults,
            ...config.data
          }
          if (/^application\/x-www-form-urlencoded/.test(config.headers['content-type'])) {
            // 序列化请求数据
            config.data = qs.stringify(config.data)
          }
        }
        return config
      },
      error => {
        // 发送失败
        console.log(error)
        return Promise.reject(error)
      }
    )
    
    /**
     * 响应拦截
     */
    service.interceptors.response.use(
      response => {
         // 处理响应
        if (response.data.code === 401 || response.data.code === 10001) {
          // clearLoginInfo()
          // alert('TODO clearLoginInfo')
          // TODO: 清除用户信息
          router.replace({ name: 'login' })
          return Promise.reject(response.data.msg)
        }
        if (response.data.code !== 0) {
          errorLog(new Error(response.data.msg))
          return Promise.reject(response.data.msg)
        }
        return response.data.data
      },
      error => {
        errorLog(error)
        return Promise.reject(error)
      }
    )
    
    export default service
</details>
登录的话，需要调用api，按照d2-admin的项目结构，在src/api下定义api接口，如sys.login.js:

```js
    import request from '@/plugin/axios'
    
    export function login (data) {
      return request({
        url: '/login',
        method: 'post',
        data
      })
    }
```
调用api进行登录：
```js
// ...
import { login } from '@api/sys.login'
// ...
submit () {
  this.$refs.loginForm.validate((valid) => {
    if (!valid) return
    login(this.form)
      .then(async res => {
        await this.login(res)
        this.$router.replace(this.$route.query.redirect || '/')
      })
      .catch(this.updateUUID)
  })
}
// ...
```
当然还需要对数据进行处理，比如登录状态持久化、设置vuex用户信息等等，这里暂时只做简单的处理，另外安利一个vscode插件(乳沟您恰巧用的宇宙第一神器)--[TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight),用来突出显示代码中的todo、fixme和其他注释，听说老司机都在用。有时，在将代码发布到生产环境之前，在编码时忘记查看添加的TODO。所以就有了这个拓展，提醒我们有一些笔记或者事情还没有完成。mark一下！

![d2-admin-renren-security-enterprise-TODO](https://user-gold-cdn.xitu.io/2019/5/20/16ad4cd3c75af38a?w=752&h=556&f=png&s=45729)

### 标准化cookie使用
作为后台管理系统，免不了涉及到cookie的使用，按照大佬的思路，定义了工具集函数并基于[js-cookie](https://github.com/js-cookie/js-cookie)二次封装了cookie。一般来说，cookie用得最多的就是get和set两个方法。
<details>
       <summary>cookie简单封装</summary>
       
~~~js
import Cookie from 'js-cookie'

/**
 * @description 存储 cookie 值
 * @param {String} name cookie name
 * @param {String} value cookie value
 * @param {Object} setting cookie setting
 */
export const cookieSet = function (name = 'default', value = '', cookieSetting = {}) {
  let currentCookieSetting = {
    expires: 1
  }
  Object.assign(currentCookieSetting, cookieSetting)
  Cookie.set(`d2admin-${process.env.VUE_APP_VERSION}-${name}`, value, currentCookieSetting)
}

/**
 * @description 拿到 cookie 值
 * @param {String} name cookie name
 */
export const cookieGet = function (name = 'default') {
  return Cookie.get(`d2admin-${process.env.VUE_APP_VERSION}-${name}`)
}

/**
 * @description 拿到 cookie 全部的值
 */
export const cookieGetAll = function () {
  return Cookie.get()
}

/**
 * @description 删除 cookie
 * @param {String} name cookie name
 */
export const cookieRemove = function (name = 'default') {
  return Cookie.remove(`d2admin-${process.env.VUE_APP_VERSION}-${name}`)
}
~~~
</details>
如图，能看到目前通过此次标准化封装之后存的cookie的name都加了**d2admin-**的前缀。

![d2-admin-renren-security-enterprise-cookie](https://user-gold-cdn.xitu.io/2019/5/20/16ad4d2de1512354?w=1754&h=716&f=png&s=71105)

### 防止过度点击
节流这个知识点我也是一直懵懵懂懂，经常和防抖混淆，理解不深刻，还只是停留在字面意思理解上：函数节流是指定时间间隔内只执行一次，函数防抖是频繁触发只有间隔超过指定时间间隔才执行。请参考[debouncing-throttling-explained-examples](https://css-tricks.com/debouncing-throttling-explained-examples/)
这里简单粗暴的用了[lodash](https://github.com/lodash/lodash)--一个一致性、模块化、高性能的 JavaScript 实用工具库。。
lodash中包含一系列数组、数字、对象、字符串等操作的API，当然还有一些常用的工具函数如节流(throttle)、防抖(debounce)。
```js
// ...
import { debounce } from 'lodash'
// ...
submit: debounce(function () {
  // ...
}, 1000, { 'leading': true, 'trailing': false })  
// _.debounce(func, [wait=0], [options={}])  
// options.leading 与|或 options.trailing 决定延迟前后是先调用后等待,还是先等待后调用
// ...
```
前后对比:   
未处理的时候，触发的请求令人发指！
![d2-admin-renren-security-enterprise-debounce](https://user-gold-cdn.xitu.io/2019/5/20/16ad4d4ebd835cad?w=1503&h=798&f=gif&s=3302964)

处理之后，控制台让人感觉很清爽
![](https://user-gold-cdn.xitu.io/2019/5/20/16ad4d690eec71f4?w=1503&h=798&f=gif&s=3456950)

### 关于全局配置
项目做得太少了，尤其还不会java，对网站的全局配置这一块的理解还停留在初级认知阶段。一般来说，在网页开发中往往一些版本控制、CDN静态资源、api接口地址、常用的公共变量等都会写到window下面并提升至首页方便管理，如网易一些爆款的H5中这种手法非常常见。在我之前使用开源的renren-fast-vue中这种手法更是大量运用，这次学习d2-admin也借鉴一下这种全局变量的使用(挂载变量一时爽，一直挂载一直爽,小心别翻车了)。先不管了，一顿Copy操作猛如虎，定睛一看，注释占了百分之九十五！当然，代码了瞬间有了后端的痕迹，不过在本项目 public/index.html中使用的模板语法来源于[ lodash 模板插入](https://lodash.com/docs/4.17.11#template),和public文件夹相关的内容可以去翻翻d2-admin文档关于[cli 和 webpack 配置](https://doc.d2admin.fairyever.com/zh/sys-cli3-webpack/)部分，这里就不再赘述，总之，万丈高楼平地起，基础建设很重要！
<details>
       <summary>全局配置window.SITE_CONFIG</summary>
       
~~~js
  window.SITE_CONFIG = {};
  window.SITE_CONFIG['version'] = '<%= process.env.VUE_APP_VERSION %>';     // 版本
  window.SITE_CONFIG['nodeEnv'] = '<%= process.env.VUE_APP_NODE_ENV %>';    // node env
  window.SITE_CONFIG['apiURL'] = '<%= process.env.VUE_APP_API %>';          // api请求地址
  window.SITE_CONFIG['storeState'] = {};                                    // vuex本地储存初始化状态（用于不刷新页面的情况下，也能重置初始化项目中所有状态）
  window.SITE_CONFIG['contentTabDefault'] = {                               // 内容标签页默认属性对象
    'name': '',                                                             // 名称, 由 this.$route.name 自动赋值（默认，名称 === 路由名称 === 路由路径）
    'params': {},                                                           // 参数, 由 this.$route.params 自动赋值 
    'query': {},                                                            // 查询参数, 由 this.$route.query 自动赋值 
    'menuId': '',                                                           // 菜单id（用于选中侧边栏菜单，与this.$store.state.sidebarMenuActiveName进行匹配）
    'title': '',                                                            // 标题
    'isTab': true,                                                          // 是否通过tab展示内容?
    'iframeURL': ''                                                         // 是否通过iframe嵌套展示内容? (以http[s]://开头, 自动匹配)
  };
  window.SITE_CONFIG['menuList'] = [];                                      // 左侧菜单列表（后台返回，未做处理）
  window.SITE_CONFIG['permissions'] = [];                                   // 页面按钮操作权限（后台返回，未做处理）
  window.SITE_CONFIG['dynamicRoutes'] = [];                                 // 动态路由列表
  window.SITE_CONFIG['dynamicMenuRoutes'] = [];                             // 动态(菜单)路由列表
  window.SITE_CONFIG['dynamicMenuRoutesHasAdded'] = false;                  // 动态(菜单)路由是否已经添加的状态标示（用于判断是否需要重新拉取数据并进行动态添加操作）
~~~
</details>

大厂某H5案例中全局配置挂载
![d2-admin-renren-security-enterprise-windowConfig](https://user-gold-cdn.xitu.io/2019/5/20/16ad4da00fd8f2f4?w=1020&h=619&f=png&s=201188)

### 前端轻量级web进度条-[NProgress](https://github.com/rstacruz/nprogress/)
感觉像我这种资深Copy级别的零级工程师，对于一些炫酷的页面效果，除了感叹"牛掰",就是一顿复制粘贴。当我看到d2-admin使用的NProgress是0.2.0版本的时候，我以为是个比较新的第三方库，抱着刨根到底的学习心态，我点开了NProgress的github仓库，看到作者[@rstacruz](https://github.com/rstacruz)的主页，不禁赞叹："牛掰!"。说来也巧，@justjavac 大神翻译的速查表就源自作者的[cheatsheets](https://github.com/rstacruz/cheatsheets)。虽然NProgress诞生于2013年8月,(那时我还在学校把妹，对js的了解还只是不小心按到F12),[@rstacruz](https://github.com/rstacruz)对她的维护长达5年之久，目前有18.8K的star，而[@rstacruz](https://github.com/rstacruz)本尊更是值得我辈瞻仰的大神。  
![d2-admin-renren-security-enterprise-rstacruz](https://user-gold-cdn.xitu.io/2019/5/20/16ad4dbf9eaf79fe?w=1265&h=843&f=png&s=197309)
来看看NProgress怎么使用：一行代码实现web进度条。   

```js
//...
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'
//...
NProgress.start()
//...
NProgress.done()
```
NProgress的实现原理也很好理解，源码比较简洁，大概是加载开始调用start，加载完成调用done，至于加载进度、具体加载到哪了，都不关心，中间状态是随机的进度，从源码中看到大概加载到99.4%的位置就停了。
<details>
       <summary>NProgress核心源码</summary>
       
~~~js
  NProgress.inc = function(amount) {
    var n = NProgress.status;

    if (!n) {
      return NProgress.start();
    } else if(n > 1) {
      return;
    } else {
      if (typeof amount !== 'number') {
        if (n >= 0 && n < 0.2) { amount = 0.1; }
        else if (n >= 0.2 && n < 0.5) { amount = 0.04; }
        else if (n >= 0.5 && n < 0.8) { amount = 0.02; }
        else if (n >= 0.8 && n < 0.99) { amount = 0.005; }
        else { amount = 0; }
      }

      n = clamp(n + amount, 0, 0.994);
      return NProgress.set(n);
    }
  };
  //...
    /**
   * Helpers
   */

  function clamp(n, min, max) {
    if (n < min) return min;
    if (n > max) return max;
    return n;
  }
~~~
</details>

感兴趣的同学可以看看源码学习学习！[☞nprogress.js](https://github.com/rstacruz/nprogress/blob/master/nprogress.js)

### iframe的支持
在d2-admin中，其实是有实现iframe类型的内容页组件的-- [d2-container-frame](https://github.com/d2-projects/d2-admin/blob/804dbed41082669b1737b97d47cb481e372766ef/src/components/d2-container-frame/index.vue),从源码来看，是iframe是嵌套在d2-container组件中的，利用绝对定位实现iframe充满d2-container盒子。
<details>
       <summary>d2-container-frame简单实现</summary>
       
~~~js
<template>
  <d2-container v-bind="$attrs">
    <iframe
      class="d2-container-frame"
      :src="src"
      frameborder="0"/>
  </d2-container>
</template>

<script>
export default {
  name: 'd2-container-frame',
  props: {
    src: {
      type: String,
      required: false,
      default: 'https://doc.d2admin.fairyever.com/zh/'
    }
  }
}
</script>

<style lang="scss" scoped>
.d2-container-frame {
  position: absolute;
  top: 0px;
  left: 0px;
  height: 100%;
  width: 100%;
}
</style>
~~~
</details>

在改造renren的项目中，大佬巧妙的利用组装route的方式，实现了iframe单独渲染，具体可以看下源码：[☞支持 iframe 加载方式](https://github.com/d2-projects/d2-admin-renren-security-enterprise/commit/ab986b4e52f9309622da5e64e7f0e02c13062308)：
```js
// ...
// 组装路由
var route = {
  path: '',
  component: null,
  name: '',
  meta: {
    ...window.SITE_CONFIG['contentTabDefault'],
    menuId: menuList[i].id,
    title: menuList[i].name
  }
}
// ...
route['path'] = route['name'] = `i-${menuList[i].id}`
route['meta']['iframeURL'] = URL
route['component'] = {
  render (h) {
    return h('d2-container', {}, [
      h('iframe', {
        style: {
          position: 'absolute',
          top: '0px',
          left: '0px',
          height: '100%',
          width: '100%'
        },
        attrs: {
          src: URL,
          frameborder: 0
        }
      })
    ])
  }
}
// ...

```
### 后记
源码虽然没有细看，不过还是根据commits提交记录，粗略的一步一步copy实现了一番。整个过程还是很有趣的，毕竟算是参与了开源，还给大佬提了issue，捉了bug。但是，总得来说，还有很多知识点没细看，如vue的mixins、众多页面的具体实现、iconfont的使用、Vuex的使用、自定义皮肤的实现、顶部菜单栏的实现等等，期间也遇到一些编译上的问题，如el-table的坑[☞Error: if there's nested data, rowKey is required.](https://segmentfault.com/a/1190000019220574)。感觉整个过程还学的不踏实，很多知识点只是一搜带过，可能还是项目做少了。路漫漫其修远，慢慢摸索吧。
HR的领导来电话催回家了，匆匆落笔，结束此篇，江湖再见！