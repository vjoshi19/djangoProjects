from django.db import models

  # * Performer model should:
  # * have a name
  # * return the name when turned into a string
class Performer(models.Model):
    name = models.CharFeild(max_length=255)

   def __str__(self):
    return self.name

  # * Song model should:
  # * have a title
  # * have an artist (original performer)
  # * have a performer (who's singing it for karaoke) (make this another model)
  # * have a length (number of seconds in duration)
  # * return '<title> by <artist>' when turned into a string
class Song(models.Model):
    title = models.CharFeild(max_length=255)
    artist = models.CharFeild(max_length=255)
    length = models.IntegerFeild()
    performer = models.ForeignKey(Performer)

class Meta:
    ordering = ['order',]

def __str__(self):
    return (self.title + " by " + self.artist)
