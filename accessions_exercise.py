#this is the Accesion names exercise in PFB

import re


#make a list of the given names
gene_accession_names = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]



#prints the names that contain the number 5
print('The names that contain 5 are: ')
for names in gene_accession_names:
    if re.search(r"5", names):
        print(names)



#prints the names that contain the letters d or e
print('The names that contain d or e are: ')
for names in gene_accession_names:
    if re.search(r"(d|e)", names):
        print(names)


#prints the names that contain the letters d and e in order
print('The names that contain d and e in order are: ')
for names in gene_accession_names:
    if re.search(r"de", names):
        print(names)

#prints the names that contain the letters d and e with a single latter between them
print('The names that contain d and e with a single latter between them are: ')
for names in gene_accession_names:
    if re.search(r"d.e", names):
        print(names)


#prints the names that contain the letters d and e in any order
print('The names that contain d and e in any order are: ')
for names in gene_accession_names:
    if re.search(r"de", names) or re.search(r'ed', names):
        print(names)


#prints the names that start with x or y
print('The names that start with x or y are: ')
for names in gene_accession_names:
    if re.search(r"^x", names) or re.search(r'^y', names):
        print(names)



#prints the names that start with x or y and ends with e
print('The names that start with x or y and ends with an e are: ')
for names in gene_accession_names:
    if re.search(r"^(x).*(e$)", names) or re.search(r"^(y).*(e$)", names):
        print(names)

#prints the names that contain 3 or more numbers in a row
print('The names that contain 3 or more numbers in a row are: ')
for names in gene_accession_names:
    if re.search(r"\d{3,}", names):
        print(names)

#prints the names that end with d followed by a, r, or p
print('The names that contain 3 or more numbers in a row are: ')
for names in gene_accession_names:
    if re.search(r"(d)[arp]$", names):
        print(names)



