import GroupIcon from '@mui/icons-material/Group';
import Link from '@mui/material/Link';

import './Footer.css';

function Footer() {
    return (
        <>
            <footer className='footer'>
                <Link href="https://canvas.upenn.edu/groups/823653/users">
                    <GroupIcon className='icon' />
                </Link>
                <p>Created by Group 26</p>
            </footer>
        </>
    );
}

export default Footer;