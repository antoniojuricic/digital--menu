import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom'
import CategoryCard from './CategoryCard'

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
      <div className="container">
        <div className="header">MENU</div>
        {
          categories
            .map(category =>
              <Link to = {`category/${category.slug}/`} style={{ textDecoration: 'none' }}>
                <CategoryCard title={category.title} image={category.image}/>
                <hr/>
              </Link> 
              
            )
        }
      </div>
    );
    
}

export default Home