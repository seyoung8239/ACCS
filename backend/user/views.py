from django.shortcuts import render
import pyrebase

# Create your views here.

config = {
    apiKey: "AIzaSyASbSNdJYPNqQWkERYQC4adD_x-nSsmL2E",
    authDomain: "codingpotato-6daf2.firebaseapp.com",
    databaseURL: "https://codingpotato-6daf2-default-rtdb.firebaseio.com",
    projectId: "codingpotato-6daf2",
    storageBucket: "codingpotato-6daf2.appspot.com",
    messagingSenderId: "928429289034",
    appId: "1:928429289034:web:4968cf24ad7b04db4600b3",
    measurementId: "G-995VVB7TKN"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
