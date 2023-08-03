# start node
#start q_1
#
# edges
q_1 -> q_1: input(thread_1, x, v, a_1)
q_1 -> q_1: copy(a_2, a_1)
q_1 -> q_2: input(thread_2, y, v, a_2)
q_2 -> q_2: output(thread_3, z, a_1)
q_2 -> q_3: copy(a_3, a_1)
q_3 -> q_2: output(thread_1, y, a_2)
q_3 -> q_3: input(thread_3   , x, v, a_4)
q_2 -> q_4: copy(a_4, a_2)
q_4 -> q_4: output(thread_1, x, a_4)
q_4 -> q_1: input(thread_2, y, a_3,  a_4)
#  the following edge is the one that makes RA (the script pass_fail) print fail. When program prints fail is because this is what it is suppsoed to do. The issue is when the progam does NOT print fail, even when it should. 
# initial edge was q_2->q_2, but this somehow is buggy and the if statement for rule 13 did not pattern match it properly (even though all necessary triples etc were there). 
# to reproduce error replace the triple given on last line with q_2 -> q_2: output(thread_3, x, a_4)
# The important thing is that the if statement of rule 13 should be satisfied with both versions of this edge, as the triple {q_2, a_2, thread_3} should patern match correcly with both. 
# However, it does not when the edge is a loop on q_2.
# For checking one can remove the "edge.destination_node == node " at the if statement of rule 13. Then they both patern match, but of course also ther things patern match as that condition is there for a reason. 
# The fact that it works without that part of the if statement indicates that somehow, in the difinition of an edge, the source node is not returned properly if source and target node are the same. 
# I have no clue why this happens. Also I am not sure that is the issue 100%, it is just a conjecture from my experiments. It could also be an issue with the ==? 
# Without the loop edge there the example works fine, and I recomend running it as is first to better understand how the patern matching should work once on node q_2 between the triple {q_2, a_2, thread_3} 
# the edge q_1 -> q_2 out(thread_3, x, a_4)
q_1 -> q_2: output(thread_3, x, a_4)
