import requests
from bs4 import BeautifulSoup

sports = input("Enter the sports name: ")

final_url = 'http://timesofindia.indiatimes.com/sports/' + sports

f = open('times_of_india_news.csv', 'w')
list_of_cell = []

# FOOTBALL
# OKAY HAI !!
if sports == "football":

        # NEWS FROM TOP_STORIES
        top_Stories_url = final_url + '/top-stories'
        response = requests.get(top_Stories_url)
        html = response.content
        source = BeautifulSoup(html)
        i = 1
        print("NEWS FROM THE TOP STORIES: \n")
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # NEWS FROM INTERVIEWS
        Interviews_url = final_url + '/interviews'
        response = requests.get(Interviews_url)
        html = response.content
        source = BeautifulSoup(html)
        print("NEWS FROM THE INTERVIEWS: \n")
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # NEWS FROM EPL Top-Stories
        epl_url = final_url + '/epl'
        response = requests.get(epl_url + '/top-stories')
        html = response.content
        source = BeautifulSoup(html)
        print("NEWS FROM THE EPL TOP_STORIES: \n")
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # NEWS FROM ChampionsLeague Top-Stories
        champion_league_url = 'http://timesofindia.indiatimes.com/sports/football/champions-league/articlelist/40924344.cms'
        response = requests.get(champion_league_url)
        html = response.content
        source = BeautifulSoup(html)
        print("NEWS FROM THE CHAMPIONS_LEAGUE TOP_STORIES: \n")
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # NEWS FROM Copa_America Top-Stories
        copa_america_url = 'http://timesofindia.indiatimes.com/sports/Copa-America-2015/articlelist/47642055.cms'
        response = requests.get(copa_america_url)
        html = response.content
        source = BeautifulSoup(html)
        print("NEWS FROM THE COPA_AMERICA TOP_STORIES: \n")
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # NEWS FROM I-LEAGUE TOP_STORIES
        i_league_url = final_url + '/i-league'
        response = requests.get(i_league_url)
        html = response.content
        source = BeautifulSoup(html)

        print("NEWS FROM THE I-LEAGUE TOP_STORIES: \n")
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # NEWS FROM ISL TOP-STORIES
        isl_url = 'http://timesofindia.indiatimes.com/sports/football/indian-super-league/top-stories/articlelist/24669705.cms'
        response = requests.get(isl_url)
        html = response.content
        source = BeautifulSoup(html)
        print("NEWS FROM THE ISL TOP_STORIES: \n")
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))


