import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./Pages/Home/Home";
import UserEngagementHome from "./Pages/UserEngagementHome/UserEngagementHome";
import TopUsers from "./Pages/TopUsers/TopUsers";
import UserActivity from "./Pages/UserActivity/UserActivity";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/user-engagement' element={<UserEngagementHome />} />
        <Route path='user-engagement/top-users' element={<TopUsers />} />
        <Route path='/user-engagement/activity-breakdown' element={<UserActivity />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
