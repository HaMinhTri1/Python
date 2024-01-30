a = 'spam'
b = list(a)#chuyen doi kieu string sang list, hien thi tung phan tu trong kieu string
print(b)
c = 'spam spam spam'
d = c.split()#chia cac phan tu string sang list bang dau cach " "
print(d)
e = 'spam-spam1-spam2'
delimiter = '-'
f = e.split(delimiter)#chia cacs tu trong string sang list danh dau bang "-"
print(f)
delim = 'a'
g=e.split(delim)#chia cac phan tu trong string sang list danh dau bang ky tu 'a
print(g)
print(delim.join(g))#chen cac ky tu 'a' vao list bi cat, noi tiep vao cac phan tu