import aiml
import re

#from simpler_nlg import SimplerNLG # calee
from nltk.tokenize import casual_tokenize

#import sys
#sys.path.append('../../RULE')  # just copy all the files in bot_code directory

class RULE:
    def __init__(self):
        self.kernel = aiml.Kernel()
        self.kernel.learn("startup-ALICE_ALL_convai.xml")
        self.kernel.respond("load aiml b")

        self.num_turn_history = 3


    def get_reply(self, history_context, history_reply, message=""):
        # Note : history_context & history_reply : collections.deque
        history_context_text = ""
        if (len(history_context) >= self.num_turn_history):
            for i in range(self.num_turn_history):
                history_context_text += history_context[len(history_context) + i - self.num_turn_history] + " "

        history_reply_text = ""
        if (len(history_reply) >= self.num_turn_history):
            for i in range(self.num_turn_history):
                history_reply_text += history_reply[len(history_reply) + i - self.num_turn_history] + " "


        """
        sentence = []
        for token in casual_tokenize(message, preserve_case=False, reduce_len=True):
            # make a space before apostrophe
            token = re.sub(r'^([a-z]+)\'([a-z]+)$', '\\1 \'\\2', token)
            for w in token.split():
                sentence.append(self.vocab[w] if w in self.vocab else self.unk)
        """

        reply = self.kernel.respond(message)

        #return SimplerNLG.realise(reply)
        return reply


if __name__ == "__main__":
    rule = RULE()
    while True:
        print(rule.get_reply([],[],input('type your mesesage : ')))
    #print(rule.get_reply([], [], "Hi."))
