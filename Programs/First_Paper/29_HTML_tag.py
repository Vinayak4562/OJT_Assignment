import re

tag = input("enter the tag: ")
x = re.findall("<\w{5,}[^>]*>|<\/\w{5,}[^>]*>",tag)

print(x)
# enter the tag: <param> </paramod>
# OUT-PUT=['<param>', '</paramod>']

# enter the tag: <param>'HELLO" </param>  
# OUT-PUT=['<param>', '</param>']
