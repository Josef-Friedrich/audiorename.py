"""Test all metatag fields, the fields from MediaFile too."""

import unittest
import helper
import datetime
import phrydy

# from audiorename import args
# from phrydy import doc as pdoc
#
# print(args.all_fields)
#
# for field in sorted(args.all_fields):
#     print(field)

# acoustid_fingerprint
# acoustid_id
# album
# ar_classical_album
# ar_combined_album
# ar_initial_album
# albumartist
# albumartist_credit
# albumartist_sort
# albumdisambig
# albumstatus
# albumtype
# arranger
# art
# artist
# artist_credit
# ar_initial_artist
# artist_sort
# ar_combined_artist
# ar_combined_artist_sort
# asin
# bitdepth
# bitrate
# bpm
# catalognum
# channels
# comments
# comp
# composer
# ar_initial_composer
# ar_combined_composer
# composer_sort
# country
# date
# day
# disc
# disctitle
# disctotal
# ar_combined_disctrack
# encoder
# format
# genre
# genres
# grouping
# images
# initial_key
# label
# language
# length
# lyricist
# lyrics
# mb_albumartistid
# mb_albumid
# mb_artistid
# mb_releasegroupid
# mb_trackid
# mb_workid
# media
# month
# original_date
# original_day
# original_month
# original_year
# ar_classical_performer
# r128_album_gain
# r128_track_gain
# rg_album_gain
# rg_album_peak
# rg_track_gain
# rg_track_peak
# samplerate
# script
# title
# ar_classical_title
# track
# ar_classical_track
# tracktotal
# work
# year
# ar_combined_year


