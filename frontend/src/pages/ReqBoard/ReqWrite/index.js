import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import Container from '@material-ui/core/Container';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

import useStyles from '../styles';

import { initializeApp } from "firebase/app";
import { getFirestore, collection, addDoc } from "firebase/firestore";

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
const db = getFirestore(app);

function yyyymmdd(d) {
  var mm = d.getMonth() + 1; // getMonth() is zero-based
  var dd = d.getDate();

  return [d.getFullYear(),
  (mm > 9 ? '' : '0') + mm,
  (dd > 9 ? '' : '0') + dd
  ].join('-');
};


const ReqWrite = () => {
  const classes = useStyles();
  const navigate = useNavigate();

  const [title, setTitle] = useState();
  const [location, setLocation] = useState();
  const [content, setContent] = useState();

  const handleClick = async () => {
    try {
      const docRef = await addDoc(collection(db, "board"), {
        content: content,
        location: location,
        title: title,
        date: yyyymmdd(new Date())
      })
    } catch (e) {
      console.log(e);
    } finally {
      alert('요청에 성공했습니다.');
      navigate('/board');
    }
  }
  // console.log(new Date().toString());

  return (<>
    <div style={{height: '150px'}}></div>
    <Container className={classes.container} style={{ width: '85%', borderRadius: '15px', padding: '50px', border: '4px solid rgba(25,118,210, 1)' }}>
      <TextField label="제목" value={title} onChange={e => setTitle(e.target.value)} variant="outlined" fullWidth sx={{ marginBottom: '10px' }} />
      <TextField label="요청 위치" value={location} onChange={e => setLocation(e.target.value)} variant="outlined" fullWidth sx={{ marginBottom: '30px' }} />
      <TextField label="상세 요청을 입력하세요." value={content} onChange={e => setContent(e.target.value)} variant="outlined" fullWidth multiline rows={12} sx={{ marginBottom: '10px'}} />
      <Button variant='contained' onClick={handleClick} sx={{
        position: 'relative',
        padding: '10px',
        width: '140px',
        marginTop: '60px',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        fontSize: '14pt'
      }}>
        등록하기
      </Button>
    </Container>
  </>);
}

export default ReqWrite;