import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        if (fact.name == 'fact'):
            if fact not in self.facts:
                #print("Asserting {!r}".format(fact))
                self.facts.append(fact)
       #     else: print("The Fact already exist in KB")
       # else: print("Type is not a fact")
        
    def kb_ask(self, fact):
        answ = False
        if (fact.name == 'fact'):
            for fac in self.facts:
                bind = match(fac.statement, fact.statement)
                if (bind != False):
                    if(answ == False):
                        answ = ListOfBindings()
                    answ.add_bindings(bind,fact)
                else:
                    continue
        return answ
       # print("Asking {!r}".format(fact))
