var __CML__GLOBAL = require("../../manifest.js");
__CML__GLOBAL.webpackJsonp([4],{

/***/ "../../../node_modules/babel-loader/lib/index.js?{\"filename\":\"C:\\\\Users\\\\huqi\\\\AppData\\\\Roaming\\\\npm\\\\node_modules\\\\chameleon-tool\\\\chameleon.js\"}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-loader/src/selector.js?type=script&index=0&fileType=page&media=dev&cmlType=wx&isInjectBaseStyle=true&check={\"enable\":true,\"enableTypes\":[]}!./src/pages/index/index.cml":
/***/ (function(module, exports, __webpack_require__) {

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _store = __webpack_require__("./src/store/index.js");

var _store2 = _interopRequireDefault(_store);

var _chameleonRuntime = __webpack_require__("./node_modules/chameleon-runtime/index.js");

var _chameleonRuntime2 = _interopRequireDefault(_chameleonRuntime);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Index = function () {
  function Index() {
    _classCallCheck(this, Index);

    this.data = {
      currentComp: 'home',
      tabbar: {
        tabbarStyle: "height:120cpx;background-color:#efefef; border-top: 1px solid #dedede;", //tabbar最外层的样式支持自定义
        textStyle: "color:#3b3b3b", //文案默认style ,可以这里控制文案的大小，样式等
        selectedTextStyle: "color:#3baaff", //文案被选择style
        useFixedLayout: true, //是否通过fixed布局进行tabbar的布局
        list: [{
          compName: "home",
          text: "home",
          icon: __webpack_require__("./src/assets/images/chameleon.png")
        }, {
          compName: "about",
          text: "about",
          icon: __webpack_require__("./src/assets/images/chameleon.png")
        }]
      }
    };
    this.methods = {};
  }

  _createClass(Index, [{
    key: "beforeCreate",
    value: function beforeCreate() {}
  }, {
    key: "mounted",
    value: function mounted() {}
  }]);

  return Index;
}();

exports.default = new Index();


exports.default = _chameleonRuntime2.default.createPage(exports.default).getOptions();

/***/ }),

/***/ "./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/extract-text-webpack-plugin/dist/loader.js?{\"omit\":1,\"remove\":true}!../../../node_modules/vue-style-loader/index.js!../../../node_modules/css-loader/index.js?{\"sourceMap\":false}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-css-loader/index.js?{\"platform\":\"miniapp\"}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/postcss-loader/lib/index.js?{\"sourceMap\":false,\"config\":{\"path\":\"C:\\\\Users\\\\huqi\\\\AppData\\\\Roaming\\\\npm\\\\node_modules\\\\chameleon-tool\\\\configs\\\\postcss\\\\wx\\\\.postcssrc.js\"}}!../../../node_modules/less-loader/dist/cjs.js?{\"sourceMap\":false}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-css-loader/index.js?{\"media\":true,\"cmlType\":\"wx\"}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-loader/src/selector.js?type=styles&index=0&fileType=page&media=dev&cmlType=wx&isInjectBaseStyle=true&check={\"enable\":true,\"enableTypes\":[]}!./src/pages/index/index.cml":
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ "./src/pages/index/index.cml":
/***/ (function(module, exports, __webpack_require__) {

var __cml__style0 = __webpack_require__("./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/extract-text-webpack-plugin/dist/loader.js?{\"omit\":1,\"remove\":true}!../../../node_modules/vue-style-loader/index.js!../../../node_modules/css-loader/index.js?{\"sourceMap\":false}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-css-loader/index.js?{\"platform\":\"miniapp\"}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/postcss-loader/lib/index.js?{\"sourceMap\":false,\"config\":{\"path\":\"C:\\\\Users\\\\huqi\\\\AppData\\\\Roaming\\\\npm\\\\node_modules\\\\chameleon-tool\\\\configs\\\\postcss\\\\wx\\\\.postcssrc.js\"}}!../../../node_modules/less-loader/dist/cjs.js?{\"sourceMap\":false}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-css-loader/index.js?{\"media\":true,\"cmlType\":\"wx\"}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-loader/src/selector.js?type=styles&index=0&fileType=page&media=dev&cmlType=wx&isInjectBaseStyle=true&check={\"enable\":true,\"enableTypes\":[]}!./src/pages/index/index.cml");
var __cml__script = __webpack_require__("../../../node_modules/babel-loader/lib/index.js?{\"filename\":\"C:\\\\Users\\\\huqi\\\\AppData\\\\Roaming\\\\npm\\\\node_modules\\\\chameleon-tool\\\\chameleon.js\"}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-loader/src/selector.js?type=script&index=0&fileType=page&media=dev&cmlType=wx&isInjectBaseStyle=true&check={\"enable\":true,\"enableTypes\":[]}!./src/pages/index/index.cml");


/***/ })

},["./src/pages/index/index.cml"]);