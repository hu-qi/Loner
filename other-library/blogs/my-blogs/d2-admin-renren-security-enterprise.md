  # D2-Admin实战renren-security

## 前置准备
- 前端开发环境
[](https://doc.d2admin.fairyever.com/zh/learn-guide/getting-started.html#%E5%AE%89%E8%A3%85%E7%8E%AF%E5%A2%83)
- fork D2-Admin 1.6.18
- 了解d2Admin项目结构
<details>
   <summary>项目结构</summary>
   ```
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
   ```
</details>


- 删除无关文件
删除.browserslistrc、.env.nomock、.env.travis 、.gitignore、.postcssrc.js、.travis.yml、cdnrefresh-dirs.txt 、package-lock.json、 qiniu-config 、qshell、README.zh.md、README.md、doc/image、package/\*、 


- 修改package.json
去除暂时未用到的包
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
删除build:nomock命令

- 去除暂时未用到的模块
如多语言，这个版本将简化多语言目录机构；
图表库、富文本编辑等

- 增加环境变量
.env、.env.production、.env.production.sit、.env.production.uat


- 重写国际化
至于为什么要重写，要问大佬了。我也只能妄加揣测：简化结构！之前的结构是一个index.js+lang文件夹，lang文件夹里又包含多个语言文件夹，现在的结构直接了当--index.js+多个语言js文件。关于国际化我也只是很肤浅的了解，虽然之前接触过的项目也做过，里边坑的确挺多的，除了基本的翻译还要结合当地的文化习俗，这里就不展开讨论，搜索关键字**i18n**便有众多的解决方案。回到大佬@FairyEver 的源码，跟着他了解一下vue-i18n的使用：
1. 安装依赖
`npm install vue-i18n`
2. main.js中引入
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
3. 新建语言包，构建js
核心代码：
index.js
```js
// 引入相关依赖及语言包
import Vue from 'vue'
import VueI18n from 'vue-i18n'
import Cookies from 'js-cookie'
// 附带引入element-ui的多语言切换
import zhCNLocale from 'element-ui/lib/locale/lang/zh-CN'
import zhTWLocale from 'element-ui/lib/locale/lang/zh-TW'
import enLocale from 'element-ui/lib/locale/lang/en'

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
```
语言包以湾湾繁体为例
```js
// 定义语言对象
const t = {}

t.loading = '加載中...'

// 构建对象
t.brand = {}
t.brand.lg = '人人權限企業版'
t.brand.mini = '人人'

// ...
export default t
```
4. 使用
```js
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
```
5. 检验成果
修改i18n/index.js 将locale改为湾湾繁体，就能直观的看到title的变化，（别问我为啥页面上的文字怎么没变化？因为写死为简体中文啦！）
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
页面中使用，如：
```js
// template
{{ $t('login.motto.text') }}
:placeholder="$t('login.form.placeholderUsername')"
// script
this.$t('login.motto.text')
```
再次对比一下，这回可不仅仅是标题不同了！

- 多语言切换
既然有了国际化的基础，那么实现一个多语言切换的小功能应该是水到渠成。来看看大佬是怎么教的！
偶然间看到d2-admin中的标签可以使用flex这个属性，感到很好奇。flex，对于新世纪的前端开发来说最熟悉不过，但是标签上直接写flex属性，作为很水很水的老菜鸟却是孤落寡闻，不过职业病的直觉告诉我一定是跟flex布局有关。于是我按图索骥，先翻阅了一下package.json，里边果然找到一个[flex.css](https://github.com/lzxb/flex.css/blob/master/docs/zh-ch.md)的依赖包。大概实现怎样的效果呢？我的认知是通过标签的flex属性，无需写css即可实现flex布局，flex.css内部通过定义属性选择器样式来实现flex布局，更多关于flex.css请戳☞[flex.cc]()
这里通过elemen-ui的[el-dropdown](https://element.eleme.io/#/zh-CN/component/dropdown)实现,通过command事件修改语言设置
```html
<el-dropdown size="small" @command="command => $i18n.locale = command">
   <span class="page-login--content-header-side-text"><d2-icon name="language"/> {{ $t('login.language') }}</span>
   <el-dropdown-menu slot="dropdown">
      <el-dropdown-item v-for="(language, index) in $languages" :key="index" :command="language.value">{{ language.label }}</el-dropdown-item>
    </el-dropdown-menu>
</el-dropdown>
```
- 对接人人验证码
一般来说，做登录页的时候，我们或多或少会遇到验证码的需求，对了，这里的验证码只的是图形验证码。最简单的实践是直接拿后台给过来的图片直接渲染的在页面上，使用img标签或者background-image引入。之前做renren-fast-vue二次开发的时候用的img标签，这里用的背景图片，思路都一样：拿后台给的图片直接渲染。众所周知，Just do it！
定义获取[uuid](https://zh.wikipedia.org/wiki/%E9%80%9A%E7%94%A8%E5%94%AF%E4%B8%80%E8%AF%86%E5%88%AB%E7%A0%81)的工具函数
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
使用uuid获取图形验证码
```html
<template slot="append">
  <div class="login-captcha" :style="{ backgroundImage: `url(${captchaPath})` }" @click="updateUUID" />
</template>
```
```js
// ...
export default {
  data () {
    return {
      // ...
      form: {
        // ...
        captcha: '',
        uuid: ''
      }
    }
  },
  computed: {
    // 校验
    rules () {
      return {
        // ...
        captcha: [
          { required: true, message: this.$t('login.ruleMessage.captcha'), trigger: 'blur' }
        ]
      }
    },
    // 验证码图片地址
    captchaPath () {
      return `${process.env.VUE_APP_API}/captcha?uuid=${this.form.uuid}`
    }
  },
  created () {
    // 刷新验证码和 uuid
    this.updateUUID()
  },
  // ...
  methods: {
    // ...
    /**
     * @description 刷新 uuid
     */
    updateUUID () {
      this.form.uuid = util.getUUID()
    },
    /**
     * @description 刷新后面的时间背景
     */
    refreshTime () {
      this.time = dayjs().format('HH:mm:ss')
    },
    // ...
    }
  }
}
```

- axios及登录逻辑
自从摆脱了JQuery大法，阿贾克斯和我从此是陌生人，以至于面试官要我阐述阿贾克斯原理，我真是哑巴吃黄连，哦不，是哑口无言，一个以CP(Copy&Paste)为生的搬砖工，你们还指望他侃侃而谈什么原理什么底层？至于什么[axios](https://github.com/axios/axios)拦截，总之，这一块涉及到前后交互的知识点还是蛮多的，我也是七窍通灵六窍--一窍不通，勉勉强强解读一下大佬的封装：
```js
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
```
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
当然还需要对数据进行处理，比如登录状态持久化、设置vuex用户信息等等，这里暂时只做简单的处理，另外安利一个vscode插件(乳沟您恰巧用的宇宙第一神器)--TODO Highlight,用来突出显示代码中的todo、fixme和其他注释，听说老司机都在用。有时，在将代码发布到生产环境之前，在编码时忘记查看添加的TODO。所以就有了这个拓展，提醒我们有一些笔记或者事情还没有完成。mark一下！
// 此处应有图

- 标准化cookie使用
作为后台管理系统，免不了涉及到cookie的使用，按照大佬的思路，定义了工具集函数并基于[js-cookie](https://github.com/js-cookie/js-cookie)二次封装了cookie。一般来说，cookie用得最多的就是get和set两个方法。
```js
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

```
如图，能看到目前通过此次标准化封装之后存的cookie的name都加了**d2admin-**的前缀。

- 防止过度点击
节流这个知识点我也是一直懵懵懂懂，经常和防抖混淆，理解不深刻，还只是停留在字面意思理解上：函数节流是指定时间间隔内只执行一次，函数防抖是频繁触发只有间隔超过指定时间间隔才执行。请参考[debouncing-throttling-explained-examples](https://css-tricks.com/debouncing-throttling-explained-examples/)
这里简单粗暴的用了[lodash](https://github.com/lodash/lodash)--一个一致性、模块化、高性能的 JavaScript 实用工具库。。
lodash中包含一系列数组、数字、对象、字符串等操作的API，当然还有一些常用的工具函数如节流(throttle)、防抖(debounce)。
```js
// ...
import { debounce } from 'lodash'
// ...
submit: debounce(function () {
  // ...
}, 1000, { 'leading': true, 'trailing': false })  // _.debounce(func, [wait=0], [options={}])  options.leading 与|或 options.trailing 决定延迟前后是先调用后等待,还是先等待后调用
// ...
```
前后对比



- 关于全局配置window.SITE_CONFIG
项目做得太少了，尤其还不会java，对网站的全局配置这一块的理解还停留在初级认知阶段。一般来说，在网页开发中往往一些版本控制、CDN静态资源、api接口地址、常用的公共变量等都会写到window下面并提升至首页方便管理，如网易一些爆款的H5中这种手法非常常见。在我之前使用开源的renren-fast-vue中这种手法更是大量运用，这次学习d2-admin也借鉴一下这种全局变量的使用(挂载变量一时爽，一直挂载一直爽,小心别翻车了)。先不管了，一顿Copy操作猛如虎，定睛一看，注释占了百分之九十五！当然，代码了瞬间有了后端的痕迹，不过在本项目 public/index.html中使用的模板语法来源于[ lodash 模板插入](https://lodash.com/docs/4.17.11#template),和public文件夹相关的内容可以去翻翻d2-admin文档关于[cli 和 webpack 配置](https://doc.d2admin.fairyever.com/zh/sys-cli3-webpack/)部分，这里就不再赘述，总之，万丈高楼平地起，基础建设很重要！
```js
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
```