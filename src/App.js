import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card, Button, Table } from 'react-bootstrap';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [wantedVisible, setWantedVisible] = useState(true);
  const [jobkoreaVisible, setJobkoreaVisible] = useState(true);
  const [saraminVisible, setSaraminVisible] = useState(true);
  const [wantedData, setWantedData] = useState([]);
  const [jobkoreaData, setJobkoreaData] = useState([]);
  const [saraminData, setSaraminData] = useState([]);

  useEffect(() => {
    axios.get('<YOUR_DJANGO_API_ENDPOINT>/wanted/')
      .then(response => setWantedData(response.data));

    axios.get('<YOUR_DJANGO_API_ENDPOINT>/jobkorea/')
      .then(response => setJobkoreaData(response.data));

    axios.get('<YOUR_DJANGO_API_ENDPOINT>/saramin/')
      .then(response => setSaraminData(response.data));
  }, []);

  // toggleVisibility function remains unchanged

  return (
    <Container>
      {/* The rest of the code remains unchanged */}

      {wantedVisible && (
        <Card.Body>
          <Table>
            <thead>
              {/* Your table headers */}
            </thead>
            <tbody>
              {wantedData.map((item) => (
                <tr key={item.id}>
                  {/* Your table data */}
                </tr>
              ))}
            </tbody>
          </Table>
        </Card.Body>
      )}

      {/* Similar table structures for Jobkorea and Saramin */}
    </Container>
  );
}

export default App;