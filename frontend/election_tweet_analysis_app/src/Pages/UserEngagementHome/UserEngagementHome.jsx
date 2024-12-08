import AppNavbar from "../../Components/AppNavbar/AppNavbar";
import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';

function UserEngagementHome() {
    return (
        <>
            <AppNavbar />
            <h3 style={{ textAlign: "center" }}>Welcome to our User Analytics Page!</h3>

            <p className='para-text'>Here, you can choose the user metric that you would like to see in more detail.</p>
            <div>
            <ButtonGroup variant="outlined" color="secondary" aria-label="Basic button group" orientation="vertical">
                <Button href='/user-engagement/top-users'>Top Users</Button>
                <Button href='/user-engagement/activity-breakdown'>User Activity Breakdown</Button>
            </ButtonGroup>
            </div>
        </>
    );
}

export default UserEngagementHome;