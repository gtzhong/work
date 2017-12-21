from urllib import request
import re

#断点调试

class Spider():
    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    member_pattern ='<span class="video-number">([\s\S]*?)</span>'


    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls

    # 1.获取列表的数据
    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        anchors = []
        for html in root_html:
            _name = re.findall(Spider.name_pattern,html)
            _number = re.findall(spider.member_pattern,html)
            anchor ={'name':_name,'number':_number}
            anchors.append(anchor)
        #print(anchors)
        return anchors

    # 2.过滤空格之类
    def __refine(self,anchors):
        _list = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
        }
        return map(_list,anchors)  

    # 3.排序
    def __sort(self, anchors):
        # reverse=True为降序
        _sort_anchors = sorted(anchors,key=self.__sort_seed,reverse=True)
        return _sort_anchors

    # 3.1 选择以哪个字段做为排序    
    def __sort_seed(self,anchor_row):
        r=re.findall('\d',anchor_row['number'])
        number = float(r[0])
        if '万' in anchor_row['number']:
            number *=10000
        return number

    # 4.结果输出
    def __show(self,anchors):
       # for anchor in anchors:
       #     print(anchor['name'] + '------'+anchor['number'])
       for rank in range(0,len(anchors)):
           print('rank |' + str(rank+1)
           + '  : '+anchors[rank]['name']
           + '   '+anchors[rank]['number']
           ) 

    # 运行入口
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))  #输出 <map object at 0x928392832) 使用list即可输出
        anchors = self.__sort(anchors)
        anchors = self.__show(anchors)
        print(anchors)
        a = 1

spider = Spider()
spider.go()

""""
#输出
rank |96  : 熊猫TV丶阿心   212
rank |97  : 电竞蛇哥   205
rank |98  : 井田使牛   204
rank |99  : L0L龟龟   1149
rank |100  : 有梦想的风铃儿   1112
rank |101  : 糖神丶   1045
rank |102  : PSL英雄联盟   1027
rank |103  : 空丿紫   188
rank |104  : 丿Black丶琳爷   174
rank |105  : 星星工作室   174
rank |106  : 子哲Q2Q   172
rank |107  : 阿枫丶丶丶   169
rank |108  : 心之所芷0   159
rank |109  : 大眉毛丶娃儿   150
rank |110  : 瓜皮球球   150
rank |111  : 金克喵的猫珥朵丶   137
rank |112  : miniCissy   124
rank |113  : 折纸的寓意   114
rank |114  : 熊猫风语主宰者   112
rank |115  : 傲然携姬出风尘灬   111
rank |116  : 鸽子夜   110
rank |117  : LEG丶Nirvana   105
rank |118  : 伪妹   103
None


"""