import re


def main():
    li = re.findall(r".*\n", txt)
    print(len(li))
    json =[]
    for i in li:
        l = i.split("|")
        json.append({"bookname": l[0],
                     "number": l[1],
                     "ifend": '已完结' if l[2]=='是' else '更新',
                     "author": l[3][:-1]})
    print(json)

txt = '''从前有座灵剑山|287.24万|是|国王陛下
蓝白社|117.82万|否|魔性沧月
脑洞大爆炸|198.82万|是|魔性沧月
进化的四十六亿重奏|923.50万|否|相位行者
我的女友是恶女|119.81万|否|海底漫步者
天外寄生|142.54万|是|迷路的鱼
仙逆|651.44万|是|耳根
求魔|458.51万|是|耳根
斗罗大陆|298.95万|是|唐家三少
回到过去变成猫|144.41万|是|陈词懒调
步川小姐的贫穷物语|302.19万|否|乔治亚
全球高武|284.17万|否|老鹰吃小鸡
山海八荒录|41.05万|是|洛水
大医凌然|108.06万|否|志鸟村
我才不会被女孩子欺负|446万|是|废铁行者
欺负仇人的女儿难道有错吗|163万 |否|废铁行者
雪中悍刀行|455万|是|烽火戏诸侯
限制级末日症候|1000.03万|否|全部成为F
金棺陵兽|20万|是|天下霸唱
重生之超级战舰|329.68万|是|彩虹之门
惊悚乐园|489.55万|是|三天两觉
废土|232万|是|黑天魔神
感染体|215万|是|黑天魔神
事象的宏图|116万|否|ddt药剂
魔王奶爸|643万|是|盘古混沌
狩魔笔记|224万|是|烟雨江南
寂静王冠|301万|是|风月
疯狂的多塔|255万|是|奥丁信使
单机狂魔|137.30万|是|静谧长夜
龙蛇演义|220万|是|梦入神机
妞非在下|312万|是|月下小羊
露米娅的微小印记|58万|是|相位行者
'''

main()

'''
<div style="width:70%;margin: auto">
  <table class="layui-hide" id="books">
  </table>
</div>
<link rel="stylesheet" href="/lib/lay/css/layui.css" media="all">
<script src="/lib/lay/layui.js" charset="utf-8"></script>
<script>
layui.use('table', function(){
  var table = layui.table;
  table.render({
    elem: '#books'
    ,cellMinWidth: 80//全局定义常规单元格的最小宽度，layui 2.2.1 新增
   	//,width: 550
    ,cols: [[
      {field:'bookname', align: 'center', title: '书名', sort: true,minWidth: 200 }
      ,{field:'number', align: 'center', title: '字数', width: 100,sort: true}
      ,{field:'ifend', align: 'center', title: '完结',width: 90, sort: true}
      ,{field:'author', align: 'center', title: '作者', sort: true,
  width: 150,}
    ]]
  	 ,data: [{'bookname': '从前有座灵剑山', 'number': '287.24万', 'ifend': '已完结', 'author': '国王陛下'}, {'bookname': '蓝白社', 'number': '117.82万', 'ifend': '更新', 'author': '魔性沧月'}, {'bookname': '脑洞大爆炸', 'number': '198.82万', 'ifend': '已完结', 'author': '魔性沧月'}, {'bookname': '进化的四十六亿重奏', 'number': '923.50万', 'ifend': '更新', 'author': '相位行者'}, {'bookname': '我的女友是恶女', 'number': '119.81万', 'ifend': '更新', 'author': '海底漫步者'}, {'bookname': '天外寄生', 'number': '142.54万', 'ifend': '已完结', 'author': '迷路的鱼'}, {'bookname': '仙逆', 'number': '651.44万', 'ifend': '已完结', 'author': '耳根'}, {'bookname': '求魔', 'number': '458.51万', 'ifend': '已完结', 'author': '耳根'}, {'bookname': '斗罗大陆', 'number': '298.95万', 'ifend': '已完结', 'author': '唐家三少'}, {'bookname': '回到过去变成猫', 'number': '144.41万', 'ifend': '已完结', 'author': '陈词懒调'}, {'bookname': '步川小姐的贫穷物语', 'number': '302.19万', 'ifend': '更新', 'author': '乔治亚'}, {'bookname': '全球高武', 'number': '284.17万', 'ifend': '更新', 'author': '老鹰吃小鸡'}, {'bookname': '山海八荒录', 'number': '41.05万', 'ifend': '已完结', 'author': '洛水'}, {'bookname': '大医凌然', 'number': '108.06万', 'ifend': '更新', 'author': '志鸟村'}, {'bookname': '我才不会被女孩子欺负', 'number': '446万', 'ifend': '已完结', 'author': '废铁行者'}, {'bookname': '欺负仇人的女儿难道有错吗', 'number': '163万 ', 'ifend': '更新', 'author': '废铁行者'}, {'bookname': '雪中悍刀行', 'number': '455万', 'ifend': '已完结', 'author': '烽火戏诸侯'}, {'bookname': '限制级末日症候', 'number': '1000.03万', 'ifend': '更新', 'author': '全部成为F'}, {'bookname': '金棺陵兽', 'number': '20万', 'ifend': '已完结', 'author': '天下霸唱'}, {'bookname': '重生之超级战舰', 'number': '329.68万', 'ifend': '已完结', 'author': '彩虹之门'}, {'bookname': '惊悚乐园', 'number': '489.55万', 'ifend': '已完结', 'author': '三天两觉'}, {'bookname': '废土', 'number': '232万', 'ifend': '已完结', 'author': '黑天魔神'}, {'bookname': '感染体', 'number': '215万', 'ifend': '已完结', 'author': '黑天魔神'}, {'bookname': '事象的宏图', 'number': '116万', 'ifend': '更新', 'author': 'ddt药剂'}, {'bookname': '魔王奶爸', 'number': '643万', 'ifend': '已完结', 'author': '盘古混沌'}, {'bookname': '狩魔笔记', 'number': '224万', 'ifend': '已完结', 'author': '烟雨江南'}, {'bookname': '寂静王冠', 'number': '301万', 'ifend': '已完结', 'author': '风月'}, {'bookname': '疯狂的多塔', 'number': '255万', 'ifend': '已完结', 'author': '奥丁信使'}, {'bookname': '单机狂魔', 'number': '137.30万', 'ifend': '已完结', 'author': '静谧长夜'}, {'bookname': '龙蛇演义', 'number': '220万', 'ifend': '已完结', 'author': '梦入神机'}, {'bookname': '妞非在下', 'number': '312万', 'ifend': '已完结', 'author': '月下小羊'}, {'bookname': '露米娅的微小印记', 'number': '58万', 'ifend': '已完结', 'author': '相位行者'}]
  	,even: true
  	,page: false
   ,limit: 9999
  });
});
</script>
'''
