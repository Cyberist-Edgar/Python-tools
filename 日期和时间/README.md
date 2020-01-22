### Python日期和时间

- 时间戳
  > 时间戳是以秒为单位的浮点小数，每个时间戳都是从1970/1/1午夜经历了多长时间来表示的
  ```python
  import time
  ticks = time.time()
  print(ticks)
  ```

  <br/>
  
- 时间元组
  
  > 用一个元组装起来的9组数据

<table>
    <tbody>
        <tr>
            <th style="width:10%">序号
            </th>
            <th style="width:40%">字段</th>
            <th>值</th>
        </tr>
        <tr>
            <td>0</td>
            <td>4位数年</td>
            <td>2008</td>
        </tr>
        <tr>
            <td>1</td>
            <td>月</td>
            <td>1 到 12</td>
        </tr>
        <tr>
            <td>2</td>
            <td>日</td>
            <td>1到31</td>
        </tr>
        <tr>
            <td>3</td>
            <td>小时</td>
            <td>0到23</td>
        </tr>
        <tr>
            <td>4</td>
            <td>分钟</td>
            <td>0到59</td>
        </tr>
        <tr>
            <td>5</td>
            <td>秒</td>
            <td>0到61 (60或61 是闰秒)</td>
        </tr>
        <tr>
            <td>6</td>
            <td>一周的第几日</td>
            <td>0到6 (0是周一)</td>
        </tr>
        <tr>
            <td>7</td>
            <td>一年的第几日</td>
            <td>1到366 (儒略历)</td>
        </tr>
        <tr>
            <td>8</td>
            <td>夏令时</td>
            <td>-1, 0, 1, -1是决定是否为夏令时的旗帜</td>
        </tr>
    </tbody>
</table>

 上面的也就是struct_time元组，有如下属性：

<table>
    <tbody>
        <tr>
            <th style="width:10%">序号</th>
            <th style="width:40%">属性</th>
            <th>值</th>
        </tr>
        <tr>
            <td>0</td>
            <td>tm_year</td>
            <td>2008</td>
        </tr>
        <tr>
            <td>1</td>
            <td>tm_mon</td>
            <td>1 到 12</td>
        </tr>
        <tr>
            <td>2</td>
            <td>tm_mday</td>
            <td>1 到 31</td>
        </tr>
        <tr>
            <td>3</td>
            <td>tm_hour</td>
            <td>0 到 23</td>
        </tr>
        <tr>
            <td>4</td>
            <td>tm_min</td>
            <td>0 到 59</td>
        </tr>
        <tr>
            <td>5</td>
            <td>tm_sec</td>
            <td>0 到 61 (60或61 是闰秒)</td>
        </tr>
        <tr>
            <td>6</td>
            <td>tm_wday</td>
            <td>0到6 (0是周一)</td>
        </tr>
        <tr>
            <td>7</td>
            <td>tm_yday</td>
            <td>1 到 366(儒略历)</td>
        </tr>
        <tr>
            <td>8</td>
            <td>tm_isdst</td>
            <td>-1, 0, 1, -1是决定是否为夏令时的旗帜</td>
        </tr>
    </tbody>
</table>



- 获取当前时间
  > 从返回的浮点数的时间戳方式向时间元组进行转化，只要将浮点数传递给如localtime之类的函数
  ```python
  import time
  localtime = time.localtime(time.time())
  print(localtime)
  ```
  
  输出的结果：
  
  ```python
  time.struct_time(tm_year=2020, tm_mon=1, tm_mday=22, tm_hour=9, tm_min=23, tm_sec=30, tm_wday=2, tm_yday=22, tm_isdst=0)
  ```
  
  

- 获取格式化的时间

  > 可以根据需求选取各种格式，最简单的是`asctime()`

  ```python
  import time 
  localtime = time.asctime(time.localtime(time.time()))
  print(localtime)
  ```
  输出结果：
  ```
  Wed Jan 22 09:27:40 2020
  ```



- 格式化日期

  > 可以使用`time`模块中的`strftime`方法来格式化日期

  ```python
  time.strftime(format[, t])
  ```

  ```python
  import time
  # 格式化成2020-01-22 09:36:51形式
  print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
   
  # 格式化成Wed Jan 22 09:36:51 2020形式
  print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) )
    
  # 将格式字符串转换为时间戳 
  a = "Wed Jan 22 09:36:51 2020"
  print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
  ```



​		python 中日期格式化符号

<ul>
    <li>%y 两位数的年份表示（00-99）</li>
    <li>%Y 四位数的年份表示（000-9999）</li>
    <li>%m 月份（01-12）</li>
    <li>%d 月内中的一天（0-31）</li>
    <li>%H 24小时制小时数（0-23）</li>
    <li>%I 12小时制小时数（01-12）</li>
    <li>%M 分钟数（00=59）</li>
    <li>%S 秒（00-59）</li>
    <li>%a 本地简化星期名称</li>
    <li>%A 本地完整星期名称</li>
    <li>%b 本地简化的月份名称</li>
    <li>%B 本地完整的月份名称</li>
    <li>%c 本地相应的日期表示和时间表示</li>
    <li>%j 年内的一天（001-366）</li>
    <li>%p 本地A.M.或P.M.的等价符</li>
    <li>%U 一年中的星期数（00-53）星期天为星期的开始</li>
    <li>%w 星期（0-6），星期天为星期的开始</li>
    <li>%W 一年中的星期数（00-53）星期一为星期的开始</li>
    <li>%x 本地相应的日期表示</li>
    <li>%X 本地相应的时间表示</li>
    <li>%Z 当前时区的名称</li>
    <li>%% %号本身</li>
