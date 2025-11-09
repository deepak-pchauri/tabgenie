from tabgenie.loaders.cacapo import CACAPO
from tabgenie.loaders.charttotext_s import ChartToTextS
from tabgenie.loaders.dart import DART
from tabgenie.loaders.e2e import E2E
from tabgenie.loaders.eventnarrative import EventNarrative
from tabgenie.loaders.hitab import HiTab
from tabgenie.loaders.logic2text import Logic2Text
from tabgenie.loaders.logicnlg import LogicNLG
from tabgenie.loaders.multiwoz22 import MultiWOZ22
from tabgenie.loaders.numericnlg import NumericNLG
from tabgenie.loaders.scigen import SciGen
from tabgenie.loaders.sportsett import SportSettBasketball
from tabgenie.loaders.totto import ToTTo
from tabgenie.loaders.webnlg import WebNLG
from tabgenie.loaders.wikibio import WikiBio
from tabgenie.loaders.wikisql import WikiSQL
from tabgenie.loaders.wikitabletext import WikiTableText


DATASET_CLASSES = {
    "cacapo": CACAPO,
    "charttotext-s": ChartToTextS,
    "dart": DART,
    "e2e": E2E,
    "eventnarrative": EventNarrative,
    "hitab": HiTab,
    "multiwoz22": MultiWOZ22,
    "logic2text": Logic2Text,
    "logicnlg": LogicNLG,
    "numericnlg": NumericNLG,
    "scigen": SciGen,
    "sportsett": SportSettBasketball,
    "totto": ToTTo,
    "webnlg": WebNLG,
    "wikibio": WikiBio,
    "wikisql": WikiSQL,
    "wikitabletext": WikiTableText,
}
