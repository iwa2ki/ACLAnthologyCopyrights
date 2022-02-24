import re
class ACLCopyrights:
    def __init__(self) -> None:
        self.institutes={
            'ACL': 'ACL',
            'NAACL': 'ACL',
            'EACL': 'ACL',
            'COLING': 'ICCL',
            'HLT': 'DARPA',
            'SemEval': 'ACL',
            'CoNLL': 'ACL',
            'EMNLP': 'ACL',
            'LREC': 'ELRA',
            'IJCNLP': 'AFNLP',
            'RANLP': 'RANLP',
            'Workshop': 'ACL'
        }
        self.conferences={
            'A': 'ANLP',
            'C': 'COLING',
            'D': 'EMNLP',
            'E': 'EACL',
            'H': 'HLT',
            'I': 'IJCNLP',
            'J': 'CL',
            'K': 'CoNLL',
            'L': 'LREC',
            'N': 'NAACL',
            'P': 'ACL',
            'Q': 'TACL',
            'R': 'RANLP',
            'S': 'SemEval',
            'W': 'Workshop',
            'acl': 'ACL',
            'conll': 'CoNLL',
            'emnlp': 'EMNLP',
            'naacl': 'NAACL',
            'eacl': 'EACL',
            'lrec': 'LREC'
        }
        self.legacy_id=re.compile(r'^[A-Z]\d\d-\d\d\d\d$')
    def get_licence(self, institute, year):
        if institute=='ACL':
            if year>=2016:
                return 'CC-BY 4.0'
            else:
                return 'CC-BY-NC-SA 3.0'
        elif institute=='ICCL':
            if year in [2014, 2016, 2018, 2020]:
                return 'CC-BY 4.0'
            elif year in [2008, 2012]:
                return 'CC-BY-NC-SA 3.0'
            else:
                return 'Proprietary'
        elif institute=='DARPA':
            return 'Proprietary'
        elif institute=='AFNLP':
            return 'Proprietary'
        elif institute=='RANLP':
            return 'Proprietary'
        elif institute=='ELRA':
            if year>=2014:
                return 'CC-BY-NC 4.0'
            else:
                return 'Proprietary'
        else:
            return 'Proprietary'
    def conf2inst(self, conference):
        if conference not in self.institutes:
            return None
        return self.institutes[conference]
    def prefix2conf(self, prefix):
        if prefix not in self.conferences:
            return None
        return self.conferences[prefix]
    def id2prefix(self, paper_id):
        if self.legacy_id.match(paper_id):
            return paper_id[0]
        else:
            return paper_id.split('.')[1].split('-')[0]
    def id2year(self, paper_id):
        if self.legacy_id.match(paper_id):
            year=int(paper_id[1:3])
            if year<50:
                year+=2000
            else:
                year+=1900
            return year
        else:
            return int(paper_id.split('.')[0])
    def __call__(self, paper_id):
        prefix=self.id2prefix(paper_id)
        year=self.id2year(paper_id)
        conference=self.prefix2conf(prefix)
        institute=self.conf2inst(conference)
        return self.get_licence(institute, year)

