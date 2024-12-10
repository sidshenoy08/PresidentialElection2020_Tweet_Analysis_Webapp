import AppNavbar from "../../Components/AppNavbar/AppNavbar";

import { useState, useEffect } from 'react';
import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import { Bar } from "react-chartjs-2";
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
    PointElement,
    LineElement
} from "chart.js";
import { DataGrid } from '@mui/x-data-grid';
import Paper from '@mui/material/Paper';


function SentimentAnalysis() {

    const [trumpData, setTrumpData] = useState([]);
    const [trumpDataFormat, setTrumpDataFormat] = useState('chart');

    const [bidenData, setBidenData] = useState([]);
    const [bidenDataFormat, setBidenDataFormat] = useState('chart');

    ChartJS.register(
        CategoryScale,
        LinearScale,
        BarElement,
        Title,
        Tooltip,
        Legend,
        PointElement,
        LineElement
    );

    const tableColumns = [
        { field: 'week_start', headerName: 'Week Start', width: 250 },
        { field: 'positive', headerName: 'Positive Tweets', type: 'number', width: 100 },
        { field: 'negative', headerName: 'Negative Tweets', type: 'number', width: 100 },
        { field: 'neutral', headerName: 'Neutral Tweets', type: 'number', width: 100 },
        { field: 'tweet_count', headerName: 'Total Tweets', type: 'number', width: 100 }
    ];

    let trumpChartData = {
        labels: trumpData.map((row) => row.week_start),
        datasets: [
            {
                label: "Positive",
                data: trumpData.map((row) => row.positive),
                backgroundColor: "rgba(75, 192, 192, 0.6)"
            },
            {
                label: "Neutral",
                data: trumpData.map((row) => row.neutral),
                backgroundColor: "rgba(153, 102, 255, 0.6)"
            },
            {
                label: "Negative",
                data: trumpData.map((row) => row.negative),
                backgroundColor: "rgba(255, 99, 132, 0.6)"
            }
        ]
    };

    let bidenChartData = {
        labels: bidenData.map((row) => row.week_start),
        datasets: [
            {
                label: "Positive",
                data: bidenData.map((row) => row.positive),
                backgroundColor: "rgba(75, 192, 192, 0.6)"
            },
            {
                label: "Neutral",
                data: bidenData.map((row) => row.neutral),
                backgroundColor: "rgba(153, 102, 255, 0.6)"
            },
            {
                label: "Negative",
                data: bidenData.map((row) => row.negative),
                backgroundColor: "rgba(255, 99, 132, 0.6)"
            }
        ]
    }

    const chartOptions = {
        responsive: true,
        plugins: {
            legend: {
                position: "top",
            },
            title: {
                display: true,
                text: "Weekly Tweet Sentiment Analysis",
            },
        },
        scales: {
            x: {
                stacked: true
            },
            y: {
                stacked: true,
                beginAtZero: true
            }
        }
    };

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/engagement-trends/weekly-sentiment?candidate=Trump`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setTrumpData(data))
            .catch((err) => {
                console.log(err.message);
            });

        fetch(`http://127.0.0.1:5000/api/engagement-trends/weekly-sentiment?candidate=Biden`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setBidenData(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, []);

    return (
        <>
            <AppNavbar />
            <h3>Analysis of Tweets made about Trump</h3>
            <ToggleButtonGroup
                color="primary"
                value={trumpDataFormat}
                exclusive
                onChange={(event, newFormat) => setTrumpDataFormat(newFormat)}
                aria-label="Data View"
            >
                <ToggleButton value="chart">Chart</ToggleButton>
                <ToggleButton value="table">Table</ToggleButton>
            </ToggleButtonGroup>
            {trumpDataFormat === "chart" ? <Bar data={trumpChartData} options={chartOptions} />
                : <Paper sx={{ height: 400, width: '100%' }}>
                    <DataGrid
                        rows={trumpData}
                        getRowId={(row) => row.week_start}
                        columns={tableColumns}
                        sx={{ border: 0 }}
                    />
                </Paper>}
            <h3>Analysis of Tweets made about Biden</h3>
            <ToggleButtonGroup
                color="primary"
                value={bidenDataFormat}
                exclusive
                onChange={(event, newFormat) => setBidenDataFormat(newFormat)}
                aria-label="Data View"
            >
                <ToggleButton value="chart">Chart</ToggleButton>
                <ToggleButton value="table">Table</ToggleButton>
            </ToggleButtonGroup>
            {bidenDataFormat === "chart" ? <Bar data={bidenChartData} options={chartOptions} />
                : <Paper sx={{ height: 400, width: '100%' }}>
                    <DataGrid
                        rows={bidenData}
                        getRowId={(row) => row.week_start}
                        columns={tableColumns}
                        sx={{ border: 0 }}
                    />
                </Paper>}
        </>
    );
}

export default SentimentAnalysis;