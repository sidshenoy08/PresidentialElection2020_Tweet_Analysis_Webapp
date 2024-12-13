import AppNavbar from "../../Components/AppNavbar/AppNavbar";
import Download from "../../Components/Download/Download";
import Footer from "../../Components/Footer/Footer";

import { DataGrid } from '@mui/x-data-grid';
import Paper from '@mui/material/Paper';
import { TextField } from "@mui/material";
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import Box from "@mui/material/Box";
import { useState, useEffect } from "react";
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';
import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import { Bar } from 'react-chartjs-2';

import './RegionTimezoneAnalysis.css';

const config = require("../../config.json");

function RegionTimezoneAnalysis() {
    const [regionData, setRegionData] = useState([]);
    const [timezoneData, setTimezoneData] = useState([]);
    const [timezoneDataFormat, setTimezoneDataFormat] = useState('chart');

    const [continent, setContinent] = useState();
    const [country, setCountry] = useState();
    const [state, setState] = useState();
    const [city, setCity] = useState();
    const [limit, setLimit] = useState();
    const [sortMetric, setSortMetric] = useState();
    const [order, setOrder] = useState('DESC');
    const [candidate, setCandidate] = useState('Trump');

    const paginationModel = { page: 0, pageSize: 5 };

    const regionColumns = [
        { field: 'tweet_id', headerName: 'Tweet ID', width: 200 },
        { field: 'user_name', headerName: 'Username', width: 150 },
        { field: 'tweet', headerName: 'Tweet', width: 600 },
        { field: 'retweet_count', headerName: 'Retweets', type: 'number', width: 100 },
        { field: 'likes', headerName: 'Likes', type: 'number', width: 100 },
        { field: 'location', headerName: 'Location', width: 350 }
    ];

    const timezoneColumns = [
        { field: 'time_zone', headerName: 'Timezone', width: 250 },
        { field: 'tweet_count', headerName: 'Number of Tweets', type: 'number', width: 350 },
        { field: 'retweets', headerName: 'Number of Retweets', type: 'number', width: 350 },
        { field: 'likes', headerName: 'Number of Likes', type: 'number', width: 350 }
    ];

    ChartJS.register(
        CategoryScale,
        LinearScale,
        BarElement,
        Title,
        Tooltip,
        Legend
    );

    let timezoneChartData = {
        labels: timezoneData.map((row) => row.time_zone),
        datasets: [
            {
                label: "Number of Tweets",
                data: timezoneData.map((row) => row.tweet_count),
                backgroundColor: "#1DA1F2"
            },
            {
                label: "Number of Retweets",
                data: timezoneData.map((row) => row.retweets),
                backgroundColor: "#4CAF50"
            },
            {
                label: "Number of Likes",
                data: timezoneData.map((row) => row.likes),
                backgroundColor: "#FF6F61"
            }
        ]
    };

    const timezoneChartOptions = {
        responsive: true,
        plugins: {
            legend: {
                position: "top",
            },
            title: {
                display: true,
                text: "Number of Tweets, Likes, and Retweets by Timezone",
            },
        },
    };

    useEffect(() => {
        fetch(`${config.api_url}/geographic-analysis/top-tweets-by-region?continent=${continent}&country=${country}&state=${state}&city=${city}&limit=${limit}&sort_by=${sortMetric}&order=${order}`)
            .then((response) => response.json())
            .then((data) => setRegionData(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, [continent, country, state, city, limit, sortMetric, order]);

    useEffect(() => {
        fetch(`${config.api_url}/geographic-analysis/engagement-by-timezone?candidate=${candidate}`)
            .then((response) => response.json())
            .then((data) => setTimezoneData(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, [candidate]);

    return (
        <div className="body">
            <AppNavbar />
            <h3>Top Tweets By Region</h3>
            <Box className="query-params">
                <TextField id="outlined-basic" label="Continent" style={{ marginLeft: "2rem" }} onChange={(event) => setContinent(event.target.value)} variant="outlined" />
                <TextField id="outlined-basic" label="Country" style={{ marginLeft: "2rem" }} onChange={(event) => setCountry(event.target.value)} variant="outlined" />
                <TextField id="outlined-basic" label="State" style={{ marginLeft: "2rem" }} onChange={(event) => setState(event.target.value)} variant="outlined" />
                <TextField id="outlined-basic" label="City" style={{ marginLeft: "2rem" }} onChange={(event) => setCity(event.target.value)} variant="outlined" />
                <TextField id="outlined-basic" label="Number of Tweets" style={{ marginLeft: "2rem" }} onChange={(event) => setLimit(event.target.value)} variant="outlined" />
                <FormControl style={{ marginLeft: "2rem" }}>
                    <InputLabel id="demo-simple-select-label">Sort By</InputLabel>
                    <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        label="Sort By"
                        value={sortMetric}
                        sx={{ width: 150 }}
                        onChange={(event) => setSortMetric(event.target.value)}
                    >
                        <MenuItem value="tweet_id">Tweet ID</MenuItem>
                        <MenuItem value="retweet_count">Retweets</MenuItem>
                        <MenuItem value="likes">Likes</MenuItem>
                    </Select>
                </FormControl>
                <FormControl style={{ marginLeft: "2rem" }}>
                    <FormLabel id="demo-radio-buttons-group-label">Sorting Order</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        name="radio-buttons-group"
                        defaultValue={order}
                    >
                        <FormControlLabel value="ASC" onChange={(event) => setOrder(event.target.value)} control={<Radio />} label="Ascending" />
                        <FormControlLabel value="DESC" onChange={(event) => setOrder(event.target.value)} control={<Radio />} label="Descending" />
                    </RadioGroup>
                </FormControl>
            </Box>
            <div className="data">
                <Paper sx={{ height: 400, width: '99%', marginLeft: 'auto', marginRight: 'auto' }}>
                    <DataGrid
                        rows={regionData}
                        getRowId={(row) => row.tweet_id}
                        columns={regionColumns}
                        initialState={{ pagination: { paginationModel } }}
                        pageSizeOptions={[5, 10, 100]}
                    />
                    <Download data={regionData} filename="top-tweets-by-region" />
                </Paper>
            </div>
            <h3>Tweet Engagement By Timezone</h3>
            <Box className="query-params">
                <FormControl style={{ marginLeft: "2rem" }}>
                    <InputLabel id="demo-simple-select-label">Candidate</InputLabel>
                    <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        label="Candidate"
                        value={candidate}
                        sx={{ width: 150 }}
                        onChange={(event) => setCandidate(event.target.value)}
                    >
                        <MenuItem value="Trump">Trump</MenuItem>
                        <MenuItem value="Biden">Biden</MenuItem>
                    </Select>
                </FormControl>
            </Box>
            <ToggleButtonGroup
                color="primary"
                value={timezoneDataFormat}
                exclusive
                onChange={(event, newFormat) => setTimezoneDataFormat(newFormat)}
                aria-label="Data View"
                style={{ marginLeft: "2rem", marginBottom: "1rem" }}
            >
                <ToggleButton value="chart">Chart</ToggleButton>
                <ToggleButton value="table">Table</ToggleButton>
            </ToggleButtonGroup>
            <div className="data">
                {timezoneDataFormat === "chart" ? <Bar data={timezoneChartData} options={timezoneChartOptions} />
                    : <Paper sx={{ height: 400, width: '90%', marginLeft: 'auto', marginRight: 'auto' }}>
                        <DataGrid
                            rows={timezoneData}
                            getRowId={(row) => row.time_zone}
                            columns={timezoneColumns}
                            initialState={{ pagination: { paginationModel } }}
                            pageSizeOptions={[5, 10, 100]}
                        />
                        <Download data={timezoneData} filename="tweet-engagement-by-timezone" />
                    </Paper>}
            </div>
            <Footer />
        </div>
    );
}

export default RegionTimezoneAnalysis;