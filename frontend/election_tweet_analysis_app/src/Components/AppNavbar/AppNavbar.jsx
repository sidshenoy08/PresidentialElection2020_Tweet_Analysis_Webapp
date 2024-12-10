import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom';
import NavDropdown from 'react-bootstrap/NavDropdown';

import './AppNavbar.css';

function AppNavbar() {
    return (
        <>
            <Navbar sticky="top" expand="lg" className="bg-body-tertiary">
                <Container>
                    <Navbar.Brand as={Link} to='/'>PollPulse</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className='ms-auto'>
                            <Nav.Link as={Link} to='/'>Home</Nav.Link>
                            <NavDropdown title="Analytics" id="basic-nav-dropdown">
                                <NavDropdown.Item href='/trend-analytics'>Trend Analytics</NavDropdown.Item>
                                <NavDropdown.Item href='/user-engagement'>User Analytics</NavDropdown.Item>
                                <NavDropdown.Item href='/geographic-analytics'>Geographic Analytics</NavDropdown.Item>
                                <NavDropdown.Item href='/sentiment-analytics'>Sentiment Analytics</NavDropdown.Item>
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