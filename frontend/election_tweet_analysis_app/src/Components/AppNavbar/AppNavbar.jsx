import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom';
import NavDropdown from 'react-bootstrap/NavDropdown';

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
                                <NavDropdown.Item>Candidate Analytics</NavDropdown.Item>
                                <NavDropdown.Item href='/user-engagement'>User Analytics</NavDropdown.Item>
                                <NavDropdown.Item href='/geographic-analytics'>Geographic Analytics</NavDropdown.Item>
                                <NavDropdown.Item>Source Analytics</NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    )
}

export default AppNavbar;