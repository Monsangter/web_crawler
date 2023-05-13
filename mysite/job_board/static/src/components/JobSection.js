import React, { useEffect, useState } from 'react';
import axios from 'axios';

function JobSection({ url }) {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    axios.get(url)
      .then(res => setJobs(res.data))
      .catch(err => console.error(err));
  }, [url]);

  return (
    <div>
      {jobs.map(job => (
        <div key={job.id}>
          {/* Display job information */}
          <h2>{job.title}</h2>
          <p>{job.description}</p>
        </div>
      ))}
    </div>
  );
}

export default JobSection;