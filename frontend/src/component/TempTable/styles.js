import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(() => ({
  box: {
    height: '100px'
  },
  tableHeader: {
    backgroundColor: 'black'
  },
  table: {
    position: 'absolute',
    width:'400px',
    height: '80%',
    backgroundColor: 'white',
    borderRadius: '10px',
    right: '20px',
    overflow: 'scroll'
  }
}));

export default useStyles;