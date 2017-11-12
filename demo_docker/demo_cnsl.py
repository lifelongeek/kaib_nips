from bot_code.RULE import RULE
from bot_code.CC import CC
from bot_code.DA_CNN import DA_CNN
from bot_code.QA import QA, get_opt
from bot_code.DR import DocumentRetriever

class Demo(object):
    def __init__(self, use_gpu=False):
        self.cuda = use_gpu
        print('use_gpu = ' + str(self.cuda))

        # QA
        QA_mdl_path = '../model/kaib_qa.mdl'
        qa_opt =  get_opt(QA_mdl_path)
        qa_opt['pretrained_model'] = QA_mdl_path
        qa_opt['datatype'] = 'valid'
        #qa_opt['embedding_file'] = '../ParlAI/data/glove.840B.300d.txt'
        qa_opt['embedding_file'] = '' # we don't need it anymore (since all of the embeddings are stored in model file)

        # DA
        da_checkpoint_dir = "../model/checkpoint_DA/" # bot.sh

        # CC
        cc_dict_dir = "../model/dict_file_th5.dict"
        cc_checkpoint_dir = "../model/exp-emb300-hs1024-lr0.0001-gc0.5"

        # DR
        dr_file_path = "../wikipedia_en_all_nopic_2017-08.zim"
        dr_dir_path = "../index_small"

        # Initialize all models
        self.RULE = RULE()
        self.DR = DocumentRetriever(dr_file_path , dr_dir_path)
        self.QA = QA(qa_opt, cuda=self.cuda)
        self.DA = DA_CNN(da_checkpoint_dir, cuda=self.cuda)
        self.CC = CC(cc_checkpoint_dir, cc_dict_dir, cuda=self.cuda)


    def run(self, passage, question):
        qa_mode = self.DA.classify_user_query(question, passage)

        if qa_mode:
            print('qa mode')
            passage2 = self.DR.retrieve(question)
            print('retrieved document = ' + passage2)
            passage = passage + '\n' + passage2
            response = self.QA.get_reply(passage, question)

        else:
            rep = self.RULE.get_reply('', '', question)
            if(len(rep) > 0):
                print('cc-rule')
                response = rep
            else:
                print('cc-seq2seq')
                response = self.CC.get_reply(question, 'sample_context','sample_reply')

        return response
if __name__ == "__main__":
    demo = Demo()

    my_passage = "sample passage"
    my_question = "who are you ?"
    my_answer = demo.run(my_passage, my_question)

    print('passage = ')
    print(my_passage)
    print('question = ')
    print(my_question)
    print('answer = ')
    print(my_answer)


    my_question = "So, how about some humor?"
    my_answer = demo.run(my_passage, my_question)

    print('question = ')
    print(my_question)
    print('answer = ')
    print(my_answer)
