mutation是同步更新数据(内部会进行是否为异步方式更新数据的检测)

action 异步操作，可以获取数据后调佣mutation提交最终数据
action可以做axios请求


action的使用场景
1.需要调用接口（异步操作） 2.接口返回数据需要存在store里面  满足这两个条件才上action吗