class TestAllFields(unittest.TestCase):

    # Pop-Rock
    def test_Yesterday(self):
        meta = helper.get_meta('show-case', 'Beatles_Yesterday.mp3')

        self.assertEqual(meta.acoustid_fingerprint, None)
        self.assertEqual(meta.acoustid_id, None)
        self.assertEqual(meta.album, u'Help!')
        self.assertEqual(meta.ar_classical_album, u'')
        self.assertEqual(meta.ar_combined_album, u'Help!')
        self.assertEqual(meta.ar_initial_album, u'h')
        self.assertEqual(meta.albumartist, u'The Beatles')
        self.assertEqual(meta.albumartist_credit, None)
        self.assertEqual(meta.albumartist_sort, u'Beatles, The')
        self.assertEqual(meta.albumdisambig, None)
        self.assertEqual(meta.albumstatus, u'official')
        self.assertEqual(meta.albumtype, u'album/soundtrack')
        self.assertEqual(meta.arranger, None)
        # self.assertEqual(meta.art, u'')
        self.assertEqual(meta.artist, u'The Beatles')
        self.assertEqual(meta.artist_credit, None)
        self.assertEqual(meta.ar_initial_artist, u'b')
        self.assertEqual(meta.artist_sort, u'Beatles, The')
        self.assertEqual(meta.ar_combined_artist, u'The Beatles')
        self.assertEqual(meta.ar_combined_artist_sort, u'Beatles, The')
        self.assertEqual(meta.asin, u'B000002UAL')
        self.assertEqual(meta.bitdepth, 0)
        self.assertEqual(meta.bitrate, 8000)
        self.assertEqual(meta.bpm, None)
        self.assertEqual(meta.catalognum, u'CDP 7 46439 2')
        self.assertEqual(meta.channels, 1)
        self.assertEqual(meta.comments, None)
        self.assertEqual(meta.comp, None)
        self.assertEqual(meta.composer, None)
        # should b
        self.assertEqual(meta.ar_initial_composer, u't')
        self.assertEqual(meta.ar_combined_composer, u'The Beatles')
        self.assertEqual(meta.composer_sort, None)
        self.assertEqual(meta.country, u'GB')
        self.assertEqual(meta.date, datetime.date(1987, 4, 30))
        self.assertEqual(meta.day, 30)
        self.assertEqual(meta.disc, 1)
        self.assertEqual(meta.disctitle, None)
        self.assertEqual(meta.disctotal, 1)
        # int
        self.assertEqual(meta.ar_combined_disctrack, '13')
        self.assertEqual(meta.encoder, None)
        self.assertEqual(meta.format, u'MP3')
        self.assertEqual(meta.genre, None)
        self.assertEqual(meta.genres, [])
        self.assertEqual(meta.grouping, None)
        self.assertTrue(isinstance(meta.images[0], phrydy.mediafile.Image))
        self.assertEqual(meta.initial_key, None)
        self.assertEqual(meta.label, u'Parlophone')
        self.assertEqual(meta.language, None)
        self.assertEqual(meta.length, 0.296)
        self.assertEqual(meta.lyricist, None)
        self.assertEqual(meta.lyrics, None)
        self.assertEqual(meta.mb_albumartistid,
                         u'b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d')
        self.assertEqual(meta.mb_albumid,
                         u'95e9dc60-a6d9-315f-be99-bd5b69a6582f')
        self.assertEqual(meta.mb_artistid,
                         u'b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d')
        self.assertEqual(meta.mb_releasegroupid,
                         u'0d44e1cb-c6e0-3453-8b68-4d2082f05421')
        self.assertEqual(meta.mb_trackid,
                         u'c05194a3-f6f0-4f52-b78a-13fb5580bc0f')
        self.assertEqual(meta.mb_workid, None)
        self.assertEqual(meta.media, u'CD')
        self.assertEqual(meta.month, 4)
        self.assertEqual(meta.original_date, datetime.date(1965, 1, 1))
        self.assertEqual(meta.original_day, None)
        self.assertEqual(meta.original_month, None)
        self.assertEqual(meta.original_year, 1965)
        self.assertEqual(meta.ar_classical_performer, u'The Beatles')
        self.assertEqual(meta.r128_album_gain, None)
        self.assertEqual(meta.r128_track_gain, None)
        self.assertEqual(meta.rg_album_gain, None)
        self.assertEqual(meta.rg_album_peak, None)
        self.assertEqual(meta.rg_track_gain, None)
        self.assertEqual(meta.rg_track_peak, None)
        self.assertEqual(meta.samplerate, 24000)
        self.assertEqual(meta.ar_combined_soundtrack, True)
        self.assertEqual(meta.script, u'Latn')
        self.assertEqual(meta.title, u'Yesterday')
        self.assertEqual(meta.ar_classical_title, u'Yesterday')
        self.assertEqual(meta.track, 13)
        #  int
        self.assertEqual(meta.ar_classical_track, '13')
        self.assertEqual(meta.tracktotal, 14)
        self.assertEqual(meta.work, None)
        self.assertEqual(meta.year, 1987)
        # int
        self.assertEqual(meta.ar_combined_year, 1965)

    # Classical
    def test_Nachtmusik(self):
        meta = helper.get_meta('show-case', 'Mozart_Nachtmusik.mp3')

        self.assertEqual(meta.acoustid_fingerprint, None)
        self.assertEqual(meta.acoustid_id, None)
        self.assertEqual(meta.album, u'Divertimenti')
        self.assertEqual(meta.ar_classical_album, u'')
        self.assertEqual(meta.ar_combined_album, u'Divertimenti')
        self.assertEqual(meta.ar_initial_album, u'd')
        self.assertEqual(meta.albumartist,
                         u'Wolfgang Amadeus Mozart; Berliner '
                         'Philharmoniker, Herbert von Karajan')
        self.assertEqual(meta.albumartist_credit, None)
        self.assertEqual(meta.albumartist_sort, u'Mozart, Wolfgang Amadeus; '
                         'Berliner Philharmoniker, Karajan, Herbert von')
        self.assertEqual(meta.albumdisambig, None)
        self.assertEqual(meta.albumstatus, u'official')
        self.assertEqual(meta.albumtype, u'album')
        self.assertEqual(meta.arranger, None)
        # self.assertEqual(meta.art, u'')
        self.assertEqual(meta.artist, u'Wolfgang Amadeus Mozart')
        self.assertEqual(meta.artist_credit, None)
        self.assertEqual(meta.ar_initial_artist, u'm')
        self.assertEqual(meta.artist_sort, u'Mozart, Wolfgang Amadeus')
        self.assertEqual(meta.ar_combined_artist,
                         u'Wolfgang Amadeus Mozart; Berliner '
                         'Philharmoniker, Herbert von Karajan')
        self.assertEqual(meta.ar_combined_artist_sort,
                         u'Mozart, Wolfgang Amadeus; '
                         'Berliner Philharmoniker, Karajan, Herbert von')
        self.assertEqual(meta.asin, u'B0007DHPQ2')
        self.assertEqual(meta.bitdepth, 0)
        self.assertEqual(meta.bitrate, 8000)
        self.assertEqual(meta.bpm, None)
        self.assertEqual(meta.catalognum, u'477 5436')
        self.assertEqual(meta.channels, 1)
        self.assertEqual(meta.comments, None)
        self.assertEqual(meta.comp, None)
        self.assertEqual(meta.composer, None)
        self.assertEqual(meta.ar_initial_composer, u'w')
        self.assertEqual(meta.ar_combined_composer,
                         u'Wolfgang Amadeus Mozart; Berliner '
                         'Philharmoniker, Herbert von Karajan')
        self.assertEqual(meta.composer_sort, None)
        self.assertEqual(meta.country, u'DE')
        self.assertEqual(meta.date, datetime.date(2005, 3, 10))
        self.assertEqual(meta.day, 10)
        self.assertEqual(meta.disc, 1)
        self.assertEqual(meta.disctitle, None)
        self.assertEqual(meta.disctotal, 2)
        self.assertEqual(meta.ar_combined_disctrack, u'1-01')
        self.assertEqual(meta.encoder, None)
        self.assertEqual(meta.format, u'MP3')
        self.assertEqual(meta.genre, None)
        self.assertEqual(meta.genres, [])
        self.assertEqual(meta.grouping, None)
        self.assertTrue(isinstance(meta.images[0], phrydy.mediafile.Image))
        self.assertEqual(meta.initial_key, None)
        self.assertEqual(meta.label, u'Deutsche Grammophon')
        self.assertEqual(meta.language, None)
        self.assertEqual(meta.length, 0.296)
        self.assertEqual(meta.lyricist, None)
        self.assertEqual(meta.lyrics, None)
        self.assertEqual(meta.mb_albumartistid,
                         u'b972f589-fb0e-474e-b64a-803b0364fa75/'
                         'dea28aa9-1086-4ffa-8739-0ccc759de1ce/'
                         'd2ced2f1-6b58-47cf-ae87-5943e2ab6d99')
        self.assertEqual(meta.mb_albumid,
                         u'73678131-46a7-442b-8cce-27a8b3bf99c7')
        self.assertEqual(meta.mb_artistid,
                         u'b972f589-fb0e-474e-b64a-803b0364fa75')
        self.assertEqual(meta.mb_releasegroupid,
                         u'17267766-771b-45fe-969f-14b9c4b15e4a')
        self.assertEqual(meta.mb_trackid,
                         u'0db2cdc3-8272-44ef-9810-c75c3939ece8')
        self.assertEqual(meta.mb_workid, None)
        self.assertEqual(meta.media, u'CD')
        self.assertEqual(meta.month, 3)
        self.assertEqual(meta.original_date, datetime.date(2005, 1, 1))
        self.assertEqual(meta.original_day, None)
        self.assertEqual(meta.original_month, None)
        self.assertEqual(meta.original_year, 2005)
        self.assertEqual(meta.ar_classical_performer,
                         u'Berliner Philharmoniker, Herbert von Karajan')
        self.assertEqual(meta.r128_album_gain, None)
        self.assertEqual(meta.r128_track_gain, None)
        self.assertEqual(meta.rg_album_gain, None)
        self.assertEqual(meta.rg_album_peak, None)
        self.assertEqual(meta.rg_track_gain, None)
        self.assertEqual(meta.rg_track_peak, None)
        self.assertEqual(meta.samplerate, 24000)
        self.assertEqual(meta.script, u'Latn')
        self.assertEqual(meta.ar_combined_soundtrack, False)
        self.assertEqual(meta.title,
                         u'Serenade no. 13 for Strings in G major, K. 525 '
                         '"Eine kleine Nachtmusik": I. Allegro')
        self.assertEqual(meta.ar_classical_title, u'I. Allegro')
        self.assertEqual(meta.track, 1)
        self.assertEqual(meta.ar_classical_track, u'01')
        self.assertEqual(meta.tracktotal, 16)
        self.assertEqual(meta.work, None)
        self.assertEqual(meta.year, 2005)
        self.assertEqual(meta.ar_combined_year, 2005)

    # Jazz
    def test_Wonderful(self):
        meta = helper.get_meta('show-case', 'Armstrong_Wonderful-World.mp3')
        self.assertEqual(meta.acoustid_fingerprint, None)
        self.assertEqual(meta.acoustid_id, None)
        self.assertEqual(meta.album, u'Greatest Hits')
        self.assertEqual(meta.ar_classical_album, u'')
        self.assertEqual(meta.ar_combined_album, u'Greatest Hits')
        self.assertEqual(meta.ar_initial_album, u'g')
        self.assertEqual(meta.albumartist, u'Louis Armstrong')
        self.assertEqual(meta.albumartist_credit, None)
        self.assertEqual(meta.albumartist_sort, u'Armstrong, Louis')
        self.assertEqual(meta.albumdisambig, None)
        self.assertEqual(meta.albumstatus, u'official')
        self.assertEqual(meta.albumtype, u'album/compilation')
        self.assertEqual(meta.arranger, None)
        # self.assertEqual(meta.art, u'')
        self.assertEqual(meta.artist, u'Louis Armstrong')
        self.assertEqual(meta.artist_credit, None)
        self.assertEqual(meta.ar_initial_artist, u'a')
        self.assertEqual(meta.artist_sort, u'Armstrong, Louis')
        self.assertEqual(meta.ar_combined_artist, u'Louis Armstrong')
        self.assertEqual(meta.ar_combined_artist_sort, u'Armstrong, Louis')
        self.assertEqual(meta.asin, u'B000003G2C')
        self.assertEqual(meta.bitdepth, 0)
        self.assertEqual(meta.bitrate, 8000)
        self.assertEqual(meta.bpm, None)
        self.assertEqual(meta.catalognum, u'09026-68486-2')
        self.assertEqual(meta.channels, 1)
        self.assertEqual(meta.comments, None)
        self.assertEqual(meta.comp, None)
        self.assertEqual(meta.composer, None)
        self.assertEqual(meta.ar_initial_composer, u'l')
        self.assertEqual(meta.ar_combined_composer, u'Louis Armstrong')
        self.assertEqual(meta.composer_sort, None)
        self.assertEqual(meta.country, u'US')
        self.assertEqual(meta.date, datetime.date(1996, 1, 1))
        self.assertEqual(meta.day, None)
        self.assertEqual(meta.disc, 1)
        self.assertEqual(meta.disctitle, None)
        self.assertEqual(meta.disctotal, 1)
        self.assertEqual(meta.ar_combined_disctrack, u'13')
        self.assertEqual(meta.encoder, None)
        self.assertEqual(meta.format, u'MP3')
        self.assertEqual(meta.genre, None)
        self.assertEqual(meta.genres, [])
        self.assertEqual(meta.grouping, None)
        self.assertTrue(isinstance(meta.images[0], phrydy.mediafile.Image))
        self.assertEqual(meta.initial_key, None)
        # self.assertEqual(meta.label, u'')
        # self.assertEqual(meta.language, u'')
        # self.assertEqual(meta.length, u'')
        self.assertEqual(meta.lyricist, None)
        self.assertEqual(meta.lyrics, None)
        # self.assertEqual(meta.mb_albumartistid, u'')
        # self.assertEqual(meta.mb_albumid, u'')
        # self.assertEqual(meta.mb_artistid, u'')
        # self.assertEqual(meta.mb_releasegroupid, u'')
        # self.assertEqual(meta.mb_trackid, u'')
        # self.assertEqual(meta.mb_workid, u'')
        # self.assertEqual(meta.media, u'')
        self.assertEqual(meta.month, None)
        self.assertEqual(meta.original_date, datetime.date(1996, 1, 1))
        self.assertEqual(meta.original_day, None)
        self.assertEqual(meta.original_month, None)
        self.assertEqual(meta.original_year, 1996)
        self.assertEqual(meta.ar_classical_performer, u'Louis Armstrong')
        self.assertEqual(meta.r128_album_gain, None)
        self.assertEqual(meta.r128_track_gain, None)
        self.assertEqual(meta.rg_album_gain, None)
        self.assertEqual(meta.rg_album_peak, None)
        self.assertEqual(meta.rg_track_gain, None)
        self.assertEqual(meta.rg_track_peak, None)
        self.assertEqual(meta.samplerate, 24000)
        self.assertEqual(meta.script, u'Latn')
        self.assertEqual(meta.ar_combined_soundtrack, False)
        self.assertEqual(meta.title, u'What a Wonderful World')
        self.assertEqual(meta.ar_classical_title, u'What a Wonderful World')
        self.assertEqual(meta.track, 13)
        self.assertEqual(meta.ar_classical_track, '13')
        self.assertEqual(meta.tracktotal, 13)
        self.assertEqual(meta.work, None)
        self.assertEqual(meta.year, 1996)
        self.assertEqual(meta.ar_combined_year, 1996)


if __name__ == '__main__':
    unittest.main()
