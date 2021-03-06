import torch.nn as nn
from nlp.w2v.globalconfig import *

class Sentiment(nn.Module):

    # def __init__(self, vocab):
    #     super().__init__()
    #     self.embed = nn.Embedding.from_pretrained(vocab.vectors)
    #     self.fc1 = nn.Linear(MAX_SEQ_LEN * W2V_DIM, 1)
    #     self.sigmoid = nn.Sigmoid()
    #
    # def forward(self, x):
    #     x = self.embed(x)
    #     x = x.reshape(BATCH_SIZE, -1)
    #     x = self.fc1(x)
    #     log_ps = self.sigmoid(x)
    #
    #     return log_ps

    def __init__(self, vocab):
        super().__init__()
        self.embed = nn.Embedding.from_pretrained(vocab.vectors)
        self.fc1 = nn.Linear(MAX_SEQ_LEN * W2V_DIM, 2000)
        self.fc2 = nn.Linear(2000, 1000)
        self.fc3 = nn.Linear(1000, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.embed(x)
        x = x.reshape(BATCH_SIZE, -1)
        x = self.sigmoid(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        x = self.sigmoid(self.fc3(x))

        return x