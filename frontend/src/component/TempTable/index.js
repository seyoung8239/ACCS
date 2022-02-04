import React, { useEffect, useState } from 'react';
import axios from 'axios';
import useStyles from './styles';

import Table from '@mui/material/Table';
import TableHead from '@mui/material/TableHead';
import TableBody from '@mui/material/TableBody';
import TableRow from '@mui/material/TableRow';
import TableCell from '@mui/material/TableCell';

const TempTable = () => {
  const classes = useStyles();
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(()=> {
    const fetchData = async() => {
      try {
        const res = await axios.get('');
        setData(res.data);
      } catch(e) {
        console.log(e)
      }
      setIsLoading(true);
    };
    // fetchData();
  }, []);

  if(!isLoading) return <>Loading..</>
  if(!data) return <>No data..</>

  return (<>
    <Table>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>지역</TableCell>
            <TableCell>기온</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((row, i)=>(
            <TableRow key={i}>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Table>
  </>)
}

export default TempTable;