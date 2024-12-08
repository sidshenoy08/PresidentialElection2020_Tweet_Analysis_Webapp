import AppNavbar from "../../Components/AppNavbar/AppNavbar";
import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';

function GeographicAnalysisHome() {
    return (
        <>
            <AppNavbar />
            <h3 style={{ textAlign: "center" }}>Welcome to our Geographic Analytics Page!</h3>

            <p className='para-text'>Here, you can choose the geographic metric that you would like to see in more detail.</p>
            <div>
            <ButtonGroup variant="outlined" color="secondary" aria-label="Basic button group" orientation="vertical">
                <Button href='/geographic-analysis/country-city-analysis'>Country/City Tweet Analysis</Button>
                <Button href='/geographic-analysis/region-timezone-analysis'>Region/Timezone Tweet Analysis</Button>
            </ButtonGroup>
            </div>
        </>
    );
}

export default GeographicAnalysisHome;