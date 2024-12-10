import { CSVLink } from "react-csv";
import Button from '@mui/material/Button';

function Download(props) {
    return (
        <>
            <CSVLink data={props.data} filename={props.filename}>
                <Button variant="outlined">Download</Button>
            </CSVLink>
        </>
    );
}

export default Download;