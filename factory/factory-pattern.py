import json
import xml.etree.ElementTree as etree

class JSONDataExtractor:
	"""docstring for JSONDataExtractor"""
	def __init__(self, filepath):
		self.data = dict()
		with open(filepath, mode='r', encoding='utf-8') as f:
			self.data = json.load(f)

	@property
	def parsed_data(self):
		return self.data
		


class XMLDataExtractor:
	"""docstring for XMLDataExtractor"""
	def __init__(self, filepath):
		self.tree = etree.parse(filepath)

	@property
	def parsed_data(self):
		return self.tree


def data_extraction_factory(filepath):
	if filepath.endswith('json'):
		extractor = JSONDataExtractor
	elif filepath.endswith('xml'):
		extractor = XMLDataExtractor
	else:
		raise ValueError('Cannot extract data from {}'.format(filepath))

	return extractor(filepath)

def extract_data_from(filepath):
	factory = None
	try:
		factory = data_extraction_factory(filepath)
	except ValueError as e:
		print(e)

	return factory

def print_movies(movies):
	for movie in movies:
		print("Title: {}".format(movie['title']))

		year = movie['year']
		if(year):
			print("Year: {}".format(year))

		director = movie['director']
		if(director):
			print("Director: {}".format(director))

		genre = movie['genre']
		if(genre):
			print("Genre: {}".format(genre))

		print()


def main():
	sqlite_factory = extract_data_from('./movies.sq3')
	print()

	json_factory = extract_data_from('./movies.json')
	json_data    = json_factory.parsed_data

	print_movies(json_data)

	xml_factory = extract_data_from('./person.xml')
	xml_data    = xml_factory.parsed_data

	liars = xml_data.findall(".//person[lastName='Liar']")
	print('found: {} persons'.format(len(liars)))

	for liar in liars:
		firstname = liar.find('firstName').text
		print('first name: {}'.format(firstname))

		lastname = liar.find('lastName').text
		print('last name: {}'.format(lastname))

		[print("phone number ({}):".format(p.attrib['type']), p.text)
		for p in liar.find('phoneNumbers')]
		print()



if __name__ == '__main__':
    main()

	
		