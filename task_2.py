class Movies:
    def __init__(self):
        # Инициализируем пустой список фильмов
        self.movies = []

    def add_movie(self, movie):
        # Добавляем фильм в список
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        # Добавляем фильм с помощью метода суперкласса
        super().add_movie(movie)
        # Возвращаем строку с текущим списком комедий
        return f'Комедии: {self.movies}'


class Drama(Movies):
    def add_movie(self, movie):
        # Добавляем фильм с помощью метода суперкласса
        super().add_movie(movie)
        # Возвращаем строку с текущим списком драм
        return f'Драмы: {self.movies}'


# Создаём объект Comedy и добавляем фильм
comedy = Comedy()
print(comedy.add_movie('Большой куш'))  # Вывод: Комедии: ['Большой куш']

# Создаём объект Drama и добавляем фильм
drama = Drama()
print(drama.add_movie('Оружейный барон'))  # Вывод: Драмы: ['Оружейный барон']
