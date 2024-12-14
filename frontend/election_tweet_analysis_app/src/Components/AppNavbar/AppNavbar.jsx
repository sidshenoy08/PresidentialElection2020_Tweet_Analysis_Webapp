import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom';
import NavDropdown from 'react-bootstrap/NavDropdown';

import './AppNavbar.css';

function AppNavbar() {
    return (
        <>
            <Navbar sticky="top" expand="lg" bg="dark" data-bs-theme="dark">
                <Container>
                    <Navbar.Brand as={Link} to= '/'>
                        <img
                            src="./logo.png"
                            width="30"
                            height="30"
                            className="d-inline-block align-top"
                            alt="React Bootstrap logo"
                        />
                    </Navbar.Brand>
                    <Navbar.Brand as={Link} to='/'>PollPulse</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className='ms-auto'>
                            <Nav.Link as={Link} to='/'>Home</Nav.Link>
                            <NavDropdown title="Analytics" id="basic-nav-dropdown">
                                <NavDropdown.Item as={Link} to='/trend-analytics'>Trend Analytics</NavDropdown.Item>
                                <NavDropdown.Item as={Link} to='/user-engagement'>User Analytics</NavDropdown.Item>
                                <NavDropdown.Item as={Link} to='/geographic-analytics'>Geographic Analytics</NavDropdown.Item>
                                <NavDropdown.Item as={Link} to='/sentiment-analytics'>Sentiment Analytics</NavDropdown.Item>
                                <NavDropdown.Item as={Link} to='/candidate-analytics'>Candidate Analytics</NavDropdown.Item>
                                <NavDropdown.Item as={Link} to='/optimization'>Optimization</NavDropdown.Item>
                            </NavDropdown>
                            <Nav.Link as={Link} className='hof glow' to='/hall-of-fame'>Hall of Fame</Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    )
}

export default AppNavbar;