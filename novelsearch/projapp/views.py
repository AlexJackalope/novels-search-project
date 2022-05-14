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
                   'form': form})
