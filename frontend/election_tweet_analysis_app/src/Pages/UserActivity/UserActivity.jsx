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

function UserActivity() {
    const [users, setUsers] = useState([]);
    const [candidate, setCandidate] = useState('Trump');
    const [limit, setLimit] = useState();
    const [order, setOrder] = useState();

    const paginationModel = { page: 0, pageSize: 5 };

    const backgroundStyle = {
        Trump: {
            backgroundColor: '#FF0000'
        },
        Biden: {
            backgroundColor: '#0015BC'
        }
    };

    const columns = [
        { field: 'user_id', headerName: 'User ID', width: 150 },
        { field: 'user_name', headerName: 'Username', width: 150 },
        { field: 'user_screen_name', headerName: 'User Screen Name', width: 150 },
        { field: 'tweet_count', headerName: 'Number of Tweets', type: 'number', width: 250 },
        { field: 'total_engagement', headerName: 'Total Engagement', type: 'number', width: 250 }
    ];

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/user-engagement/activity-breakdown`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setUsers(data))
            .catch((err) => {
                console.log(err.message);
            });
    }, []);

    function handleCandidateChange(event) {
        setCandidate(event.target.value);
    }

    function handleLimitChange(event) {
        setLimit(event.target.value);
    }

    function handleOrderChange(event) {
        setOrder(event.target.value);
    }

    function handleParamChange() {
        fetch(`http://127.0.0.1:5000/api/user-engagement/activity-breakdown?candidate=${candidate}&limit=${limit}&order=${order}`, { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => setUsers(data))
            .catch((err) => {
                console.log(err.message);
            });
    }

    return (
        <>

            <AppNavbar />
            <div style={backgroundStyle[candidate]}>
                <Box>
                    <FormControl>
                        <InputLabel id="demo-simple-select-label">Candidate</InputLabel>
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            label="Candidate"
                            sx={{ width: 150 }}
                            value={candidate}
                            onChange={handleCandidateChange}
                        >
                            <MenuItem value="Trump">Trump</MenuItem>
                            <MenuItem value="Biden">Biden</MenuItem>
                        </Select>
                    </FormControl>

                    <TextField id="outlined-basic" label="Number of Users" onChange={handleLimitChange} variant="outlined" />
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
                </Box>
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
            </div>
        </>
    );
}

export default UserActivity;