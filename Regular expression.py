#here we learn about regular expression in python#
import re
# pattern="and"
pattern=r"[A-Z]+ollaborating"#it is a string which we used to match in a text#
text='''
At Internshala, we are making this dream a reality!

This role is for those who love solving meaningful problems through modular and functional code. Our SDEs (web) work with our product team to deliver high-quality, high-impact products.

The learning curve for engineers at Internshala is huge. Our team works on several products (we have 2 main websites and an app, along with several minor websites in parallel). We work on some of the most advanced technologies, using languages like HTML, CSS, JS, PHP, React, Python, and more. Adding to this is a ton of analytics, server maintenance, and security-related tasks, resulting in a journey full of learning and fun. This role would be an ideal career start for a developer.
Selected intern's day-to-day responsibilities include:
1. Collaborating with our product and design teams to deliver high-quality and high-impact products
2. Taking ownership of the entire development process, from prototyping and creation to testing, deployment, and optimization
3. Writing accurate, modular, and readable code
4. Researching and implementing new technologies to enhance application performance and development efficiency
'''

match=re.search(pattern, text)#here we use match in that we use re.search inside pattern,text to search pattern string inside text#
matches=re.finditer(pattern, text)#here we use match in that we use re.finditer inside pattern text to find number of patterns in a text#

# print(match)

for match in matches:
    # print(match)
    # print(type(match.span()))
    print(match.span())