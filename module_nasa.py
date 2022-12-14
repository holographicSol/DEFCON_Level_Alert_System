import os
import distutils.dir_util
import datetime
import requests
import time
import requests
import subprocess
from bs4 import BeautifulSoup
import codecs
import re

nasa_climate_data = []
global_temperature = ''
carbon_dioxide = ''
arctic_sea_ice_extent, arctic_sea_ice_extent_units = '', ''
ice_sheets, ice_sheets_units = '', ''
sea_level, sea_level_error, sea_level_units = '', '', ''
ocean_heat_content, ocean_heat_content_error, ocean_heat_content_units = '', '', ''
debug_output = []
output = False


def nasa_climate():
    global nasa_climate_data, output

    try:
        dat_file = './data/nasa_climate' + '.txt'


        nasa_climate_data = []
        global_temperature = ''
        carbon_dioxide = ''
        arctic_sea_ice_extent, arctic_sea_ice_extent_units = '', ''
        ice_sheets, ice_sheets_units = '', ''
        sea_level, sea_level_error, sea_level_units = '', '', ''
        ocean_heat_content, ocean_heat_content_error, ocean_heat_content_units = '', '', ''

        url = 'https://climate.nasa.gov/vital-signs/global-temperature/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] [SCANNING] [NASA] ' + url)
        if output is True:
            debug_output.append(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            if row is not None:
                var = str(row).strip()
                if var.startswith('<div class="value">'):
                    global_temperature = var
        global_temperature = global_temperature.split()

        global_temperature_file = 'Global Temperature: ' + str(global_temperature[2]) + '°C'

        url = 'https://climate.nasa.gov/vital-signs/carbon-dioxide/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] [SCANNING] [NASA] ' + url)
        if output is True:
            debug_output.append(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            # print(row)
            if row is not None:
                var = str(row).strip()
                if var.startswith('<div class="value">'):
                    carbon_dioxide = var
        carbon_dioxide = carbon_dioxide.split()

        carbon_dioxide_file = 'Carbon Dioxide: ' + str(carbon_dioxide[2]) + 'ppm'

        url = 'https://climate.nasa.gov/vital-signs/arctic-sea-ice/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] [SCANNING] [NASA] ' + url)
        if output is True:
            debug_output.append(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            if row is not None:
                var = str(row).strip()
                if var.startswith('<div class="change_number">'):
                    arctic_sea_ice_extent = var
                if var.startswith('<div class="graph_rate_units">'):
                    arctic_sea_ice_extent_units = var
        arctic_sea_ice_extent = arctic_sea_ice_extent.split()
        arctic_sea_ice_extent_units = arctic_sea_ice_extent_units.split()

        arctic_sea_ice_extent_file = 'Antarctica Ice: ' + str(arctic_sea_ice_extent[2]) + '% ' + str(arctic_sea_ice_extent_units[3]) + ' ' + str(arctic_sea_ice_extent_units[4])

        url = 'https://climate.nasa.gov/vital-signs/ice-sheets/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] [SCANNING] [NASA] ' + url)
        if output is True:
            debug_output.append(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            if row is not None:
                var = str(row).strip()
                if var.startswith('<div class="change_number">'):
                    ice_sheets = var
                if var.startswith('<div class="graph_rate_units">'):
                    ice_sheets_units = var
        ice_sheets = ice_sheets.split()
        ice_sheets_units = ice_sheets_units.split()

        ice_sheets_file = 'Greenland Ice: ' + str(ice_sheets[2]) + ' ' + str(ice_sheets_units[2]) + ' ' + str(ice_sheets_units[3]) + ' ' + str(ice_sheets_units[4]) + ' ' + str(ice_sheets_units[5]) + ' ' + str(ice_sheets_units[6])

        url = 'https://climate.nasa.gov/vital-signs/sea-level/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] [SCANNING] [NASA] ' + url)
        if output is True:
            debug_output.append(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            if row is not None:
                var = str(row).strip()
                if var.startswith('<div class="value">'):
                    sea_level = var
        sea_level = sea_level.split()

        sea_level_file = 'Sea Level: ' + str(sea_level[2]) + str(sea_level[5]) + str(sea_level[6]) + str(sea_level[10])

        url = 'https://climate.nasa.gov/vital-signs/ocean-heat/'
        technical_data = str('[' + str(datetime.datetime.now()) + '] [SCANNING] [NASA] ' + url)
        if output is True:
            debug_output.append(technical_data)

        rHead = requests.get(url)
        data = rHead.text
        soup = BeautifulSoup(data, "html.parser")
        for row in soup.find_all():
            if row is not None:
                var = str(row).strip()
                if var.startswith('<div class="value">'):
                    ocean_heat_content = var
        ocean_heat_content = ocean_heat_content.split()

        ocean_heat_content_file = 'Ocean Heat Content: ' + str(ocean_heat_content[2]) + str(ocean_heat_content[5]) + str(ocean_heat_content[6]) + str(ocean_heat_content[10])

        tm_stamp = str(datetime.datetime.now())
        toFile = '[' + tm_stamp + ']' + '   ' + str(global_temperature_file + '   ' + carbon_dioxide_file + '   ' + arctic_sea_ice_extent_file + '   ' + ice_sheets_file + '   ' + sea_level_file + '   ' + ocean_heat_content_file)
        to_file_check = str(global_temperature_file + '   ' + carbon_dioxide_file + '   ' + arctic_sea_ice_extent_file + '   ' + ice_sheets_file + '   ' + sea_level_file + '   ' + ocean_heat_content_file)

        # if output is True:
        #     print(toFile)

        tmp_str_in_file = ''
        if os.path.exists(dat_file):
            with codecs.open(dat_file, 'r', encoding='utf-8') as fo:
                for line in fo:
                    line = line.strip()
                    tmp_str_in_file = line

        if not tmp_str_in_file.endswith(to_file_check):
            if output is True:
                debug_output.append('[' + str(datetime.datetime.now()) + ']' + ' [NASA] Updating Stored Data')
            with codecs.open('./data/nasa_climate.txt', 'a', encoding="UTF-8") as fo:
                fo.write(toFile + '\n')
            fo.close()
        else:
            if output is True:
                debug_output.append('[' + str(datetime.datetime.now()) + '] [NASA] Data is already up to date')

    except Exception as e:
        technical_data = str('[' + str(datetime.datetime.now()) + '] [NASA] ' + str(e))
        debug_output.append(technical_data)

