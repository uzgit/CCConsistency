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
#  the following edge is the one that makes RA (the script pass_fail) print fail. 
q_1 -> q_2: output(thread_3, x, a_4)
