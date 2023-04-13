# f = open('mecz.txt', 'r')
# content = f.read()
# content = content.replace('\n','')
# l = 0
# for i in range(len(content)):
#     if i+1 != len(content):
#         print(i)
#         if content[i] != content[i+1]:
#             l = l + 1
#
# f = open('mecz.txt', 'r')
# content = f.read()
# content = content.replace('\n','')
#
# la = 0
# lb = 0
#
# for i in range(len(content)):
#     if content[i] == 'A':
#         la = la + 1
#     else:
#         lb = lb + 1
#     if abs(la - lb) > 2 and (la > 999 or lb > 999):
#         if la > 999:
#             print(f"A {la}:{lb}")
#         else:
#             print(f"B {la}:{lb}")
#         break

f = open('mecz.txt', 'r')
content = f.read()
content = content.replace('\n','')
passa = 0
passamax = 0
l = 1
team = ''
for i in range(len(content)):
    if i+1 != len(content):
        if content[i+1] == content[i]:
            passa = passa + 1
            if passa == 10:
                l = l + 1
            if passa > passamax:
                passamax = passa
                team = content[i]
        else:
            passa = 1
