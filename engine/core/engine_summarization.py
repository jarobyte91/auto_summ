# from transformers import MobileBertTokenizer, MobileBertModel
# import torch
import re
import pandas as pd
# import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import Normalizer

# tokenizer = MobileBertTokenizer.from_pretrained('google/mobilebert-uncased')
# model = MobileBertModel.from_pretrained('google/mobilebert-uncased')

def algorithm(text):
    # sentences = re.findall(r"[^\.]+\.", text.replace("\n", ""))
    # sentences = re.split(r"(?<=\\.)\\s[\\d\\s\\.]*(?=[A-Z])", text)
    text = re.sub(r"\s{2,}|\n", " ", text)
    text = re.sub(r"\.", ".  ", text)
    #text = re.sub(r"(?<=\d\.)\s*(?=\d)", "", text)
    #text = re.sub(r"(?<=[a-z]\.)\s*(?=[\"a-z])", "", text)
    text = re.sub(r"(?<=\d\.)\s*(?=\d)|(?<=[a-z]\.)\s*(?=[\"a-z])", "", text)
    #sentences = re.split(r"(?<=\.)\s*(?=[A-Z])", text)
    sentences = re.split(r"(?<=\.)\s+", text)
    # print("sentences", len(sentences))
    model = TfidfVectorizer()
#     model = CountVectorizer()
    sentence_embeddings = model.fit_transform(sentences).toarray()
    # print("sentence_embeddings", sentence_embeddings.shape)
    norm = Normalizer()
    sentence_embeddings = norm.fit_transform(sentence_embeddings)
    centralities = (sentence_embeddings @ sentence_embeddings.T)
    centralities = centralities.sum(axis = 1)
    # print("centralities", centralities.shape)
    centralities = pd.DataFrame({"sentence":sentences,
                                 "centrality":centralities})#.sort_values()

    # producing sentence embeddings

    ## approach 1
    #text_tokens = [tokenizer(l, return_tensors="pt") for l in sentences]
    #model_outputs = [model(**i) for i in text_tokens]
    #last_hidden_states = [o[0] for o in model_outputs]
    #sentence_embeddings = torch.stack([t.squeeze().mean(axis = 0) for t in last_hidden_states]).detach().numpy()

    ## aproach 2
    # sentence_embeddings_list = []
    # for s in sentences:
    #     sentence_embeddings_list.append(model(**tokenizer(s, return_tensors="pt"))[0].detach().numpy().squeeze().mean(axis = 0))
    # sentence_embeddings = np.array(sentence_embeddings_list)


    
    # # computing distances

    # ## approach 1
    # distances = np.linalg.norm(np.expand_dims(sentence_embeddings, 1) - np.expand_dims(sentence_embeddings, 0), axis = 2)
    # normalized_distances = distances / distances.max()
    # centralities = pd.Series(normalized_distances.sum(0)).sort_values()
    
    # ## approach 2
    #centralities_list = []
    #for e in sentence_embeddings:
    #    distances = np.linalg.norm(sentence_embeddings - e, axis = -1).sum()
    #    centralities_list.append(distances)
    #centralities = pd.Series(centralities_list).sort_values()

    ## approach 3

    

    return centralities

if __name__ == "__main__":
    text = 'Artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, unlike the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.[1] Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving".[2]\n\nAs machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.[3] A quip in Tesler\'s Theorem says "AI is whatever hasn\'t been done yet".[4] For instance, optical character recognition is frequently excluded from things considered to be AI,[5] having become a routine technology.[6] Modern machine capabilities generally classified as AI include successfully understanding human speech,[7] competing at the highest level in strategic game systems (such as chess and Go),[8] autonomously operating cars, intelligent routing in content delivery networks, and military simulations.[9]\n\nArtificial intelligence was founded as an academic discipline in 1955, and in the years since has experienced several waves of optimism,[10][11] followed by disappointment and the loss of funding (known as an "AI winter"),[12][13] followed by new approaches, success and renewed funding.[11][14] For most of its history, AI research has been divided into sub-fields that often fail to communicate with each other.[15] These sub-fields are based on technical considerations, such as particular goals (e.g. "robotics" or "machine learning"),[16] the use of particular tools ("logic" or artificial neural networks), or deep philosophical differences.[17][18][19] Sub-fields have also been based on social factors (particular institutions or the work of particular researchers).[15]\n\nThe traditional problems (or goals) of AI research include reasoning, knowledge representation, planning, learning, natural language processing, perception and the ability to move and manipulate objects.[16] General intelligence is among the field\'s long-term goals.[20] Approaches include statistical methods, computational intelligence, and traditional symbolic AI. Many tools are used in AI, including versions of search and mathematical optimization, artificial neural networks, and methods based on statistics, probability and economics. The AI field draws upon computer science, information engineering, mathematics, psychology, linguistics, philosophy, and many other fields.\n\nThe field was founded on the assumption that human intelligence "can be so precisely described that a machine can be made to simulate it".[21] This raises philosophical arguments about the mind and the ethics of creating artificial beings endowed with human-like intelligence. These issues have been explored by myth, fiction and philosophy since antiquity.[22] Some people also consider AI to be a danger to humanity if it progresses unabated.[23][24] Others believe that AI, unlike previous technological revolutions, will create a risk of mass unemployment.[25]\n\nIn the twenty-first century, AI techniques have experienced a resurgence following concurrent advances in computer power, large amounts of data, and theoretical understanding; and AI techniques have become an essential part of the technology industry, helping to solve many challenging problems in computer science, software engineering and operations research.'

    sentences, centralities = algorithm(text)

    print("Your text is:")
    print(text)
    print()
    
    print("Your summary is:")
    for  l in [sentences[i] for i in centralities.head().index.to_list()]:
        print(l)




