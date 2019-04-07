var __CML__GLOBAL = require("./manifest.js");
__CML__GLOBAL.webpackJsonp([1],{

/***/ "../../../node_modules/babel-loader/lib/index.js?{\"filename\":\"C:\\\\Users\\\\huqi\\\\AppData\\\\Roaming\\\\npm\\\\node_modules\\\\chameleon-tool\\\\chameleon.js\"}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-loader/src/selector.js?type=script&index=0&fileType=app&media=dev&cmlType=wx&isInjectBaseStyle=true&check={\"enable\":true,\"enableTypes\":[]}!./src/app/app.cml":
/***/ (function(module, exports, __webpack_require__) {

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _index = __webpack_require__("./src/store/index.js");

var _index2 = _interopRequireDefault(_index);

var _routerConfig = __webpack_require__("./src/router.config.json");

var _routerConfig2 = _interopRequireDefault(_routerConfig);

var _chameleonRuntime = __webpack_require__("./node_modules/chameleon-runtime/index.js");

var _chameleonRuntime2 = _interopRequireDefault(_chameleonRuntime);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var App = function () {
  function App() {
    _classCallCheck(this, App);

    this.data = {
      store: _index2.default,
      routerConfig: _routerConfig2.default
    };
  }

  _createClass(App, [{
    key: 'created',
    value: function created(res) {}
  }]);

  return App;
}();

exports.default = new App();


exports.default = _chameleonRuntime2.default.createApp(exports.default).getOptions();

/***/ }),

/***/ "./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/extract-text-webpack-plugin/dist/loader.js?{\"omit\":1,\"remove\":true}!../../../node_modules/vue-style-loader/index.js!../../../node_modules/css-loader/index.js?{\"sourceMap\":false}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-css-loader/index.js?{\"platform\":\"miniapp\"}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/postcss-loader/lib/index.js?{\"sourceMap\":false,\"config\":{\"path\":\"C:\\\\Users\\\\huqi\\\\AppData\\\\Roaming\\\\npm\\\\node_modules\\\\chameleon-tool\\\\configs\\\\postcss\\\\wx\\\\.postcssrc.js\"}}!../../../node_modules/less-loader/dist/cjs.js?{\"sourceMap\":false}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-css-loader/index.js?{\"media\":true,\"cmlType\":\"wx\"}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-loader/src/selector.js?type=styles&index=0&fileType=app&media=dev&cmlType=wx&isInjectBaseStyle=true&check={\"enable\":true,\"enableTypes\":[]}!./src/app/app.cml":
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ "./src/app/app.cml":
/***/ (function(module, exports, __webpack_require__) {

var __cml__style0 = __webpack_require__("./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/extract-text-webpack-plugin/dist/loader.js?{\"omit\":1,\"remove\":true}!../../../node_modules/vue-style-loader/index.js!../../../node_modules/css-loader/index.js?{\"sourceMap\":false}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-css-loader/index.js?{\"platform\":\"miniapp\"}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/postcss-loader/lib/index.js?{\"sourceMap\":false,\"config\":{\"path\":\"C:\\\\Users\\\\huqi\\\\AppData\\\\Roaming\\\\npm\\\\node_modules\\\\chameleon-tool\\\\configs\\\\postcss\\\\wx\\\\.postcssrc.js\"}}!../../../node_modules/less-loader/dist/cjs.js?{\"sourceMap\":false}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-css-loader/index.js?{\"media\":true,\"cmlType\":\"wx\"}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-loader/src/selector.js?type=styles&index=0&fileType=app&media=dev&cmlType=wx&isInjectBaseStyle=true&check={\"enable\":true,\"enableTypes\":[]}!./src/app/app.cml");
var __cml__script = __webpack_require__("../../../node_modules/babel-loader/lib/index.js?{\"filename\":\"C:\\\\Users\\\\huqi\\\\AppData\\\\Roaming\\\\npm\\\\node_modules\\\\chameleon-tool\\\\chameleon.js\"}!./C:/Users/huqi/AppData/Roaming/npm/node_modules/chameleon-tool/node_modules/chameleon-loader/src/selector.js?type=script&index=0&fileType=app&media=dev&cmlType=wx&isInjectBaseStyle=true&check={\"enable\":true,\"enableTypes\":[]}!./src/app/app.cml");


/***/ }),

/***/ "./src/router.config.json":
/***/ (function(module, exports) {

module.exports = {"mode":"hash","domain":"https://www.chameleon.com","routes":[{"url":"/cml/h5/index","path":"/pages/index/index","name":"首页","mock":"index.php"},{"url":"/cml/h5/city","path":"/pages/city/city","name":"city","mock":"index.php"}]}

/***/ })

},["./src/app/app.cml"]);