import React, { useEffect } from 'react';
import { initializeApp } from "firebase/app";
import {getFirestore} from 'firebase/firestore';

const firebaseConfig = {
  apiKey: "AIzaSyASbSNdJYPNqQWkERYQC4adD_x-nSsmL2E",
  authDomain: "codingpotato-6daf2.firebaseapp.com",
  projectId: "codingpotato-6daf2",
  storageBucket: "codingpotato-6daf2.appspot.com",
  messagingSenderId: "928429289034",
  appId: "1:928429289034:web:3c04e1b24bc76d284600b3",
  measurementId: "G-7H025MFM3M"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore();

const ReqBoard = () => {
  return (
    <>
      ReqBoard
    </>
  )
}

export default ReqBoard;