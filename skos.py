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
            SELECT ?prefLabel ?concept ?chapitre
            WHERE {
            ?concept a skos:Collection .
            ?concept isothes:microThesaurusOf ?thesaurus .
            ?concept skos:notation ?chapitre .
            ?concept skos:prefLabel ?prefLabel .
            FILTER(langMatches(lang(?prefLabel), 'fr'))
            } ORDER BY ?chapitre
        """
        result = self.g.query(request)
        return self.rdf_to_dict(result)

    def read_topic(self, chapter):
        request = """
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX isothes: <http://purl.org/iso25964/skos-thes#>
            SELECT (STR(?frLabel) AS ?francais) ?collection ?rubrique WHERE {
              ?collection isothes:superGroup <%s> .
              ?collection skos:notation ?rubrique .
              ?collection skos:prefLabel ?frLabel.
              FILTER(langMatches(lang(?frLabel), 'fr'))
            }
            ORDER BY ?frLabel
            """ % chapter
        result = self.g.query(request)
        return self.rdf_to_dict(result)

    def read_song(self, topic):
        request = """
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX isothes: <http://purl.org/iso25964/skos-thes#>
            PREFIX opentheso: <http://purl.org/umu/uneskos#>
            SELECT (STR(?frLabel) AS ?francais) ?concept ?chanson WHERE {
              ?concept opentheso:memberOf <%s> .
              ?concept skos:notation ?chanson .
              ?concept skos:prefLabel ?frLabel.
              FILTER(langMatches(lang(?frLabel), 'fr'))
            }
            ORDER BY ?frLabel
            """ % topic
        result = self.g.query(request)
        return self.rdf_to_dict(result)

    def rdf_to_dict(self, data):
        """
        Convert RDF data to a dictionnary list
        """
        result = []
        # Concert RDF's to a list
        records = list(data)

        for record in records:
            # Build a dictionnary with the values
            dict = {}
            dict["name"] = record[0].encode('utf-8')
            dict["uri"] = record[1].encode('utf-8')
            dict["number"] = record[2].encode('utf-8')
            # Append the dictionnary to the result list
            result.append(dict)
        return result
