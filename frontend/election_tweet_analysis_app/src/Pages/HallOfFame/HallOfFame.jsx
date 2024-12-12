import AppNavbar from "../../Components/AppNavbar/AppNavbar";
import Download from "../../Components/Download/Download";

import { useState, useEffect } from "react";
import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import { DataGrid } from '@mui/x-data-grid';
import Paper from '@mui/material/Paper';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
import { TextField } from "@mui/material";
import Box from "@mui/material/Box";
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';

function HallOfFame() {
    const [activeUsers, setActiveUsers] = useState([]);
    const [activeUsersDataFormat, setActiveUsersDataFormat] = useState('chart');
    const [activeUsersLimit, setActiveUsersLimit] = useState();
    const [page, setPage] = useState(0);

    const [popularTweets, setPopularTweeets] = useState([]);
    const [popularTweetsLimit, setPopularTweeetsLimit] = useState();
    const [metric, setMetric] = useState('retweets');
    const [popularityCandidate, setPopularityCandidate] = useState('Trump');

    const [locationInsights, setLocationInsights] = useState([]);
    const [cityLimit, setCityLimit] = useState();
    const [locationCandidate, setLocationCandidate] = useState('Trump');
    const [locationInsightsFormat, setLocationInsightsFormat] = useState('chart')

    ChartJS.register(
        CategoryScale,
        LinearScale,
        BarElement,
        Title,
        Tooltip,
        Legend
    );

    const activeUsersColumns = [
        { field: 'user_id', headerName: 'User ID', width: 150 },
        { field: 'user_name', headerName: 'Username', width: 150 },
        { field: 'tweet_count', headerName: 'Number of Tweets', type: 'number', width: 250 }
    ];

    const popularTweetsColumns = [
        { field: 'tweet_id', headerName: 'User ID', width: 200 },
        { field: 'user_name', headerName: 'Username', width: 150 },
        { field: 'tweet', headerName: 'Tweet', width: 750 },
        { field: 'retweet_count', headerName: 'Retweets', type: 'number', width: 80 },
        { field: 'likes', headerName: 'Likes', type: 'number', width: 80 },
        { field: 'city', headerName: 'City', width: 100 },
        { field: 'state', headerName: 'State', width: 150 }
    ];

    const locationInsightsColumns = [
        { field: 'city', headerName: 'City', width: 150 },
        { field: 'state', headerName: 'State', width: 150 },
        { field: 'tweet_count', headerName: 'Number of Tweets', type: 'number', width: 250 }
    ]

    const paginationModel = { page: 0, pageSize: 5 };

    let activeUsersChartData = {
        labels: activeUsers.map((row) => row.user_name),
        datasets: [
            {
                label: "Number of Tweets",
                data: activeUsers.map((row) => row.tweet_count),
                backgroundColor: "rgba(75, 192, 192, 0.6)"
            }
        ]
    };

    let locationInsightsChartData = {
        labels: locationInsights.map((row) => row.city + ", " + row.state),
        datasets: [
            {
                label: "Number of Tweets",
                data: locationInsights.map((row) => row.tweet_count),
                backgroundColor: "rgba(75, 192, 192, 0.6)"
            }
        ]
    };

    const activeUsersChartOptions = {
        responsive: true,
        plugins: {
            legend: {
                position: "top"
            },
            title: {
                display: true,
                text: "Number of Tweets By Users"
            },
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: "User"
                },
            },
            y: {
                title: {
                    display: true,
                    text: "Number of Tweets"
                }
            }
        }
    };

    const locationInsightsChartOptions = {
        responsive: true,
        indexAxis: "y",
        plugins: {
            legend: {
                position: "top"
            },
            title: {
                display: true,
                text: "Number of Tweets By City"
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: "Number of Tweets"
                },
            },
            y: {
                title: {
                    display: true,
                    text: "Location"
                }
            }
        }
    }

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/homepage/most-active-users?limit=${activeUsersLimit}&page=${page}`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setActiveUsers(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, [activeUsersLimit, page]);

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/popular-tweets/${metric}?candidate=${popularityCandidate}&limit=${popularTweetsLimit}`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setPopularTweeets(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, [metric, popularityCandidate, popularTweetsLimit]);

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/popular-tweets/location-insights?candidate=${locationCandidate}&limit=${cityLimit}`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setLocationInsights(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, [locationCandidate, cityLimit]);

    return (
        <>
            <AppNavbar />
            <h3>Most Active Users</h3>
            <Box>
                <TextField id="outlined-basic" label="Number of Users" onChange={(event) => setActiveUsersLimit(event.target.value)} variant="outlined" />
                <TextField id="outlined-basic" label="Page Number" onChange={(event) => setPage(event.target.value)} variant="outlined" />
            </Box>
            <ToggleButtonGroup
                color="primary"
                value={activeUsersDataFormat}
                exclusive
                onChange={(event, newFormat) => setActiveUsersDataFormat(newFormat)}
                aria-label="Data View"
            >
                <ToggleButton value="chart">Chart</ToggleButton>
                <ToggleButton value="table">Table</ToggleButton>
            </ToggleButtonGroup>
            {activeUsersDataFormat === "chart" ? <Bar data={activeUsersChartData} options={activeUsersChartOptions} />
                : <Paper sx={{ height: 400, width: '100%' }}>
                    <DataGrid
                        rows={activeUsers}
                        getRowId={(row) => row.user_id}
                        columns={activeUsersColumns}
                        initialState={{ pagination: { paginationModel } }}
                        pageSizeOptions={[5, 10, 100]}
                        sx={{ border: 0 }}
                    />
                    <Download data={activeUsers} filename="most-active-users" />
                </Paper>}
            <div style={{ marginTop: "4rem" }}>
                <h3 style={{ display: "inline" }}>Most Popular Tweets By </h3>
                <FormControl>
                    <InputLabel id="popular-metric-select-label">Popularity Metric</InputLabel>
                    <Select
                        labelId="metric-select-label"
                        id="metric-simple-select"
                        label="Metric"
                        sx={{ width: 150 }}
                        onChange={(event) => setMetric(event.target.value)}
                        defaultValue={metric}
                    >
                        <MenuItem value="retweets">Retweets</MenuItem>
                        <MenuItem value="likes">Likes</MenuItem>
                    </Select>
                </FormControl>
            </div>
            <Box>
                <FormControl>
                    <InputLabel id="popular-candidate-select-label">Candidate</InputLabel>
                    <Select
                        labelId="popular-candidate-select-label"
                        id="popular-candidate-simple-select"
                        label="Metric"
                        sx={{ width: 150 }}
                        onChange={(event) => setPopularityCandidate(event.target.value)}
                        defaultValue={popularityCandidate}
                    >
                        <MenuItem value="Trump">Trump</MenuItem>
                        <MenuItem value="Biden">Biden</MenuItem>
                    </Select>
                </FormControl>
                <TextField id="outlined-basic" label="Number of Tweets" onChange={(event) => setPopularTweeetsLimit(event.target.value)} variant="outlined" />
            </Box>
            <Paper sx={{ height: 400, width: '100%' }}>
                <DataGrid
                    rows={popularTweets}
                    getRowId={(row) => row.tweet_id}
                    columns={popularTweetsColumns}
                    initialState={{ pagination: { paginationModel } }}
                    pageSizeOptions={[5, 10, 100]}
                    sx={{ border: 0 }}
                />
                <Download data={popularTweets} filename="most-popular-tweets" />
            </Paper>
            <div style={{ marginTop: "4rem" }}>
                <h3 style={{ display: "inline" }}>Location Insights of Tweets Made About </h3>
                <FormControl>
                    <InputLabel id="location-candidate-select-label">Candidate</InputLabel>
                    <Select
                        labelId="location-candidate-select-label"
                        id="location-candidate-simple-select"
                        label="Candidate"
                        sx={{ width: 150 }}
                        onChange={(event) => setLocationCandidate(event.target.value)}
                        defaultValue={locationCandidate}
                    >
                        <MenuItem value="Trump">Trump</MenuItem>
                        <MenuItem value="Biden">Biden</MenuItem>
                    </Select>
                </FormControl>
            </div>
            <Box>
                <TextField id="outlined-basic" label="Number of Cities" onChange={(event) => setCityLimit(event.target.value)} variant="outlined" />
            </Box>
            <ToggleButtonGroup
                color="primary"
                value={locationInsightsFormat}
                exclusive
                onChange={(event, newFormat) => setLocationInsightsFormat(newFormat)}
                aria-label="Data View"
            >
                <ToggleButton value="chart">Chart</ToggleButton>
                <ToggleButton value="table">Table</ToggleButton>
            </ToggleButtonGroup>
            {locationInsightsFormat === "chart" ? <Bar data={locationInsightsChartData} options={locationInsightsChartOptions} />
                : <Paper sx={{ height: 400, width: '100%' }}>
                    <DataGrid
                        rows={locationInsights}
                        getRowId={(row) => row.city}
                        columns={locationInsightsColumns}
                        initialState={{ pagination: { paginationModel } }}
                        pageSizeOptions={[5, 10, 100]}
                        sx={{ border: 0 }}
                    />
                    <Download data={locationInsights} filename="location-insights" />
                </Paper>}
        </>
    );
}

export default HallOfFame;