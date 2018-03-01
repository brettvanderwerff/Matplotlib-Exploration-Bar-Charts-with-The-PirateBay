from category_keys import category_keys
from collections import Counter
import csv
import matplotlib.pyplot as plt

def get_torrent_list(file):
    '''Function opens a torrent_dump csv file and creates a list where each element in the list represents a line of
    the torrent dump file csv. The elements of this list are nested lists, each element in the nested lists represents
    columns in the semicolon delimited torrent_dump csv.
    '''
    torrent_list = []
    with open(file, 'r', encoding='utf-8') as read_obj:
        reader = csv.reader(read_obj, delimiter=';')
        for item in reader:
            torrent_list.append(item)
    return torrent_list

def get_categories(torrent_list):
    '''Function takes the returned torrent_list from the get_torrent_list function and isolates only the category code
    elements from the nested tuple and places the category codes in a list. The category code list is then translated
     from a three number category code to the corresponding category name by using the imported category key
     dictionary the category list is then returned.
    '''
    categories_num_list = []
    categories_list = []
    for item in torrent_list:
        categories_num_list.append(item[-1].strip('\n'))
    for item in categories_num_list:
        categories_list.append(category_keys[item])
    return categories_list

def count_categories(categories_list):
    '''Function takes the category_list returned by the get_categories function and counts the occurrences of each
    category by using the Counter subclass of the collections module. A dictionary of category counts is returned.
    '''
    categories_count = Counter(categories_list)
    return dict(categories_count)

def get_x_y(dictionary, top_n):
    '''Function takes the returned categories_count dictionary from the count_categories function and splits the keys
     and values of that dictionary into two separate lists, one for keys(x) and one for values(y). This conversion is
     necessary for downstream plotting. The function also takes top_n as an argument, which indicates how many of
     the top categories the user wants for downstream graphing (i.e. top_n = 5 will get the five most common categories
      from the categories_count dictionary).
      '''
    x = sorted(dictionary, key=lambda x: dictionary.get(x), reverse=True)[:top_n]
    y = []
    for key in x:
        y.append(dictionary[key])
    return x, y

def bar_chart(x, y, title, xlabel, ylabel):
    '''Function makes a bar chart of the x and y arguments, which are returned by the get_x_y function. Title, xlabel,
    and ylabel are taken as arguments to properly label the chart.
    '''
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.bar(x=x, height=y)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    torrent_list = get_torrent_list(file='torrent_dump_2016.csv')
    categories_list = get_categories(torrent_list=torrent_list)
    catergories_count = count_categories(categories_list)
    x, y = get_x_y(dictionary=catergories_count, top_n=10)
    bar_chart(x=x, y=y, title='Top 10 Torrent Categories 2016', xlabel='Torrent Category', ylabel='# of Torrents')











