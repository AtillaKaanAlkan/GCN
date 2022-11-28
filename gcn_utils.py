import json
import glob
from operator import itemgetter
import gzip
from dateutil import parser
import matplotlib.pyplot as plt
import collections

def extract_metada_from_circular(circular):

    number = circular[1].split('NUMBER: ')[1].strip()
    subject = circular[2].split('SUBJECT: ')[1].strip()
    date = circular[3].split('DATE: ')[1].strip().split(' ')[0]
    year = parser.parse(date, yearfirst = True).year # extract the year
    author = circular[4].split('FROM: ')[1].strip()

    return number, subject, date, year, author

def dicts_to_jsonl(data_list: list, filename: str, compress: bool = True) -> None:
    """
    Method saves list of dicts into jsonl file.

    :param data: (list) list of dicts to be stored,
    :param filename: (str) path to the output file. If suffix .jsonl is not given then methods appends
        .jsonl suffix into the file.
    :param compress: (bool) should file be compressed into a gzip archive?
    """

    sjsonl = '.jsonl'
    sgz = '.gz'

    # Check filename

    if not filename.endswith(sjsonl):
        filename = filename + sjsonl

    # Save data
    
    if compress:
        filename = filename + sgz
        with gzip.open(filename, 'w') as compressed:
            for ddict in data_list:
                jout = json.dumps(ddict) + '\n'
                jout = jout.encode('utf-8')
                compressed.write(jout)
    else:
        with open(filename, 'w') as out:
            for ddict in data_list:
                jout = json.dumps(ddict) + '\n'
                out.write(jout)