import build_graph
import comm_detect
import comm_util

#G = build_graph.karate()
#G = build_graph.les_miserables()
#G = build_graph.football()
G = build_graph.barn_swallow()
#G = build_graph.email_univ()
#G = build_graph.fb_pages()
partion_louvain = comm_detect.louvain(G)
partion_girvan_newman = comm_detect.girvan_newman(G)
partion_cnm = comm_detect.cnm(G)
comm_util.print_modularity(G, partion_louvain, 'louvain')
comm_util.print_modularity(G, partion_girvan_newman, 'girvan_newman')
comm_util.print_modularity(G, partion_cnm, 'CNM')
comm_util.draw_louvain(G, partion_louvain, 'louvain')
comm_util.draw_louvain(G, partion_girvan_newman, 'girvan_newman')
comm_util.draw_louvain(G, partion_cnm, 'CNM')