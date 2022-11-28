from gcn_utils import *

# Location of the folder containing all gcn circulars ;
path_to_tarfile = '/home/alkan/Téléchargements/all_gcn_circulars/gcn3/'

# Create a list with the paths to all gcn circulars ;
all_circulars = glob.glob(path_to_tarfile + '*.gcn3')

# If you want to save the output (into a json file) regarding the extracted information for further statistics change the boolean to True.
# if you only use the script to get the plot let the boolean to False ;
SAVE_OUTPUT = False 


list_of_dict = []

for file in all_circulars:
    dictionary = {}

    with open(file, 'r', encoding = 'ISO-8859-1') as f:
        
        fulltext = f.read()
        fr = fulltext.split('\n')

        if len(fr) != 0:
        
            if 'TITLE: ' in fr[0]: 

                number, subject, date, year, author = extract_metada_from_circular(fr)
                dictionary['number'], dictionary['subject'], dictionary['date'], dictionary['year'], dictionary['author'], dictionary['fulltext'] = number, subject, date, year, author, fulltext
                list_of_dict.append(dictionary)
            
            else:
                pass


if SAVE_OUTPUT:
    dicts_to_jsonl(list_of_dict, 'gcn_corpus', False)
    print('saved as a json file.')




# count the number of published gcn circulars per year
result = {}
for k in list_of_dict:
    if 'year' in k:
        result[k['year']] = result.get(k['year'], 0) + 1

sorted_result = dict(sorted(result.items()))
print(sorted_result)

# Plot the evolution of GCN circulars vs. year
plt.figure(figsize = (16, 8))
bars = plt.bar(range(len(sorted_result)), list(sorted_result.values()), tick_label = list(sorted_result.keys()))

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + .005, yval)

plt.ylabel('# GCN Circulars')
plt.xlabel('Year')
plt.grid(True)
plt.show() 
plt.close()
