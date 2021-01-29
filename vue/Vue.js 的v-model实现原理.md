组件的 v-model 是 value + input 方法的语法糖

<el-checkbox :value="" @input=""></el-checkbox>
<el-checkbox v-model="check"></el-checkbox>