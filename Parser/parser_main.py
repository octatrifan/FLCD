from Parser.parser import Parser
from Parser.parser_output import ParserOutput

parser = Parser()
# print(parser.print_first())
# print(parser.print_follow())
# print(parser.get_first_concat(['E`','T']))
# print(parser.parserTable)
# print(parser.print_parser_table())
print(parser.analyze_sequence("id + id"))

parserOutput = ParserOutput(parser, "id + id", "tree_output.out")
print(parserOutput.print_tree_to_file())
