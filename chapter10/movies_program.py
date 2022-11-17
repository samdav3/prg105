

class Movie:
    def __init__(self, title, release_year, story_year):
        self.__title = title
        self.__release_year = release_year
        self.__story_year = story_year

    def set_title(self, title):
        self.__title = title

    def set_release_year(self, release_year):
        self.__release_year = release_year

    def set_story_year(self, story_year):
        self.__story_year = story_year

    def get_title(self):
        return self.__title

    def get_release_year(self):
        return self.__release_year

    def get_story_year(self):
        return self.__story_year


def main():
    movies = []
    file = open('MarvelMovies.csv', 'r')

    all_line = file.readline()
    all_line.rstrip('\n')

    for all_line in file:
        all_line.rstrip('\n')
        movies.append(all_line)
        all_line.rstrip('\n')
        for lines in movies:
            movies.append(lines)
            title = Movie.get_title(lines)
            release_year = Movie.get_release_year(lines)
            story_year = Movie.get_story_year(lines)

    print(f'\t\t' + 'Title' + '\t\t\t' + 'Release Year' + '\t' + 'Story Year')
    print(f'{title}' + '\t\t\t\t\t\t' + f'{release_year}' + '\t\t\t\t' + f'{story_year}')

    print(movies)


main()
