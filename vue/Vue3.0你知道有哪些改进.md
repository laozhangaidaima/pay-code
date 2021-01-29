- Vue3 采用了 TS 来编写

- 支持 Composition API

- Vue3 中响应式数据原理改成 proxy

- vdom 的对比算法更新，只更新 vdom 的绑定了动态数据的部分

- 可以单独引用生命周期
- 编译速度快3倍
- template内不用写div来包裹
-  setup() {}内定义data methods 生命周期 需要用什么要return出去
-  兼容vue2



# 数据劫持从object.defineProperty  改为了proxy 速度变快
# 定义data methods watch computed 生命周期 都放在了setup函数里面
# 生命周期 mounted需要import
# template 下可以不止一个根元素了
# 生命周期名字改变 普遍加了个on 
# 定义响应数据用ref和reactive