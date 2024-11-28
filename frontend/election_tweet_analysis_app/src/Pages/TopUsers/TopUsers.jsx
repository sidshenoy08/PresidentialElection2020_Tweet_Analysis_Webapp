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
import { useState, useEffect } from "react";

function TopUsers() {
    const [users, setUsers] = useState([]);
    const [limit, setLimit] = useState();
    const [order, setOrder] = useState();

    const columns = [
        { field: 'user_id', headerName: 'User ID', width: 150 },
        { field: 'user_name', headerName: 'Username', width: 150 },
        { field: 'user_screen_name', headerName: 'User Screen Name', width: 150 },
        { field: 'total_engagement', headerName: 'Total Engagement', type: 'number', width: 250 },
        { field: 'followers', headerName: 'Follower Count', type: 'number', width: 250 },
        { field: 'engagement_to_followers_ratio', headerName: 'Engagement to Followers Ratio', type: 'number', width: 250 }
    ];

    const paginationModel = { page: 0, pageSize: 5 };

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/user-engagement/top-users`, { mode: 'cors' })
        .then((response) => response.json())
        .then((data) => setUsers(data))
        .catch((err) => {
            console.log(err.message);
        });
    }, []);

    function handleLimitChange(event) {
        setLimit(event.target.value);
    }

    function handleOrderChange(event) {
        setOrder(event.target.value);
    }

    function handleParamChange(event) {
        fetchTopUsers();
    }

    function fetchTopUsers() {
        fetch(`http://127.0.0.1:5000/api/user-engagement/top-users?limit=${limit}&order=${order}`, { mode: 'cors' })
        .then((response) => response.json())
        .then((data) => setUsers(data))
        .catch((err) => {
            console.log(err.message);
        });
    }

    return (
        <>
            <AppNavbar />
            <TextField id="outlined-basic" label="Number of Top Users" onChange={handleLimitChange} variant="outlined" />
            <FormControl>
                <FormLabel id="demo-radio-buttons-group-label">Sorting Order</FormLabel>
                <RadioGroup
                    aria-labelledby="demo-radio-buttons-group-label"
                    defaultValue="female"
                    name="radio-buttons-group"
                >
                    <FormControlLabel value="asc" onChange={handleOrderChange} control={<Radio />} label="Ascending" />
                    <FormControlLabel value="desc" onChange={handleOrderChange} control={<Radio />} label="Descending" />
                </RadioGroup>
            </FormControl>
            <Fab color="primary" aria-label="add" onClick={handleParamChange}>
                <SearchIcon />
            </Fab>
            <Paper sx={{ height: 400, width: '100%' }}>
                <DataGrid
                    rows={users}
                    getRowId={(row) => row.user_id}
                    columns={columns}
                    initialState={{ pagination: { paginationModel } }}
                    pageSizeOptions={[5, 10]}
                    sx={{ border: 0 }}
                />
            </Paper>
        </>
    );
}

export default TopUsers;