import requests
import re
from . import GameInfo


class ItchIoParser:
    def __init__(self, pages_to_go_through=1):
        self._pages = pages_to_go_through
        self._itch = 'https://itch.io/games/genre-visual-novel'
        single_desc_patterns = [
            '(?<=<h1>)[^<]+',
            '(?<=<h2>)[^<]+',
            '(?<=<p>)[^<]+',
            '(?<=<strong>)[^<]+',
            '(?<=<blockquote>)[^<]+',
            '(?<=class="text-justify">)[^<]+',
            '(?<=class="text-center">)[^<]+',
            '(?<=<em>)[^<]+',
            '(?<=<em><class>)[^<]+'
        ]
        self._description_patterns = re.compile('|'.join(single_desc_patterns))
        self._game_links_pattern = \
            re.compile('(?<=href=\")https://[^/\"]+/[^\"]+')
        desc_block_r = '(?<=formatted_description user_formatted\">).+' + \
                       '(?=<div class=\"more_information_toggle)'
        self._description_block_pattern = re.compile(desc_block_r, re.DOTALL)
        self._symbols = re.compile('&[^;]+;')
        self._image_link = re.compile(
            r'(?<=has_image align_center" id="header"><img src=")[^"]+')
        self._shot_link = re.compile(r'(?<=screenshot_list"><a href=")[^"]+')

    def get_games(self):
        games = []
        for page in range(self._pages):
            r = requests.get(self._itch + '?page={}&format=json'.format(page))
            content = r.json()['content']
            game_links = set(self._game_links_pattern.findall(content))

            c = 1
            for link in game_links:
                try:
                    games.append(self._get_game_info(link))
                    print('page', page + 1, 'game', c,
                          '(printed from ItchIoParser.get_games())')
                    c += 1
                except requests.exceptions.ConnectionError:
                    continue

        return games

    def _get_game_info(self, link):
        r = requests.get(link)
        game_page_content = r.content.decode('utf-8')
        description = self._get_description(game_page_content)
        image_link = self._get_image_link(game_page_content)
        return GameInfo.GameInfo(link, image_link, description)

    def _get_image_link(self, game_page_content):
        main_image = self._image_link.findall(game_page_content)
        if len(main_image) > 0:
            return main_image[0]
        else:
            screenshot = self._shot_link.findall(game_page_content)
            return screenshot[0] if len(screenshot) > 0 else ''

    def _get_description(self, game_page_content):
        try:
            block_with_description = \
                self._description_block_pattern.findall(game_page_content)[0]
            desc_lines = \
                self._description_patterns.findall(block_with_description)
            spaced_lines = [self._symbols.sub(' ', l) for l in desc_lines]
            return ' '.join(spaced_lines)
        except IndexError as e:
            raise e


