import attr
from pathlib import Path

from pylexibank import Concept, Language, Lexeme
from pylexibank.dataset import Dataset as BaseDataset
from pylexibank.util import progressbar

from clldutils.misc import slug


@attr.s
class CustomLexeme(Lexeme):
    CU = attr.ib(default=None)


@attr.s
class CustomConcept(Concept):
    Spanish_Gloss = attr.ib(default=None)
    Number = attr.ib(default=None)
    Page_in_Source = attr.ib(default=None)


@attr.s
class CustomLanguage(Language):
    Latitude = attr.ib(default=None)
    Longitude = attr.ib(default=None)
    SubGroup = attr.ib(default=None)
    ID_in_Source = attr.ib(default=None)


class Dataset(BaseDataset):
    dir = Path(__file__).parent
    id = "constenlachibchan"
    language_class = CustomLanguage
    lexeme_class = CustomLexeme
    concept_class = CustomConcept

    def cmd_makecldf(self, args):
        args.writer.add_sources()

        concept_lookup = {}
        for concept in self.conceptlists[0].concepts.values():
            idx = concept.id.split("-")[-1] + "_" + slug(concept.attributes["spanish"])
            args.writer.add_concept(
                    ID=idx,
                    Name=concept.gloss,
                    Spanish_Gloss=concept.attributes["spanish"],
                    Number=concept.number,
                    Page_in_Source=concept.attributes["page_in_source"],
                    Concepticon_ID=concept.concepticon_id,
                    Concepticon_Gloss=concept.concepticon_gloss
                    )
            concept_lookup[concept.attributes["spanish"]] = idx
        languages = args.writer.add_languages(lookup_factory='ID_in_Source')

        for idx, language, concept, value, cogid, cu in progressbar(self.raw_dir.read_csv(
                'constenla2005.csv', delimiter=',')[1:]):
            for lexeme in args.writer.add_forms_from_value(
                    Language_ID=languages[language],
                    Parameter_ID=concept_lookup[concept],
                    Value=value.strip(),
                    Source="Constenla2005",
                    Cognacy=cogid,
                    CU=cu
                    ):

                args.writer.add_cognate(
                        lexeme=lexeme,
                        Cognateset_ID=cogid,
                        Source="Constenla2005"
                        )
