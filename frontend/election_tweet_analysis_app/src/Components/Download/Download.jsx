import { CSVLink } from "react-csv";
import Button from '@mui/material/Button';

function Download(props) {
    return (
        <>
            <CSVLink data={props.data} filename={props.filename}>
                <Button style={{marginTop: "0.5rem", position: 'absolute'}} variant="contained">Export</Button>
            </CSVLink>
        </>
    );
}

export default Download;