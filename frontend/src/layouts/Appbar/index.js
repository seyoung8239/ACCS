import * as React from 'react';
import { NavLink } from 'react-router-dom';

import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Button from '@mui/material/Button';

import useStyles from './styles';

const pages = [
  { primary: "전국 무더위쉼터 지도", to: "/map" },
  { primary: "온열질환자 데이터", to: "/table" },
  { primary: "지원요청 게시판", to: "/board" }
];

const ResponsiveAppBar = () => {
  const classes = useStyles();

  return (
    <AppBar position="absolute" >
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Button
            component={NavLink}
            to="/map"
            sx={{marginRight: '35px'}}
          >
            <Typography
              variant="h5"
              noWrap
              component="div"
              sx={{ mr: 2, display: {md: 'flex' }, color: 'white' }}
            >
              ACCS
            </Typography>
          </Button>

          <Box sx={{ flexGrow: 1, display: {xs:'none', md: 'flex' }}}>
            {pages.map((page, i) => (
              <Button
                component={NavLink}
                to={page.to}
                className={classes.pageEl}
                key={i}
                sx={{ my: 2, color: 'white', display: 'block', marginRight: '20px', fontSize: '12pt' }}
              >
                {page.primary}
              </Button>
            ))}
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};
export default ResponsiveAppBar;
