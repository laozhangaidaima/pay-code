v-show：display: none 和 display: block 之间切换  经常切换用v-show
v-if：不渲染

if 如果条件不成立不会渲染当前指令所在节点的 dom 元素
v-show 只是切换当前 dom 的显示或者隐藏

v-show 只是在 display: none 和 display: block 之间切换。⽆论初始条件是什么 都会被渲染出来，后⾯只需要切换 CSS ， DOM 还是⼀直保留着的。所以总的来说 v- show 在初始渲染时有更⾼的开销，但是切换开销很⼩，更适合于频繁切换的场景。

v-if 的话就得说到 Vue 底层的编译了。当属性初始为 false 时，组件就不会被渲 染，直到条件为 true ，并且切换条件时会触发销毁/挂载组件，所以总的来说在切换时开 销更⾼，更适合不经常切换的场景。
