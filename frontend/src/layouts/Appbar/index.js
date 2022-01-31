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
  {primary: "전국 기온 지도", to: "/map"},
  {primary: "온열질환자 데이터", to: "/table"},
  {primary: "물자요청 게시판", to: "/board"}
];

const ResponsiveAppBar = () => {
  const classes = useStyles();

  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Typography
            variant="h5"
            noWrap
            component="div"
            sx={{ mr: 2, display: { xs: 'none', md: 'flex' } }}
          >
            ACCS
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
            {pages.map((page) => (
              <Button
                component={NavLink}
                to={page.to}
                className={classes.pageEl}
                key={page}
                sx={{ my: 2, color: 'white', display: 'block' }}
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
