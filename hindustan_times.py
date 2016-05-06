import requests
from bs4 import BeautifulSoup

sports = input("Enter the sport: ")
print('\n')

f = open('hindustan_times_news.csv', 'w')
list_of_cells = []
final_url = 'http://www.hindustantimes.com/' + sports

# CRICKET
# OKAY HAI !!
if sports == 'cricket':
    response = requests.get(final_url)
    html = response.content
    source = BeautifulSoup(html)
    i = 1
    for division in source.findAll('div', {'class': 'top_single_story_option2_txt'}):
        print(str(i) + '--->' + division.text)
        i += 1
        text = division.text.replace('\n', '')
        text = division.text.replace(',', ';')
        list_of_cells.append(text)

    for division1 in source.findAll('div', {'class': 'top_news_txt'}):
        for link in division1.findAll('a'):
            print(str(i) + '--->' + link.text)
            i += 1
            text = link.text.replace('\n', '')
            text = link.text.replace(',', ';')
            list_of_cells.append(text)

    for division2 in source.findAll('div', {'class': 'list_txt'}):
        for link1 in division2.findAll('a'):
            print(str(i) + '--->' + link1.text)
            i += 1
            text = link1.text.replace('\n', '')
            text = link1.text.replace(',', ';')
            list_of_cells.append(text)

    for division3 in source.findAll('div', {'class': 'india_topNews_links'}):
        for link2 in division3.findAll('a'):
            print(str(i) + '--->' + link2.text)
            i += 1
            text = link2.text.replace(str('\n'), '')
            text = link2.text.replace(',', ';')
            list_of_cells.append(text)


# FOOTBALL
# OKAY HAI !!
elif sports == 'football':
    response = requests.get(final_url)
    html = response.content
    source = BeautifulSoup(html)
    i = 1
    for division in source.findAll('div', {'class': 'top_single_story_option2_txt'}):
        print(str(i) + '--->' + division.text)
        i += 1
        text = division.text.replace(',', ';')
        list_of_cells.append(text)

    for division1 in source.findAll('div', {'class': 'top_news_txt'}):
        for link in division1.findAll('a'):
            print(str(i) + '--->' + link.text)
            i += 1
            text = link.text.replace(',', ';')
            list_of_cells.append(text)

    for division2 in source.findAll('div', {'class': 'list_txt'}):
        for link1 in division2.findAll('a'):
            print(str(i) + '--->' + link1.text)
            i += 1
            text = link1.text.replace(',', ';')
            list_of_cells.append(text)

    for division3 in source.findAll('div', {'class': 'india_topNews_links'}):
        for link2 in division3.findAll('a'):
            print(str(i) + '--->' + link2.text)
            i += 1
            text = link2.text.replace(',', ';')
            list_of_cells.append(text)


# TENNIS
elif sports == 'tennis':
    response = requests.get(final_url)
    html = response.content
    source = BeautifulSoup(html)
    i = 1
    for division in source.findAll('div', {'class': 'top_single_story_option2_txt'}):
        print(str(i) + '--->' + division.text)
        i += 1
        print ("yolo1")
        text = division.text.replace(',', '-')
        list_of_cells.append(text)

    for division1 in source.findAll('div', {'class': 'top_news_txt'}):
        for link in division1.findAll('a'):
            print(str(i) + '--->' + link.text)
            i += 1
            print ("yolo2")
            text = link.text.replace(',', '-')
            list_of_cells.append(text)

    for division2 in source.findAll('div', {'class': 'list_txt'}):
        for link1 in division2.findAll('a'):
            print(str(i) + '--->' + link1.text)
            i += 1
            print ("yolo3")
            text = link1.text.replace(',', '-')
            list_of_cells.append(text)

    for division3 in source.findAll('div', {'class': 'india_topNews_links'}):
        for link2 in division3.findAll('a'):
            print(str(i) + '--->' + link2.text)
            i += 1
            print ("yolo4")
            text = link2.text.replace(',', '-')
            list_of_cells.append(text)


# OKAY HAI !!
else:
    final_url = 'http://www.hindustantimes.com/other-sports'
    response = requests.get(final_url)
    html = response.content
    source = BeautifulSoup(html)
    i = 1

    for division in source.findAll('div', {'class': 'top_single_story_option2_txt'}):
        print(str(i) + '--->' + division.text)
        i += 1
        text = division.text.replace(u'\u2009', "'")
        list_of_cells.append(text.replace(',', ';'))
        print(list_of_cells)

    for division1 in source.findAll('div', {'class': 'top_news_txt'}):
        for link in division1.findAll('a'):
            print(str(i) + '--->' + link.text)
            i += 1
            text = link.text.replace(u'\u2009', "'")
            list_of_cells.append(text.replace(',', ';'))
            print(list_of_cells)

    for division2 in source.findAll('div', {'class': 'list_txt'}):
        for link1 in division2.findAll('a'):
            print(str(i) + '--->' + link1.text)
            i += 1
            text = link1.text.replace(u'\u2009', "'")
            list_of_cells.append(text.replace(',', ';'))

    for division3 in source.findAll('div', {'class': 'india_topNews_links'}):
        for link2 in division3.findAll('a'):
            print(str(i) + '--->' + link2.text)
            i += 1
            text = link2.text.replace(u'\u2009', "'")
            list_of_cells.append(text.replace(',', ';'))



to_write = "\n".join(list_of_cells) 
print ("=-----------------------------------------------------------------------=")
print (to_write)
f.write(to_write.encode('ascii', 'ignore'))
f.close()
