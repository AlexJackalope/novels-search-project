class GameInfo:
    def __init__(self, link, image_link, description):
        self.link = link
        self.image_link = image_link
        self.description = description
        self.developer = '/'.join(link.split('/')[:-1])
