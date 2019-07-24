//自执行函数
(function (arg) {
    var status = 1;  //封装变量
    arg.extend({
    'wangsen':function () {
        return 'sb';
        }
    });
})(JQuery);