import { Navigate, Route, Routes } from 'react-router-dom';

import Appbar from './layouts/Appbar';
import HSTable from './pages/HSTable';
import ReqBoard from './pages/ReqBoard';
import ReqWrite from './pages/ReqBoard/ReqWrite';
import TempMap from './pages/TempMap';

function App() {
  return (
    <>
      <Appbar />
      <Routes>
        <Route path="/map" element={<TempMap />} />
        <Route path="/table" element={<HSTable />} />
        <Route path="/board/new" element={<ReqWrite />} />
        <Route path="/board" exact element={<ReqBoard />} />
        <Route path="*" element={<Navigate to="/map" />} />
      </Routes>
    </>
  );
}

export default App;
