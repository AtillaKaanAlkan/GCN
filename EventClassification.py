from gcn_utils import *


"""
Ce script permet de classifier les circulaires par type d'evenement (e.g. GRB, SGR, GW etc.) en utilisant des expressions regulieres sur metadonnees accompagnant le texte.
"""




with open("/home/alkan/Documents/NLP/GCN/GCN/gcn_corpus_28112022(copie).jsonl", 'r') as f:
    gcn_json = [json.loads(l) for l in list(f)]


def is_GRB(title):

    if (re.search("GRB\s\d+",title) or re.search("GRB\d+",title) or re.search("GRB",title)):
        return True
    else:
        return False

def is_GW(title):

    if (re.search("GW\d+",title) or re.search("LIGO/Virgo",title) or re.search("LIGO/VIRGO",title) or re.search("LIGO-Virgo",title) or re.search("GW\s\d+",title) or re.search("GW",title) or re.search("Ligo",title) or re.search("Virgo",title)):
        return True
    else:
        return False

def is_SGR(title):

    if (re.search("SGR\s\d+",title) or re.search("SGR\d+",title) or re.search("SGR",title)):
        return True
    else:
        return False

def is_Neutrino(title):

    if (re.search("ANTARES",title) or re.search("IceCube-\d+",title)):
        return True
    else:
        return False

def event_classification(gcn_json):

    for doc in gcn_json:

        if is_GRB(doc['subject']):
            doc['event_type'] = 'GRB'

        elif is_GW(doc['subject']):
            doc['event_type'] = 'GW'
        
        elif is_SGR(doc['subject']):
            doc['event_type'] = 'SGR'
        
        elif is_Neutrino(doc['subject']):
            doc['event_type'] = 'Neutrino'
        
        else:
            doc['event_type'] = 'Other'
    
    return gcn_json



if __name__ == '__main__':

    gcn_json_classified = event_classification(gcn_json)
    dicts_to_jsonl(gcn_json_classified, 'gcn_corpus_28112022_classified', False)

    nb_grb = 0
    nb_gw = 0
    nb_sgr = 0
    nb_neutrino = 0
    nb_other = 0
    
    for doc in gcn_json_classified:

        if doc['event_type'] == 'GRB':
            nb_grb += 1
        
        elif doc['event_type'] == 'GW':
            nb_gw += 1
        
        elif doc['event_type'] == 'SGR':
            nb_sgr += 1
        
        elif doc['event_type'] == 'Neutrino':
            nb_neutrino += 1
        
        else:
            nb_other += 1

    print(f'Nombre de circulaires total : {len(gcn_json_classified)}')
    print(f'Nombre de GRB : {nb_grb}')
    print(f'Nombre de GW : {nb_gw}')
    print(f'Nombre de SGR : {nb_sgr}')
    print(f'Nombre de Neutrino : {nb_neutrino}')
    print(f'Autres : {nb_other}')
    


