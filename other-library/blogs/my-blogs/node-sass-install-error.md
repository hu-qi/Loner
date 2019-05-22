## 记录一下同事node-sass安装踩坑一二事
本来，作为分部唯一的全职前端，理应有担当，可是当一堆需求提过来，我是彻底怂了。目前一大波React Native、React、Vue、Weapp、Node等等技术栈正在袭来，APP开发、后台管理系统、企业网站、政务小程序、电商小程序……一大堆项目急着开发。我开始怀疑自己，我还是个三年经验的老菜鸟吗？忧伤之际，后台大佬说他前端项目安装node-sass依赖的时候，报错了！
### 报错截图

[!node-sass-install-error-1](../../../public-repertory/img/node-sass-install-error-1.jpg)

[!node-sass-install-error-2](../../../public-repertory/img/node-sass-install-error-2.jpg)

### 解决
尝试了很多办法，最终：
卸载原来的版本，改用taobao源，重新安装。
```
npm unisntall node-sass
npm i -g nrm
nrm use taobao
npm i node-sass --save-dev   // 这里由于package.json里是放在devdependencies中的
```