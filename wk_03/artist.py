from datetime import datetime

class Artist:

    def __init__(self, name: str, num_members: int, start_year: int, genre: str|list):
        self.name = name
        self.num_members = num_members
        self.start_year = start_year
        self.end_year = datetime.now().year
        # self.genre = genre
        self.__genre = []
        self.add_genre(genre)
        self.catalog = {}

    @property
    def years_active(self):
        return self.end_year - self.start_year

    '''@years_active.setter
    def years_active(self, years):
        self.years_active = years'''
    
    @property
    def genre(self):
        self.__genre.sort()
        return self.__genre

    def add_genre(self, genre: str|list):
        if isinstance(genre, str):
            self.__genre.append(genre)
        elif isinstance(genre, list):
            self.__genre.extend(genre)

    def add_song(self, song: Song):
        # Confusing Code
        '''if song.album != '' and song.album not in self.catalog:
            self.catalog[song.album]= [song]
        elif song.album != '':
            self.catalog[song.album].append(song)
        elif song.album == '' and 'Single' not in self.catalog:
            self.catalog['Single'] = [song]
        elif song.album == '' and 'Single' in self.catalog:
            self.catalog['Single'].append(song)'''

        # Moderately better code
        if song.album != '':
            if song.album not in self.catalog:
                self.catalog[song.album] = []
            self.catalog[song.album] = song
        else:
            if 'Single' not in self.catalog:
                self.catalog['Single'] = []
            self.catalog['Single'] = song

    def __str__(self):
        st = f'Artsit: {self.name}\n'
        st += f'Year Started: {self.start_year}\n'
        st += f'Years Active: {self.years_active}\n'
        st += f'Genre: '
        for i in self.genre:
            st += f'{i}, '
        return st[:-2] 

class Song:

    def __init__(self, title, length, year_released, album=''):
        self.title = title
        self.length = length
        self.year_released = year_released
        self.album = album

if __name__ == "__main__":
    icenine = Artist('Ice Nine Kills', 6, 2000, ['Ska Punk'])
    icenine.add_genre('Metalcore')
    icenine.add_genre(['Post-Hardcore', 'Heavy Metal', 'Symphonic Metal'])
    print(icenine.genre)
    print(icenine.years_active)
    print(icenine)

    anarchist = Song("Baby I'm an anarchist",'2:40', 2002, 'Reinventing Axl Rose')
    againstme = Artist('Against Me!', 4, 1997, ['Folk Punk', 'Punk', 'Alternative Rock'])
    againstme.add_song(anarchist)
    for i in againstme.catalog:
        print(i, againstme.catalog[i].title)