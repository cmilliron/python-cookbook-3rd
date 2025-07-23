from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)

nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)