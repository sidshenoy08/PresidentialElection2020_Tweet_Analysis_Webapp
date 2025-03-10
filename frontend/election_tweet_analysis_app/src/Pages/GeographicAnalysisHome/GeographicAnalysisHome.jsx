import React from "react";
import AppNavbar from "../../Components/AppNavbar/AppNavbar";
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import { Link } from "react-router-dom";
import './GeographicAnalysisHome.css'; // Custom CSS file

import Footer from '../../Components/Footer/Footer';

function GeographicAnalysisHome() {
    return (
        <>
            <AppNavbar />
            <div className="geo-analysis-container">
                <Typography variant="h3" align="center" gutterBottom>
                    Geographic Analytics Page
                </Typography>

                <Typography variant="body1" align="center" paragraph>
                    Explore geographic metrics of tweets related to the 2020 US Presidential Election.
                    Select the desired analysis type to dive deeper into the data.
                </Typography>

                <Grid container spacing={3} justifyContent="center">
                    {/* Card 1 */}
                    <Grid item xs={12} sm={6} md={4}>
                        <Paper className="geo-card" elevation={3}>
                            <Typography variant="h6" align="center">
                                Country/City Analysis
                            </Typography>
                            <Typography variant="body2" align="center" paragraph>
                                Analyze tweets based on the country and city from which they were posted.
                            </Typography>
                            <Link to='/geographic-analysis/country-city-analysis'>
                                <Button
                                    variant="contained"
                                    sx={{ backgroundColor: 'red', '&:hover': { backgroundColor: 'darkred' } }}
                                    // href="/geographic-analysis/country-city-analysis"
                                    fullWidth
                                >
                                    Explore
                                </Button>
                            </Link>
                        </Paper>
                    </Grid>

                    {/* Card 2 */}
                    <Grid item xs={12} sm={6} md={4}>
                        <Paper className="geo-card" elevation={3}>
                            <Typography variant="h6" align="center">
                                Region/Timezone Analysis
                            </Typography>
                            <Typography variant="body2" align="center" paragraph>
                                Discover insights by analyzing tweets based on regions and timezones.
                            </Typography>
                            <Link to="/geographic-analysis/region-timezone-analysis">
                                <Button
                                    variant="contained"
                                    sx={{ backgroundColor: 'blue', '&:hover': { backgroundColor: 'darkblue' } }}
                                    // href="/geographic-analysis/region-timezone-analysis"
                                    fullWidth
                                >
                                    Explore
                                </Button>
                            </Link>
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

export default GeographicAnalysisHome;
