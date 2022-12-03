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

        if lower == False:
            for chaos in json_input["sentences"]:
                token_list = []
                for token in chaos["tokens"]:
                    if token["special_status"] != None:
                        continue
                    else:
                        if " " in token["token_text"]:
                            token_list.extend(token["token_text"].split())
                        else:
                            token_list.append(token["token_text"])
                    sentence_dict[chaos["sentence_id"]] = token_list
        else:
            for chaos in json_input["sentences"]:
                token_list = []
                for token in chaos["tokens"]:
                    if token["special_status"] != None:
                        continue
                    else:
                        if " " in token["token_text"]:
                            token_list.extend(token["token_text"].lower().split())
                        else:
                            token_list.append(token["token_text"].lower())
                    sentence_dict[chaos["sentence_id"]] = token_list
                    
        return sentence_dict