#using sklearn

from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import pickle


#Initialization of embedding & recognizer
embeddingFile = "output/embeddings.pickle"
recognizerFile = "output/recognizer.pickle"
labelEncFile = "output/le.pickle"


print("Loading face embeddings...")
data = pickle.loads(open(embeddingFile, "rb").read())


print("Encoding Lables...")
labelEnc = LabelEncoder()
labels = labelEnc.fit_transform(data["names"])



print("Training Model...")
recognizer = SVC(C=1.0, kernel ="linear", probability=True)
recognizer.fit(data["embeddings"], labels)


f = open(recognizerFile, "wb")
f.write(pickle.dumps(recognizer))
f.close()

f=open(labelEncFile, "wb")
f.write(pickle,dumps(LabelEnc))
f.close()



