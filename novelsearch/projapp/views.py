from django.shortcuts import render
import pandas as pd
from .temp_models import Classifier
from .temp_models import Filtration
from .temp_models import GameInfo
from .temp_models import DataLoader
from django import forms


games_info = [
    GameInfo.GameInfo(
        'https://laburatory.itch.io/lgd',
        'https://img.itch.zone/aW1hZ2UvNjYwODIvNjUyMTEzLnBuZw==/original/xXHSUM.png',
        'Long Gone Days is a  2D modern-day military RPG set in our current times After being deployed to his first mission,  Rourke The Core the consequences of deserting an inescapable war With no place to call home now, he must prevent the war from spreading any further, forming strong bonds along the way that will forever change his life. Communication is Key: Keep Morale High: Sniper Mode: No Random Encounters'),
    GameInfo.GameInfo(
        'https://paranoidhawk.itch.io/lookouts',
        'https://img.itch.zone/aW1nLzg1NDkwMTQucG5n/original/yyDw%2FF.png',
        'Two lookouts meet in a desert, far from the sight of their gangs. With more in common than they could ve expected, they scout out a town with rumours of gold. What will become of this fateful meeting? Lookouts is a romance visual novel about two masc outlaws in the old west, finding refuge in each other, and a little hope for a better life. With roughly 45,000 words of story and a 5-6 hour reading time, it s a much expanded version of the original jam game we made for the Gay Western Jam. The original jam version can be played'),
    GameInfo.GameInfo(
        'https://teamsalvato.itch.io/ddlc',
                      'https://img.itch.zone/aW1hZ2UvMTA2NTk5LzQ5NDk5Ni5wbmc=/original/DuY5IT.png',
        'Hi, Monika here! Welcome to the Literature Club! It s always been a dream of mine to make something special out of the things I love. Now that you re a club member, you can help me make that dream come true in this cute game! Every day is full of chit-chat and fun activities with all of my adorable and unique club members: Sayori Natsuki Yuri Monika I m super excited for you to make friends with everyone and help the Literature Club become a more intimate place for all my members. But I can tell already that you re a sweetheart will you promise to spend the most time with me? ♥ DDLC Fan Pack Doki Doki Literature Club DDLC Fan Pack Just click the  Download DDLC Official Soundtrack High-resolution wallpapers DDLC Concept Art Booklet The Team Doki Doki Literature Club Dan Salvato Satchely Velinquent This game is not suitable for children'),
    GameInfo.GameInfo(
        'https://cantusmori.itch.io/froggy-pot',
        'https://img.itch.zone/aW1nLzc3NDI0NzQucG5n/original/qRKSbw.png',
        'A short cozy game with a small side of existential crisis. A super short, linear visual novel about a Froggy chilling a pot. The pot is warm now, but it will reach a boil soon... It will be dangerous then...so you try convincing Froggy to get out of the pot, as you  both begin to chat... About meaningless things,  mindless things... Why won t Froggy leave the pot? ⋆┈┈｡ﾟ❃ུ۪ ❀ུ۪ ❁ུ۪ ❃ུ۪ ❀ུ۪ ﾟ｡┈┈⋆ Notes :  ⋆┈┈｡ﾟ❃ུ۪ ❀ུ۪ ❁ུ۪ ❃ུ۪ ❀ུ۪ ﾟ｡┈┈⋆ Credits: Story, Art, Music'),
    GameInfo.GameInfo(
        'https://nikita-kryukov.itch.io/pmkm',
        'https://img.itch.zone/aW1nLzQxMjkxMTkucG5n/original/e8X%2BH3.png',
        'A short story about what sort of challenges everyday little things can be. Help the girl buy milk, be the first not to disappoint her. The game is a small visual novel, showing either funny abstraction and wordplay or painful psychological episodes. The claim that history is based on real events will be too specific, so it is easier to pretend that it is just a set of abstractions and wordplay. First of all, this is an artistic manipulation with word and form, only then - a game.'),
    GameInfo.GameInfo(
        'https://cozygamepals.itch.io/tokyo-snap-demo',
        'https://img.itch.zone/aW1nLzIzMzU1ODQucG5n/original/PZ76YD.png',
        'Warning! There is a bug on Safari with saving photos.  Spend a week in Tokyo to get some great photos for your feed. Learn the latest fashion trends, make friends, and take the perfect pictures to rack up likes on Street Snaps. If you enjoyed this demo, please support us by adding to your Steam wishlist. It improves our rankings and helps share this game with more people!'),
    GameInfo.GameInfo(
        'https://studioclump.itch.io/ssml',
        'https://img.itch.zone/aW1nLzg1MzE5NjMucG5n/original/sNRUjj.png',
        'A short comedy visual novel about your lunch and a thief... both of which are hot.'),
    GameInfo.GameInfo(
        'https://hectorbometon.itch.io/superego-1-2',
        'https://img.itch.zone/aW1nLzg0NjE0NTEucG5n/original/Wc4bFY.png',
        'Superego, Chap. 1+2 Superego Documentary Graphic Adventure'),
    GameInfo.GameInfo(
        'https://studio-elfriede.itch.io/because-were-here',
        'https://img.itch.zone/aW1nLzI5NDEyODEucG5n/original/zb1d9D.png',
        'Because We’re Here Can you find love amongst doomed youth? 1915, Wesslinger National Calendar. The Great War rages on. As neurotic Postal Corps volunteer Elfriede Rauss, you walk the trenches with the men of a lost generation. And amidst the chaos and brutality of the front lines, you encounter an obstacle that you are absolutely and categorically not prepared for: love. However. Love can be a difficult thing to hold on to at the best of times. And these are not the best of times...  A Horror-Tinged Anti-War Epic Romance a Diverse Array of Bachelors  Discover a Rich WW1-Inspired Setting  Master the  Battle of Wits m Estimated playthrough time for Act I ( Never Such Innocence Act II of Because We re Here '),
    GameInfo.GameInfo(
        'https://clowndream.itch.io/hikeback',
        'https://img.itch.zone/aW1nLzU0OTI5NzgucG5n/original/y2pX9J.png',
        'Let me tell you a story.  Originally created over the course of 10 days for the  HIKEBACK  INFINITY THRESHOLD --- FEATURES: --- BEFORE YOU PLAY: Due to the nature of this game, there are limited opportunities to  save  your progress. In general,  whenever you ve been returned to the title screen, your progress has been  saved.  Currently, the web version of the game suffers from lower audio/visual quality as well as some minor bugs due to the limitations of the software. However, it is still stable/playable, and the desktop version can be downloaded at any time. Additionally,  there is a  true  ending'),
]

#games_info = DataLoader.load_from_itch(1)
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