</ul>



​		

- 获取某月的日历

  > `calendar` 模块有很多方法来处理年历和月历

  ```python
  import calendar 
  cal = calendar.month(2016,1)
  print(cal)
  ```

  ```
      January 2020
  Mo Tu We Th Fr Sa Su
         1  2  3  4  5
   6  7  8  9 10 11 12
  13 14 15 16 17 18 19
  20 21 22 23 24 25 26
  27 28 29 30 31
  ```

  

- time 模块

  - 函数
  
  <table class="reference">
      <tbody>
          <tr>
              <th style="width:5%">序号</th>
              <th style="width:95%">函数及描述</th>
          </tr>
          <tr>
              <td>1</td>
              <td> time.altzone</a><br>返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。</td>
          </tr>
          <tr>
              <td>2</td>
              <td> time.asctime([tupletime])</a><br>接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14
                  2008"（2008年12月11日&nbsp;周二18时07分14秒）的24个字符的字符串。</td>
          </tr>
          <tr>
              <td>3</td>
              <td> time.clock( )</a><br>用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。</td>
          </tr>
          <tr>
              <td>4</td>
              <td> time.ctime([secs])</a><br>作用相当于asctime(localtime(secs))，未给参数相当于asctime()</td>
          </tr>
          <tr>
              <td>5</td>
              <td> time.gmtime([secs])</a><br>接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0</td>
          </tr>
          <tr>
              <td>6</td>
              <td> time.localtime([secs])</a><br>接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。</td>
          </tr>
          <tr>
              <td>7</td>
              <td> time.mktime(tupletime)</a><br>接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）。</td>
          </tr>
          <tr>
              <td>8</td>
              <td> time.sleep(secs)</a><br>推迟调用线程的运行，secs指秒数。</td>
          </tr>
          <tr>
              <td>9</td>
              <td> time.strftime(fmt[,tupletime])</a><br>接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。</td>
          </tr>
          <tr>
              <td>10</td>
              <td> time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')</a><br>根据fmt的格式把一个时间字符串解析为时间元组。</td>
          </tr>
          <tr>
              <td>11</td>
              <td> time.time( )</a><br>返回当前时间的时间戳（1970纪元后经过的浮点秒数）。</td>
          </tr>
          <tr>
              <td>12</td>
              <td> time.tzset()</a><br>根据环境变量TZ重新初始化时间相关设置。 </td>
          </tr>
      </tbody>
  </table>
  

     - 属性
  
  <table class="reference">
    <tbody>
        <tr>
            <th style="width:5%">序号</th>
            <th style="width:95%">属性及描述</th>
        </tr>
        <tr>
            <td>1</td>
            <td><b>time.timezone</b><br>属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（&gt;0，美洲;&lt;=0大部分欧洲，亚洲，非洲）。</td>
        </tr>
        <tr>
            <td>2</td>
            <td><b>time.tzname</b><br>属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。</td>
        </tr>
    </tbody>
  </table>



- 日历模块



<table>
    <tbody>
        <tr>
            <th style="width:5%">序号</th>
            <th style="width:95%">函数及描述</th>
        </tr>
        <tr>
            <td>1</td>
            <td><b>calendar.calendar(year,w=2,l=1,c=6)</b><br>返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21*
                W+18+2* C。l是每星期行数。</td>
        </tr>
        <tr>
            <td>2</td>
            <td><b>calendar.firstweekday( )</b><br>返回当前每周起始日期的设置。默认情况下，首次载入 calendar 模块时返回 0，即星期一。</td>
        </tr>
        <tr>
            <td>3</td>
            <td><b>calendar.isleap(year)</b><br>
                <p>是闰年返回 True，否则为 False。</p></td>
        </tr>
            <td>5</td>
            <td><b>calendar.month(year,month,w=2,l=1)</b><br>返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7*
                w+6。l是每星期的行数。</td>
        </tr>
        <tr>
            <td>6</td>
            <td><b>calendar.monthcalendar(year,month)</b><br>返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
            </td>
        </tr>
        <tr>
            <td>7</td>
            <td><b>calendar.monthrange(year,month)</b><br>返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。</td>
        </tr>
        <tr>
            <td>8</td>
            <td><b>calendar.prcal(year,w=2,l=1,c=6)</b><br>相当于 <strong>print
                    calendar.calendar(year,w=2,l=1,c=6)</strong>。</td>
        </tr>
        <tr>
            <td>9</td>
            <td><b>calendar.prmonth(year,month,w=2,l=1)</b><br>相当于 <strong>print
                    calendar.month(year,month,w=2,l=1)</strong> 。</td>
        </tr>
        <tr>
            <td>10</td>
            <td><b>calendar.setfirstweekday(weekday)</b><br>设置每周的起始日期码。0（星期一）到6（星期日）。</td>
        </tr>
        <tr>
            <td>11</td>
            <td><b>calendar.timegm(tupletime)</b><br>和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）。</td>
        </tr>
        <tr>
            <td>12</td>
            <td><b>calendar.weekday(year,month,day)</b><br>返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。</td>
        </tr>
    </tbody>
</table>

