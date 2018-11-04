def tag(name,*content,cls=None,**attres):
    if cls:
        attres['class']=cls
    if attres:
        attr_str=''.join(' %s=""%s' % (attr,value) for attr, value in sorted(attres.items()))
    else:
        attr_str=''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name,attr_str,c,name) for c in content)
    else:
        return '<%s%s />' % (name,attr_str)


a=tag('br')
print(a)
a=tag('p','hello')
print(a)
a=tag('p','hello','world')
print(a)
a=tag('p','hello',id=3)
print(a)
a=tag(content='testing',name='img')
print(a)
my_tag={'name':'img','title':'sunset boulevard','src':'sunset.jpg','cls':'framed'}
a=tag(**my_tag)
print(a) 