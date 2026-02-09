
from bs4 import BeautifulSoup
#open and read the books .html file
with open ("book.html")as html_file:
    content=html_file.read()
#print(content)
soup = BeautifulSoup(content,'html.parser')

print(soup.prettify())

tags = soup.find('h5')
heading = soup.find_all('h5')
h5_content = tags.text
print(tags)
print(heading)
print(content)

for  heading in heading :
    print(heading.text)

course_cards = soup.find_all('div',class_='card')

for course in course_cards:
    course_title =course.h5.text
    course_auth =course.p.text
    course_price=course.a.text.split()[-1]
    print(f"{course_title} cost{course_price} {course_auth}cost ")




