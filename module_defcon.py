"""
Written by Benjamin Jack Cullen aka Holographic_Sol
"""
import os
import codecs
import datetime
import requests
from bs4 import BeautifulSoup

title = []
defcon_level = []

debug_output = []

soup_defcon_news_current_level = []
soup_defcon_news_strat_com = []
soup_defcon_news_indo_pac_com = []
soup_defcon_news_euro_com = []
soup_defcon_news_africa_com = []
soup_defcon_news_cent_com = []
soup_defcon_news_cyber_com = []
soup_defcon_news_northern_com = []
soup_defcon_news_southern_com = []
soup_defcon_news_space_com = []
soup_defcon_news_spacial_op_com = []
soup_defcon_news_transportation_com = []

dc_img = ['https://www.defconlevel.com/levels/defcon-1.php',
          'https://www.defconlevel.com/levels/defcon-2.php',
          'https://www.defconlevel.com/levels/defcon-3.php',
          'https://www.defconlevel.com/levels/defcon-4.php',
          'https://www.defconlevel.com/levels/defcon-5.php']

levels = ['DEFCON 1: Cocked Pistol',
          'DEFCON 2: Fast Pace',
          'DEFCON 3: Round House',
          'DEFCON 4: Double Take',
          'DEFCON 5: Fade Out']

output = True
debug = False


def get_defcon_levels(save_defcon_levels=False):
    global title, defcon_level, output
    title = []
    defcon_level = []

    url = ('https://www.defconlevel.com/current-alerts.php')
    rHead = requests.get(url)
    data = rHead.text
    soup = BeautifulSoup(data, "html.parser")

    for row in soup.find_all('div', class_='page-sub-titles'):
        text = row.get_text()
        text = str(text).strip()
        if text not in title:
            if not text.endswith('|'):
                debug_output.append(('[' + str(datetime.datetime.now()) + '] [SCANNING] [DEFCON] ' + str(text)))
                title.append(text.replace(' (OSINT Estimate)', ''))

    i = 0
    for link in soup.find_all('a'):
        href = (link.get('href'))
        href = str(href).strip()

        if href in dc_img:
            if i >= 5:
                debug_output.append('[' + str(datetime.datetime.now()) + '] [SCANNING] [DEFCON] ' + str(href))
                defcon_level.append(str(dc_img.index(href)+1))
            i += 1

    if save_defcon_levels is True:
        write_defcon_levels()