# TENNIS
# OKAY HAI !!
elif sports == 'tennis':
        tennis_url = final_url + '/tennis'

        # NEWS FROM TOP STORIES
        response = requests.get(final_url + '/top-stories')
        html = response.content
        source = BeautifulSoup(html)
        i = 1
        print('NEWS FROM TOP_STORIES:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # NEWS FROM INTERVIEWS
        response = requests.get(final_url + '/interviews')
        html = response.content
        source = BeautifulSoup(html)
        print('NEWS FROM INTERVIEWS:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # NEWS FROM CHENNAI OPEN
        response = requests.get('http://timesofindia.indiatimes.com/sports/tennis/chennai-open-2016/articlelist/49058499.cms')
        html = response.content
        source = BeautifulSoup(html)
        print('NEWS FROM CHENNAI OPEN:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # NEWS FROM AUSTRALIAN OPEN TOP_STORIES
        response = requests.get('http://timesofindia.indiatimes.com/sports/tennis/australian-open-2016/top-stories/articlelist/50369586.cms')
        html = response.content
        source = BeautifulSoup(html)
        print('NEWS FROM AUSTRALIAN OPEN TOP_STORIES:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # NEWS FROM IPTL
        response = requests.get('http://timesofindia.indiatimes.com/sports/tennis/iptl/articlelist/31481400.cms')
        html = response.content
        source = BeautifulSoup(html)
        print('NEWS FROM IPTL:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))


# CRICKET
# OKAY HAI !!
elif sports == "cricket":
        final_url = 'http://www.cricbuzz.com/?utm_source=TOISports_Cricwidget&utm_medium=ABtest&utm_campaign=TOISports'
        response = requests.get(final_url)
        html = response.content
        source = BeautifulSoup(html)
        i = 1
        print("NEWS: \n")
        for divisions in source.findAll('div', {'class': 'cb-col-100 cb-lst-itm cb-lst-itm-sm'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        for divisions1 in source.findAll('div', {'class': 'big-crd-main cb-bg-white'}):
            print(str(i) + "--->" + divisions1.text)
            i += 1
            text = divisions1.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        for headings in source.findAll('h2', {'div': 'big-crd-hdln'}):
            print(str(i) + "--->" + headings.text)
            i += 1
            text = headings.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        for headings1 in source.findAll('h2', {'div': 'sml-crd-hdln'}):
            print(str(i) + "--->" + headings1.text)
            i += 1
            text = headings1.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        for divisions2 in source.findAll('div', {'class': 'big-crd-reltd-itm'}):
            print(str(i) + "--->" + divisions2.text)
            i += 1
            text = divisions2.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        for divisions3 in source.findAll('div', {'class': 'cb-nws-intr'}):
            print(str(i) + "--->" + divisions3.text)
            i += 1
            text = divisions3.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        for divisions4 in source.findAll('div', {'class': 'cb-nws-intr cb-lst-itr-txt'}):
            print(str(i) + "--->" + divisions4.text)
            i += 1
            text = divisions4.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        for divisions5 in source.findAll('div', {'class': 'module-content-container'}):
            print(str(i) + "--->" + divisions5.text)
            i += 1
            text = divisions5.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))


# BADMINTON
elif sports == "badminton":
        response = requests.get(final_url)
        html = response.content
        source = BeautifulSoup(html)
        i = 1
        print("NEWS: \n")
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u200B', "")
            list_of_cell.append(text.replace(',', ';'))


# HOCKEY
elif sports == 'hockey':

        # TOP_STORIES
        response = requests.get(final_url + '/top-stories')
        html = response.content
        source = BeautifulSoup(html)
        i = 1
        print('NEWS FROM TOP_STORIES:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + '--->' + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # HOCKEY INDIA LEAGUE TOP_STORIES
        hil_url = 'http://timesofindia.indiatimes.com/sports/hockey/hockey-india-league/top-stories/articlelist/18007462.cms'
        response = requests.get(hil_url)
        html = response.content
        source = BeautifulSoup(html)
        print('NEWS FROM HOCKEY INDIA LEAGUE:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + '--->' + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))


# GOLF
elif sports == 'golf':

        # TOP_STORIES
        response = requests.get(final_url + '/top-stories')
        html = response.content
        source = BeautifulSoup(html)
        i = 1
        print('NEWS FROM TOP_STORIES:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + '--->' + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # GOLF INTERVIEWS NEWS:
        response = requests.get(final_url + '/interviews')
        html = response.content
        source = BeautifulSoup(html)
        print('NEWS FROM INTERVIEWS:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + '--->' + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))


# RACING
elif sports == 'racing':

        # TOP_STORIES
        response = requests.get(final_url + '/top-stories')
        html = response.content
        source = BeautifulSoup(html)
        i = 1
        print('NEWS FROM TOP_STORIES:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + '--->' + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # RACING INTERVIEWS NEWS:
        response = requests.get(final_url + '/interviews')
        html = response.content
        source = BeautifulSoup(html)
        print('NEWS FROM INTERVIEWS:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + '--->' + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # NEWS FROM INDIAN-GP:
        response = requests.get(final_url + '/indian-gp')
        html = response.content
        source = BeautifulSoup(html)
        print('NEWS FROM INDIAN-GP:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + '--->' + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

# NBA
elif sports == 'nba':

        # TOP_STORIES
        response = requests.get(final_url + '/top-stories')
        html = response.content
        source = BeautifulSoup(html)
        i = 1
        print('NEWS FROM TOP_STORIES:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + '--->' + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

        # OFF THE COURT
        response = requests.get('http://timesofindia.indiatimes.com/sports/nba/off-the-court/articlelist/8014746.cms')
        html = response.content
        source = BeautifulSoup(html)
        print('NEWS FROM OFF THE COURT:')
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + '--->' + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))


# CHESS
elif sports == "chess":
        response = requests.get(final_url)
        html = response.content
        source = BeautifulSoup(html)
        i = 1
        print("NEWS: \n")
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

# BOXING
elif sports == "boxing":
        final_url = 'http://timesofindia.indiatimes.com/sports/boxing/articlelist/3413166.cms'
        response = requests.get(final_url)
        html = response.content
        source = BeautifulSoup(html)
        i = 1
        print("NEWS: \n")
        for divisions in source.findAll('div', {'id': 'fsts'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))


# MORE_SPORTS
else:
        final_url = 'http://timesofindia.indiatimes.com/sports/more-sports'
        response = requests.get(final_url)
        html = response.content
        source = BeautifulSoup(html)
        i = 1
        print("NEWS: \n")
        for divisions in source.findAll('td', {'style': 'padding:10px 0px 10px 15px;font-size:13px;height:82px;'}):
            print(str(i) + "--->" + divisions.text)
            i += 1
            text = divisions.text.replace(u'\u2009', "'")
            list_of_cell.append(text.replace(',', ';'))

print(list_of_cell)
f.write("\n".join(list_of_cell))
f.close()
