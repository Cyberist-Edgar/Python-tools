### 正则表达式匹配的模式
<table>
    <tbody>
    <tr>
        <th style="width:25%">模式</th>
        <th>描述</th>
    </tr>
    <tr>
        <td>^</td>
        <td>匹配字符串的开头</td>
    </tr>
    <tr>
        <td>$</td>
        <td>匹配字符串的末尾。</td>
    </tr>
    <tr>
        <td>.</td>
        <td>匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。</td>
    </tr>
    <tr>
        <td>[...]</td>
        <td>用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'</td>
    </tr>
    <tr>
        <td>[^...]</td>
        <td>不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。</td>
    </tr>
    <tr>
        <td>*</td>
        <td>匹配0个或多个的表达式。</td>
    </tr>
    <tr>
        <td>+</td>
        <td>匹配1个或多个的表达式。</td>
    </tr>
    <tr>
        <td>?</td>
        <td> 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式</td>
    </tr>
    <tr>
        <td>{n}</td>
        <td>匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。</td>
    </tr>
    <tr>
        <td>{ n,}</td>
        <td>精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。</td>
    </tr>
    <tr>
        <td>{ n, m}</td>
        <td>匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式</td>
    </tr>
    <tr>
        <td>a| b</td>
        <td>匹配a或b</td>
    </tr>
    <tr>
        <td>()</td>
        <td>匹配括号内的表达式，也表示一个组</td>
    </tr>
    <tr>
        <td>(?imx)</td>
        <td>正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。</td>
    </tr>
    <tr>
        <td>(?-imx)</td>
        <td>正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。</td>
    </tr>
    <tr>
        <td>(?: re)</td>
        <td> 类似 (...), 但是不表示一个组</td>
    </tr>
    <tr>
        <td>(?imx: re)</td>
        <td>在括号中使用i, m, 或 x 可选标志</td>
    </tr>
    <tr>
        <td>(?-imx: re)</td>
        <td>在括号中不使用i, m, 或 x 可选标志</td>
    </tr>
    <tr>
        <td>(?#...)</td>
        <td>注释.</td>
    </tr>
    <tr>
        <td>(?= re)</td>
        <td>前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。</td>
    </tr>
    <tr>
        <td>(?! re)</td>
        <td>前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。</td>
    </tr>
    <tr>
        <td>(?&gt; re)</td>
        <td>匹配的独立模式，省去回溯。</td>
    </tr>
    <tr>
        <td>\w</td>
        <td> 匹配数字字母下划线</td>
    </tr>
    <tr>
        <td>\W</td>
        <td>匹配非数字字母下划线</td>
    </tr>
    <tr>
        <td>\s</td>
        <td> 匹配任意空白字符，等价于 [\t\n\r\f]。</td>
    </tr>
    <tr>
        <td>\S</td>
        <td>匹配任意非空字符</td>
    </tr>
    <tr>
        <td>\d</td>
        <td> 匹配任意数字，等价于 [0-9]。</td>
    </tr>
    <tr>
        <td>\D</td>
        <td>匹配任意非数字</td>
    </tr>
    <tr>
        <td>\A</td>
        <td>匹配字符串开始</td>
    </tr>
    <tr>
        <td>\Z</td>
        <td>匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。</td>
    </tr>
    <tr>
        <td>\z</td>
        <td>匹配字符串结束</td>
    </tr>
    <tr>
        <td>\G</td>
        <td>匹配最后匹配完成的位置。</td>
    </tr>
    <tr>
        <td>\b</td>
        <td>匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。</td>
    </tr>
    <tr>
        <td>\B</td>
        <td>匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。</td>
    </tr>
    <tr>
        <td>\n, \t, 等。</td>
        <td>匹配一个换行符。匹配一个制表符, 等</td>
    </tr>
    <tr>
        <td>\1...\9</td>
        <td>匹配第n个分组的内容。</td>
    </tr>
    <tr>
        <td>\10</td>
        <td>匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。</td>
    </tr>
    </tbody>
</table>

### 正则表达式匹配的修饰符
<table class="reference">
    <tbody>
    <tr>
        <th style="width:25%">修饰符</th>
        <th>描述</th>
    </tr>
    <tr>
        <td>re.I</td>
        <td>使匹配对大小写不敏感</td>
    </tr>
    <tr>
        <td>re.L</td>
        <td>做本地化识别（locale-aware）匹配</td>
    </tr>
    <tr>
        <td>re.M</td>
        <td>多行匹配，影响 ^ 和 $</td>
    </tr>
    <tr>
        <td>re.S</td>
        <td>使 . 匹配包括换行在内的所有字符</td>
    </tr>
    <tr>
        <td>re.U</td>
        <td>根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.</td>
    </tr>
    <tr>
        <td>re.X</td>
        <td>该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。</td>
    </tr>
    </tbody>
</table>



`re.match`函数

> `re.match` 尝试从字符串的起始位置匹配一个模式，如果不是其实位置匹配成功的话，返回`None`

语法：

```python
re.match(pattern, string, flags=0)
```

匹配成功返回一个匹配的对象，使用`group(num)` `groups()`可以获取匹配表达式，有`括号`限定优先显示括号里的



`re.search`函数

> `re.search` 扫描整个字符串并返回第一个成功的匹配

用法与`re.match`函数类似



`re.sub` 函数

> `re.sub`函数用来替换字符串中的匹配项

语法：

```python
re.sub(pattern, repl, string, count=0, flags=0)
```

`count`-> 最大替换次数，默认0表示匹配所有

`repl` -> 替换的字符串，也可以为一个函数`



`re.compile` 函数

> `re.compile` 函数用来编译正则表达式，生成一个正则表达式对象

语法：

```python
re.compile(pattern[, flags])
```

注意：`flag`只能在这里指定



`findall`函数

> `findall`函数可以在正则表达式中找到所有的子串，并返回一个列表，如果没有则返回空列表

语法：

```python
re.findall(string[,pos[,endpos]])
```



`re.finditer`函数

> `re.finditer`函数与`re.findall`函数类似，只是返回的是一个迭代器

语法：

```python
re.finditer(pattern, string, flags=0)
```



`re.split`函数

> `re.split`函数按照匹配的子串将字符串分割后返回列表

语法：

```python
re.split(pattern, string[,maxsplit=0,flags=0])
```





`贪婪模式`和`非贪婪模式`

> 在上面我们使用的其实都是贪婪模式，所谓贪婪模式其实就是正则匹配的时候尽可能多的匹配，非贪婪模式则与之相反



在匹配的时候使用 `?`可以转化成非贪婪模式

比如：

贪婪模式：

```python  
re.findall(r"hi.*", string)
```

非贪婪模式：

```python
re.findall(r"hi.*?", string)
```

对于字符串 `string="hi, how are you?"`匹配的结果如下：

```
贪婪模式 -> ['hi, how are you?']
非贪婪模式 -> ['hi']
```



