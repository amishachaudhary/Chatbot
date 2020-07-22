# sample chatbot

import numpy as np
import tensorflow as tf
import re
import time

lines = open('movie_lines.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
convo= open('movie_conversations.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')

#creating a dictionary that maps each line and its id

id2line={}
for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5 :
        id2line[_line[0]] = _line[4]
        
#creating a list of all the conversations
conversations_ids = []
for conversation in convo[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
    conversations_ids.append(_conversation.split(','))
    

#creating separately the question and answers
questions = []
answers = []
for conversation in conversations_ids:
    for i in range(len(conversation) -1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])

#cleaning the text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm","i am",text)
    text = re.sub(r"he's","he is",text)
    text = re.sub(r"thats","she is",text)
    text = re.sub(r"that's","that is",text)
    text = re.sub(r"what's","what is",text)
    text = re.sub(r"\'ll"," will",text)
    text = re.sub(r"\'re"," are",text)
    text = re.sub(r"'d"," would",text)
    text = re.sub(r"won't","will not",text)
    text = re.sub(r"can't","cannot",text)
    text = re.sub(r"[-()+_=#&@/;:<>{}|]","",text)
    return text

#cleaning the questions
clean_question=[]
for question in questions:
    clean_question.append(clean_text(question))

#cleanin the answers
clean_answer=[]
for answer in answers:
    clean_answer.append(clean_text(answer))
    
#creating a dictionary that maps each word to its number of occurences
word_count = {}
for question in clean_question:
        for word in question.split():
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
for answer in clean_answer:
    for word in answer.split():
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

##tokenization and filtering non freq words!!
#creating two dict that map questions words and answer words to a unique integer
threshold = 20
questionsword2int = {}
word_number = 0
for word, count in word_count.items():
    if count >= threshold:
        questionsword2int[word] = word_number
        word_number += 1
        
answerword2int = {}
word_number = 0
for word, count in word_count.items():
    if count >= threshold:
        answerword2int[word] = word_number
        word_number += 1

# adding the last tokens to these two dictionaries
tokens = ['<PAD>','<EOS>','<OUT>','<SOS>']
for token in tokens:
    questionsword2int[token] = len(questionsword2int) + 1

for token in tokens:
    answerword2int[token] = len(answerword2int) + 1

#creating the inverse dict of the answerwords2int dict
answerint2word = {w_i: w for w, w_i in answerword2int.items()}

#adding the EOS token to the end of every answer
for i in range(len(clean_answer)):
    clean_answer[i] += ' <EOS>' 
    
#Translate all the questions and answers into integers
#Replacing all the least freq words that were filtered out by <OUT>
questions_to_int = []
for questions in clean_question:
    question_int=[]
    for word in questions.split():
        if word not in questionsword2int:
            question_int.append(questionsword2int['<OUT>'])
        else:
            question_int.append(questionsword2int[word])
    questions_to_int.append(question_int)

answers_to_int = []
for answers in clean_answer:
    answer_int = []
    for word in answers.split():
        if word not in answerword2int:
            answer_int.append(answerword2int['<OUT>'])
        else:
            answer_int.append(answerword2int[word])
    answers_to_int.append(answer_int)

# Sorting questions and answers by the length of questions
sorted_clean_questions = []
sorted_clean_answers = []

for length in range(1, 25 + 1) :
    for i in enumerate(questions_to_int):
        if len(i[1]) == length:
            sorted_clean_questions.append(questions_to_int[i[0]])
            sorted_clean_answers.append(answers_to_int[i[0]])




# SEQ2SEQ I.E ARCHITECTURE OF CHATBOT

#creating placeholders for input and targets(outputs)
def input_model():
    inputs = tf.placeholder(tf.int32, [None, None], name='inputs')
    targets = tf.placeholder(tf.int32, [None, None], name='targets')
    lr = tf.placeholder(tf.float32, name='learning_rate')
    keep_prob = tf.placeholder(tf.float32, name='keep_prob')
    return inputs, targets , lr , keep_prob


#preprocessing the targets
def preprocess_targets(targets, word2int, batch_size):
    left_side = tf.fill([batch_size, 1], word2int['<SOS>'])
    right_side = tf.strided_slice(targets, [0,0], [batch_size, -1], [1,1])
    preprocessed_targets = tf.concat([left_side,right_side], 1)
    return preprocessed_targets

#Creating the Encoder RNN layer
def encoder_rnn_layer(rnn_inputs, rnn_size,num_layers, keep_prob, sequence_length):
    lstm = tf.contrib.rnn.BasicLSTMCell(rnn_size)
    lstm_dropout = tf.contrib.rnn.DropoutWrapper(lstm, input_keep_prob = keep_prob)
    encoder_cell = tf.contrib.rnn.MultiRNNcell([lstm_dropout] * num_layers)
    _, encoder_state = tf.nn.bidirectional_dynamic_rnn(cell_fw = encoder_cell,
                                                                    cell_bw = encoder_cell,
                                                                    sequence_length = sequence_length,
                                                                    inputs = rnn_inputs,
                                                                    dtype = tf.float32)
    return encoder_state












        
    
    
    
    
    
    
    
    
    
    