import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./Pages/Home/Home";
import UserEngagementHome from "./Pages/UserEngagementHome/UserEngagementHome";
import TopUsers from "./Pages/TopUsers/TopUsers";
import UserActivity from "./Pages/UserActivity/UserActivity";
import GeographicAnalysisHome from "./Pages/GeographicAnalysisHome/GeographicAnalysisHome";
import CountryCityAnalysis from "./Pages/CountryCityAnalysis/CountryCityAnalysis";
import RegionTimezoneAnalysis from "./Pages/RegionTimezoneAnalysis/RegionTimezoneAnalysis";
import HallOfFame from "./Pages/HallOfFame/HallOfFame";
import TrendAnalysis from "./Pages/TrendAnalysis/TrendAnalysis";
import SentimentAnalysis from "./Pages/SentimentAnalysis/SentimentAnalysis";
import CandidateAnalysis from "./Pages/CandidateAnalysis/CandidateAnalysis";
import Optimization from "./Pages/Optimization/Optimization";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/user-engagement' element={<UserEngagementHome />} />
        <Route path='user-engagement/top-users' element={<TopUsers />} />
        <Route path='/user-engagement/activity-breakdown' element={<UserActivity />} />
        <Route path='/geographic-analytics' element={<GeographicAnalysisHome />} />
        <Route path='/geographic-analysis/country-city-analysis' element={<CountryCityAnalysis />} />
        <Route path='/geographic-analysis/region-timezone-analysis' element={<RegionTimezoneAnalysis />} />
        <Route path='/hall-of-fame' element={<HallOfFame />} />
        <Route path='/trend-analytics' element={<TrendAnalysis />} />
        <Route path='/sentiment-analytics' element={<SentimentAnalysis />} />
        <Route path='/candidate-analytics' element={<CandidateAnalysis />} />
        <Route path='/optimization' element={<Optimization />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
