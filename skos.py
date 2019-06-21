# -*- coding: utf-8 -*-
# @Author: luc
# @Date:   2019-06-21T10:57:44+02:00
# @Email:  artefacts.lle@gmail.com
# @Last modified by:   luc
# @Last modified time: 2019-06-21T11:12:39+02:00
# @Copyright: Coopérative Artéfacts / Luc LEGER

import rdflib


class Skos():

    def __init__(self):
        self.g = rdflib.Graph()

    def open(self, file_name):
        self.g.parse(file_name, format="xml")

    def read_chapter(self):
        request = """
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX isothes: <http://purl.org/iso25964/skos-thes#>
            SELECT ?prefLabel ?chapitre
            WHERE {
            ?concept a skos:Collection .
            ?concept isothes:microThesaurusOf ?thesaurus .
            ?concept skos:notation ?chapitre .
            ?concept skos:prefLabel ?prefLabel .
            FILTER(langMatches(lang(?prefLabel), 'fr'))
            } ORDER BY ?chapitre
        """
        result = self.g.query(request)
        return result
