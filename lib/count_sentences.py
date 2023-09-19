#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value = None):
        self._value = value

    def set_value(self,value):
        if type(value) == str:
            self._value = value
        else:
            print("The value must be a string.")
    
    def get_value(self):
        return self._value
    
    value = property(get_value,set_value)

    def is_sentence(self):
        if  (self.value.endswith(".")):
           return True
        else:
            return False
        
    def is_question(self):
      if(self.value.endswith("?")):
        return True
      else:
        return False
    
    def is_exclamation(self):
      if(self.value.endswith("!")):
        return True
      else:
        return False

    def count_sentences(self):
        if self._value is not None:
            sentences = re.sub(r'[!?]', '.', self._value).split('.')
            sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
            return len(sentences)
        else:
            return 0
string = MyString()
string.value = "This is a string! It has three sentences. Right?"

print(string.value)

sentence_count = string.count_sentences()
print(f"The number of sentences is: {sentence_count}")