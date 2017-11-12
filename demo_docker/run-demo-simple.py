#from squad.demo_prepro import prepro
#print('import demo_cnsl')
from flask import Flask, render_template, request
from demo_cnsl import Demo
#from bot_code.DR import DocumentRetriever

#import json
#import requests

import argparse

parser = argparse.ArgumentParser(description='launch https server for chatbot, team kAIb')
parser.add_argument('--use_gpu', type=bool, help='Use gpu or not', default=False)
args = parser.parse_args()

app = Flask(__name__)
print('initialize demo module')
demo = Demo(args.use_gpu)
# DR (DEBUG)
#dr_file_path = "../wikipedia_en_all_nopic_2017-08.zim"
#dr_dir_path = "../index_small"
#DR = DocumentRetriever(dr_file_path , dr_dir_path)

@app.route('/')
def main():
    return render_template('index.html')

def getAnswer(paragraph, question):
    #second_passage = DR.retrieve(question) #DEBUG
    return demo.run(paragraph, question)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    paragraph = request.args.get('paragraph')
    question = request.args.get('question')
    answer = getAnswer(paragraph, question)
    return answer

if __name__ == "__main__":
    print('execute https server')
    app.run(host="0.0.0.0", port="1990", threaded=True)
