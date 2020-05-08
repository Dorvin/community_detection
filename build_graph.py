import networkx as nx
import csv

def build_unweighted_G(edge_file, delimiter):
    G = nx.Graph()
    reader = csv.reader(open(edge_file), delimiter=delimiter)
    for line in reader:
        G.add_edge(int(line[0]),int(line[1]))
    return G

def build_weighted_G(edge_file, delimiter):
    G = nx.Graph()
    reader = csv.reader(open(edge_file), delimiter=delimiter)
    for line in reader:
        G.add_edge(int(line[0]),int(line[1]),weight=float(line[2]))
    return G

def karate():
    G = nx.karate_club_graph()
    print("karate_club_graph => |V| =", G.number_of_nodes())
    return G

def les_miserables():
    G = nx.les_miserables_graph()
    print("les_miserables_graph => |V| =", G.number_of_nodes())
    return G

def football():
    try:  # Python 3.x
        import urllib.request as urllib
    except ImportError:  # Python 2.x
        import urllib
    import io
    import zipfile

    url = "http://www-personal.umich.edu/~mejn/netdata/football.zip"

    sock = urllib.urlopen(url)  # open URL
    s = io.BytesIO(sock.read())  # read into BytesIO "file"
    sock.close()

    zf = zipfile.ZipFile(s)  # zipfile object
    txt = zf.read('football.txt').decode()  # read info file
    gml = zf.read('football.gml').decode()  # read gml data
    # throw away bogus first line with # from mejn files
    gml = gml.split('\n')[1:]
    G = nx.parse_gml(gml)  # parse gml data
    print("football_graph => |V| =", G.number_of_nodes())
    return G

def barn_swallow():
    G = build_unweighted_G('dataset/aves-barn-swallow-contact-network.txt', ' ')
    print("barn_swallow_graph => |V| =", G.number_of_nodes())
    return G

def email_univ():
    G = build_unweighted_G('dataset/ia-email-univ.txt', ' ')
    print("email_univ_graph => |V| =", G.number_of_nodes())
    return G

def fb_pages():
    G = build_unweighted_G('dataset/fb-pages-artist.txt', ',')
    print("fb_pages_graph => |V| =", G.number_of_nodes())
    return G