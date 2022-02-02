import React, { useState, useEffect } from 'react';
import { initializeApp } from "firebase/app";
import { getFirestore, collection, getDocs } from 'firebase/firestore';

import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Container from '@material-ui/core/Container';
import useStyles from './styles';

import BoardCard from '../../component/BoardCard';

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

const ReqBoard = () => {
  const classes = useStyles();
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      setPosts([]);
      const querySnapshot = await getDocs(collection(db, 'board'));
      querySnapshot.forEach((doc) => {
        setPosts(p => p.concat(doc.data()));
      });
    }
    fetchPosts();
  }, []);

  return (
    <>
      {console.log(posts)}
      <Box className={classes.box} />
      <Container>
        <Grid container spacing={2}>
          {posts.map((post, i) => (
            <Grid item xs={4}>
              <BoardCard post={post} key={i} />
            </Grid>
          ))}
        </Grid>
      </Container>
    </>
  )
}

export default ReqBoard;