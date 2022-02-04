import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { heatwave_total, heatwave_region } from '../../routeAPI';

import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';

import { Chart as ChartJS } from 'chart.js/auto'
import { Bar } from 'react-chartjs-2';

import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import ArrowDropUpIcon from '@mui/icons-material/ArrowDropUp';

import useStyles from './styles';

const HSTable = () => {
  const classes = useStyles();
  const [dataTotal, setDataTotal] = useState([]);
  const [dataRegion, setDataRegion] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [isRowOpen, setIsRowOpen] = useState([]);
  const [chartData, setChartData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const resTotal = await axios.get(heatwave_total);
        setDataTotal(resTotal.data);
        const resRegion = await axios.get(heatwave_region);
        setDataRegion(resRegion.data);
        setIsRowOpen(new Array(resTotal.data.length).fill(false));
      } catch (e) {
        console.log(e);
      }
      setIsLoading(true);
    };
    fetchData();
  }, []);

  useEffect(() => {
    if (dataRegion) {
      dataRegion.forEach(year => {
        const lables = year.map(city => city.region);
        const data = year.map(city => parseInt(city.total));
        setChartData(prev => prev.concat({ labels: lables, datasets: [{ label: '지역별 온열 질환자 현황', data: data, backgroundColor: "rgba(255, 99, 132, 0.9)" }] }));
      })
    }
  }, [dataRegion]);

  const handleRowClick = (i) => {
    setIsRowOpen(prev => prev.map((x, index) => {
      if (index === i)
        return !x;
      else
        return x;
    }));
  }

  const options = {
    responsive: false,
  };

  if (!isLoading) return <>Loading...</>
  if (!dataTotal || !dataRegion) return <>No Data...</>

  // console.log(dataTotal);
  console.log(dataRegion);
  // console.log(isRowOpen);
  // console.log(chartData);

  return (
    <>
      <Box className={classes.box} />
      <Container style={{ width: '90%', }}>
        <TableContainer component={Paper} style={{ backgroundColor: 'white' }}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell align="center" sx={{backgroundColor: "#0e4472", color: 'white'}}><b>기준년도</b></TableCell>
                <TableCell align="center" sx={{backgroundColor: "#0e4472", color: 'white'}}><b>전체 환자</b></TableCell>
                <TableCell align="center" sx={{backgroundColor: "#0e4472", color: 'white'}}><b>실외 환자</b></TableCell>
                <TableCell align="center" sx={{backgroundColor: "#0e4472", color: 'white'}}><b>실내 환자</b></TableCell>
                <TableCell align="center" className={classes.button} sx={{backgroundColor: "#0e4472", color: 'white'}}>지역별</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {dataTotal.map((row, i) => (
                <>
                  <TableRow key={i} onClick={() => handleRowClick(i)}>
                    <TableCell align="center">{row.year}</TableCell>
                    <TableCell align="center">{row.total}</TableCell>
                    <TableCell align="center">{row.otdoor_subtot}</TableCell>
                    <TableCell align="center">{row.indoor_subtot}</TableCell>
                    <TableCell align="center">{isRowOpen[i] ? <ArrowDropUpIcon /> : <ArrowDropDownIcon />}</TableCell>
                  </TableRow>
                  {isRowOpen[i] && chartData && <TableCell align="center" className={classes.chart} colSpan={5} >
                    <Bar data={chartData[i]} key={i} options={options} height={200} width={400} />
                  </TableCell>}
                </>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Container>
    </>
  )
}





export default HSTable;