# -*- coding: utf-8 -*-
from skos import Skos

sk = Skos()
sk.open("15_skos.xml")


def test_read_chapter():
    # Read the RDF file and discover every chapter
    res = sk.read_chapter()
    # Number of chapters
    assert len(res) == 15


def test_read_topic():
    # Read the RDF file and discover every topic in a chapter
    chapter = "http://sha.univ-poitiers.fr/musicologie/vocabulaires/coirault/collection_I"  # noqa
    res = sk.read_topic(chapter)
    assert len(res) == 3
