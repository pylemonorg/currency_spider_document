# -*- coding: utf-8 -*-
'''
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
        '.*www.douban.com/group2/topic/.*': {"follow": True,},
        '.*www.douban.com/group3/topic/.*': {},

    },

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

    # 文章内容编码方式, 防止乱码
    # 'encode': 'utf-8',

    # 提取规则
    # xpath 提取规则
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
            'xpath': ['//span[@class="from"]//text()'],
            'replace': ['来自: '],
            're_sub': ['来自：']  # 正则替换
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
}