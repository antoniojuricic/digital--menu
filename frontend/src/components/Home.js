import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom'

const Home = () => {
  const [categories, setCategories] = useState([]);
  
  useEffect(() => {
    const fetchData = async () => {
        try {
            const res = await axios.get(`http://localhost:8000/api/categories/`);
            setCategories(res.data);
        }
        catch (err) {

        }
    }

    fetchData();
}, []);

    return (
      <ul>
        {
          categories
            .map(category =>
              <li key={category.id}><Link to={`category/${category.slug}`}>{category.title}</Link></li>
            )
        }
      </ul>
    );
    
}

export default Home