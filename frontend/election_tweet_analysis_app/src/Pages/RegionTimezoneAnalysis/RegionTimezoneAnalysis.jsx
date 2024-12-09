import AppNavbar from "../../Components/AppNavbar/AppNavbar";

import { DataGrid } from '@mui/x-data-grid';
import Paper from '@mui/material/Paper';
import { TextField } from "@mui/material";
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import Fab from '@mui/material/Fab';
import SearchIcon from '@mui/icons-material/Search';
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

function RegionTimezoneAnalysis() {
    const [regionData, setRegionData] = useState([]);
    const [timezoneData, setTimezoneData] = useState([]);
    const [timezoneDataFormat, setTimezoneDataFormat] = useState('chart');

    const [continent, setContinent] = useState();
    const [country, setCountry] = useState();
    const [state, setState] = useState();
    const [city, setCity] = useState();
    const [limit, setLimit] = useState();
    const [sortMetric, setSortMetric] = useState('');
    const [order, setOrder] = useState();
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

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/geographic-analysis/top-tweets-by-region`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setRegionData(data))
            .catch((err) => {
                console.log(err.message);
            });

        fetch(`http://127.0.0.1:5000/api/geographic-analysis/engagement-by-timezone`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setTimezoneData(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, []);

    let timezoneChartData = {
        labels: timezoneData.map((row) => row.time_zone),
        datasets: [
            {
                label: "Number of Tweets",
                data: timezoneData.map((row) => row.tweet_count),
                backgroundColor: "rgba(75, 192, 192, 0.6)"
            },
            {
                label: "Number of Retweets",
                data: timezoneData.map((row) => row.retweets),
                backgroundColor: "rgba(153, 102, 255, 0.6)"
            },
            {
                label: "Number of Likes",
                data: timezoneData.map((row) => row.likes),
                backgroundColor: "rgba(255, 159, 64, 0.6)"
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

    function handleContinentChange(event) {
        setContinent(event.target.value);
    }

    function handleCountryChange(event) {
        setCountry(event.target.value);
    }

    function handleStateChange(event) {
        setState(event.target.value);
    }

    function handleCityChange(event) {
        setCity(event.target.value);
    }

    function handleLimitChange(event) {
        setLimit(event.target.value);
    }

    function handleSortMetricChange(event) {
        setSortMetric(event.target.value);
    }

    function handleOrderChange(event) {
        setOrder(event.target.value);
    }

    function handleCandidateChange(event) {
        setCandidate(event.target.value);
    }

    function handleTimezoneDataFormatChange(event, newFormat) {
        setTimezoneDataFormat(newFormat);
    }

    function handleRegionParamsChange() {
        fetch(`http://127.0.0.1:5000/api/geographic-analysis/top-tweets-by-region?continent=${continent}&country=${country}&state=${state}&city=${city}&limit=${limit}&sort_by=${sortMetric}&order=${order}`)
            .then((response) => response.json())
            .then((data) => setRegionData(data))
            .catch((err) => {
                console.log(err.message);
            });
    }

    function handleTimezoneParamsChange() {
        fetch(`http://127.0.0.1:5000/api/geographic-analysis/engagement-by-timezone?candidate=${candidate}`)
            .then((response) => response.json())
            .then((data) => setTimezoneData(data))
            .catch((err) => {
                console.log(err.message);
            });

            timezoneChartData = {
                labels: timezoneData.map((row) => row.time_zone),
                datasets: [
                    {
                        label: "Number of Tweets",
                        data: timezoneData.map((row) => row.tweet_count),
                        backgroundColor: "rgba(75, 192, 192, 0.6)"
                    },
                    {
                        label: "Number of Retweets",
                        data: timezoneData.map((row) => row.retweets),
                        backgroundColor: "rgba(153, 102, 255, 0.6)"
                    },
                    {
                        label: "Number of Likes",
                        data: timezoneData.map((row) => row.likes),
                        backgroundColor: "rgba(255, 159, 64, 0.6)"
                    }
                ]
            };
    }

    return (
        <>
            <AppNavbar />
            <h3>Top Tweets By Region</h3>
            <Box>
                <TextField id="outlined-basic" label="Continent" onChange={handleContinentChange} variant="outlined" />
                <TextField id="outlined-basic" label="Country" onChange={handleCountryChange} variant="outlined" />
                <TextField id="outlined-basic" label="State" onChange={handleStateChange} variant="outlined" />
                <TextField id="outlined-basic" label="City" onChange={handleCityChange} variant="outlined" />
                <TextField id="outlined-basic" label="Number of Tweets" onChange={handleLimitChange} variant="outlined" />
                <FormControl>
                    <InputLabel id="demo-simple-select-label">Sort By</InputLabel>
                    <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        label="Sort By"
                        value={sortMetric}
                        sx={{ width: 150 }}
                        onChange={handleSortMetricChange}
                    >
                        <MenuItem value="tweet_id">Tweet ID</MenuItem>
                        <MenuItem value="retweet_count">Retweets</MenuItem>
                        <MenuItem value="likes">Likes</MenuItem>
                    </Select>
                </FormControl>
                <FormControl>
                    <FormLabel id="demo-radio-buttons-group-label">Sorting Order</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        name="radio-buttons-group"
                    >
                        <FormControlLabel value="ASC" onChange={handleOrderChange} control={<Radio />} label="Ascending" />
                        <FormControlLabel value="DESC" onChange={handleOrderChange} control={<Radio />} label="Descending" />
                    </RadioGroup>
                </FormControl>
                <Fab color="primary" aria-label="add" onClick={handleRegionParamsChange}>
                    <SearchIcon />
                </Fab>
            </Box>
            <Paper sx={{ height: 400 }}>
                <DataGrid
                    rows={regionData}
                    getRowId={(row) => row.tweet_id}
                    columns={regionColumns}
                    initialState={{ pagination: { paginationModel } }}
                    pageSizeOptions={[5, 10, 100]}
                />
            </Paper>
            <Box>
                <FormControl>
                    <InputLabel id="demo-simple-select-label">Candidate</InputLabel>
                    <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        label="Candidate"
                        value={candidate}
                        sx={{ width: 150 }}
                        onChange={handleCandidateChange}
                    >
                        <MenuItem value="Trump">Trump</MenuItem>
                        <MenuItem value="Biden">Biden</MenuItem>
                    </Select>
                </FormControl>
                <Fab color="primary" aria-label="add" onClick={handleTimezoneParamsChange}>
                    <SearchIcon />
                </Fab>
            </Box>
            <ToggleButtonGroup
                color="primary"
                value={timezoneDataFormat}
                exclusive
                onChange={handleTimezoneDataFormatChange}
                aria-label="Data View"
            >
                <ToggleButton value="chart">Chart</ToggleButton>
                <ToggleButton value="table">Table</ToggleButton>
            </ToggleButtonGroup>
            {timezoneDataFormat === "chart" ? <Bar data={timezoneChartData} options={timezoneChartOptions} />
            : <Paper sx={{ height: 400 }}>
                <DataGrid
                    rows={timezoneData}
                    getRowId={(row) => row.time_zone}
                    columns={timezoneColumns}
                    initialState={{ pagination: { paginationModel } }}
                    pageSizeOptions={[5, 10, 100]}
                />
            </Paper>}
        </>
    );
}

export default RegionTimezoneAnalysis;