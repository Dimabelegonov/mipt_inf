class Task1:
    """Проблема с порядком элементов массива"""
    def __init__(self, french, pianists, swimmers):
        self.french = french
        self.pianists = pianists
        self.swimmers = swimmers

    def special_students(self):
        # TODO
        return list(set(self.swimmers) & set(self.pianists) - set(self.french))


class Task2:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def get_unique_list_1(self):
        """return unique elements of the first list"""
        # TODO
        return list(set(self.list_1))

    def get_unique_both_lists(self):
        """return unique elements of the both lists"""
        # TODO
        return list(set(self.list_1).union(set(self.list_2)))


class Task3:
    """Проблема с порядком элементов массива"""
    def __init__(self, films):
        self.films = films

    def get_results(self):
        import collections
        """return dict with counts"""
        # TODO
        d = collections.OrderedDict()
        films_set = set(self.films)
        for k in films_set:
            d[k] = self.films.count(k)

        return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))


class Task4:
    """Проблема с порядком элементов массива"""
    def __init__(self, text):
        self.text = text

    def word_counter(self):
        """word counter dict in descending order"""
        # TODO
        import collections
        d = collections.OrderedDict()
        self.text = self.text.lower()
        self.text = self.text.replace(".", "")
        a = self.text.split()
        a_set = set(a)
        for k in a_set:
            d[k] = self.text.count(k)

        return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))


class Task5:

    def __init__(self, family):
        self.family = family

    def parents(self, name):
        """ returns list of parents """
        # TODO
        return self.family[name]

    def grandparents(self, name):
        """ returns list of grandmothers and grandfathers """
        # TODO
        a = []
        for k in self.family[name]:
            for h in self.family[k]:
                a.append(h)
        return a

    def siblings(self, name):
        """ returns list of siblings """
        # TODO
        a = []
        for k in self.family:
            if k != name and self.family[k][0] in self.family[name] and self.family[k][1] in self.family[name]:
                a.append(k)
        return a

    def children(self, name):
        """ returns list of children """
        # TODO
        a = []
        for k in self.family:
            if name in self.family[k]:
                a.append(k)
        return a

    def grandchildren(self, name):
        """ returns list of grandchildren """
        # TODO
        a = []
        for k in self.family:
            if name in self.family[k]:
                for h in self.family:
                    if k in self.family[h]:
                        a.append(h)
        return a
