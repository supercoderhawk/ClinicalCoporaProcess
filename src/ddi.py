#-*- coding: UTF-8 -*-
from lxml import etree
import os
def read_single_file(filename):
  tree = etree.parse(filename)
  sentences = tree.xpath('//document/sentence')
  for sentence in sentences:
    entities = sentence.xpath('entity')
    if len(entities) == 0:
      print(sentence.xpath('@id'))
    else:
      print(sentence.xpath('@text'))

def read(base_folder):
  for file in os.listdir(base_folder):
    read_single_file(base_folder+file)

if __name__ == '__main__':
  base_folder = ['../Data/raw/Semeval/'+f for f in ['DrugBank/','MedLine/']]
  read_single_file('..\Data\\raw\SemEval\DrugBank\Abarelix_ddi.xml')