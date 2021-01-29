# 放在 mounted 和 created 里面都可以 如果不需要操作 dom 可以放在 created 但 created 效果会更好,加载速度更快

# 一般在，created，mounted 中都可以发送数据请求，但是，大部分时候，会在created发送请求。

# 客户端

一般情况下都放到 mounted 中,保证逻辑的统一性,因为生命周期是同步执行的，ajax 是异步执行的

在 created 的时候，视图中的 dom 并没有渲染出来，所以此时如果直接去操 dom 节点，无法找到相关的元素

在 mounted 中，由于此时 dom 已经渲染出来了，所以可以直接操作 dom 节点

# 服务端

服务端渲染不支持 mounted 方法，所以在服务端渲染的情况下统一放到 created 中
