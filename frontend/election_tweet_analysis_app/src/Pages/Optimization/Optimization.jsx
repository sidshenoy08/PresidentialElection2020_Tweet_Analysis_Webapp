import AppNavbar from "../../Components/AppNavbar/AppNavbar";
import { useState, useEffect } from "react";
import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import { DataGrid } from '@mui/x-data-grid';
import Paper from '@mui/material/Paper';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    LineElement,
    Title,
    Tooltip,
    Legend,
    PointElement,
    ArcElement
} from 'chart.js';
import { Pie } from 'react-chartjs-2';
import { TextField } from "@mui/material";
import Box from "@mui/material/Box";
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import FormLabel from '@mui/material/FormLabel';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Download from "../../Components/Download/Download";
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import dayjs from 'dayjs';

function Optimization() {
    const [highVolumeData, setHighVolumeData] = useState([]);
    const [limit, setLimit] = useState();
    const [highVolumeSortMetric, setHighVolumeSortMetric] = useState('date');
    const [highVolumeOrder, setHighVolumeOrder] = useState('desc');

    const [userCandidateData, setUserCandidateData] = useState([]);
    const [userCandidateDataFormat, setUserCandidateDataFormat] = useState('chart');

    const [eventData, setEventData] = useState([]);
    const [eventDates, setEventDates] = useState(['2020-10-15']);

    const [userEngagementData, setUserEngagementData] = useState([]);

    ChartJS.register(
        CategoryScale,
        LinearScale,
        LineElement,
        Title,
        Tooltip,
        Legend,
        PointElement,
        ArcElement
    );

    const highVolumeColumns = [
        { field: 'tweet_date', headerName: 'Tweet Date', width: 250 },
        { field: 'candidate', headerName: 'Candidate', width: 100 },
        { field: 'tweet_count', headerName: 'Number of Tweets', type: 'number', width: 200 },
        { field: 'total_engagement', headerName: 'Total Engagement', type: 'number', width: 200 }
    ];

    const userCandidateColumns = [
        { field: 'user_id', headerName: 'User ID', width: 150 },
        { field: 'user_name', headerName: 'Username', width: 150 },
        { field: 'user_followers_count', headerName: 'Followers', type: 'number', width: 100 },
        { field: 'user_join_date', headerName: 'User Join Date', width: 250 },
        { field: 'most_tweeted_about', headerName: 'Most Tweeted About', width: 150 },
        { field: 'total_likes', headerName: 'Total Likes', type: 'number', width: 100 },
        { field: 'total_retweets', headerName: 'Total Retweets', type: 'number', width: 120 }
    ];

    const eventColumns = [
        { field: 'candidate', headerName: 'Candidate', width: 150 },
        { field: 'event_date', headerName: 'Event Date', width: 150 },
        { field: 'tweet_week', headerName: 'Tweet Week', type: 'number', width: 250 },
        { field: 'event_engagement', headerName: 'Engagement on the Event Day', width: 220 },
        { field: 'event_tweet_count', headerName: 'Number of Tweets on the Event Day', width: 250 },
        { field: 'weekly_engagement', headerName: 'Engagement during the Week', type: 'number', width: 220 },
        { field: 'weekly_tweet_count', headerName: 'Number of Tweets during the Week', type: 'number', width: 250 }
    ];

    const userEngagementColumns = [
        { field: 'candidate', headerName: 'Candidate', width: 150 },
        { field: 'user_id', headerName: 'User ID', width: 200 },
        { field: 'user_name', headerName: 'Username', width: 150 },
        { field: 'total_engagement', headerName: 'Total Engagement', type: 'number', width: 150 },
        { field: 'user_followers_count', headerName: 'Followers', type: 'number', width: 100 },
        { field: 'engagement_to_followers_ratio', headerName: 'Ratio of Total Engagement to Followers', type: 'number', width: 300 },
        { field: 'total_tweets', headerName: 'Number of Tweets', type: 'number', width: 150 }
    ]

    const paginationModel = { page: 0, pageSize: 5 };

    let trumpData = userCandidateData.filter((row) => row.most_tweeted_about === "Trump");
    let bidenData = userCandidateData.filter((row) => row.most_tweeted_about === "Biden");

    const aggregatedData = {
        Trump: {
            totalLikes: trumpData.reduce((sum, row) => sum + row.total_likes, 0),
            totalRetweets: trumpData.reduce((sum, row) => sum + row.total_retweets, 0)
        },
        Biden: {
            totalLikes: bidenData.reduce((sum, row) => sum + row.total_likes, 0),
            totalRetweets: bidenData.reduce((sum, row) => sum + row.total_retweets, 0)
        }
    };

    let userCandidateChartData = {
        labels: ["Trump - Total Likes", "Trump - Total Retweets", "Biden - Total Likes", "Biden - Total Retweets"],
        datasets: [
            {
                label: "Engagement Distribution",
                data: [
                    aggregatedData.Trump.totalLikes,
                    aggregatedData.Trump.totalRetweets,
                    aggregatedData.Biden.totalLikes,
                    aggregatedData.Biden.totalRetweets
                ],
                backgroundColor: [
                    "rgba(255, 99, 132, 0.5)",
                    "rgba(255, 159, 64, 0.5)",
                    "rgba(255, 205, 86, 0.5)",
                    "rgba(54, 162, 235, 0.5)"
                ],
                borderColor: [
                    "rgba(255, 99, 132, 1)",
                    "rgba(255, 159, 64, 1)",
                    "rgba(255, 205, 86, 1)",
                    "rgba(54, 162, 235, 1)"
                ],
                borderWidth: 1
            }
        ]
    };

    const userCandidateChartOptions = {
        responsive: true,
        plugins: {
            legend: { position: "top" },
            tooltip: { mode: "index" },
        },
    };

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/optimization/most-tweeted-about`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setUserCandidateData(data))
            .catch((err) => {
                console.log(err.message);
            });

        fetch(`http://127.0.0.1:5000/api/optimization/user-engagement-with-candidate`, {mode: 'cors'})
            .then((response) => response.json())
            .then((data) => setUserEngagementData(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, []);

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/engagement-trends/high-volume-days?limit=${limit}&sort_by=${highVolumeSortMetric}&order=${highVolumeOrder}`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setHighVolumeData(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, [limit, highVolumeSortMetric, highVolumeOrder]);

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/optimization/weekly-engagement-with-events`, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                event_dates: eventDates
            }),
            mode: 'cors'
        })
            .then((response) => response.json())
            .then((data) => setEventData(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, [eventDates]);

    return (
        <>
            <AppNavbar />
            <h3>Days with High Volume of Tweets</h3>
            <Box>
                <TextField id="outlined-basic" label="Number of Days" onChange={(event) => setLimit(event.target.value)} variant="outlined" />
                <FormControl>
                    <InputLabel id="rollavg-metric-select-label">Sort Metric</InputLabel>
                    <Select
                        labelId="rollavg-metric-select-label"
                        id="rollavg-metric-simple-select"
                        label="Sort Metric"
                        sx={{ width: 150 }}
                        onChange={(event) => setHighVolumeSortMetric(event.target.value)}
                        defaultValue={highVolumeSortMetric}
                    >
                        <MenuItem value="date">Date</MenuItem>
                        <MenuItem value="engagement">Total Engagement</MenuItem>
                    </Select>
                </FormControl>
                <FormControl>
                    <FormLabel id="demo-radio-buttons-group-label">Sorting Order</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        name="radio-buttons-group"
                        defaultValue={highVolumeOrder}
                    >
                        <FormControlLabel value="asc" onChange={(event) => setHighVolumeOrder(event.target.value)} control={<Radio />} label="Ascending" />
                        <FormControlLabel value="desc" onChange={(event) => setHighVolumeOrder(event.target.value)} control={<Radio />} label="Descending" />
                    </RadioGroup>
                </FormControl>
            </Box>
            <Paper sx={{ height: 400, width: '100%' }}>
                <DataGrid
                    rows={highVolumeData}
                    getRowId={(row) => row.tweet_date + row.candidate}
                    columns={highVolumeColumns}
                    initialState={{ pagination: { paginationModel } }}
                    pageSizeOptions={[5, 10, 100]}
                    sx={{ border: 0 }}
                />
                <Download data={highVolumeData} filename="high-volume-days" />
            </Paper>
            <h3>Most Tweeted About Candidate By Users</h3>
            <ToggleButtonGroup
                color="primary"
                value={userCandidateDataFormat}
                exclusive
                onChange={(event, newFormat) => setUserCandidateDataFormat(newFormat)}
                aria-label="Data View"
            >
                <ToggleButton value="chart">Chart</ToggleButton>
                <ToggleButton value="table">Table</ToggleButton>
            </ToggleButtonGroup>
            {userCandidateDataFormat === "chart" ? <Pie data={userCandidateChartData} options={userCandidateChartOptions} />
                : <Paper sx={{ height: 400, width: '100%' }}>
                    <DataGrid
                        rows={userCandidateData}
                        getRowId={(row) => row.user_name}
                        columns={userCandidateColumns}
                        initialState={{ pagination: { paginationModel } }}
                        pageSizeOptions={[5, 10, 100]}
                        sx={{ border: 0 }}
                    />
                    <Download data={userCandidateData} filename="most-tweeted-candidate-by-users" />
                </Paper>}
            <h3>Weekly Engagement with Events</h3>
            <LocalizationProvider dateAdapter={AdapterDayjs}>
                <DatePicker label="Event Date" minDate={dayjs('2020-10-15')} maxDate={dayjs('2020-11-08')} onChange={(newDate) => setEventDates([...eventDates, dayjs(newDate).format('YYYY-MM-DD')])
                } />
            </LocalizationProvider>
            <Paper sx={{ height: 400, width: '100%' }}>
                <DataGrid
                    rows={eventData}
                    getRowId={(row) => row.candidate + row.event_date + row.tweet_week}
                    columns={eventColumns}
                    initialState={{ pagination: { paginationModel } }}
                    pageSizeOptions={[5, 10, 100]}
                    sx={{ border: 0 }}
                />
                <Download data={eventData} filename="weekly-engagement-with-events" />
            </Paper>
            <h3>User Engagement By Candidate</h3>
            <Paper sx={{ height: 400, width: '100%' }}>
                <DataGrid
                    rows={userEngagementData}
                    getRowId={(row) => row.candidate + row.user_id}
                    columns={userEngagementColumns}
                    initialState={{ pagination: { paginationModel } }}
                    pageSizeOptions={[5, 50, 100]}
                    sx={{ border: 0 }}
                />
                <Download data={userEngagementData} filename="user-engagement-by-candidate" />
            </Paper>
        </>
    );
}

export default Optimization;