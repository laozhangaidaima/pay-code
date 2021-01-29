# vue 的 data 是挂在在 prototype 上面的 构造函数的 prototype 如果是对象的话 改一个地方其它地方都要被修改 所有必须是函数

# new Vue() 的时候 可以传对象 也可一次传函数 因为 new vue()生成根组件 data 不会被复用

# prototype 对象会共用

function Component(){
}
Component.prototype.data = {
name:'jack',
age:22,
}
var componentA = new Component();
var componentB = new Component();
componentA.data.age=55;
console.log(componentA,componentB)
