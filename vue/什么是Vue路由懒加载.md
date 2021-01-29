# 对于SPA单页应用，当打包构建时，JavaScript包会变得非常大，影响页面加载速度，将不同路由对应的组件分割成不同的代码块，然后当路由被访问的时候才加载对应组件，这就是路由的懒加载。

不同路由 不同组件 分割为代码块  路由被访问才加载组件

# 事实上我们在Vue-Router的配置上可以直接定义懒加载
{
  path: "/example",
  name: "example",
  //打包后，每个组件单独生成一个chunk文件
  component: () => import("@/views/example.vue")
}