def write_defcon_levels():
    global title, defcon_level, output

    defcon_l_title = ['Live Overall Defcon Level',
                      'Live Regional Africa Command Alert',
                      'Live Regional Central Command Alert',
                      'Live Regional Cyber Command Alert',
                      'Live Regional European Command Alert',
                      'Live Regional Indo-Pacific Command Alert',
                      'Live Regional Northern Command Alert',
                      'Live Regional Southern Command Alert',
                      'Live Regional Space Command Alert']

    checks_passed = False

    # check data before writing
    if title and defcon_level:

        if debug is True:
            print('check 1: title and defcon_level has data.')

        # check len of title
        if len(title) == len(defcon_l_title):

            if debug is True:
                print('check 2: title list alignment: True')

            # check len of defcon level
            if len(defcon_level) == len(defcon_l_title):

                if debug is True:
                    print('check 3: defcon_level list alignment: True')

                # check titles
                check_title = []
                i = 0
                for _ in title:
                    if _ == defcon_l_title[i]:
                        check_title.append(True)
                    i += 1

                # check all titles passed check
                if len(check_title) == len(defcon_l_title):

                    if debug is True:
                        print('check 4: title list has correct values: True')

                    # check defcon levels
                    check_levels = []
                    i = 0
                    for _ in defcon_level:
                        if _.isdigit():
                            check_levels.append(True)
                        i += 1

                    # check all levels passed check
                    if len(check_levels) == len(defcon_l_title):

                        if debug is True:
                            print('check 4: defcon_level list has correct values: True')

                        checks_passed = True

                    else:
                        if debug is True:
                            print('check 4: defcon_level list has correct values: True')

                else:
                    if debug is True:
                        print('check 4: title list has correct values: False')

            else:
                if debug is True:
                    print('check 3: defcon_level list alignment: False')

        else:
            if debug is True:
                print('check 2: title list alignment: False')

    else:
        if debug is True:
            print('check 1: title and or defcon_level has no data.')

    if checks_passed is True:
        if debug is True:
            print('passed checks.')
        debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] Data checks: passed')

        bool_write = False
        to_file = []

        # compile lines to be written to file
        i = 0
        for _ in title:
            to_file.append(defcon_level[i] + '   ' + _ + '   ' + levels[int(defcon_level[i])-1])
            i += 1

        # check for changes before writing
        if os.path.exists('./data/defcon_level.txt'):
            with open('./data/defcon_level.txt', 'r') as fo:
                i = 0
                for line in fo:
                    if i != 0:
                        line = line.strip()
                        if debug is True:
                            print('comparing:', line, '-->', to_file[i - 1])
                        if line != to_file[i-1]:
                            bool_write = True
                    i += 1
        else:
            bool_write = True

        # finally update values on disk
        if bool_write is True:
            if debug is True:
                print('new values are different from values stored on disk: updating stored values.')
            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] updating stored values.')
            open('./data/defcon_level.txt', 'w').close()
            with open('./data/defcon_level.txt', 'a') as fo:
                fo.write('[LAST_UPDATED]   ' + str(datetime.datetime.now()) + '\n')
            i = 0
            for _ in to_file:
                with open('./data/defcon_level.txt', 'a') as fo:
                    fo.write(_ + '\n')
                i += 1
        else:
            if debug is True:
                print('new values are not different from values stored on disk: stored vales will not be overwritten.')
            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] no changes: stored data will not be overwritten.')
    else:
        if debug is True:
            print('failed checks.')
        debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] Data checks: failed')


