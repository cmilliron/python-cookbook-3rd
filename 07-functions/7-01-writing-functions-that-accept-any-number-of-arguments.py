def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

# Sample use
print(avg(1, 2))          # 1.5
print(avg(1, 2, 3, 4))    # 2.5



def anyargs(*args, **kwargs):
    print(args)      # A tuple
    print(kwargs)    # A dict
    
    
import html

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                  name=name,
                  attrs=attr_str,
                  value=html.escape(value))
    return element

# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
make_element('item', 'Albatross', size='large', quantity=6)

# Creates '<p>&lt;spam&gt;</p>'
make_element('p', '<spam>')