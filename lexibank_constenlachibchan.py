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
        concepts = {}
        for concept in self.concepts:
            idx = concept['NUMBER']+'_'+slug(concept['GLOSS'])
            args.writer.add_concept(
                    ID=idx,
                    Name=concept['GLOSS'],
                    Concepticon_ID=concept['CONCEPTICON_ID'],
                    Concepticon_Gloss=concept['CONCEPTICON_GLOSS'],
                    Page_in_Source=concept['PAGE_IN_SOURCE']
                    )
            concepts[concept['SPANISH']] = idx
        languages = args.writer.add_languages(lookup_factory='ID_in_Source')
        for idx, language, concept, form, cogid, cu in progressbar(self.raw_dir.read_csv(
                'constenla2005.csv', delimiter=',')[1:]):
            for lexeme in args.writer.add_forms_from_value(
                    Language_ID=languages[language],
                    Parameter_ID=concepts[concept],
                    Value=form,
                    Source="constenla2005",
                    Cognacy=cogid,
                    CU=cu
                    ):
                args.writer.add_cognate(
                        lexeme=lexeme,
                        Cognateset_ID=cogid,
                        Source="constenla2005"
                        )
            
