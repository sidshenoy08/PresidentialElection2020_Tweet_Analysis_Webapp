import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { useState, useEffect } from 'react';

import AppNavbar from '../../Components/AppNavbar/AppNavbar';

import 'bootstrap/dist/css/bootstrap.min.css';
import './Home.css';
import trump_img from './trump.png';
import biden_img from './biden.png';

function Home() {
    const [trumpStats, setTrumpStats] = useState({});
    const [bidenStats, setBidenStats] = useState({});

    useEffect(() => {
        fetch('http://127.0.0.1:5000/api/homepage/tweet-stats-by-candidate', { mode: 'cors' })
            .then((response) => response.json())
            .then((data) => {
                for (let i in data) {
                    if (data[i].tweet_about === 'Trump') {
                        setTrumpStats(data[i]);
                    } else {
                        setBidenStats(data[i]);
                    }
                }
            })
            .catch((err) => {
                console.log(err.message);
            })
    }, []);


    return (
        <>
            <AppNavbar />
            <h3 style={{ textAlign: "center" }}>Welcome to PollPulse!</h3>

            <div>
                <p className='para-text'>The 2020 US Presidential Election generated immense discussion on Twitter, with users sharing their thoughts on both candidates, Joe Biden and Donald Trump. This application provides insights into key trends, user behaviors, and geographic patterns by utilizing complex SQL queries on structured tweet data. The application can be used by political analysts, researchers, and data scientists to derive meaningful information from the election conversation.</p>
            </div>

            <div className="trump-container">
                <div className="trump-thumb"><img src={trump_img} alt="Donald Trump" /></div>
                <div className="candidate-content">
                    <p className="candidate-title">Here are some statistics of tweets made about Donald Trump</p>
                    <Row>
                        <Col xs={6} md={4}>
                            Total Tweets <br /> {trumpStats.total_tweets}
                        </Col>
                        <Col xs={6} md={4}>
                            Total Retweets <br /> {trumpStats.total_retweets}
                        </Col>
                        <Col xs={6} md={4}>
                            Total Likes <br /> {trumpStats.total_likes}
                        </Col>
                    </Row>
                </div>
            </div>

            <div className="biden-container">
                <div className="candidate-content">
                    <p className="candidate-title">Here are some statistics of tweets made about Joe Biden</p>
                    <Row>
                        <Col xs={6} md={4}>
                            Total Tweets <br /> {bidenStats.total_tweets}
                        </Col>
                        <Col xs={6} md={4}>
                            Total Retweets <br /> {bidenStats.total_retweets}
                        </Col>
                        <Col xs={6} md={4}>
                            Total Likes <br /> {bidenStats.total_likes}
                        </Col>
                    </Row>
                </div>
                <div className="biden-thumb"><img src={biden_img} alt="Joe Biden" /></div>
            </div>

            <footer>
                <p>Created by Group 26</p>
            </footer>
        </>
    );
}

export default Home;