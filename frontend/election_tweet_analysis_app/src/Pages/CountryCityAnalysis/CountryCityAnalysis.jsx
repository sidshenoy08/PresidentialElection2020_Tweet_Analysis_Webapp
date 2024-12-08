import { useEffect, useState } from "react";
import AppNavbar from "../../Components/AppNavbar/AppNavbar";

import { Chart } from 'react-google-charts';
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

function CountryCityAnalysis() {
    const [geoChartData, setGeoChartData] = useState([]);
    const [geoChartDataFormat, setGeoChartDataFormat] = useState('map');

    const [groupedBarChartData, setGroupedBarChartData] = useState([]);
    const [groupedBarChartDataFormat, setGroupedBarChartDataFormat] = useState('chart');
    
    const [cityLimit, setCityLimit] = useState();
    const [sortMetric, setSortMetric] = useState();
    const [order, setOrder] = useState();

    ChartJS.register(
        CategoryScale,
        LinearScale,
        BarElement,
        Title,
        Tooltip,
        Legend
    );

    const geoChartColumns = [
        { field: 'country', headerName: 'Country', width: 250 },
        { field: 'tweet_count', headerName: 'Number of Tweets', type: 'number', width: 350 },
    ];

    const groupedBarChartColumns = [
        { field: 'city', headerName: 'City', width: 250 },
        { field: 'tweet_count', headerName: 'Number of Tweets', type: 'number', width: 350 },
        { field: 'retweets', headerName: 'Number of Retweets', type: 'number', width: 350 },
        { field: 'likes', headerName: 'Number of Likes', type: 'number', width: 350 }
    ];

    const geoChartPaginationModel = { page: 0, pageSize: 25 };
    const groupedBarChartPaginationModel = { page: 0, pageSize: 5 };

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/geographic-analysis/most-tweets-by-country`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setGeoChartData(data))
            .catch((err) => {
                console.log(err.message);
            });

        fetch(`http://127.0.0.1:5000/api/geographic-analysis/city-level-analysis`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setGroupedBarChartData(data))
            .catch((err) => {
                console.log(err.message);
            })
    }, []);

    const finalGeoChartData = [
        ["Country", "Number of Tweets"],
        ...geoChartData.map((row) => [handleCountryNames(row.country), row.tweet_count])
    ];

    const geoChartOptions = {
        colorAxis: { minValue: 1, maxValue: 172473, colors: ["#00FFFF", "#FF00FF"] },
        backgroundColor: "#f5f5f5",
        datalessRegionColor: "#cccccc",
        defaultColor: "#f5f5f5",
    };

    let groupedBarChart = {
        labels: groupedBarChartData.map((row) => row.city),
        datasets: [
            {
                label: "Number of Tweets",
                data: groupedBarChartData.map((row) => row.tweet_count),
                backgroundColor: "rgba(75, 192, 192, 0.6)"
            },
            {
                label: "Number of Retweets",
                data: groupedBarChartData.map((row) => row.retweets),
                backgroundColor: "rgba(153, 102, 255, 0.6)"
            },
            {
                label: "Number of Likes",
                data: groupedBarChartData.map((row) => row.likes),
                backgroundColor: "rgba(255, 159, 64, 0.6)"
            }
        ]
    };

    const groupedBarChartOptions = {
        responsive: true,
        plugins: {
            legend: {
                position: "top",
            },
            title: {
                display: true,
                text: "Number of Tweets, Likes, and Retweets by City",
            },
        },
    };

    function handleCountryNames(country) {
        if (country === "United States of America") {
            return "United States";
        } else if (country === "The Netherlands") {
            return "Netherlands";
        } else {
            return country;
        }
    }

    function handleGeoFormatChange(event, newFormat) {
        setGeoChartDataFormat(newFormat);
    }

    function handleCityLimitChange(event) {
        setCityLimit(event.target.value);
    }

    function handleSortMetricChange(event) {
        setSortMetric(event.target.value);
    }

    function handleOrderChange(event) {
        setOrder(event.target.value);
    }

    function handleGroupedFormatChange(event, newFormat) {
        setGroupedBarChartDataFormat(newFormat);
    }

    function handleCityParamsChange() {
        fetch(`http://127.0.0.1:5000/api/geographic-analysis/city-level-analysis?limit=${cityLimit}&sort_by=${sortMetric}&order=${order}`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setGroupedBarChartData(data))
            .catch((err) => {
                console.log(err.message);
            });

        groupedBarChart = {
            labels: groupedBarChartData.map((row) => row.city),
            datasets: [
                {
                    label: "Number of Tweets",
                    data: groupedBarChartData.map((row) => row.tweet_count),
                    backgroundColor: "rgba(75, 192, 192)"
                },
                {
                    label: "Number of Retweets",
                    data: groupedBarChartData.map((row) => row.retweets),
                    backgroundColor: "rgba(153, 102, 255)"
                },
                {
                    label: "Number of Likes",
                    data: groupedBarChartData.map((row) => row.likes),
                    backgroundColor: "rgba(255, 159, 64)"
                }
            ]
        };
    }

    return (
        <>
            <AppNavbar />
            <div>
                <h3>Number of Tweets By Country</h3>
                <ToggleButtonGroup
                    color="primary"
                    value={geoChartDataFormat}
                    exclusive
                    onChange={handleGeoFormatChange}
                    aria-label="Data View"
                >
                    <ToggleButton value="map">Map</ToggleButton>
                    <ToggleButton value="table">Table</ToggleButton>
                </ToggleButtonGroup>
                {geoChartDataFormat === "map" ? <Chart
                    chartType="GeoChart"
                    data={finalGeoChartData}
                    options={geoChartOptions}
                    width="100%"
                    height="500px"
                /> : <Paper sx={{ height: 400, width: '100%' }}>
                    <DataGrid
                        rows={geoChartData}
                        getRowId={(row) => row.country}
                        columns={geoChartColumns}
                        initialState={{ pagination: { geoChartPaginationModel } }}
                        pageSizeOptions={[25, 50, 100]}
                        sx={{ border: 0 }}
                    />
                </Paper>}
            </div>
            <Box>
                <TextField id="outlined-basic" label="Number of Cities" onChange={handleCityLimitChange} variant="outlined" />
                <FormControl>
                    <InputLabel id="demo-simple-select-label">Sort By Metric</InputLabel>
                    <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        label="Metric"
                        sx={{ width: 150 }}
                        onChange={handleSortMetricChange}
                    >
                        <MenuItem value="city">City</MenuItem>
                        <MenuItem value="tweet_count">Number of Tweets</MenuItem>
                        <MenuItem value="retweets">Number of Retweets</MenuItem>
                        <MenuItem value="likes">Number of Likes</MenuItem>
                    </Select>
                </FormControl>
                <FormControl>
                    <FormLabel id="demo-radio-buttons-group-label">Sorting Order</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        name="radio-buttons-group"
                    >
                        <FormControlLabel value="asc" onChange={handleOrderChange} control={<Radio />} label="Ascending" />
                        <FormControlLabel value="desc" onChange={handleOrderChange} control={<Radio />} label="Descending" />
                    </RadioGroup>
                </FormControl>
                <Fab color="primary" aria-label="add" onClick={handleCityParamsChange}>
                    <SearchIcon />
                </Fab>
            </Box>
            <ToggleButtonGroup
                color="primary"
                value={groupedBarChartDataFormat}
                exclusive
                onChange={handleGroupedFormatChange}
                aria-label="Data View"
            >
                <ToggleButton value="chart">Chart</ToggleButton>
                <ToggleButton value="table">Table</ToggleButton>
            </ToggleButtonGroup>
            {groupedBarChartDataFormat === "chart" ? <Bar data={groupedBarChart} options={groupedBarChartOptions} />
                : <Paper sx={{ height: 400, width: '100%' }}>
                    <DataGrid
                        rows={groupedBarChartData}
                        getRowId={(row) => row.city}
                        columns={groupedBarChartColumns}
                        initialState={{ pagination: { groupedBarChartPaginationModel } }}
                        pageSizeOptions={[5, 10]}
                        sx={{ border: 0 }}
                    />
                </Paper>}
        </>
    );
}

export default CountryCityAnalysis;