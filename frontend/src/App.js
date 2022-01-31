import { Redirect, Route, Switch } from 'react-router-dom';

import Appbar from './layouts/Appbar';
import HSTable from './pages/HSTable';
import ReqBoard from './pages/ReqBoard';
import TempMap from './pages/TempMap';

function App() {
  return (
    <>
      <Appbar />
      <Switch>
        <Route exact path='/'>
          <Redirect to='/map' />
        </Route>
        <Route path="/map" component={TempMap} />
        <Route path="/table" component={HSTable} />
        <Route path="/board" component={ReqBoard} />
      </Switch>
    </>
  );
}

export default App;
