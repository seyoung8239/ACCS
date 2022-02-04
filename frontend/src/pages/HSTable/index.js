import React, { useState, useEffect } from 'react';
import axios from 'axios';

import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';

import useStyles from './styles';

const HSTable = () => {
  const classes = useStyles();
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await axios.get('http://34.64.174.66:8000/heatwave/total');
        setData(res.data);
      } catch (e) {
        console.log(e);
      }
      setIsLoading(true);
    };
    fetchData();

  }, []);

  if (!isLoading) return <>Loading...</>
  if (!data) return <>No Data...</>

  console.log(data);

  return (
    <>
      <Box className={classes.box} />
      <Container>
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>year</TableCell>
                <TableCell>total</TableCell>
                <TableCell>region</TableCell>
                <TableCell>outdoor</TableCell>
                <TableCell>indoor</TableCell>
              </TableRow>
            </TableHead>
            {/* <TableBody>
            {data.map((row, i) => (
              <TableRow key={i}>
                <TableCell>{row}</TableCell>
                <TableCell></TableCell>
                <TableCell></TableCell>
                <TableCell></TableCell>
                <TableCell></TableCell>
              </TableRow>
            ))}
          </TableBody> */}

            <TableRow>
              <TableCell>{data['2020'].year}</TableCell>
              <TableCell>{data['2020'].total}</TableCell>
              <TableCell>{data['2020'].region}</TableCell>
              <TableCell>{data['2020'].otdoor_subtot}</TableCell>
              <TableCell>{data['2020'].indoor_subtot}</TableCell>
            </TableRow>
          </Table>
        </TableContainer>
      </Container>
    </>
  )
}

export default HSTable;