```
js里可能会影响dom结构，不阻塞的话，前前后后的js争相往dom里插入，乱了套了，要处理一堆append， document.write

js会改变dom 可能会引发回流

```