import React, { useEffect } from 'react';
import DeckMap from '../../component/DeckMap';
import TempTable from '../../component/TempTable';

import Container from '@material-ui/core/Container';

import useStyles from './styles';

const TempMap = () => {
  const classes = useStyles();
  return (
    <>
        <DeckMap />
        <TempTable className={classes.table}/>
    </>
  )
}

export default TempMap;