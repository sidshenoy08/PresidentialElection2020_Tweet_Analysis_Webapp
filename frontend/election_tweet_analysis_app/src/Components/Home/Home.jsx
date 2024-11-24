import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Home.css';
import trump_img from './trump.png';
import biden_img from './biden.png';

function Home() {
    return (
        <>
            <Navbar sticky="top" expand="lg" className="bg-body-tertiary">
                <Container>
                    <Navbar.Brand href="#home">PollPulse</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className='ms-auto'>
                            <Nav.Link href="#home">Home</Nav.Link>
                            <NavDropdown title="Analytics" id="basic-nav-dropdown">
                                <NavDropdown.Item href="#action/3.1">Candidate Analytics</NavDropdown.Item>
                                <NavDropdown.Item href="#action/3.2">
                                    User Analytics
                                </NavDropdown.Item>
                                <NavDropdown.Item href="#action/3.3">Geographic Analytics</NavDropdown.Item>
                                <NavDropdown.Item href="#action/3.4">
                                    Source Analytics
                                </NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>

            <h3 style={{ textAlign: "center" }}>Welcome to PollPulse!</h3>

            <div className="flex-container1">
                <p className='para-text'>The 2020 US Presidential Election generated immense discussion on Twitter, with users sharing their thoughts on both candidates, Joe Biden and Donald Trump. This application provides insights into key trends, user behaviors, and geographic patterns by utilizing complex SQL queries on structured tweet data. The application can be used by political analysts, researchers, and data scientists to derive meaningful information from the election conversation.</p>
            </div>

            <div className="trump-container">
                <div class="trump-thumb"><img src={trump_img} alt="Donald Trump" /></div>
                <div className="candidate-content">
                    <p className="candidate-title">Here are some statistics of tweets made about Donald Trump</p>
                    <p>Average</p>
                </div>
            </div>

            <div className="biden-container">
                <div className="candidate-content">
                    <p className="candidate-title">Here are some statistics of tweets made about Joe Biden</p>
                    <p>Average</p>
                </div>
                <div class="biden-thumb"><img src={biden_img} alt="Joe Biden" /></div>
            </div>

            <footer>
                <p>Created by Group 26</p>
            </footer>
        </>
    );
}

export default Home;