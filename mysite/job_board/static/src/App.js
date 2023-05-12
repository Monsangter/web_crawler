import React, { useState, useEffect } from 'react';
import { Container, Card, Button, Table } from 'react-bootstrap';
import axios from 'axios';

function App() {
  const [wantedVisible, setWantedVisible] = useState(true);
  const [jobkoreaVisible, setJobkoreaVisible] = useState(true);
  const [saraminVisible, setSaraminVisible] = useState(true);
  const [data, setData] = useState({
    wanted: [],
    jobkorea: [],
    saramin: [],
  });

  const fetchData = () => {
    axios.get('http://127.0.0.1:8000/job_board/jobs/').then((response) => {
      setData(response.data);
    });
  };

  useEffect(() => {
    fetchData();
  }, []);

  const toggleVisibility = (model) => {
    if (model === 'wanted') setWantedVisible(!wantedVisible);
    else if (model === 'jobkorea') setJobkoreaVisible(!jobkoreaVisible);
    else if (model === 'saramin') setSaraminVisible(!saraminVisible);
  };

  return (
    <Container>
      <Card>
        <Card.Header>
          <Button onClick={() => toggleVisibility('wanted')}>Wanted</Button>
        </Card.Header>
        {wantedVisible && (
          <Card.Body>
            <Table>
              {/* Render Wanted data */}
              {data.wanted.map((item) => (
                <tr key={item.id}>
                  {/* Your table data */}
                </tr>
              ))}
            </Table>
          </Card.Body>
        )}
      </Card>

      <Card>
        <Card.Header>
          <Button onClick={() => toggleVisibility('jobkorea')}>Jobkorea</Button>
        </Card.Header>
        {jobkoreaVisible && (
          <Card.Body>
            <Table>
              {/* Render Jobkorea data */}
              {data.jobkorea.map((item) => (
                <tr key={item.id}>
                  {/* Your table data */}
                </tr>
              ))}
            </Table>
          </Card.Body>
        )}
      </Card>

      <Card>
        <Card.Header>
          <Button onClick={() => toggleVisibility('saramin')}>Saramin</Button>
        </Card.Header>
        {saraminVisible && (
          <Card.Body>
            <Table>
              {/* Render Saramin data */}
              {data.saramin.map((item) => (
                <tr key={item.id}>
                  {/* Your table data */}
                </tr>
              ))}
            </Table>
          </Card.Body>
        )}
      </Card>
    </Container>
  );
}

export default App;