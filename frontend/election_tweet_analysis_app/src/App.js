import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./Pages/Home/Home";
import UserEngagementHome from "./Pages/UserEngagementHome/UserEngagementHome";
import TopUsers from "./Pages/TopUsers/TopUsers";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/user-engagement' element={<UserEngagementHome />} />
        <Route path='user-engagement/top-users' element={<TopUsers />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
