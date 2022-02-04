import React, { useEffect, useState } from 'react';
import axios from 'axios';
import useStyles from './styles';

import TableContainer from '@mui/material/TableContainer';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableHead from '@mui/material/TableHead';
import TableBody from '@mui/material/TableBody';
import TableRow from '@mui/material/TableRow';
import TableCell from '@mui/material/TableCell';

import { temperatureInfo } from '../../routeAPI';

const TempTable = () => {
  const classes = useStyles();
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(()=> {
    const fetchData = async() => {
      try {
        const res = await axios.get(temperatureInfo);
        setData(res.data);
      } catch(e) {
        console.log(e)
      }
      setIsLoading(true);
    };
    fetchData();
  }, []);

  if(!isLoading) return <>Loading..</>
  if(!data) return <>No data..</>

  console.log(data);

  return (<>
    <div className={classes.box}/>
    <div className={classes.table}>
      <Table stickyHeader>
        <TableHead >
          <TableRow className={classes.tableHeader}>
            <TableCell sx={{backgroundColor: "#0e4472", color: 'white'}}><b>지역</b></TableCell>
            <TableCell sx={{backgroundColor: "#0e4472", color: 'white'}}><b>최대 기온</b></TableCell>
            <TableCell sx={{backgroundColor: "#0e4472", color: 'white'}}><b>평균 기온</b></TableCell>
            <TableCell sx={{backgroundColor: "#0e4472", color: 'white'}}><b>최소 기온</b></TableCell>
            <TableCell sx={{backgroundColor: "#0e4472", color: 'white'}}><b>위험도</b></TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((row, i)=>(
            <TableRow key={i}>
              <TableCell><b>{row.stnNm}</b></TableCell>
              <TableCell>{row.maxTa}</TableCell>
              <TableCell>{row.avgTa}</TableCell>
              <TableCell>{row.minTa}</TableCell>
              <TableCell>{row.value}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  </>)
}

export default TempTable;