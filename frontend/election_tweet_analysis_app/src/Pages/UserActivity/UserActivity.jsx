import AppNavbar from "../../Components/AppNavbar/AppNavbar";
import Download from "../../Components/Download/Download";

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

function UserActivity() {
    const [userActivity, setUserActivity] = useState([]);
    const [activityCandidate, setActivityCandidate] = useState('Trump');
    const [activityLimit, setActivityLimit] = useState();
    const [order, setOrder] = useState('desc');

    const [influentialUsers, setInfluentialUsers] = useState([]);
    const [influenceCandidate, setInfluenceCandidate] = useState('Trump');
    const [influenceLimit, setInfluenceLimit] = useState();

    const paginationModel = { page: 0, pageSize: 5 };

    // const backgroundStyle = {
    //     Trump: {
    //         backgroundColor: '#FF0000'
    //     },
    //     Biden: {
    //         backgroundColor: '#0015BC'
    //     }
    // };

    const activityColumns = [
        { field: 'user_id', headerName: 'User ID', width: 150 },
        { field: 'user_name', headerName: 'Username', width: 150 },
        { field: 'user_screen_name', headerName: 'User Screen Name', width: 150 },
        { field: 'tweet_count', headerName: 'Number of Tweets', type: 'number', width: 250 },
        { field: 'total_engagement', headerName: 'Total Engagement', type: 'number', width: 250 }
    ];

    const influenceColumns = [
        { field: 'user_id', headerName: 'User ID', width: 150 },
        { field: 'user_name', headerName: 'Username', width: 150 },
        { field: 'user_followers_count', headerName: 'Follower Count', type: 'number', width: 250 },
        { field: 'engagement_ratio', headerName: 'Engagement to Followers Ratio', type: 'number', width: 250 }
    ];

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/user-engagement/activity-breakdown?candidate=${activityCandidate}&limit=${activityLimit}&order=${order}`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setUserActivity(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, [activityCandidate, activityLimit, order]);

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/user-engagement/influential-users?candidate=${influenceCandidate}&limit=${influenceLimit}`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setInfluentialUsers(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, [influenceCandidate, influenceLimit])

    return (
        <>
            <AppNavbar />
            <h3>User Activity Breakdown</h3>
            <Box>
                <FormControl>
                    <InputLabel id="demo-simple-select-label">Candidate</InputLabel>
                    <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        label="Candidate"
                        sx={{ width: 150 }}
                        value={activityCandidate}
                        onChange={(event) => setActivityCandidate(event.target.value)}
                    >
                        <MenuItem value="Trump">Trump</MenuItem>
                        <MenuItem value="Biden">Biden</MenuItem>
                    </Select>
                </FormControl>
                <TextField id="outlined-basic" label="Number of Users" onChange={(event) => setActivityLimit(event.target.value)} variant="outlined" />
                <FormControl>
                    <FormLabel id="demo-radio-buttons-group-label">Sorting Order</FormLabel>
                    <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        name="radio-buttons-group"
                        defaultValue={order}
                    >
                        <FormControlLabel value="asc" onChange={(event) => setOrder(event.target.value)} control={<Radio />} label="Ascending" />
                        <FormControlLabel value="desc" onChange={(event) => setOrder(event.target.value)} control={<Radio />} label="Descending" />
                    </RadioGroup>
                </FormControl>
            </Box>
            <Paper sx={{ height: 400 }}>
                <DataGrid
                    rows={userActivity}
                    getRowId={(row) => row.user_id}
                    columns={activityColumns}
                    initialState={{ pagination: { paginationModel } }}
                    pageSizeOptions={[5, 10]}
                />
                <Download data={userActivity} filename="user-activity-breakdown" />
            </Paper>
            <h3>Influential Users</h3>
            <Box>
                <FormControl>
                    <InputLabel id="demo-simple-select-label">Candidate</InputLabel>
                    <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        label="Candidate"
                        sx={{ width: 150 }}
                        value={influenceCandidate}
                        onChange={(event) => setInfluenceCandidate(event.target.value)}
                    >
                        <MenuItem value="Trump">Trump</MenuItem>
                        <MenuItem value="Biden">Biden</MenuItem>
                    </Select>
                </FormControl>
                <TextField id="outlined-basic" label="Number of Users" onChange={(event) => setInfluenceLimit(event.target.value)} variant="outlined" />
            </Box>
            <Paper sx={{ height: 400 }}>
                <DataGrid
                    rows={influentialUsers}
                    getRowId={(row) => row.user_id}
                    columns={influenceColumns}
                    initialState={{ pagination: { paginationModel } }}
                    pageSizeOptions={[5, 10, 100]}
                />
                <Download data={influentialUsers} filename="influential-users" />
            </Paper>
        </>
    );
}

export default UserActivity;