# hash 模式：在浏览器中符号 “#” ，#以及#后⾯的字符称之为 hash ，⽤ window.location.hash 读取。

特点： hash 虽然在 URL 中，但不被包括在 HTTP 请求中；⽤来指导浏览器动作，对服务端安全⽆⽤， hash 不会重加载⻚⾯。


# history 模式：h istory 采⽤ HTML5 的新特性；且提供了两个新⽅法：pushState() ， replaceState() 
可以对浏览器历史记录栈进⾏修改，以及 popState 事件的监听到状态变更
