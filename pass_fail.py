#!/usr/bin/python3

import argparse

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
    print(f"{nodes=}")

    for edge in edges:
        print(edge, end="\n\n")

if __name__ == "__main__":

    graph = read_graph( arguments.input_file )

