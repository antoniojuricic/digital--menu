import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const Home = () => {
  const { slug } = useParams();
  const [items, setItems] = useState([]);
  console.log(slug)
  useEffect(() => {
    const fetchData = async () => {
        try {
            const res = await axios.get(`http://localhost:8000/api/categories/${slug}/`);
            setItems(res.data);
        }
        catch (err) {

        }
    }

    fetchData();
}, []);

    return (
      <ul>
        {
          items
            .map(category =>
              <li key={category.id}>{category.title}</li>
            )
        }
      </ul>
    );
    
}

export default Home