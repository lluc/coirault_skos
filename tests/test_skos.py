# -*- coding: utf-8 -*-
from ..skos import Skos

sk = Skos()
sk.open("15_skos.xml")


def test_read_chapter():
    # Read the RDF file and discover every chapter
    res = sk.read_chapter()
    # Number of chapters
    assert len(res) == 15
    # First chapter
    assert res[0]["name"] == "La Poésie"
    assert res[0]["number"] == "I"
    assert res[0]["uri"] == "http://sha.univ-poitiers.fr/musicologie/vocabulaires/coirault/collection_I"  # noqa


def test_read_topic():
    # Read the RDF file and discover every topic in a chapter
    chapter = "http://sha.univ-poitiers.fr/musicologie/vocabulaires/coirault/collection_I"  # noqa
    res = sk.read_topic(chapter)
    assert len(res) == 3
    # Fisrt topic
    assert res[0]["name"] == "BADINES, LÉGÈRES"
    assert res[0]["uri"] == "http://sha.univ-poitiers.fr/musicologie/vocabulaires/coirault/collection_3"  # noqa
    assert res[0]["number"] == "I.3"


def test_read_song():
    # Read the RDF file and discover every songs in a topic
    topic = "http://sha.univ-poitiers.fr/musicologie/vocabulaires/coirault/collection_1"  # noqa
    res = sk.read_song(topic)
    assert len(res) == 22
    # First song
    assert res[0]["name"] == "Ah ! si l'amour prenait racine"
    assert res[0]["uri"] == "http://sha.univ-poitiers.fr/musicologie/vocabulaires/coirault/concept_119"  # noqa
    assert res[0]["number"] == "119"
