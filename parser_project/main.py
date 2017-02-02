from parser_package.parser import Parser


oktv = 'http://oktv.ua/id1336515'
dobovo = 'http://www.dobovo.com/odessa-apartments/apartment-in-the-historical-center-88937.html'

my_parser = Parser()

my_parser.retrieve_elements(oktv)
my_parser.save_data()
