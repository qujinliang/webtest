from pyecharts import Bar

def _bar(fz,value):
	fz = fz
	value = value
	bar = Bar("我的第一个图表",'单位/万')
	bar.add('服装',fz,value)
	bar.show_config()
	bar.render()

fz = ['衬衫','羊毛衫','雪纺娃','裤子','高跟鞋','袜子']
value = [5,20,36,10,75,90]
_bar(fz,value)