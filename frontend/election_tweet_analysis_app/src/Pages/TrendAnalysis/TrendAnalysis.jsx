import AppNavbar from "../../Components/AppNavbar/AppNavbar";
import Download from "../../Components/Download/Download";
import Footer from "../../Components/Footer/Footer";

import './TrendAnalysis.css';

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
    PointElement
} from 'chart.js';
import { Line } from 'react-chartjs-2';
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

const config = require("../../config.json");

function TrendAnalysis() {
    const [rollavgData, setRollavgData] = useState([]);
    const [rollavgCandidate, setRollavgCandidate] = useState('Trump');
    const [window, setWindow] = useState();
    const [rollavgSortMetric, setRollavgSortMetric] = useState('date');
    const [rollavgOrder, setRollavgOrder] = useState('desc');
    const [rollavgDataFormat, setRollAvgDataFormat] = useState('chart');

    const [spikeData, setSpikeData] = useState([]);
    const [spikeCandidate, setSpikeCandidate] = useState('Trump');
    const [threshold, setThreshold] = useState();
    const [spikeSortMetric, setSpikeSortMetric] = useState('date');
    const [spikeOrder, setSpikeOrder] = useState('desc');
    const [spikeDataFormat, setSpikeDataFormat] = useState('chart');

    ChartJS.register(
        CategoryScale,
        LinearScale,
        LineElement,
        Title,
        Tooltip,
        Legend,
        PointElement
    );

    const rollavgColumns = [
        { field: 'date', headerName: 'Date', width: 250 },
        { field: 'engagement', headerName: 'Engagement', type: 'number', width: 100 },
        { field: 'rolling_avg', headerName: 'Rolling Average', type: 'number', width: 150 }
    ];

    const spikeColumns = [
        { field: 'date', headerName: 'Date', width: 250 },
        { field: 'engagement', headerName: 'Total Engagement', type: 'number', width: 200 }
    ];

    const paginationModel = { page: 0, pageSize: 5 };

    let rollavgChartData = {
        labels: rollavgData.map((row) => row.date.substring(0, row.date.indexOf(" 00:00:00"))),
        datasets: [
            {
                label: "Total Engagement",
                data: rollavgData.map((row) => row.engagement),
                borderColor: "rgba(75, 192, 192, 1)",
                backgroundColor: "rgba(75, 192, 192)",
                borderWidth: 2,
                tension: 0.4
            },
            {
                label: "Rolling Average",
                data: rollavgData.map((row) => row.rolling_avg),
                borderColor: "rgba(153, 102, 255)",
                backgroundColor: "rgba(153, 102, 255)",
                borderWidth: 2,
                tension: 0.4,
                borderDash: [5, 5]
            }
        ]
    };

    let spikeChartData = {
        labels: spikeData.map((row) => row.date.substring(0, row.date.indexOf(" 00:00:00"))),
        datasets: [
            {
                label: "Total Engagement",
                data: spikeData.map((row) => row.engagement),
                borderColor: "rgba(75, 192, 192)",
                backgroundColor: "rgba(75, 192, 192)"
            }
        ]
    };

    const rollavgChartOptions = {
        responsive: true,
        plugins: {
            legend: {
                position: "top",
            },
            title: {
                display: true,
                text: "Engagement over Time: Total vs Rolling Average",
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: "Day"
                },
            },
            y: {
                title: {
                    display: true,
                    text: "Engagement"
                }
            }
        }
    };

    const spikeChartOptions = {
        responsive: true,
        plugins: {
            legend: {
                position: "top",
            },
            title: {
                display: true,
                text: "Spikes in Engagement over Time",
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: "Day"
                },
            },
            y: {
                title: {
                    display: true,
                    text: "Total Engagement"
                }
            }
        }
    };

    useEffect(() => {
        fetch(`${config.api_url}/engagement-trends/rolling-average?candidate=${rollavgCandidate}&window=${window}&sort_by=${rollavgSortMetric}&order=${rollavgOrder}`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setRollavgData(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, [rollavgCandidate, window, rollavgSortMetric, rollavgOrder]);

    useEffect(() => {
        fetch(`${config.api_url}/engagement-trends/spikes?candidate=${spikeCandidate}&threshold=${threshold}&sort_by=${spikeSortMetric}&order=${spikeOrder}`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setSpikeData(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, [spikeCandidate, threshold, spikeSortMetric, spikeOrder]);

    return (
        <div className="body">
            <AppNavbar />
            <h3>Rolling Average By Day</h3>
            <Box className="query-params">
                <FormControl style={{ marginLeft: "2rem" }}>
                    <InputLabel id="rollavg-candidate-select-label">Candidate</InputLabel>
                    <Select
                        labelId="rollavg-candidate-select-label"
                        id="rollavg-candidate-simple-select"
                        label="Candidate"
                        sx={{ width: 150 }}
                        onChange={(event) => setRollavgCandidate(event.target.value)}
                        defaultValue={rollavgCandidate}
                    >
                        <MenuItem value="Trump">Trump</MenuItem>
                        <MenuItem value="Biden">Biden</MenuItem>
                    </Select>
                </FormControl>
                <TextField id="outlined-basic" label="Window" style={{ marginLeft: "2rem" }} onChange={(event) => setWindow(event.target.value)} variant="outlined" />
                <FormControl style={{ marginLeft: "2rem" }}>
                    <InputLabel id="rollavg-metric-select-label">Sort Metric</InputLabel>
                    <Select
                        labelId="rollavg-metric-select-label"
                        id="rollavg-metric-simple-select"
                        label="Sort Metric"
                        sx={{ width: 150 }}
                        onChange={(event) => setRollavgSortMetric(event.target.value)}
                        defaultValue={rollavgSortMetric}
                    >
                        <MenuItem value="date">Date</MenuItem>
                        <MenuItem value="engagement">Total Engagement</MenuItem>
                        <MenuItem value="rolling_avg">Rolling Average</MenuItem>
                    </Select>
                </FormControl>
                <FormControl style={{ marginLeft: "2rem" }}>
                    <FormLabel id="demo-radio-buttons-group-label">Sorting Order</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        name="radio-buttons-group"
                        defaultValue={rollavgOrder}
                    >
                        <FormControlLabel value="asc" onChange={(event) => setRollavgOrder(event.target.value)} control={<Radio />} label="Ascending" />
                        <FormControlLabel value="desc" onChange={(event) => setRollavgOrder(event.target.value)} control={<Radio />} label="Descending" />
                    </RadioGroup>
                </FormControl>
            </Box>
            <ToggleButtonGroup
                color="primary"
                value={rollavgDataFormat}
                exclusive
                onChange={(event, newFormat) => setRollAvgDataFormat(newFormat)}
                aria-label="Data View"
                style={{ marginLeft: "2rem", marginBottom: "1rem" }}
            >
                <ToggleButton value="chart">Chart</ToggleButton>
                <ToggleButton value="table">Table</ToggleButton>
            </ToggleButtonGroup>
            <div className="data">
                {rollavgDataFormat === "chart" ? <Line data={rollavgChartData} options={rollavgChartOptions} />
                    : <Paper sx={{ height: 400, width: '40%', marginLeft: 'auto', marginRight: 'auto' }}>
                        <DataGrid
                            rows={rollavgData}
                            getRowId={(row) => row.date}
                            columns={rollavgColumns}
                            initialState={{ pagination: { paginationModel } }}
                            pageSizeOptions={[5, 10, 100]}
                            sx={{ border: 0 }}
                        />
                        <Download data={rollavgData} filename="rolling-average-by-day" />
                    </Paper>}
            </div>
            <h3>Spikes in Total Engagment</h3>
            <Box className='query-params'>
                <FormControl style={{ marginLeft: "2rem" }}>
                    <InputLabel id="spike-candidate-select-label">Candidate</InputLabel>
                    <Select
                        labelId="spike-candidate-select-label"
                        id="spike-candidate-simple-select"
                        label="Candidate"
                        sx={{ width: 150 }}
                        onChange={(event) => setSpikeCandidate(event.target.value)}
                        defaultValue={spikeCandidate}
                    >
                        <MenuItem value="Trump">Trump</MenuItem>
                        <MenuItem value="Biden">Biden</MenuItem>
                    </Select>
                </FormControl>
                <TextField id="outlined-basic" label="Threshold" style={{ marginLeft: "2rem" }} onChange={(event) => setThreshold(event.target.value)} variant="outlined" />
                <FormControl style={{ marginLeft: "2rem" }}>
                    <InputLabel id="spike-metric-select-label">Sort Metric</InputLabel>
                    <Select
                        labelId="spike-metric-select-label"
                        id="spike-metric-simple-select"
                        label="Sort Metric"
                        sx={{ width: 150 }}
                        onChange={(event) => setSpikeSortMetric(event.target.value)}
                        defaultValue={spikeSortMetric}
                    >
                        <MenuItem value="date">Date</MenuItem>
                        <MenuItem value="engagement">Total Engagement</MenuItem>
                    </Select>
                </FormControl>
                <FormControl style={{ marginLeft: "2rem" }}>
                    <FormLabel id="demo-radio-buttons-group-label">Sorting Order</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        name="radio-buttons-group"
                        defaultValue={spikeOrder}
                    >
                        <FormControlLabel value="asc" onChange={(event) => setSpikeOrder(event.target.value)} control={<Radio />} label="Ascending" />
                        <FormControlLabel value="desc" onChange={(event) => setSpikeOrder(event.target.value)} control={<Radio />} label="Descending" />
                    </RadioGroup>
                </FormControl>
            </Box>
            <ToggleButtonGroup
                color="primary"
                value={spikeDataFormat}
                exclusive
                onChange={(event, newFormat) => setSpikeDataFormat(newFormat)}
                aria-label="Data View"
                style={{ marginLeft: "2rem", marginBottom: "1rem" }}
            >
                <ToggleButton value="chart">Chart</ToggleButton>
                <ToggleButton value="table">Table</ToggleButton>
            </ToggleButtonGroup>
            <div className="data">
                {spikeDataFormat === "chart" ? <Line data={spikeChartData} options={spikeChartOptions} />
                    : <Paper sx={{ height: 400, width: '30%', marginLeft: 'auto', marginRight: 'auto' }}>
                        <DataGrid
                            rows={spikeData}
                            getRowId={(row) => row.date}
                            columns={spikeColumns}
                            initialState={{ pagination: { paginationModel } }}
                            pageSizeOptions={[5, 10, 100]}
                            sx={{ border: 0 }}
                        />
                        <Download data={spikeData} filename="spikes-in-total-engagement" />
                    </Paper>}
            </div>
            <Footer />
        </div>
    );
}

export default TrendAnalysis;