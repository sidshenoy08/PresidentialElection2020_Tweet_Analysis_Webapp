import AppNavbar from "../../Components/AppNavbar/AppNavbar";
import Grid from "@mui/material/Grid";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import "./UserEngagementHome.css";

import Footer from "../../Components/Footer/Footer";

function UserEngagementHome() {
    return (
        <>
            <AppNavbar />
            <div className="user-engagement-container">
                <Typography variant="h3" className="page-title">
                    Welcome to our User Analytics Page!
                </Typography>
                <Typography variant="body1" className="page-description">
                    Here, you can choose the user metric that you would like to see in more detail.
                </Typography>

                <Grid container spacing={3} justifyContent="center">
                    <Grid item xs={12} sm={6} md={4}>
                        <Paper className="engagement-card" elevation={3}>
                            <Typography variant="h6" className="card-title">
                                Top Users
                            </Typography>
                            <Typography variant="body2" className="card-description">
                                Explore the most active and impactful users during the election period.
                            </Typography>
                            <Button
                                href="/user-engagement/top-users"
                                variant="contained"
                                sx={{ backgroundColor: 'red', '&:hover': { backgroundColor: 'darkred' } }} 
                                className="custom-button red-button"
                            >
                                View Top Users
                            </Button>
                        </Paper>
                    </Grid>
                    <Grid item xs={12} sm={6} md={4}>
                        <Paper className="engagement-card" elevation={3}>
                            <Typography variant="h6" className="card-title">
                                User Activity Breakdown
                            </Typography>
                            <Typography variant="body2" className="card-description">
                                Dive into detailed insights about user activities and trends.
                            </Typography>
                            <Button
                                href="/user-engagement/activity-breakdown"
                                sx={{ backgroundColor: 'blue', '&:hover': { backgroundColor: 'darkblue' } }}
                                variant="contained"
                                className="custom-button blue-button"
                            >
                                View Activity Breakdown
                            </Button>
                        </Paper>
                    </Grid>
                </Grid>
            </div>
            <div style={{ position: "fixed", bottom: "0", width: "100%" }}>
                <Footer />
            </div>
        </>
    );
}

export default UserEngagementHome;
