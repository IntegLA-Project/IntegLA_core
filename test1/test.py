from jinja2 import Template, Environment, FileSystemLoader
 
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
template = env.get_template('axpy.cpp.in')

blastypes=["double", "float"]
 
data = {'types' : blastypes}
data['t'] = 'd'
data['name'] = 'goma'
disp_text = template.render(data)

blastypes=["double", "float"]
 
gomatypes=["int", "long"]
data = {'types' : gomatypes}
data['t'] = 'd'
data['name'] = 'goma'
disp_text += template.render(data)
print(disp_text)
