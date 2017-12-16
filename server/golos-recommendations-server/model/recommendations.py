import pandas as pd
import ffm
from sklearn.externals import joblib

model = ffm.read_model('./model/github.bin')
dataset = pd.read_csv('./model/github.csv')
history_dataset = dataset[dataset["history"]]
test_dataset = dataset[~dataset["history"]]
# uid_to_idx = joblib.load('./model/uid_to_idx.pkl')
# mid_to_idx = joblib.load('./model/mid_to_idx.pkl')
# aid_to_idx = joblib.load('./model/aid_to_idx.pkl')
# tid_to_idx = joblib.load('./model/tid_to_idx.pkl')
# tgid_to_idx = joblib.load('./model/tgid_to_idx.pkl')
k = 10

def create_user_posts_dataset(user):
  user_history_posts = test_dataset[test_dataset["actor"] == user]
  return user_history_posts

def create_ffm_dataset(dataset):
    X = []
    for index, row in dataset.iterrows(): 
        X.append([
            (0, uid_to_idx[row["actor"]], 1), 
            (1, rid_to_idx[row["repo"]], 1), 
            (2, tid_to_idx[row["type"]], 1)
        ])
    return X, [int(y) for y in dataset["like"]]

def users():
  return users_dataset.sort_values(["precision"], ascending=[0])

def history(user):
  user_history = history_dataset[(history_dataset["actor"] == user)]
  user_posts = user_history["repo"].unique()
  return user_posts

def recommendations(user):
  user_posts = create_user_posts_dataset(user)
  user_data = ffm.FFMData(*create_ffm_dataset(user_posts))
  user_posts["prediction"] = model.predict(user_data)
  return user_posts.sort_values("prediction", ascending=[0])[0:k]
