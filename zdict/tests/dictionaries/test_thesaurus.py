from unittest.mock import Mock, patch

from zdict.dictionaries.thesaurus import OxfordThesaurus
from zdict.models import Record
from zdict.zdict import get_args


class TestOxfordThesaurus:
    def setup_method(self, method):
        self.dict = OxfordThesaurus(get_args())

    def teardown_method(self, method):
        del self.dict

    def test_provider(self):
        assert self.dict.provider == 'thesaurus'

    def test__get_url(self):
        uri = 'https://od-api.oxforddictionaries.com/api/v1/entries/' \
              'en/mock/synonyms;antonyms'
        assert self.dict._get_url('mock') == uri

    @patch('zdict.dictionaries.oxford.Record')
    def test_query_normal(self, Record):
        self.dict._get_raw = Mock(return_value=SAMPLE_RESPONSE)
        self.dict._get_app_key = Mock(return_value=('id', 'key'))

        self.dict.query('string')

        Record.assert_called_with(word='string',
                                  content=SAMPLE_RESPONSE,
                                  source='thesaurus')

    def test_show(self):
        r = Record(word='string',
                   content=SAMPLE_RESPONSE,
                   source=self.dict.provider)
        self.dict.show(r)


# the sample response copied from the official website
SAMPLE_RESPONSE = """
{
  "metadata": {},
  "results": [
    {
      "id": "string",
      "language": "string",
      "lexicalEntries": [
        {
          "entries": [
            {
              "homographNumber": "string",
              "senses": [
                {
                  "antonyms": [
                    {
                      "domains": [
                        "string"
                      ],
                      "id": "string",
                      "language": "string",
                      "regions": [
                        "string"
                      ],
                      "registers": [
                        "string"
                      ],
                      "text": "string"
                    }
                  ],
                  "domains": [
                    "string"
                  ],
                  "examples": [
                    {
                      "definitions": [
                        "string"
                      ],
                      "domains": [
                        "string"
                      ],
                      "notes": [
                        {
                          "id": "string",
                          "text": "string",
                          "type": "string"
                        }
                      ],
                      "regions": [
                        "string"
                      ],
                      "registers": [
                        "string"
                      ],
                      "senseIds": [
                        "string"
                      ],
                      "text": "string",
                      "translations": [
                        {
                          "domains": [
                            "string"
                          ],
                          "grammaticalFeatures": [
                            {
                              "text": "string",
                              "type": "string"
                            }
                          ],
                          "language": "string",
                          "notes": [
                            {
                              "id": "string",
                              "text": "string",
                              "type": "string"
                            }
                          ],
                          "regions": [
                            "string"
                          ],
                          "registers": [
                            "string"
                          ],
                          "text": "string"
                        }
                      ]
                    }
                  ],
                  "id": "string",
                  "regions": [
                    "string"
                  ],
                  "registers": [
                    "string"
                  ],
                  "subsenses": [
                    {}
                  ],
                  "synonyms": [
                    {
                      "domains": [
                        "string"
                      ],
                      "id": "string",
                      "language": "string",
                      "regions": [
                        "string"
                      ],
                      "registers": [
                        "string"
                      ],
                      "text": "string"
                    }
                  ]
                }
              ],
              "variantForms": [
                {
                  "regions": [
                    "string"
                  ],
                  "text": "string"
                }
              ]
            }
          ],
          "language": "string",
          "lexicalCategory": "string",
          "text": "string",
          "variantForms": [
            {
              "regions": [
                "string"
              ],
              "text": "string"
            }
          ]
        }
      ],
      "type": "string",
      "word": "string"
    }
  ]
}"""
