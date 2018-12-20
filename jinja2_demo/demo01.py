from jinja2 import Template

# 创建一个模板，并渲染参数,{{variable}} 中是变量
template = Template('hello {{name}}')
print(template.render(name='john doe'))
