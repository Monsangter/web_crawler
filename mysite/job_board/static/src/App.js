import React from 'react';
import JobSection from './components/JobSection';

function App() {
  return (
    <div className="App">
      <h1>Job Board</h1>
      <JobSection url='/api/job_board/wanted/' />
      <JobSection url='/api/job_board/jobkorea/' />
      <JobSection url='/api/job_board/saramin/' />
    </div>
  );
}

export default App;