def defcon_news(save_news=False):
    global soup_defcon_news_current_level
    global soup_defcon_news_strat_com
    global soup_defcon_news_indo_pac_com
    global soup_defcon_news_euro_com
    global soup_defcon_news_africa_com
    global soup_defcon_news_cent_com
    global soup_defcon_news_cyber_com
    global soup_defcon_news_northern_com
    global soup_defcon_news_southern_com
    global soup_defcon_news_space_com
    global soup_defcon_news_spacial_op_com
    global soup_defcon_news_transportation_com

    try:

        # get defcon current level news
        out_file = './data/defcon_news_current_news.txt'
        _text = []
        url = ('https://www.defconlevel.com/current-level.php')
        debug_output.append('[' + str(datetime.datetime.now()) + '] [SCANNING] [DEFCON] ' + str(url))
        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all('p'):
            text = row.get_text()
            text = str(text).strip()
            if text != 'Live Defcon Level Warning System News Flash':
                if text != 'Privacy Is Important! Defcon Level Warning System currently highly recommends Express VPN to browse privately & securely. Use This Link to get 30 free days.':
                    if text != 'Want To Support What We Do? Keeping alerts, intel and news as informative and timely as possible takes a lot of research, time, effort and financial investment for required tools and services. There are many ways you can Contribute or Subscribe to Defcon Level Warning System today, for live email updates, early access for and exclusive news and alerts while supporting our work in the process. No contribution is too small. Thank you!':
                        _text.append(text)
        if _text != soup_defcon_news_current_level:
            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [CURRENT LEVEL NEWS] data: changed.')
            soup_defcon_news_current_level = _text
            if save_news is True:
                open(out_file + '.tmp', 'w').close()
                with codecs.open(out_file + '.tmp', 'a', encoding="UTF-8") as fo:
                    fo.write('[CURRENT LEVEL NEWS]' + '\n')
                    fo.writelines('[LAST UPDATED] ' + str(datetime.datetime.now()) + '\n\n')
                    for _texts in _text:
                        fo.writelines(_texts+'\n\n')
                fo.close()
                try:
                    if not os.path.exists(out_file):
                        open(out_file, 'w').close()
                    os.replace(out_file + '.tmp', out_file)
                except Exception as e:
                    debug_output.append(
                        '[' + str(datetime.datetime.now()) + '] [DEFCON] [CURRENT LEVEL NEWS] ' + str(e))
        else:
            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [CURRENT LEVEL NEWS] data: unchanged.')

        # compile list of news urls
        url = 'https://www.defconlevel.com/news-alerts.php'
        debug_output.append('[' + str(datetime.datetime.now()) + '] [SCANNING] [DEFCON] ' + str(url))
        url_item = []
        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None:
                if href.endswith('command-news.php'):
                    if 'archive' not in href:
                        if href not in url_item:
                            url_item.append(href)

        # step over each news url
        for _ in url_item:
            url = _
            debug_output.append('[' + str(datetime.datetime.now()) + '] [SCANNING] [DEFCON] ' + str(url))

            # create filename from url string
            article_title = _.replace('https://www.defconlevel.com/', '').replace('.php', '')
            out_file = './data/defcon_news_' + article_title.replace('/', '') + '.txt'

            # parse news url for news data
            rHead = requests.get(url)
            data = rHead.text
            soup = BeautifulSoup(data, "html.parser")
            to_file = []
            for row in soup.find_all('p'):
                text = row.get_text()
                text = text.strip()
                if not 'Privacy Is Important! Defcon Level Warning System currently highly recommends Express VPN to browse privately' in text:
                    if not 'Want To Support What We Do? Keeping alerts, intel and news as informative and timely as possible takes a lot of research, time, effort and financial investment for required tools and services. There are many ways you can Contribute or Subscribe to Defcon Level Warning System today, for live email updates, early access for and exclusive news and alerts while supporting our work in the process. No contribution is too small. Thank you!' in text:
                        if not text == 'Current News Flashes':
                            to_file.append(text+'\n')
                        elif text == 'Current News Flashes':
                            to_file.append('\n')

            # soup = to_file

            if 'strategic-command' in _:

                if to_file != soup_defcon_news_strat_com:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [STRATEGIC COMMAND] data: changed.')
                    soup_defcon_news_strat_com = to_file

                    if save_news is True:
                        open(out_file+'.tmp', 'w').close()
                        with codecs.open(out_file+'.tmp', 'a', encoding="UTF-8") as fo:
                            fo.writelines('[STRATEGIC COMMAND]\n')
                            fo.writelines('[LAST UPDATED] ' + str(datetime.datetime.now()) + '\n')
                            for to_files in to_file:
                                fo.writelines(to_files + '\n')
                        fo.close()
                        try:
                            if not os.path.exists(out_file):
                                open(out_file, 'w').close()
                            os.replace(out_file+'.tmp', out_file)
                        except Exception as e:
                            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [STRATEGIC COMMAND] ' + str(e))
                else:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [STRATEGIC COMMAND] data: unchanged.')

            elif 'indo-pacific-command' in _:
                if to_file != soup_defcon_news_indo_pac_com:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [INDO-PACIFIC COMMAND] data: changed.')
                    soup_defcon_news_indo_pac_com = to_file

                    if save_news is True:
                        open(out_file+'.tmp', 'w').close()
                        with codecs.open(out_file+'.tmp', 'a', encoding="UTF-8") as fo:
                            fo.writelines('[INDO-PACIFIC COMMAND]\n')
                            fo.writelines('[LAST UPDATED] ' + str(datetime.datetime.now()) + '\n')
                            for to_files in to_file:
                                fo.writelines(to_files + '\n')
                        fo.close()
                        try:
                            if not os.path.exists(out_file):
                                open(out_file, 'w').close()
                            os.replace(out_file + '.tmp', out_file)
                        except Exception as e:
                            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [INDO-PACIFIC COMMAND] ' + str(e))
                else:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [INDO-PACIFIC COMMAND] data: unchanged.')

            elif 'european-command' in _:
                if to_file != soup_defcon_news_euro_com:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [EUROPEAN COMMAND] data: changed.')
                    soup_defcon_news_euro_com = to_file

                    if save_news is True:
                        open(out_file + '.tmp', 'w').close()
                        with codecs.open(out_file + '.tmp', 'a', encoding="UTF-8") as fo:
                            fo.writelines('[EUROPEAN COMMAND]\n')
                            fo.writelines('[LAST UPDATED] ' + str(datetime.datetime.now()) + '\n')
                            for to_files in to_file:
                                fo.writelines(to_files + '\n')
                        fo.close()
                        try:
                            if not os.path.exists(out_file):
                                open(out_file, 'w').close()
                            os.replace(out_file + '.tmp', out_file)
                        except Exception as e:
                            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [EUROPEAN COMMAND] ' + str(e))
                else:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [EUROPEAN COMMAND] data: unchanged.')

            elif 'africa-command' in _:
                if to_file != soup_defcon_news_africa_com:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [AFRICA COMMAND] data: changed.')
                    soup_defcon_news_africa_com = to_file

                    if save_news is True:
                        open(out_file + '.tmp', 'w').close()
                        with codecs.open(out_file + '.tmp', 'a', encoding="UTF-8") as fo:
                            fo.writelines('[AFRICA COMMAND]\n')
                            fo.writelines('[LAST UPDATED] ' + str(datetime.datetime.now()) + '\n')
                            for to_files in to_file:
                                fo.writelines(to_files + '\n')
                        fo.close()
                        try:
                            if not os.path.exists(out_file):
                                open(out_file, 'w').close()
                            os.replace(out_file + '.tmp', out_file)
                        except Exception as e:
                            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [AFRICA COMMAND] ' + str(e))
                else:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [AFRICA COMMAND] data: unchanged.')

            elif 'central-command' in _:
                if to_file != soup_defcon_news_cent_com:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [CENTRAL COMMAND] data: changed.')
                    soup_defcon_news_cent_com = to_file

                    if save_news is True:
                        open(out_file + '.tmp', 'w').close()
                        with codecs.open(out_file + '.tmp', 'a', encoding="UTF-8") as fo:
                            fo.writelines('[CENTRAL COMMAND]\n')
                            fo.writelines('[LAST UPDATED] ' + str(datetime.datetime.now()) + '\n')
                            for to_files in to_file:
                                fo.writelines(to_files + '\n')
                        fo.close()
                        try:
                            if not os.path.exists(out_file):
                                open(out_file, 'w').close()
                            os.replace(out_file + '.tmp', out_file)
                        except Exception as e:
                            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [CENTRAL COMMAND] ' + str(e))
                else:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [CENTRAL COMMAND] data: unchanged.')

            elif 'cyber-command' in _:
                if to_file != soup_defcon_news_cyber_com:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [CYBER COMMAND] data: changed.')
                    soup_defcon_news_cyber_com = to_file

                    if save_news is True:
                        open(out_file + '.tmp', 'w').close()
                        with codecs.open(out_file + '.tmp', 'a', encoding="UTF-8") as fo:
                            fo.writelines('[CYBER COMMAND]\n')
                            fo.writelines('[LAST UPDATED] ' + str(datetime.datetime.now()) + '\n')
                            for to_files in to_file:
                                fo.writelines(to_files + '\n')
                        fo.close()
                        try:
                            if not os.path.exists(out_file):
                                open(out_file, 'w').close()
                            os.replace(out_file + '.tmp', out_file)
                        except Exception as e:
                            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [CYBER COMMAND] ' + str(e))
                else:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [CYBER COMMAND] data: unchanged.')

            elif 'northern-command' in _:
                if to_file != soup_defcon_news_northern_com:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [NORTHERN COMMAND] data: changed.')
                    soup_defcon_news_northern_com = to_file

                    if save_news is True:
                        open(out_file + '.tmp', 'w').close()
                        with codecs.open(out_file + '.tmp', 'a', encoding="UTF-8") as fo:
                            fo.writelines('[NORTHERN COMMAND]\n')
                            fo.writelines('[LAST UPDATED] ' + str(datetime.datetime.now()) + '\n')
                            for to_files in to_file:
                                fo.writelines(to_files + '\n')
                        fo.close()
                        try:
                            if not os.path.exists(out_file):
                                open(out_file, 'w').close()
                            os.replace(out_file + '.tmp', out_file)
                        except Exception as e:
                            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [NORTHERN COMMAND] ' + str(e))
                else:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [NORTHERN COMMAND] data: unchanged.')

            elif 'southern-command' in _:
                if to_file != soup_defcon_news_southern_com:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [SOUTHERN COMMAND] data: changed.')
                    soup_defcon_news_southern_com = to_file

                    if save_news is True:
                        open(out_file + '.tmp', 'w').close()
                        with codecs.open(out_file + '.tmp', 'a', encoding="UTF-8") as fo:
                            fo.writelines('[SOUTHERN COMMAND]\n')
                            fo.writelines('[LAST UPDATED] ' + str(datetime.datetime.now()) + '\n')
                            for to_files in to_file:
                                fo.writelines(to_files + '\n')
                        fo.close()
                        try:
                            if not os.path.exists(out_file):
                                open(out_file, 'w').close()
                            os.replace(out_file + '.tmp', out_file)
                        except Exception as e:
                            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [SOUTHERN COMMAND] ' + str(e))
                else:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [SOUTHERN COMMAND] data: unchanged.')

            elif 'space-command' in _:
                if to_file != soup_defcon_news_space_com:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [SPACE COMMAND] data: changed.')
                    soup_defcon_news_space_com = to_file

                    if save_news is True:
                        open(out_file + '.tmp', 'w').close()
                        with codecs.open(out_file + '.tmp', 'a', encoding="UTF-8") as fo:
                            fo.writelines('[SPACE COMMAND]\n')
                            fo.writelines('[LAST UPDATED] ' + str(datetime.datetime.now()) + '\n')
                            for to_files in to_file:
                                fo.writelines(to_files + '\n')
                        fo.close()
                        try:
                            if not os.path.exists(out_file):
                                open(out_file, 'w').close()
                            os.replace(out_file + '.tmp', out_file)
                        except Exception as e:
                            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [SPACE COMMAND] ' + str(e))
                else:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [SPACE COMMAND] data: unchanged.')

            elif 'special-operations-command' in _:
                if to_file != soup_defcon_news_spacial_op_com:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [SPECIAL OPERATIONS COMMAND] data: changed.')
                    soup_defcon_news_spacial_op_com = to_file

                    if save_news is True:
                        open(out_file + '.tmp', 'w').close()
                        with codecs.open(out_file + '.tmp', 'a', encoding="UTF-8") as fo:
                            fo.writelines('[SPECIAL OPERATIONS COMMAND]\n')
                            fo.writelines('[LAST UPDATED] ' + str(datetime.datetime.now()) + '\n')
                            for to_files in to_file:
                                fo.writelines(to_files + '\n')
                        fo.close()
                        try:
                            if not os.path.exists(out_file):
                                open(out_file, 'w').close()
                            os.replace(out_file + '.tmp', out_file)
                        except Exception as e:
                            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [SPECIAL OPERATIONS COMMAND] ' + str(e))
                else:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [SPECIAL OPERATIONS COMMAND] data: unchanged.')

            elif 'transportation-command' in _:
                if to_file != soup_defcon_news_transportation_com:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [TRANSPORTATION COMMAND] data: changed.')
                    soup_defcon_news_transportation_com = to_file

                    if save_news is True:
                        open(out_file + '.tmp', 'w').close()
                        with codecs.open(out_file + '.tmp', 'a', encoding="UTF-8") as fo:
                            fo.writelines('[TRANSPORTATION COMMAND]\n')
                            fo.writelines('[LAST UPDATED] ' + str(datetime.datetime.now()) + '\n')
                            for to_files in to_file:
                                fo.writelines(to_files + '\n')
                        fo.close()
                        try:
                            if not os.path.exists(out_file):
                                open(out_file, 'w').close()
                            os.replace(out_file + '.tmp', out_file)
                        except Exception as e:
                            debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [TRANSPORTATION COMMAND] ' + str(e))
                else:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] [TRANSPORTATION COMMAND] data: unchanged.')

    except Exception as e:
        technical_data = str('[' + str(datetime.datetime.now()) + '] [DEFCON] ' + str(e))
        debug_output.append(technical_data)
