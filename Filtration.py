

class Filtration:
    def __init__(self, pop_tags_to_links):
        self.pop_tags_to_links = pop_tags_to_links
        self.sad_answer = "Sorry, your request is too advanced. People haven't written anything about it yet."

    def find_perfect_match(self, *tags):
        perfect_matches = set()
        first_add = True
        try:
            for tag in tags:
                if first_add:
                    perfect_matches = set(self.pop_tags_to_links[tag])
                    first_add = False
                else:
                    perfect_matches = perfect_matches & set(self.pop_tags_to_links[tag])
        except KeyError as _:
            return self.sad_answer
        finally:
            if len(perfect_matches) == 0:
                return self.sad_answer
            return perfect_matches
