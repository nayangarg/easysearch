#3.

import os
import numpy as np
import pandas as pd
from read_write_create import *
import sys

def invert_num(l):
    return [(1.0/x) for x in l if x!=0]

def get_node_weight(w, df_pos):
    
    w_weight = 0
    w_row = df_pos.loc[df_pos["words"] == w]
    
    if len(w_row["words"]) > 0:
        posi = list(w_row["positions"])[0]
        posi = posi[:-1]
        if(len(posi) >0):
            w_weight = sum(invert_num(posi))
    
    return w_weight

#------ main ------#
if __name__ == '__main__':

    #print('Position_Weight')

    w = sys.argv
    w = w[1:]
    w = float(w[0])

    #print(w)

    global cwd, path, data_path

    cwd = '/home/nayan/coding/Major/EasySearch/venv'
    path = cwd
    data_path = cwd + "/data"

    create_folder(cwd,"SCScore_WPSO")
    word_score_path = cwd + "/SCScorePSO/"

    #print("Word-score-with-PositionWeight-sCake")
    li = ['255000.csv', '271426.csv', '571159.csv', '614396.csv', '296420.csv']

    for every_file in li:

    #for every_file in (os.listdir(data_path)[:5]):
        
       # print(every_file)
        file_name = every_file[:-4]
        #text = read_text_from_file(data_path,every_file)
        
        f_wordScore = read_text_from_file(cwd+"/SCScorePSO/",file_name+".csv.sortedranked.IF.txt")
        
        with open(cwd+"/positions/"+file_name+".pkl", 'rb') as f:
            df_pos = pd.read_pickle(f, compression=None)
            
        df = pd.read_csv(word_score_path + file_name  +".csv.sortedranked.IF.txt")
        words = df["Name"]
        wscore = df["IF"]
        
        node_weight = [0] * len(words)
        for index in range(len(words)):
            node_weight[index] = get_node_weight(words[index], df_pos)
        
        new_score = []

        l = len(wscore)

        for i in range(l):
            new_score.append(wscore[i] + w*node_weight[i])

        #new_score = list(wscore + w * node_weight)
        
        data = dict()
        data["Words"] = words
        data["Old_WScore"] = wscore
        data["Position_Weight"] = node_weight
        data["SCScore"] = new_score
        new_df = pd.DataFrame(data=data)
        new_df = new_df.sort_values("SCScore",ascending=False)
        
        new_df.to_csv(cwd+"/SCScore_WPSO/"+ file_name +"_ranked_list.csv")
         
