from django.shortcuts import render
import pandas as pd
from .temp_models import Classifier
from .temp_models import Filtration
from .temp_models import DataLoader
from django import forms


games_info = {gi for gi in DataLoader.load_pickled() if len(gi.image_link) > 0}
link_to_gi = {gi.link: gi for gi in games_info}
games_info_df = pd.DataFrame(data={
    'paper_text': [gi.description for gi in games_info],
    'link': [gi.link for gi in games_info]
})
classifier = Classifier.Classifier(games_info_df)
pop_tags_to_links = classifier.get_tags()
filtration = Filtration.Filtration(pop_tags_to_links)

first_visit = [
    'https://gbpatch.itch.io/our-life-nf',
    'https://oracleandbone.itch.io/a-summers-end',
    'https://zephyo.itch.io/you-left-me',
    'https://laundrybear.itch.io/morticians-tale',
    'https://batensan.itch.io/pizzaro-project-deep-dish',
    'https://via01.itch.io/dont-open-your-eyes',
    'https://nomnomnami.itch.io/contract-demon',
    'https://fymm-game.itch.io/ddp'
]
insomnia = [
    'https://hroft32.itch.io/rusty-punk',
    'https://klace.itch.io/windsofchange',
    'https://cockhole.itch.io/9-22',
    'https://deckerwolf.itch.io/super-taco-crew'
]
cute_nightmare = [
    'https://saikono.itch.io/tiny-bunny',
    'https://zephyo.itch.io/you-left-me',
    'https://clowndream.itch.io/hikeback',
    'https://garage-heathen.itch.io/whos-lila',
    'https://nikita-kryukov.itch.io/pmkm',
    'https://via01.itch.io/dont-open-your-eyes'
]

albums = {'First visit': first_visit,
          'Insomnia': insomnia,
          'Cute nightmare': cute_nightmare}

class TagForm(forms.Form):
    OPTIONS = tuple([(tag, tag) for tag in pop_tags_to_links])
    Tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                     choices=OPTIONS)


def index(req):
    if req.method == 'POST':
        form = TagForm(req.POST)
        if form.is_valid():
            selected_tags = form.cleaned_data.get('Tags')
            links = filtration.find_perfect_match(*selected_tags)
            selected_games = []
            for link in links:
                selected_games.append(link_to_gi[link])
    else:
        form = TagForm
        selected_games = games_info
    return render(req,
                  'projapp/index.html',
                  {'games': selected_games,
                   'tags': sorted(pop_tags_to_links.keys()),
                   'albums': albums,
                   'tag_form': form,
                   'albums': albums})


def album(req, album_name):
    album_games = [link_to_gi[link] for link in albums[album_name]]
    return render(req,
                  'projapp/album.html',
                  {'games': album_games,
                   'album_name': album_name})
