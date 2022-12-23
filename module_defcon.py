"""
Written by Benjamin Jack Cullen aka Holographic_Sol
"""
import os
import codecs
import datetime
import time

import requests
from bs4 import BeautifulSoup
import re

title = []
defcon_level = []
debug_output = []

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

command_str = ['current-level',
               'africa-command',
               'central-command',
               'cyber-command',
               'european-command',
               'indo-pacific-command',
               'northern-command',
               'southern-command',
               'space-command',
               'special-operations-command',
               'strategic-command',
               'transportation-command']

f_command_str = ['[CURRENT LEVEL NEWS]',
                 '[AFRICA COMMAND]',
                 '[CENTRAL COMMAND]',
                 '[CYBER COMMAND]',
                 '[EUROPEAN COMMAND]',
                 '[INDO-PACIFIC COMMAND]',
                 '[NORTHERN COMMAND]',
                 '[SOUTHERN COMMAND]',
                 '[SPACE COMMAND]',
                 '[SPECIAL OPERATIONS COMMAND]',
                 '[STRATEGIC COMMAND]',
                 '[TRANSPORTATION COMMAND]']

news_urls = ['https://www.defconlevel.com/current-level.php',
             'https://www.defconlevel.com/africa-command-news.php',
             'https://www.defconlevel.com/central-command-news.php',
             'https://www.defconlevel.com/cyber-command-news.php',
             'https://www.defconlevel.com/european-command-news.php',
             'https://www.defconlevel.com/indo-pacific-command-news.php',
             'https://www.defconlevel.com/northern-command-news.php',
             'https://www.defconlevel.com/southern-command-news.php',
             'https://www.defconlevel.com/space-command-news.php',
             'https://www.defconlevel.com/special-operations-command-news.php',
             'https://www.defconlevel.com/strategic-command-news.php',
             'https://www.defconlevel.com/transportation-command-news.php']

soup_defcon_news_current_level = []
soup_defcon_news_africa_com = []
soup_defcon_news_cent_com = []
soup_defcon_news_cyber_com = []
soup_defcon_news_euro_com = []
soup_defcon_news_indo_pac_com = []
soup_defcon_news_northern_com = []
soup_defcon_news_southern_com = []
soup_defcon_news_space_com = []
soup_defcon_news_spacial_op_com = []
soup_defcon_news_strat_com = []
soup_defcon_news_transportation_com = []

soup_defcon = [soup_defcon_news_current_level,
               soup_defcon_news_africa_com,
               soup_defcon_news_cent_com,
               soup_defcon_news_cyber_com,
               soup_defcon_news_euro_com,
               soup_defcon_news_indo_pac_com,
               soup_defcon_news_northern_com,
               soup_defcon_news_southern_com,
               soup_defcon_news_space_com,
               soup_defcon_news_spacial_op_com,
               soup_defcon_news_strat_com,
               soup_defcon_news_transportation_com]

output = True
debug = False

replchars = re.compile(r'[\n\r]')


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


def replchars_to_hex(match):
    return r'\x{0:02x}'.format(ord(match.group()))


def defcon_news(save_news=False):
    global soup_defcon

    changed_data = []
    time.sleep(1)

    try:

        # step over each news url
        i_command = 0
        for _ in news_urls:

            # create non magical url
            url = _

            # create file header
            header = f_command_str[i_command]

            # create file name
            out_file = './data/defcon_news_' + command_str[i_command] + '.txt'

            # display url
            debug_output.append('[' + str(datetime.datetime.now()) + '] [SCANNING] [DEFCON] ' + str(url))

            # parse url
            rHead = requests.get(url)
            data = rHead.text
            soup = BeautifulSoup(data, "html.parser")

            # parse soup
            to_file = []
            for row in soup.find_all('p'):
                text = row.get_text().strip()

                # remove privacy statements
                if not 'Privacy Is Important! Defcon Level Warning System currently highly recommends Express VPN to browse privately' in text:
                    if not 'Want To Support What We Do? Keeping alerts, intel and news as informative and timely as possible takes a lot of research, time, effort and financial investment for required tools and services. There are many ways you can Contribute or Subscribe to Defcon Level Warning System today, for live email updates, early access for and exclusive news and alerts while supporting our work in the process. No contribution is too small. Thank you!' in text:
                        if not text == 'Current News Flashes':
                            to_file.append(text+'\n')
                        elif text == 'Current News Flashes':
                            to_file.append('\n')

            # check for changes
            data_changed = False
            i = 0
            for to_files in to_file:
                rpc0 = replchars.sub(replchars_to_hex, str(to_files)).strip()
                rpc0 = rpc0.replace('  ', ' ')
                try:
                    # compare once memory has been populated
                    if soup_defcon[i_command][i].strip() != rpc0:
                        # print('rpc0:                     ', rpc0)
                        # print('soup_defcon[i_command][i]:', soup_defcon[i_command][i])
                        # print('-----')
                        data_changed = True
                        soup_defcon[i_command][i] = rpc0
                except:
                    data_changed = True
                    soup_defcon[i_command].append(rpc0)
                i += 1

            if data_changed is True:
                print('data changed:', command_str[i_command])
            else:
                print('data unchanged:', command_str[i_command])

            # write changes
            if save_news is True and data_changed is True:
                print('saving new data:', command_str[i_command])

                # create temporary file
                open(out_file+'.tmp', 'w').close()
                with codecs.open(out_file+'.tmp', 'a', encoding="UTF-8") as fo:
                    fo.writelines(header + '\n')
                    fo.writelines('[LAST UPDATED] ' + str(datetime.datetime.now()) + '\n')
                    for to_files in to_file:
                        fo.writelines(to_files + '\n')
                fo.close()

                # save new data file
                try:
                    if not os.path.exists(out_file):
                        open(out_file, 'w').close()
                    os.replace(out_file+'.tmp', out_file)
                except Exception as e:
                    debug_output.append('[' + str(datetime.datetime.now()) + '] [DEFCON] ' + header + ' ' + str(e))

            i_command += 1

    except Exception as e:
        technical_data = str('[' + str(datetime.datetime.now()) + '] [DEFCON] ' + str(e))
        debug_output.append(technical_data)
