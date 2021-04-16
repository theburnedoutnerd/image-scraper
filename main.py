import csv
import wget

filename = 'Hosted Catalog.csv'

with open(filename, mode='r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        if row['Picture'].find('|') != -1:
            photo_links = row['Picture'].split('|')
            url = photo_links[0].strip()
            wget.download(url, '/home/ubuntu/image-download/images/' + row['post_name'] + '.png')
        else:
            url = row['Picture']
            wget.download(url, '/home/ubuntu/image-download/images/' + row['post_name'] + '.png')

