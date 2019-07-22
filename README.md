# 通用爬虫说明文档

## 模版说明
> 这些取消的功能不会影响之前模版

### 下载第三包
在 cmd 输入下载第三方包
- pip install scrapy-redis https://pypi.douban.com/simple
- pip install redis https://pypi.douban.com/simple
- pip install selenium https://pypi.douban.com/simple

### 新功能 - 动态网页加载
- 支持动态加载 驱动chrome浏览器（版本：71.0.3573.0 (正式版本) （64 位））
> **注意**
> 由于驱动浏览器占用资源大，效率低，模版命名请加上`driver`标识，以助于管理。
> 驱动命名参考如下：
> `douban.py` 改为 **`driver_douban.py`**

### 新功能 - 正则替换
- 支持正则替换

### 舍弃/更改功能
- 取消 模版时间（expiration_day）设置（统一测试过期时间 9999天）
- 取消 搜索功能（search_key）
- 更改 抓取深度设置（DEPTH_LIMIT）字段名（统一测试抓取深度 3层，）这样意味着之前设置的深度全部失效变为3层，此次深度设置只针对重点网站


## 模版命名规则
- 不可以数字开头，不能包含特殊字符，（**下划线_除外**）
- 最好不用连续使用下划线 例如：**__douban.py** 可以改为 **_1_douban.py**
- 如果是驱动浏览器 请在模版命名中添加 **driver** 示例： **driver_douban.py**
- 模版命名必须以 `.py` 结尾

## 模版示例
### 注意点
- 请把模版信息填上，后期好维护
- 如需驱动浏览器 请在 模版命名中添加 `driver`
- 清不要轻易设置 `MAX_DEPTH_LIMIT` 字段 和 `driver` 字段

### 优化模版配置速度
1. 请先配置好链接规则 起始页（start_urls）；允许的域名（allowed_domains）；文章地址（article_url）这三个选项，其他选项暂时不用配置
2. 配置好这三个选项，运行测试文件，看看是否可以正常访问配置的链接规则，再进行其他操作。
3. 时间转换解析不确定时，可以通过运行 `junk` 文件下的时间检测程序测试是否正常
4. 链接规则设置不确定时，可以通过运行 `junk` 文件下的链接程序测试是否正确


### 示例
```python
# -*- coding: utf-8 -*-
'''
## 这里填写 模版信息
网站名称：豆瓣网
网站主页： www.douban.com
负责人： 尹强
'''

setting_rule = {
    # 开始url 起始页
    "start_urls": ['https://www.douban.com/group/explore'],
    "start_driver": True,  # 起始页是否开启浏览器， 默认不开启
    "start_drop_down": 3,  # 起始页下拉次数  默认为 不下拉

    # 允许的域名
    "allowed_domains": ["www.douban.com", "m.douban.com"],

    # 文章url 和 下一页 可以用junk文件下url匹配检测是否合格
    # follow 表示 当前页面符合匹配链接是否继续抓取 True 表示继续 False 停止
    # driver表示 驱动浏览器， True 开启， False/禁止（或者不设置此参数），
    # drop_down 表示是在驱动浏览器的情况的下次数， 默认不下拉
    "article_url": {
        '.*www.douban.com/group/topic/.*': {"follow": True, "driver": True, "drop_down": 2},
        '.*www.douban.com/group2/topic/.*': {"follow": True, },
    },
    
    # 过滤链接 正则
    'filter_url': ['www.dgworld.com.cn'],
    
    # MAX_DEPTH_LIMIT 抓取深度 等于原来模版 DEPTH_LIMIT
    # 请不要轻易设置此字段，不用时请注释
    # "MAX_DEPTH_LIMIT": 4,

    # 数据库固定字段 参考数据字典
    "ir_mediasource": "豆瓣网",  # 文章媒体来源
    "ir_mediatype": 2,  # 文章媒体类型

    # 行业ID
    # 默认:-1, 政府：1, IT：2, 汽车：3, 地产：4, 时尚：5,
    # 医疗：6, 能源：7, 广告：8, 餐饮：9, 金融：10, 家居：11,
    # 通信：12, 教育：13, 航空：14, 农业：15, 旅游：16,
    # 公共安全：17, 公共交通：18, 国内医药：19, 国外医药：20
    "ir_trade": -1,  # 行业id
    "ir_area": 2,  # 监控区域  国外：1， 国内：2
    # 添加网站备案地址  默认None ，表示未知（没有），有填写地方简称即可（例如：湘ICP备05000618号 填写: 湘 即可）
    # 如果网站没有备案地址 可以通过 http://icp.chinaz.com/www.hunan.gov.cn 查询
    # 如果特殊地区 请提前告知！！！
    "ir_librariytype": '湘',
    # 文章内容编码方式, 防止乱码
    # 'encode': 'utf-8',

    # 提取规则
    # xpath 提取规则 xath 优先级比 re_findall 高
    # re_findall 正则提取
    # replace 替换的内容 优先级比 re_sub 高
    # re_sub 正则替换
    # handle 自定义处理函数 函数第一个参数必须为 xpath提取的内容，而且是提取的原格式list类型
    # args 自定义函数的传参 自定义函数通过关键字参数
    "extract_rule": {

        # 标题
        "title": {
            # 'xpath': ['//div[@class="post-header"]//text()', ]
        },

        # 作者
        "author": {
            're_findall': ['conent:([\s\S]+?)}'],
            'xpath': ['//span[@class="from"]//text()'],
            'replace': ['来自: '],
            're_sub': ['来自：']  # 正则替换
        },
        # 来源    文章来源，自动与 ir_mediasource字段 匹配是否转发
        "source": {
            're_findall': ['source:([\s\S]+?)}'],
            'xpath': ['//span[@class="source"]//text()'],
            'replace': ['来源: '],
            're_sub': ['来源：']  # 正则替换
        },

        # 发布时间
        "pub_time": {
            'xpath': ['//span[@class="color-green"]//text()'],
        },

        # 内容
        "content": {
            'xpath': ['//div[@class="topic-richtext"]//text()'],
            # "replace": [' __dzh__detail__renderGg__12();']
        },

        # 栏目
        "column": {
            # 'xpath': ['//div[@class="article-tags"]/a/text()']

        },

        # 标签
        "label": {
            # 'xpath': ['//div[@class="mod-tags"]//text()']
        },

        # 分享数
        "share_num": {
        },

        # 喜欢数
        "like_num": {
            # 'xpath': ['//div[@class="posted-box-add"]//a[@title="赞"]//span[@class="c-alarm"]/text()'],
        },

        # 评论数
        "comment_num": {
            # 'xpath': ['//div[@class="forward-wblog"]/span/text()'],
        },

        # 阅读数
        "read_num": {
            # 'xpath': ['//div[@class="posts-stat-c"]/div[1]/span/text()'],
        },

    },

    # 请求头, 根据网站自定义请求头
    "headers": {
        # "Host": 'search.kdnet.net'
    },
    # 自定义chrome请求头：
    "driver_setting": {
        # "User-Agent": 'app....'
    },
}

```
