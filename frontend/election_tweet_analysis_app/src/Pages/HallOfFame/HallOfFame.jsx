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
    BarElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
import { TextField } from "@mui/material";
import Fab from '@mui/material/Fab';
import SearchIcon from '@mui/icons-material/Search';
import Box from "@mui/material/Box";

function HallOfFame() {
    const [activeUsers, setActiveUsers] = useState([]);
    const [activeUsersDataFormat, setActiveUsersDataFormat] = useState('chart');

    const [activeUsersLimit, setActiveUsersLimit] = useState();
    const [page, setPage] = useState(0);

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

    const activeUsersChartPaginationModel = { page: 0, pageSize: 5 };

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

    const activeUsersChartOptions = {
        responsive: true,
        plugins: {
            legend: {
                position: "top",
            },
            title: {
                display: true,
                text: "Number of Tweets By Users",
            },
        },
    };

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/homepage/most-active-users`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setActiveUsers(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, []);

    function handleActiveUsersParamsChange() {
        fetch(`http://127.0.0.1:5000/api/homepage/most-active-users?limit=${activeUsersLimit}&page=${page}`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setActiveUsers(data))
            .catch((err) => {
                console.log(err.message);
            });

        activeUsersChartData = {
            labels: activeUsers.map((row) => row.user_name),
            datasets: [
                {
                    label: "Number of Tweets",
                    data: activeUsers.map((row) => row.tweet_count),
                    backgroundColor: "rgba(75, 192, 192, 0.6)"
                }
            ]
        };
    }

    return (
        <>
            <AppNavbar />
            <h3>Most Active Users</h3>
            <Box>
                <TextField id="outlined-basic" label="Number of Users" onChange={(event) => setActiveUsersLimit(event.target.value)} variant="outlined" />
                <TextField id="outlined-basic" label="Page Number" onChange={(event) => setPage(event.target.value)} variant="outlined" />
                <Fab color="primary" aria-label="add" onClick={handleActiveUsersParamsChange}>
                    <SearchIcon />
                </Fab>
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
                        initialState={{ pagination: { activeUsersChartPaginationModel } }}
                        pageSizeOptions={[5, 10, 100]}
                        sx={{ border: 0 }}
                    />
                </Paper>}
        </>
    );
}

export default HallOfFame;