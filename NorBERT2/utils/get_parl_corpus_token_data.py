import json

class ParlamentaryCorpus():

    def __init__(self, path): # Takes input normalized_token_file
        self.path = path
        self.sentence_dict = {}

    def load_data(self, lower=False):
        sentence_dict = self.sentence_dict
        with open(self.path) as infile:
            with open(self.path, encoding="UTF-8") as infile:
                json_input = json.load(infile)

        for chaos in json_input["sentences"]:
            for k, data in chaos.items():
                token_list = []
                if isinstance(data, list):
                    for dictionary in data:
                        if dictionary["special_status"] == None and lower == True:
                            token_list.append(dictionary["token_text"].lower())
                        elif dictionary["special_status"] == None:
                            token_list.append(dictionary["token_text"])
                    sentence_dict[dictionary["sentence_id"]] = token_list
        return sentence_dict

# NESTING FOR DAYS