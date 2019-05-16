# -*- coding: utf-8 -*-
'''
这是 通用匹配 模版
网站名称：中安论坛
网站主页： http://bbs.anhuinews.com/
负责人： 尹强
'''

setting_rule = {
    # 开始url 起始页
    "start_urls": ['http://bbs.anhuinews.com/'],

    # 允许的域名
    "allowed_domains": ["bbs.anhuinews.com", "anhuinews.com", "anhuinews"],

    # 抓取深度 默认为10层   0 所有层 1 表示1层 2 表示2层 。。。
    'DEPTH_LIMIT': 5,

    # 过期时间  单位天  当天=0 昨天=1， 前天=2  1年=365
    'expiration_day': 60,

    # 搜索功能
    # "search_key": {
    #     "request_url": "https://www.douban.com/search?",
    #     "form_date": {"q": "关键字", "cat": "1015"},
    #
    #     # "search_key_encode": "gb2312",
    #     "get_type": 'get',
    #     "headers": {
    #         "Host": "www.douban.com",
    #         "Referer": "https://www.douban.com/group/explore",
    #     }
    #
    # },

    # 文章url 和 下一页 可以用junk文件下url匹配检测是否合格
    # follow 表示 当前页面符合匹配链接是否继续抓取 True 表示继续 False 停止
    "article_url": {
        'http://bbs.anhuinews.com/forum.php\?mod=forumdisplay&fid=.*': {"follow": True},
        'http://bbs.anhuinews.com/forum.php\?gid=.*': {"follow": True},
        'http://bbs.anhuinews.com/forum-.*': {"follow": True},
        'http://bbs.anhuinews.com/forum.php\?mod=viewthread&tid=.*': {"follow": False},
        'http://bbs.anhuinews.com/thread-.*': {"follow": False},
    },

    # 数据库固定字段 参考数据字典
    # 1新闻 2论坛 3博客  4贴吧 5微博
    # 7报刊 # 8社交 # 10问答 # 11电台 # 12电视节目 # 20 app # 14视频
    "ir_mediasource": "中安论坛",  # 文章媒体来源
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
    # replace 替换的内容
    # handle 自定义处理函数 函数第一个参数必须为 xpath提取的内容，而且是提取的原格式list类型
    # args 自定义函数的传参 自定义函数通过关键字参数
    "extract_rule": {

        # 发布时间
        "pub_time": {
            'xpath': ['//div[@id="postlist"]/div[1]//div[@class="authi"]/em[1]//text()', ],
        },

        # 标题
        "title": {
            'xpath': ['//h1[@class="ts"]//text()',],
            # 'replace': ['帖子主题:']

        },

        # 作者
        "author": {
            'xpath': ['//div[@id="postlist"]/div[1]//a[@class="xw1"]//text()',],
        },

        # 内容
        "content": {
            'xpath': ['//div[@id="postlist"]/div[1]//td[@class="t_f"]//text()',],
            # "replace": [' __dzh__detail__renderGg__12();']
        },

        # 栏目
        "column": {
            'xpath': ['//div[@id="pt"]/div[@class="z"]/a//text()'],
            "replace": ["中安论坛"]

        },

        # 评论数
        "comment_num": {
            'xpath': ['//div[@id="postlist"]/table[1]//div[contains(@class, "hm")]/span[5]//text()'],
        },

        # 阅读数
        "read_num": {
            'xpath': ['//div[@id="postlist"]/table[1]//div[contains(@class, "hm")]/span[2]//text()'],
        },


    },

    # 请求头, 根据网站自定义请求头
    "headers": {
        # "Referer": 'http://bbs.tiexue.net/',
        # 'Host': 'www.tiexue.net',
    },
}

if __name__ == '__main__':
    pass
