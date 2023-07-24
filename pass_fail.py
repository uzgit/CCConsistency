#!/usr/bin/python3

import argparse
import graphviz

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
arguments = parser.parse_args()

class Edge:

    def __init__(self, source_node, destination_node, operation, parameter_1, parameter_2, parameter_3=None, parameter_4=None):

        self.source_node = source_node
        self.destination_node = destination_node
        self.operation = operation

        if(   self.operation == "copy" ):
            self.destination_register = parameter_1
            self.source_register = parameter_2
        elif( self.operation == "output" ):
            self.thread = parameter_1
            self.variable = parameter_2
            self.register = parameter_3
        elif( self.operation == "input"):
            self.thread = parameter_1
            self.variable = parameter_2
            self.value = parameter_3
            self.register = parameter_4
        else:
            print(f"Error, {self.operation} is not a valid edge type!")
            exit(1)

    def __operation_repr__(self):

        operation_representation = ""

        if(   self.operation == "copy" ):
            operation_representation = f"{self.destination_register} := {self.source_register}"
        elif( self.operation == "output" ):
            operation_representation = f"out({self.thread}, {self.variable}, {self.register})"
        elif( self.operation == "input" ):
            operation_representation = f"{self.register} := in({self.thread}, {self.variable}, {self.value})"

        return operation_representation

    def __repr__(self):
        representation = f"edge {self.source_node} -> {self.destination_node}\n"
        representation += self.__operation_repr__()
        return representation

#class TripleThread:
#
#    def __init__(self, source_node, register, thread):
#
#        self.source_node = source_node
#        self.register = register
#        self.thread = thread
#
#    def __repr__(self):
#        representation = f"<{self.source_node}, {self.register}, {self.thread}>"
#        return representation
#
#    def __hash__(self):
#        #return hash( self.source_node + self.register + self.thread )
#        return hash( self.__repr__() )
#
#class TripleRegister:
#
#    def __init__(self, source_node, bad_register, potentially_bad_register):
#
#        self.source_node = source_node
#        self.bad_register = bad_register
#        self.potentially_bad_register = potentially_bad_register
#
#    def __repr__(self):
#        representation = f"<{self.source_node}, {self.bad_register}, {self.potentially_bad_register}>"
#        return representation
#
#    def __hash__(self):
#        #return hash( self.source_node + self.bad_register + self.potentially_bad_register )
#        return hash( self.__repr__() )

class TripleThread:

    def __init__(self, source_node, register, thread):

        self.source_node = source_node
        self.register = register
        self.thread = thread

    def __repr__(self):
        representation = f"<{self.source_node}, {self.register}, {self.thread}>"
        return representation

    def __hash__(self):
        return hash( self.__repr__() )

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

class TripleRegister:

    def __init__(self, source_node, bad_register, potentially_bad_register):

        self.source_node = source_node
        self.bad_register = bad_register
        self.potentially_bad_register = potentially_bad_register

    def __repr__(self):
        representation = f"<{self.source_node}, {self.bad_register}, {self.potentially_bad_register}>"
        return representation

    def __hash__(self):
        return hash( self.__repr__() )

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

def read_graph( filename ):

    print(f"Reading graph from file {filename}")

    edges = []
    nodes = []
    with open(filename, "r") as file:

        lines = file.readlines()
        relevant_lines = [line for line in lines if line[0] != "#" and len(line) > 1]
        for line in relevant_lines:

            line = "".join(line.strip().split()) # handle incorrect spacing etc
            
            components = line.split(":")
            line_nodes = components[0].split("->")
            definition = components[1].replace(")", "").split("(")

            source_node = line_nodes[0]
            destination_node = line_nodes[1]
            operation = definition[0]
            parameters = definition[1].split(",")

            edges.append( Edge( source_node, destination_node, operation, *parameters ))

            nodes += line_nodes

    nodes = sorted(list(set(nodes)))
    return nodes, edges

def print_graph( nodes, edges=None ):

    if( edges is None ):
        return print_graph( nodes[0], nodes[1] )

    print(f"{nodes=}")
    for edge in edges:
        print(edge, end="\n\n")

def draw_graph( nodes, edges=None ):

    fontsize = "9"

    if( edges is None ):
        return draw_graph( nodes[0], nodes[1] )

    graph = graphviz.Digraph(format="svg")
    for node in nodes:
        graph.node( node )

    for edge in edges:
        graph.edge( edge.source_node, edge.destination_node, _attributes={"label":edge.__operation_repr__()} )

    graph.render(view=True)#, filename="graph.svg")

def verify_ra( nodes, edges=None ):
    
    if( edges is None ):
        return verify_ra( nodes[0], nodes[1] )


    print("lalalala")

    output_edges = [edge for edge in edges if edge.operation == "output"]
    for output_edge in output_edges:

        alpha = set()
        beta  = set()
        print("lalalala")

        alpha.add( TripleThread(output_edge.source_node, output_edge.register, output_edge.thread) )

        # ellie needs to figure out how long this for loop should go for. she does not know yet
        for i in range( len(edges) ):
            
            ## rule 1  #######################################
            for node in nodes:

                triples = [triple for triple in alpha if triple.source_node == node]
                for triple in triples:

                    for edge in output_edges:
                        if( isinstance(triple, TripleThread ) and edge.thread == triple.thread and edge.destination_node == node):
                            alpha.add( TripleRegister(edge.source_node, triple.register, edge.register) )
        
                            print(f"{alpha}")

            ##################################################

if __name__ == "__main__":

    nodes, edges = read_graph( arguments.input_file )
    graph = (nodes, edges)

    #print_graph(graph)
    #draw_graph(graph)
    verify_ra(graph)
