import numpy as np

from tasks import Task1, Task2, Task3, Task4, Task5


class TestTask1:

    def test1(self):
        french = list(map(str, range(1, 100, 5)))
        pianists = list(map(str, range(1, 20, 1)))
        swimmers = list(map(str, range(1, 20, 3)))
        t = Task1(french, pianists, swimmers)
        ans = np.array(t.special_students())
        true_ans = ['10', '13', '19', '4', '7']
        assert set(true_ans) == set(ans)


class TestTask2:

    def test1(self):
        list_1 = [1, 2, 2, 3, 3, 5]
        list_2 = [2, 2, 3, 4, 3, 1, 6]
        t = Task2(list_1, list_2)
        uniq_list_1 = np.array([1, 2, 3, 5])
        uniq_both_lists = np.array([1, 2, 3, 4, 5, 6])
        assert np.all(t.get_unique_list_1() == uniq_list_1)
        assert np.all(t.get_unique_both_lists() == uniq_both_lists)

    def test2(self):
        np.random.seed(2)
        list_1 = np.random.randint(low=0, high=100, size=50)
        list_2 = np.random.randint(low=0, high=100, size=50)
        t = Task2(list_1, list_2)
        uniq_list_1 = np.array([4, 7, 8, 15, 20, 22, 31, 33, 34, 37, 38, 39, 40, 42, 43, 46, 47, 49, 50, 51, 52, 58,
                                63, 66, 67, 68, 69, 70, 72, 75, 76, 79, 80, 82, 83, 85, 88, 90, 95])
        uniq_both_lists = np.array([1, 4, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 21, 22, 26, 31, 32, 33, 34, 37, 38, 39,
                                    40, 42, 43, 46, 47, 49, 50, 51, 52, 55, 56, 57, 58, 60, 61, 62, 63, 66, 67, 68, 69,
                                    70, 72, 73, 74, 75, 76, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91, 95, 96,
                                    97, 99])
        assert np.all(t.get_unique_list_1() == uniq_list_1)
        assert np.all(t.get_unique_both_lists() == uniq_both_lists)

    def test3(self):
        list_1 = []
        list_2 = []
        t = Task2(list_1, list_2)
        uniq_list_1 = []
        uniq_both_lists = []
        assert np.all(t.get_unique_list_1() == uniq_list_1)
        assert np.all(t.get_unique_both_lists() == uniq_both_lists)


class TestTask3:

    def test1(self):
        films = list(map(str, [1, 2, 2, 3, 3, 5]))
        counts = {'2': 2, '3': 2, '1': 1, '5': 1}
        t = Task3(films)
        # Check that keys are in the right order
        assert np.all(list(t.get_results().keys()) == np.array(list(counts.keys())))
        # Check that the dicts are equal
        assert t.get_results() == counts

    def test2(self):
        np.random.seed(2)
        films = list(map(str, np.random.randint(low=0, high=20, size=1000)))
        t = Task3(films)
        counts = {'10': 59, '18': 59, '8': 59, '19': 58, '11': 56, '17': 54, '9': 54, '16': 53, '5': 52, '12': 50,
                  '0': 49, '2': 49, '6': 49, '1': 48, '15': 48, '14': 47, '7': 46, '4': 39, '13': 37, '3': 34}
        assert np.all(list(t.get_results().keys()) == np.array(list(counts.keys())))
        assert t.get_results() == counts

    def test3(self):
        films = []
        counts = {}
        t = Task3(films)
        assert np.all(list(t.get_results().keys()) == np.array(list(counts.keys())))
        assert t.get_results() == counts


class TestTask4:

    def test5(self):
        t = Task4('The quick brown fox jumps over the lazy dog.')
        counter = {'the': 2, 'quick': 1, 'over': 1, 'lazy': 1, 'jumps': 1, 'fox': 1, 'dog': 1, 'brown': 1}
        assert t.word_counter() == counter
        assert np.all(list(t.word_counter().keys()) == np.array(list(counter.keys())))


class TestTask5:

    def test6(self):
        family = {'P': ['U', 'V'], 'A': ['U', 'V'], 'I': ['U', 'V'], 'U': ['G', 'B'], 'V': ['D', 'J']}
        t = Task5(family)
        assert t.parents('I') == ['U', 'V']
        assert t.siblings('I') == ['P', 'A']
        assert t.children('I') == []
        assert t.grandparents('I') == ['G', 'B', 'D', 'J']
        assert t.grandchildren('G') == ['P', 'A', 'I']
