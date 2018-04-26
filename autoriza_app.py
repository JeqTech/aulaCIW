# -*- coding: utf-8 -*-
import tweepy
from tweepy import OAuthHandler

CONSUMER_API_KEY = 'kEzxJsRPtzfqnvUd0huaSKluU'
CONSUMER_API_SECRET = 'snaNX6ThskkuJMZGPbCHdoOJq3Vl5UOcc9pbtEs95kGGtchBWQ'
ACCESS_TOKEN = '169315101-bRamGG8OLre98TYuuffR2emOd270aFA1r2sI0FTM'
ACCESS_TOKEN_SECRET = 'ivsdVTu4QeUyAikyE6TVMQN5AxIG5VNTIATW3Acwz55co'

auth = tweepy.AppAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET)

api = tweepy.API(auth)
if (not api):
   print('Ocorreu um erro ao tentar conectar!')

