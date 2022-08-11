import math


class TrackLine:
    def __init__(self, to_x, to_y, max_speed=0):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:

    def __init__(self, start_x=0, start_y=0):
        self.start_x=start_x
        self.start_y=start_y
        self.lst_track=[]

    def add_track(self, tr):
        self.lst_track.append(tr)

    def get_tracks(self):
        return self.lst_track

    def __len__(self):
        res_1 = ((self.start_x-self.lst_track[0].to_x)**2+(self.start_y-self.lst_track[0].to_y)**2)**0.5
        return int(res_1+sum(self.__get_length(i) for i in range(1, len(self.lst_track))))

    def __get_length(self, i):
        return ((self.lst_track[i-1].to_x-self.lst_track[i-1].to_x)**2+(self.lst_track[i-1].to_y-self.lst_track[i-1].to_y))*0.5

    def __eq__(self, other):
        return len(self)==len(other)
    def __lt__(self, other):
        return len(self)<len(other)

track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
print(res_eq)