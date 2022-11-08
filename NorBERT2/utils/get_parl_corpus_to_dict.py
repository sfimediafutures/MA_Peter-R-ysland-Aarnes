import json
import re

class ParlamentaryCorpus():

    def __init__(self, path):
        self.path = path

    def load_data(self, lower=False):
        return_data = []
        with open(self.path) as infile:
            with open(self.path, encoding="UTF-8") as infile:
                data = json.load(infile)
        for sentence in data["sentences"]:
            info = {}
            if lower == True:
                re_sentence = re.sub("<.*?>", "", sentence["sentence_text"].lower())
                info[sentence["sentence_id"]] = re_sentence
            else:
                re_sentence = re.sub("<.*?>", "", sentence["sentence_text"])
                info[sentence["sentence_id"]] = re_sentence
            return_data.append(info)
        return return_data

path = r"C:\Users\Aarne\Desktop\z NPSC (norwegian parliamentary speech corpus) sample\20170207\20170207_sentence_data.json"

