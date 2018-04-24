import json

from zdict.dictionaries.oxford import OxfordDictionary
from zdict.models import Record


class OxfordThesaurus(OxfordDictionary):

    API = 'https://od-api.oxforddictionaries.com/api/v1/entries/' \
          'en/{word}/synonyms;antonyms'

    @property
    def provider(self):
        return 'thesaurus'

    @property
    def title(self):
        return 'Oxford Thesaurus'

    def show(self, record: Record):
        content = json.loads(record.content)

        # results
        for headword in content['results']:
            # word
            self.color.print(headword['word'], 'yellow')

            for lex_ent in headword['lexicalEntries']:
                # lexical category
                print()
                self.color.print(lex_ent['lexicalCategory'], 'lred')

                # entry
                idx = 1
                for entry in lex_ent['entries']:
                    for sense in entry['senses']:
                        line_prefix = '{idx}.'.format(idx=idx)
                        self._show_sense(sense, line_prefix)
                        idx += 1

        print()

    def _show_sense(self, sense: dict, prefix='', indent=1):
        print()
        self.color.print(prefix, end=' ', indent=indent)

        # regions
        if 'regions' in sense:
            regions_str = ', '.join(sense['regions'])
            regions_str = '(' + regions_str + ')'
            self.color.print(regions_str, 'yellow', end=' ')

        # register
        if 'registers' in sense:
            registers_str = ', '.join(sense['registers'])
            self.color.print(registers_str, 'red', end=' ')

        # domain
        if 'domains' in sense:
            domains_str = ', '.join(sense['domains'])
            domains_str = '(' + domains_str + ') '
            self.color.print(domains_str, 'green', end='')

        # example
        if 'examples' in sense:
            examples = ['`%s`' % ex['text'] for ex in sense['examples']]
            examples_str = ', '.join(examples)
            print(examples_str)
        else:
            print('(no example)')

        # synonyms
        if 'synonyms' in sense:
            print()
            self.color.print('Synonyms', 'lindigo', indent=indent+3)

            synonyms = (it['text'] for it in sense['synonyms'])
            synonyms_str = ', '.join(synonyms)
            self.color.print(synonyms_str, indent=indent+3)

        # antonyms
        if 'antonyms' in sense:
            print()
            self.color.print('Antonyms', 'lmagenta', indent=indent+3)

            antonyms = (it['text'] for it in sense['antonyms'])
            antonyms_str = ', '.join(antonyms)
            self.color.print(antonyms_str, indent=indent+3)

        # subsenses
        if self.args.verbose and 'subsenses' in sense:
            for idx, subsense in enumerate(sense['subsenses'], 1):
                line_prefix = '{prefix}{idx}.'.format(prefix=prefix, idx=idx)
                self._show_sense(subsense, line_prefix, indent=indent + 1)
